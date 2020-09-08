import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import interactive
from matplotlib.backends.backend_pdf import PdfPages
#read the Yield dataset save it to dataframe
dataset = pd.read_csv('/Users/abeer/Downloads/Cropsandlivestockproducts_ExportQuantity.csv')
# Select the relevant fields (Item,Year,Value)
X = dataset.iloc[:, [7, 9, 11]]
#drop the nan values
X= X.dropna()
df = X.drop('Year', 1)
#group the dataset based on the Item
grouped = X.groupby('Item')
groupedf =df.groupby('Item')
output = open("/Users/abeer/downloads/Cropsandlivestockproducts_ExportQuantity.txt", 'w')
#use discribe function to show the Value(float) statistics
output.write("Some Statistics about Exported Quantity is Saudi Arabia based on the Item(plants)")
output.write("\n")
print(groupedf.describe(),file=output)
output.write("\n")
output.write("The variance for all Items(plants) Exported Quantity in Saudi Arabia")
output.write("\n")
# Get Unbiased variance of the Value column for each group
var=X.groupby('Item')['Value'].var()
print(var,file=output)
output.write("\n")
output.write("The first row for each Items(plants) Exported Quantity is Saudi Arabia with their Year Value")
output.write("\n")
#show the first row for each group
print(grouped.first(),file =output)

#Code to draw bar plot for all the Items(plants)
items=[]
itemslist=[]
#save available data to array based on thier group
for key, item in grouped:
    itemslist.append(grouped.get_group(key))
    items.append(key)
with PdfPages(r'/Users/abeer/downloads/Cropsandlivestockproducts_ExportQuantityCharts.pdf') as export_pdf:
    for i in range(len(itemslist)):
        Y=[]
        y_values=[]
        x_values=[]
        output.write("The name of the item(value) Exported Quantity:  ")
        print(items[i],file=output)
        output.write("\n")
        output.write("The Table that shows the Year and Value of the item(value) Exported Quantity")
        output.write("\n")
        print(itemslist[i],file=output)
        output.write("\n")
        Y=itemslist[i].to_numpy()
        # create a figure
        plt.figure(i+1)
        # get x and y data
        y_values = Y[:, 0]
        x_values = Y[:, 1]
        if len(y_values) >10:
        #check if the values of the last years equalzero
            is_all_zero = np.all((x_values[-10:] == 0.0))
        #if the values of the last years equalzero
        #print the first values
            if is_all_zero:
                y_values = y_values[:10]
                x_values = x_values[:10]
        #if the values of the last years not equalzero
        #print the last years values
            else:
                y_values = y_values[-10:]
                x_values = x_values[-10:]
    #draw the chart
        y_pos = np.arange(len(y_values))
        plt.bar(y_pos, x_values, align='center')
        plt.xticks(y_pos, y_values.astype(int), fontsize=8)
        plt.xlabel('The years', fontsize=8)
        plt.yticks(fontsize=8)
        plt.ylabel('Exported Quantity Value in (tonnes)',fontsize=8)
        plt.title(items[i]+' Exported Quantity Value Vs Year')
        # create bar chart
        interactive(True)
        export_pdf.savefig()
        #plt.show()

#Please not if the graph is empty mean no production


    #draw a plot for the mean for all the Items,plants
    #calculate the mean based on the Item,plants
    df= X.groupby('Item')['Value'].mean().to_frame(name = 'mean').reset_index()
    #convert the dataframe to array
    Mean_values=df.to_numpy()
    #create figure
    plt.figure(len(itemslist)+1)
    # get x and y data
    MeanY_values =Mean_values[:, 0]
    MeanX_values= Mean_values[:, 1]
    MeanY_values = MeanY_values[:30]
    MeanX_values= MeanX_values[:30]
    #draw the chart
    y_poss=np.arange(len(MeanY_values))
    plt.barh(y_poss, MeanX_values , align='center')
    plt.yticks(y_poss,MeanY_values,fontsize=3)
    plt.xlabel('The mean Export Quantity Value in (tonnes)',fontsize=8)
    plt.title('The Items,plants in Saudi Arabia Vs Mean Export Quantity')
    interactive(False)
    export_pdf.savefig()
    #plt.show()
plt.close()








