district=['ST','BĐ','BTL','CG','ĐĐ','HBT']
population=[150300,247100,333300,266800,420900,318000]
area=[117.43,9.224,43.35,12.04,9.96,10.09]
print('district',*district)
print("population",*population)
print(max(population))
print(min(population))
print(district[population.index(max(population))])
print(district[population.index(min(population))])
density=[population[0]/area[0],population[1]/area[1],population[2]/area[2],population[3]/area[3],population[4]/area[4],population[5]/area[5]]
print(density)
average= (population[0]/area[0]+population[1]/area[1]+population[2]/area[2]+population[3]/area[3]+population[4]/area[4]+population[5]/area[5])/6
print(average)
        
        

   
