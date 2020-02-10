#menu
import math
def menu() :
    print("1. Zone finder")
    print("2. Weight converter")
    print("3. Dimension converter")
    print("4. Calculate the price of a package")
    menu_input = int(input("Enter a selection: "))

    while menu_input > 4 or menu_input <= 0 :
        print("Invalid selection.")
        menu_input = int(input("Enter a selection: "))
    else :
        selection(menu_input)

def selection(selected) :
    if selected == 1 :
        zipcode_origin = str(input("Enter the origin zip code: "))
        zipcode_dest = str(input("Enter the destination zip code: "))
        if zipcodes(zipcode_origin, zipcode_dest) != None :
            
            print("According to the zip codes the zone is", str(zipcodes(zipcode_origin, zipcode_dest)) + ".")
        else :
            print()
    elif selected == 2 :
        print("\nPlease choose the conversion you wish to run.")
        print("1. Grams to pounds and ounces")
        print("2. Pounds and ounces to grams")
        sub_select = int(input("\nEnter a selection: "))
        if sub_select == 1 :
            grams = int(input("Enter the amount in grams to convert to ounces and pounds: "))
            print(str(grams) + "g is", gtolboz(grams))
        elif sub_select == 2 :
            lb = int(input("Enter the amount in pounds: "))
            oz = int(input("Enter the amount in ounces: "))
            print(str(lb) + "lb and", str(oz) + "oz is", lboztog(lb, oz) + "g")
        else :
            print("Invalid input. Try again.")
            selection(2)
    elif selected == 3 :
        print("\nPlease choose the conversion you wish to run.")
        print("1. Centimeters to inches")
        print("2. Inches to centimeters")
        sub_select = int(input("\nEnter a selection: "))
        if sub_select == 1 :
            centimeters = int(input("Enter the amount in centimeters to convert to inches: "))
            print(str(centimeters) + "cm is", cmtoin(centimeters) + "in")
        elif sub_select == 2 :
            inch = int(input("Enter the amount in inches to convert to centimeters: "))
            print(str(inch) + "in is", intocm(inch) + "cm")
        else :
            print("Invalid input. Try again.")
            selection(3)            
    elif selected == 4 :
        print("\nThe required elements to calculate a price are:")
        print("- Zip codes (origin and destination)")
        print("- Weight of the package")
        print("- Dimensions of the package\n")
        pricePackage()
        priceLoop = input("\nWould you like to calculate another price? (yes/no) ")

        while priceLoop == "yes" :
            pricePackage()
            priceLoop = input("\nWould you like to calculate another price? (yes/no) ")

        prices = open("shipping_price.txt", "w")

        for i in range(len(zipOrigin)) :
                    
            prices.write("Origin zip code: " + "".join(zipOrigin[i]) + "\n")
            prices.write("Destination zip code: " + "".join(zipDest[i]) + "\n")
            prices.write("Type of Shipping: " + "".join(typeShip[i]) + "\n")
            prices.write("Price: $" + "".join(allPrices[i]) + "\n\n")
            
        prices.close()
        
def zipcodes(origin, destination) :
    zipdata = open("zip_code_database.txt", "r")

    verify_zip = zipdata.read().split()
    while origin in verify_zip and destination in verify_zip and len(origin) == 5 and len(destination) == 5 :
        zipdata.seek(0)
        for line in zipdata :
            element = line.split("\t")
           # if len(origin) == 5 and len(destination) == 5 :
            if element[0] == origin :
                lat1 = float(element[4]) * (math.pi/180)
                long1 = float(element[5]) * (math.pi/180)
                    
        zipdata.seek(0)

        for line in zipdata :
            element_2 = line.split("\t")
            if element_2[0] == destination :
                lat2 = float(element_2[4]) * (math.pi/180)
                long2 = float(element_2[5]) * (math.pi/180)
        dist = round(3949.99 * math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2))),2)

        if dist < 125 :
            return 1
        elif dist >= 125 and dist < 244 :
            return 2
        elif dist >= 244 and dist < 300 :
            return 3
        elif dist >= 300 and dist < 600 :
            return 4
        elif dist >= 600 and dist < 1000 :
            return 5
        elif dist >= 1000 and dist < 1400 :
            return 6
        elif dist >= 1400 and dist < 1800 :
            return 7
        elif dist >= 1800 :
            return 8

    else :
        print("It seems like the zip codes entered are invalid. Please try again.\n")
        
    zipdata.close()

