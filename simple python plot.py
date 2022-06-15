#kazem0kamali@gmail.com
import matplotlib.pyplot as plt
  
# setting the x - coordinates
x = [1, 2, 3, 4, 5, 6, 7, 8]
# setting the corresponding y and z - coordinates
y = [120, 150 , 160, 130, 120, 170, 150, 125]
z = [70, 80, 100, 130, 175, 150, 130, 120]
 
# plotting the points
plt.plot(x, y, label="Blue line(y)")
plt.plot(x, z, label="Orange line(z)")

#Customizing and making the graph a little bit fancy
plt.grid(b=True, which='major', color='#666666', linestyle='-')
# Show the minor grid lines with very faint and almost transparent grey lines
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
 
plt.xlabel('X label name')
plt.legend()
plt.title('Your Graph Name!')
# function to show the plot
plt.show()