cpu = int(input("Enter CPU usage percentage: "))
disk = int(input("Enter Disk usage percentage: "))

#cpu check
if cpu > 80:
    print("Alert: High CPU usage")
elif cpu > 60:
        print("Warning: Moderate CPU usage")      
else:
     print("CPU normal")


#disk check
if disk > 90:
    print("Alert: High Disk usage")
elif disk > 75:
    print("Warning: Moderate Disk usage")
else:
    print("Disk normal")