def gtolboz(grams) :
    if grams > 0 :
        ounces = round((grams / 28.35), 2)
        if ounces >= 16 :
            pounds = int(ounces // 16)
            remain_ounces = round(ounces % 16, 2)
            return str(pounds) + "lb and " + str(remain_ounces) + "oz"
           # print("The amount entered is", pounds, "lb and", remain_ounces, "oz.")
           # grams = int(input("Enter the amount in grams to convert to ounces: "))

        elif ounces < 16 :
            return str(ounces) + "oz"
           # print("The amount entered is", ounces, "oz")
           # grams = int(input("Enter the amount in grams to convert to ounces: "))
   # else :
 #       print("Invalid input. Try again.")

def lboztog(lb, oz) :
    if oz >= 0 and lb >= 0 :
        g = round((oz * 28.35),2)
        oz_convert = (lb * 16)
        g_convert = round((oz_convert * 28.35),2)

        g = g + g_convert
        return str(g)
       # print("The amount entered of", lb, "lb and ", oz, "oz is: ", g, "grams.")
       # lb = int(input("Enter the amount in pounds: "))
       # oz = int(input("Enter the amount in ounces: "))
    else :
        print("Invalid input. Try again.")

def cmtoin(centimeters) :
    if centimeters >= 0 :
        inches = round((centimeters * 0.39), 2)
        return str(inches)
    else :
        print("Invalid input. Try again.")

def intocm(inch) :
    if inch >= 0 :
        cm = round((inch * 2.54), 2)
        return str(cm)

zipOrigin = []
zipDest = []
allPrices = []
typeShip = []
ounce = []

def pricePackage() :
    zone = priceZip()
    newWeight = priceWeight()
    priceDimension()
    priceCal(newWeight, zone)
 #   priceLoop = input("\nWould you like to calculate another price? (yes/no) ")
 #   return priceLoop

    
def priceZip() :
    zipcode_origin = str(input("Enter the origin zip code: "))
    zipcode_dest = str(input("Enter the destination zip code: "))
    while len(zipcode_origin) != 5 or len(zipcode_dest) != 5 :
        print("It seems like the zip codes entered are invalid. Please enter your zip codes again.")

        zipcode_origin = str(input("Enter the origin zip code: "))
        zipcode_dest = str(input("Enter the destination zip code: "))

    else :
        zone = zipcodes(zipcode_origin, zipcode_dest)
        zipOrigin.append(zipcode_origin)
        zipDest.append(zipcode_dest)
        return zone


def priceWeight() :
    typeWeight = input("\nIs the weight of the package standard or metric? ")
    typeWeightLower = typeWeight.lower()

    while typeWeightLower != "standard" and typeWeightLower != "metric" :
        print("Invalid input. Try again.")
        typeWeight = input("\nIs the weight of the package standard or metric? ")
        typeWeightLower = typeWeight.lower()

    else :
        
        if typeWeightLower == "standard" :
            lb = int(input("Enter the amount in pounds: "))
            oz = int(input("Enter the amount in ounces: "))
            packageWeight = float(lboztog(lb, oz))

            while packageWeight > 9071 :
                print("The maximum weight for a package is 70lbs.\n")
                lb = int(input("Enter the amount in pounds: "))
                oz = int(input("Enter the amount in ounces: "))
                packageWeight = float(lboztog(lb, oz))

            reconv = round((packageWeight / 28.35), 2)
            if reconv >= 16 :
                newWeight = int(reconv // 16)
                return newWeight
            
            else :
                newWeight = 0
                ounce.append(oz)
                return newWeight
                
        elif typeWeightLower == "metric" :
            grams = int(input("What is the weight of the package in grams? " ))
            oz = round((grams / 28.35), 2) #change oz to ounces

            while grams > 9071 :
                print("The maximum weight for a package is 70lbs.\n")
                grams = int(input("What is the weight of the package in grams? " ))
                oz = round((grams / 28.35), 2)
                
            if oz >= 16 :
                newWeight = int(oz // 16)
                return newWeight
            else :
                newWeight = 0
                ounce.append(oz)
                return newWeight
                

def priceDimension() :
    typeDimension = input("\nAre the dimensions of the package standard or metric? ")
    typeDimensionLower = typeDimension.lower()

    while typeDimensionLower != "metric" and typeDimensionLower != "standard" :
        print("Invalid input. Try again.")
        typeDimension = input("\nAre the dimensions of the package standard or metric? ")
        typeDimensionLower = typeDimension.lower()
    else :
        
        if typeDimensionLower == "metric" :
            length = int(input("Enter the length in centimeters: "))
            width = int(input("Enter the width in centimeters: "))
            height = int(input("Enter the height in centimeters: "))
            
            packageDimensionsL = float(cmtoin(length))
            packageDimensionsW = float(cmtoin(width))
            packageDimensionsH = float(cmtoin(height))

            girth = packageDimensionsL + (2 * (packageDimensionsW + packageDimensionsH))
            
            while girth > 108 :
                print("The maximum length for a package is 108in in length + girth.")
                length = int(input("Enter the length in centimeters: "))
                width = int(input("Enter the width in centimeters: "))
                height = int(input("Enter the height in centimeters: "))
                
                packageDimensionsL = float(cmtoin(length))
                packageDimensionsW = float(cmtoin(width))
                packageDimensionsH = float(cmtoin(height))
                girth = packageDimensionsL + (2 * (packageDimensionsW + packageDimensionsH))
                
        elif typeDimensionLower == "standard" :
            length = int(input("Enter the length in inches: "))
            width = int(input("Enter the width in inches: "))
            height = int(input("Enter the height in inches: "))

def priceCal(newWeight, zone) :
    if newWeight == 0 and ounce[-1] <= 13 :
        first_class = input("\nWould you like to ship via first class? (yes/no) " )
        first_classLower = first_class.lower()
        if first_classLower == "yes" :
            first_price = open("first.txt", "r")
            for line in first_price :
                element = line.split(" ")
                if int(element[0]) > int(ounce[-1]) :
                    shipPrice = element[1]
                    print("The price is $" + shipPrice)
                    break
                
            allPrices.append(shipPrice)
            typeShip.append("First Class")
            first_price.close()
            
        else :
            priority_price = open("priority.txt", "r")
            for line in priority_price :
                element = line.split(" ")
                if int(element[0]) > int(newWeight) :
                    shipPrice = element[zone]
                    print("The price is $" + shipPrice)
                    break

            allPrices.append(shipPrice)
            typeShip.append("Priority")
            priority_price.close()

    else :

        priority_price = open("priority.txt", "r")
        for line in priority_price :
            element = line.split(" ")
            if int(element[0]) > int(newWeight) :
                shipPrice = element[zone]
                print("The price is $" + shipPrice)
                break

        allPrices.append(shipPrice)
        typeShip.append("Priority")
        priority_price.close()
    
menu()
