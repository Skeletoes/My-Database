import sqlite3 # Import the sqlite3 library
from tabulate import tabulate

architecture = [] # Create a list for architectures fetched from the database
recent_searchesL = []
usernamesL = []
headers = ["Brand", "Model", "Base Speed(GHz)", "Boost Speed(GHz)", "Architecture", "DLSS/FSR Gen", "Memory Type", "Memory Amount(GB)", "Memory Bandwidh(GB/s)", "Launch Date"]
search_options = ["- 'Brand' to search by brand", "- 'Model' to search by model", "- 'Base Speed' to search by faster or slower base speeds", "- 'Boost Speed' to search by faster or slower boost speeds", "- 'Architecture' to search by architecture", "- 'DLSS/FSR' to search by DLSS/FSR generation", "- 'Memory Type' to search by memory type", "- 'Memory Amount' to search by greater or less memory amounts", "- 'Memory Bandwidth' to search by greater or smaller memory bandwidths", "- 'Launch Date' to search by older or newer launch dates"]
edit_options = ["- 'Brand' to edit brand", "- 'Model' to edit model", "- 'Base Speed' to edit base speed", "- 'Boost Speed' to edit boost speed", "- 'Architecture' to edit architecture", "- 'DLSS/FSR' to edit DLSS/FSR generation", "- 'Memory Type' to edit memory type", "- 'Memory Amount' to edit memory amount", "- 'Memory Bandwidth' to edit memory bandwidth", "- 'Launch Date' to edit launch date"]
start_up = 0

def float_value(value): # Create a function to tell whether a value is float or not
    try:
        float(value) # Try convert value to float
        return True # Return True if value is float
    except ValueError: # Use except ValueError for if the conversion falied
        return False # Return false if value is not a float
    

def recent_searches(search):
    if len(recent_searchesL) < 5:
        recent_searchesL.append(search)
    else:
        recent_searchesL[4] = recent_searchesL[3]
        recent_searchesL[3] = recent_searchesL[2]
        recent_searchesL[2] = recent_searchesL[1]
        recent_searchesL[1] = recent_searchesL[0]
        recent_searchesL[0] = search

def gpu_edit():
    dbEdit = sqlite3.connect("Database.db")
    cursorEdit = dbEdit.cursor()
    sqlEdit = ("SELECT * FROM graphics_cards;")
    gpus_editable = []
    cursorEdit.execute(sqlEdit)
    gpusEditable = cursorEdit.fetchall()
    for gpusedit in gpusEditable:
        gpus_editable.append(gpusedit[1])
    print("\nEnter a GPU Model to edit the GPUs info.")
    while True:
        try:
            edit_gpu = input("Model: ").upper()
            if edit_gpu == 'quit':
                return
            else:
                if edit_gpu in gpus_editable:
                    for gpusedit in gpusEditable:
                        if edit_gpu == gpusedit[1]:
                            list1 = []
                            list1.append(gpusedit)
                            print(tabulate(list1, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                else:
                    print("That GPU is not in the system.")                            
                break
        except:
            print("ERROR 67!!!")
    print("\nOptions:")
    for val in edit_options:
        print(val)
    while True:
        try:
            edit_select = input("\nEdit: ").lower()
            if edit_select == 'quit':
                return
            elif edit_select == 'brand':
                while True:
                    try:
                        brand_edit = input("New Brand Name: ")
                        if brand_edit == 'quit':
                            break
                        else:
                            sqlEdit = (f"UPDATE graphics_cards SET brand = '{brand_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                    except:
                        print("ERROR 81!!!")
            elif edit_select == 'model':
                while True:
                    try:
                        model_edit = input("New Model Name: ")
                        if model_edit == 'quit':
                            break
                        else:
                            sqlEdit = (f"UPDATE graphics_cards SET model = '{model_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{model_edit}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                    except:
                        print("ERROR 74!!!")
            elif edit_select == 'base speed':
                while True:
                    try:
                        baseSpeed_edit = input("New Base Speed: ")
                        if baseSpeed_edit == "quit":
                            break
                        elif float_value(baseSpeed_edit):
                            baseSpeed_edit = float(baseSpeed_edit)
                            sqlEdit = (f"UPDATE graphics_cards SET Base_Clock_SpeedGHz = '{baseSpeed_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{model_edit}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                        else:
                            print("Input must be a number!")
                    except:
                        print("ERROR 63!!!")
            elif edit_select == 'boost speed':
                while True:
                    try:
                        boostSpeed_edit = input("New Boost Speed: ")
                        if boostSpeed_edit == 'quit':
                            break
                        elif float_value(boostSpeed_edit):
                            boostSpeed_edit = float(boostSpeed_edit)
                            sqlEdit = (f"UPDATE graphics_cards SET Boost_Clock_SpeedGHz = '{boostSpeed_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{model_edit}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                        else:
                            print("Input must be a number!")
                    except:
                        print("ERROR 80!!!")
            elif edit_select == 'architecture':
                while True:
                    try:
                        architecture_edit = input("New Architecture: ")
                        if architecture_edit == 'quit':
                            break
                        else:
                            sqlEdit = (f"UPDATE graphics_cards SET Architecture = '{architecture_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                    except:
                        print("ERROR 95!!!")
            elif edit_select == 'dlss/fsr':
                while True:
                    try:
                        dlssFsr_edit = input("New DLSS/FSR Gen: ")
                        if dlssFsr_edit == 'quit':
                            break
                        elif float_value(dlssFsr_edit):
                            sqlEdit = (f"UPDATE graphics_cards SET DLSS_FSR = '{dlssFsr_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{model_edit}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                        else:
                            print("Input must be a number!")
                    except:
                        print("ERROR 123!!!")
            elif edit_select == 'memory type':
                while True:
                    try:
                        memoryType_edit = input("New Memory Type: ")
                        if memoryType_edit == 'quit':
                            break
                        else:
                            sqlEdit = (f"UPDATE graphics_cards SET Memory_Type = '{memoryType_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                    except:
                        print("ERROR 234!!!")
            elif edit_select == 'memory amount':
                while True:
                    try:
                        memoryAmount_edit = input("New Memory Amount: ")
                        if memoryType_edit == 'quit':
                            break
                        elif float_value(memoryType_edit):
                            sqlEdit = (f"UPDATE graphics_cards SET Memory_AmountGB = '{memoryAmount_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{model_edit}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                        else:
                            print("Input must a number!")
                    except:
                        print("ERROR 345!!!")
            elif edit_select == 'memory bandwidth':
                while True:
                    try:
                        memoryBandwidth_edit = input("New Memory Amount: ")
                        if memoryBandwidth_edit == 'quit':
                            break
                        elif float_value(memoryBandwidth_edit):
                            sqlEdit = (f"UPDATE graphics_cards SET Memory_AmountGB = '{memoryBandwidth_edit}' WHERE model = '{edit_gpu}';")
                            cursorEdit.execute(sqlEdit)
                            dbEdit.commit()
                            sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{model_edit}';")
                            cursorEdit.execute(sqlEdit)
                            gpu_edited = cursorEdit.fetchall()
                            dbEdit.close()
                            gpus_editable = []
                            gpus_editable.append(gpu_edited[0])
                            print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            return
                        else:
                            print("Input must a number!")
                    except:
                        print("ERROR 456!!!")
            elif edit_select == 'launch date':
                while True:
                    try:
                        launchDate_edit = input("New Launch Date(YYYY-MM-DD): ")
                        if launchDate_edit == 'quit':
                            break
                        else:
                            launchDate_split = launchDate_edit.split("-")
                            if int(launchDate_split[0].isdigit()):
                                if int(launchDate_split[1].isdigit()) and int(launchDate_split[1]) <= 12:
                                    if int(launchDate_split[2].isdigit()) and int(launchDate_split[2]) <= 31:
                                        sqlEdit = (f"UPDATE graphics_cards SET Launch_Date = '{launchDate_edit}' WHERE model = '{edit_gpu}';")
                                        cursorEdit.execute(sqlEdit)
                                        dbEdit.commit()
                                        sqlEdit = (f"SELECT * FROM graphics_cards WHERE model = '{model_edit}';")
                                        cursorEdit.execute(sqlEdit)
                                        gpu_edited = cursorEdit.fetchall()
                                        dbEdit.close()
                                        gpus_editable = []
                                        gpus_editable.append(gpu_edited[0])
                                        print(tabulate(gpus_editable, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                                        return
                                    else:
                                        print("Invalid Date!")
                                else:
                                    print("Invalid Date!")
                            else:
                                print("Invalid Date!")
                    except:
                        print("ERROR 567!!!")
            else:
                dbEdit.close()
                return
        except:
            print("ERROR 90!!!")   


def lookup(): # Create a function for the lookup feature
    dbMain = sqlite3.connect('Database.db') # Create a variable that connects to the database
    cursor = dbMain.cursor() # Create a cursor
    sql = "SELECT * FROM graphics_cards;" # Create a variable with the prompt to fetch all data from the graphics cards table
    cursor.execute(sql) # Execute the prompt
    results = cursor.fetchall() # Store the prompts results in a variable
    print("\nSearch Options:") # Print the options for the user
    for options in search_options:
        print(options)
    while True: # Start a while true loop for all the lookup features
        try:
            search_option = input('\nSearch: ').lower() # Create an input variable for the user to select a search option
            if search_option == 'brand': # Check if the option selected is brand
                while True: # Start a while true loop for the GPUs by brand search option
                    try:
                        brand = input("\nBrand: ") # GPU brand to search by
                        if brand == 'quit': # If the input is quit the break out of the while true loop
                            break
                        else: # Else check if the brand is in the database
                            recent_search = (f"GPU/Brand/{brand}")
                            recent_searches(recent_search)
                            list = []
                            for brand_select in results: # Start a for loop to go through each GPU in the database
                                if brand.lower() == brand_select[0].lower(): # Check if the GPUs brand is equal to the brand selected
                                    list.append(brand_select)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            break
                    except:
                        print("ERROR 1!!!") # Number each except error so its easier to identify where the error is
            elif search_option == 'model': # Check if the search option is model
                while True: # Start a while true loop for the GPU by model search option
                    try:
                        model = input('\nModel: ') # GPU model to search for
                        if model == 'quit':
                            break
                        else:
                            recent_search = (f"GPU/Model/{model}")
                            recent_searches(recent_search)
                            list = []
                            for models in results: # Start a for loop to go through the results variable and look for the model selected
                                if model.upper() in models[1]: # Print the GPU if its in the database
                                    list.append(models)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            break
                    except:
                        print("ERROR 2!!!")
            elif search_option == 'base speed': # Check if the search option is base speed
                while True: # Start a while true loop for the GPUs by base speed
                    try:
                        speed = input('\nEnter speed(GHz): ') # Base speed input variable 
                        if float_value(speed): # Use the float_value() function to check if the speed is a float or integer
                            speed = float(speed) # Convert the input to a float if the function returns true
                            break
                        elif speed == 'quit':
                            break
                        else: # Prompt is printed if the function returns false
                            print('That is not a speed!')
                    except:
                        print('ERROR 3!!!')
                while True: # Start another while true loop continuing the base speed option but this is to search fo GPUs faster or slower then what the user selected
                    try:
                        if speed == 'quit': # Break if the speed input equals quit
                            break
                        else:
                            great_less = input("GPUs faster or slower than this base speed?: ") # Ask if the user wants GPUs fatser or slower than the speed chosen
                            if great_less == 'slower': # If they select slower start a for loop
                                recent_search = (f"GPU/Base Speed/Slower/{speed}GHz")
                                recent_searches(recent_search)
                                list = []
                                for base_speeds in results: # The for loop will go through the databases GPUs base speeds and convert them to a float
                                    the_speed = float(base_speeds[2])
                                    if speed >= the_speed: # After the conversion it will print GPUs the a slower than the speed chosen
                                        list.append(base_speeds)
                                print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                                break
                            elif great_less == 'faster': # If they select faster start a for loop
                                recent_search = (f"GPU/Base Speed/Faster{speed}GHz")
                                recent_searches(recent_search)
                                list = []
                                for base_speeds in results: # The for loop will convert the values to a float
                                    the_speed = float(base_speeds[2])
                                    if speed < base_speeds[2]: # It will check for GPUs faster and print them out
                                        list.append(base_speeds)
                                print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                                break
                            elif great_less == 'quit':
                                break
                            else: # If the user input doesnt match the options available the user will be prompted again
                                print("Faster or Slower?")
                    except:
                        print('ERROR 4!!!')
            elif search_option == 'boost speed': # Check if the search option is boost speed
                while True: # Start a while true loop for the GPUs by boost speed
                    try:
                        speed = input('\nEnter speed(GHz): ') # Ask for the boost speed to search by
                        if float_value(speed): # Check of the value entered is a float or integer
                            speed = float(speed) # Convert value to float if true
                            break
                        else:
                            print("That is not a speed!")
                    except:
                        print('ERROR 5!!!')
                if speed == 'quit':
                    break
                else:
                    while True: # Start another while true loop continuing the boost speed search option to show GPUs slower or faster than the speed chosen
                        try:
                            great_less = input(f"GPUs faster or slower than this boost speed of {speed}GHz?: ") # Ask if the user wants GPUs slower or faster than the chosen speed
                            if great_less == 'slower': # Start a for loop if user selects slower
                                recent_search = (f"GPU/Boost Speed/Slower/{speed}GHz")
                                recent_searches(recent_search)
                                list = []
                                for boost_speeds in results: # The for loop will convert the database boost speeds to float values
                                    the_speed = float(boost_speeds[3]) 
                                    if speed > the_speed: # After the conversion it will print out GPUs that match the users selection
                                        list.append(boost_speeds)
                                print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                                break
                            elif great_less == 'faster': # Start a for loop if the user chooses faster
                                recent_search = (f"GPU/Boost Speed/Faster/{speed}GHz")
                                recent_searches(recent_search)
                                list = []
                                for boost_speeds in results: 
                                    the_speed = float(boost_speeds[3])
                                    if speed < the_speed:
                                        list.append(boost_speeds)
                                print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                                break
                            elif great_less == 'quit':
                                break
                            else:
                                print('Invalid!')
                        except:
                            print('ERROR 6!!!')
            elif search_option == "architecture":
                while True:
                    try:
                        arch = input('\nArchitecture: ').title()
                        if arch == 'quit':
                            break
                        else:
                            for architectures in results:
                                architecture.append(architectures[4])
                        if arch in architecture:
                            recent_search = (f"GPU/Architecture/{arch}")
                            recent_searches(recent_search)
                            list = []
                            for tectures in results:
                                if arch == tectures[4]:
                                    list.append(tectures)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            break
                        else:
                            print("That architecture doesn't seem to be associated with any of the GPUs.")
                    except:
                        print('ERROR 7!!!')
            elif search_option.upper() == 'DLSS/FSR':
                gen = int(input("\nDLSS/FSR Generation: "))
                recent_search = (f"GPU/DLSS FSR Gen/{gen}")
                recent_searches(recent_search)
                list = []
                for generations in results:
                    if gen == generations[5]:
                        list.append(generations)
                print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
            elif search_option == "memory type":
                while True:
                    try:
                        type = input('\nMemory Type: ').upper()
                        if type == 'QUIT':
                            break
                        else:
                            recent_search = (f"GPU/Memory Type/{type}")
                            recent_searches(recent_search)
                            list = []
                            for memory in results:
                                if type == memory[6]:
                                    list.append(memory)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                    except:
                        print("ERROR 8!!!")
            elif search_option == "memory amount":
                while True:
                    try:
                        memory1 = int(input('\nMemory Amount: '))
                        break
                    except:
                        print('ERROR 9!!!')
                while True:
                    try:
                        more_less = input(f"GPUs with more or less than {memory1}GB?: ")
                        if more_less == 'more':
                            recent_search = (f"GPU/Memory Amount/More Than/{memory1}GB")
                            recent_searches(recent_search)
                            list = []
                            for amount in results:
                                if memory1 < amount[7]:
                                    list.append(amount)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            break
                        elif more_less == 'less':
                            recent_search = (f"GPU/Memory Amount/Less Than/{memory1}GB")
                            recent_searches(recent_search)
                            list = []
                            for amount in results:
                                if memory1 > amount[7]:
                                    list.append(amount)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            break
                        else:
                            print("Invalid!")
                    except:
                        print("ERROR 10!!!")
            elif search_option == 'memory bandwidth':
                while True:
                    try:
                        memory2 = input('\nMemory Bandwidth(GB/s): ')
                        if memory2 == 'quit':
                            break
                        elif memory2.isdigit():
                            memory2 = int(memory2)
                            break
                        else:
                            print('Invalid!')
                    except:
                        print("ERROR 11!!!")
                while True:
                    try:
                        if memory2 == 'quit':
                            break
                        else:
                            faster_slower = input(f"GPUs with a greater or smaller bandwidth than {memory2}GB/s?: ").lower()
                            if faster_slower == 'faster':
                                recent_search = (f"GPU/Memory Speed/Faster Than/{memory2}GB/s")
                                recent_searches(recent_search)
                                list = []
                                for bandwidth in results:
                                    if memory2 < bandwidth[8]:
                                        list.append(bandwidth)
                                print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                                break
                            elif faster_slower == 'slower':
                                recent_search = (f"GPU/Memory Speed/Faster Than/{memory2}GB/s")
                                recent_searches(recent_search)
                                list = []
                                for bandwidth in results:
                                    if memory2 > bandwidth[8]:
                                        list.append(bandwidth)
                                print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                                break
                            elif faster_slower == 'quit':
                                break
                            else:
                                print("Invalid!")
                    except:
                            print("ERROR 12!!!")
            elif search_option == "launch date":
                while True:
                    try:
                        date = input("\nEnter a launch date YYYY-MM-DD: ")
                        print("\nOptions:")
                        print("- 'Before' to see GPUs launched before the chosen date")
                        print("- 'After' to see GPUs launched after the chosen date")
                        before_after = input("Select: ")
                        if before_after == 'before':
                            recent_search = (f"GPU/Launch Date/Before/{date}")
                            recent_searches(recent_search)
                            sql1 = (f"SELECT * FROM graphics_cards WHERE launch_date < '{date}' ORDER BY launch_date DESC;")
                            cursor1 = dbMain.cursor()
                            cursor1.execute(sql1)
                            results2 = cursor1.fetchall()
                            list = []
                            for dates in results2:
                                list.append(dates)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            break
                        elif before_after == 'after':
                            recent_search = (f"GPU/Launch Date/After/{date}")
                            sql1 = (f"SELECT * FROM graphics_cards WHERE launch_date > '{date}' ORDER BY launch_date DESC;")
                            cursor1 = dbMain.cursor()
                            cursor1.execute(sql1)
                            results2 = cursor.fetchall()
                            list = []
                            for dates in results2:
                                list.append(dates)
                            print(tabulate(list, headers=headers, tablefmt="rst", colalign=("left", "left", "left", "left", "left", "left", "left", "left", "left", "left")))
                            break
                        elif before_after == 'quit':
                            break
                        else:
                            print("Invalid!")
                    except:
                        print("ERROR 13!!!")
            elif search_option == 'quit':
                if sign_in == "guest":
                    return
                else:
                    cursor1 = dbMain.cursor()
                    if len(recent_searchesL) == 0:
                        return
                    elif len(recent_searchesL) == 1:
                        recentVal = (f"{recent_searchesL[0]}")
                        sql_recent_search = (f"UPDATE users SET recent_searches = '{recentVal}' WHERE username = '{username}';")
                        cursor1.execute(sql_recent_search)
                        dbMain.commit()
                        dbMain.close()
                        return
                    elif len(recent_searchesL) == 2:
                        recentVal = (f"{recent_searchesL[0]},{recent_searchesL[1]}")
                        sql_recent_search = (f"UPDATE users SET recent_searches = '{recentVal}' WHERE username = '{username}';")
                        cursor1.execute(sql_recent_search)
                        dbMain.commit()
                        dbMain.close()
                        return
                    elif len(recent_searchesL) == 3:
                        recentVal = (f"{recent_searchesL[0]},{recent_searchesL[1]},{recent_searchesL[2]}")
                        sql_recent_search = (f"UPDATE users SET recent_searches = '{recentVal}' WHERE username = '{username}';")
                        cursor1.execute(sql_recent_search)
                        dbMain.commit()
                        dbMain.close()
                        return
                    elif len(recent_searchesL) == 4:
                        recentVal = (f"{recent_searchesL[0]},{recent_searchesL[1]},{recent_searchesL[2]},{recent_searchesL[3]}")
                        sql_recent_search = (f"UPDATE users SET recent_searches = '{recentVal}' WHERE username = '{username}';")
                        cursor1.execute(sql_recent_search)
                        dbMain.commit()
                        dbMain.close()
                        return
                    elif len(recent_searchesL) == 5:
                        recentVal = (f"{recent_searchesL[0]},{recent_searchesL[1]},{recent_searchesL[2]},{recent_searchesL[3]},{recent_searchesL[4]}")
                        sql_recent_search = (f"UPDATE users SET recent_searches = '{recentVal}' WHERE username = '{username}';")
                        cursor1.execute(sql_recent_search)
                        dbMain.commit()
                        dbMain.close()
                        return
                    else:
                        print('Invalid!')
        except:
            print("ERROR 43!!!")


def add_gpu():
    while True:
        try:
            gpu_brand = input("GPU Brand: ")
            if gpu_brand == 'quit':
                return
            elif len(gpu_brand) >= 3:
                gpu_brand = gpu_brand.title()
                break
            else:
                print("Please enter a brand.")
        except:
            print("ERROR 14!!!")
    while True:
        try:
            gpu_model = input("GPU Model: ")
            if gpu_model == 'quit':
                return
            elif len(gpu_model) >= 5:
                gpu_model = gpu_model.upper()
                break
            else:
                print("Please enter a model.")
        except:
            print("ERROR 15!!!")
    while True:
        try:
            gpu_base_speed = input("Base Speed(GHz): ")
            if gpu_base_speed == 'quit':
                return
            elif float_value(gpu_base_speed):
                gpu_base_speed = float(gpu_base_speed)
                break
            else:
                print("That's not a speed!")
        except:
            print("ERROR 16!!!")
    while True:
        try:
            gpu_boost_speed = input("Boost Speed(GHz): ")
            if gpu_boost_speed == 'quit':
                return
            elif float_value(gpu_boost_speed):
                gpu_boost_speed = float(gpu_boost_speed)
                break
            else:
                print("That's not a speed!")
        except:
            print("ERROR 17!!!")
    while True:
        try:
            architecture_add = input("Architecture:")
            if architecture_add == 'quit':
                return
            elif len(architecture_add) >= 4:
                architecture_add = architecture_add.title()
                break
            else:
                print("Please enter a architecture.")
        except:
            print("ERROR 18!!!")
    while True:
        try:
            dlss_fsr = input("DLSS/FSR Gen: ")
            if dlss_fsr == 'quit':
                return
            elif dlss_fsr.isdigit():
                dlss_fsr = int(dlss_fsr)
                break
            else:
                print("That's not a DLSS/FSR gen!")
        except:
            print("ERROR 19!!!")
    while True:
        try:
            memory_type = input("Memory Type: ")
            if memory_type == 'quit':
                return
            elif len(memory_type) >= 4:
                memory_type = memory_type.upper()
                break
            else:
                print("Please enter a valid memory type.")
        except:
            print("ERROR 20!!!")
    while True:
        try:
            memory_amount = input("Memory Amount(GB): ")
            if memory_amount == 'quit':
                return
            elif memory_amount.isdigit():
                memory_amount = int(memory_amount)
                break
            else:
                print("Please enter a valid memory amount.")
        except:
            print("ERROR 21!!!")
    while True:
        try:
            memory_speed = input("Memory Bandwidth(GB/s): ")
            if memory_speed == 'quit':
                return
            elif memory_speed.isdigit():
                memory_speed = int(memory_speed)
                break
            else:
                print("Please enter a valid memory bandwidth.")
        except:
            print("ERROR 22!!!")
    while True:
        try:
            launch_date = input("Launch Date(YYYY-MM-DD): ")
            if launch_date == 'quit':
                print("All the input data will not be added.")
                return
            else:
                date_values = (launch_date.split("-"))
                if int(date_values[0].isdigit()):
                    if int(date_values[1].isdigit()) and int(date_values[1]) <= 12:
                        if int(date_values[2].isdigit()) and int(date_values[2]) <= 31:
                            launch_date = (f"{date_values[0]}-{date_values[1]}-{date_values[2]}")
                            break
                        else:
                            print("Please enter a valid date.")
                    else:
                        print("Please enter a valid date.")
                else:
                    print("Please enter a valid date.")
        except:
            print("ERROR 23!!!")
    sql2 = (f"INSERT INTO graphics_cards VALUES ('{gpu_brand}', '{gpu_model}', '{gpu_base_speed}', '{gpu_boost_speed}', '{architecture_add}', '{dlss_fsr}', '{memory_type}', '{memory_amount}', '{memory_speed}', '{launch_date}');")
    dbAdd = sqlite3.connect('Database.db')
    cursor2 = dbAdd.cursor()
    cursor2.execute(sql2)
    dbAdd.commit()
    dbAdd.close()


def delete_gpu():
    dbMain = sqlite3.connect('Database.db') # Create a variable that connects to the database
    cursor = dbMain.cursor() # Create a cursor
    sql = "SELECT * FROM graphics_cards;" # Create a variable with the prompt to fetch all data from the graphics cards table
    cursor.execute(sql) # Execute the prompt
    results = cursor.fetchall() # Store the prompts results in a variable
    print("Welcome to GPU delete, select a GPU by model to delete.")
    while True:
        try:
            gpu_delete = input("Delete: ").upper()
            if gpu_delete == 'QUIT':
                dbMain.close()
                return
            else:
                for deletable_gpus in results:
                    if gpu_delete == deletable_gpus[1]:
                        sql3 = (f"DELETE FROM graphics_cards WHERE model = '{gpu_delete}';")
                        dbDelete = sqlite3.connect('Database.db')
                        cursor3 = dbDelete.cursor()
                        cursor3.execute(sql3)
                        dbDelete.commit()
                        dbDelete.close()
                        dbMain.close()
                        return
        except:
            print("ERROR 24!!!")


def user_login():
    usernames = []
    sqlLogin = ("SELECT * FROM users;")
    dbLogin = sqlite3.connect('Database.db')
    cursorLogin = dbLogin.cursor()
    cursorLogin.execute(sqlLogin)
    users = cursorLogin.fetchall()
    while True:
        try:
            global username
            username = input("Username: ")
            for usernamesAvailable in users:
                usernames.append(usernamesAvailable[2])
            if username in usernames:
                break
            elif username == 'quit':
                dbLogin.close()
                return
            else:
                print("That username is not in the system!")
        except:
            print("ERROR 25!!!")
    while True:
        try:
            global password
            password = input("Password: ")
            sqlLogin = (f"SELECT password FROM users WHERE username = '{username}';")
            cursorLogin.execute(sqlLogin)
            user_password = cursorLogin.fetchall()
            if password == 'quit':
                return
            else:
                passwordLogin1 = (password,)
                if passwordLogin1 == user_password[0]:
                    break
                else:
                    print("Password incorrect!")
        except:
            print("ERROR 28!!!")
    sqlLogin = (f"SELECT name, surname FROM users WHERE username = '{username}';")
    cursorLogin.execute(sqlLogin)
    name_surname = cursorLogin.fetchall()
    for item in name_surname:
        print(f"Welcome {item[0]} {item[1]}")
    dbLogin.close()


def user_create():
    while True:
        try:
            global name
            name = input("First Name: ").title()
            if len(name) < 2:
                print("That name is not long enough!")
            elif name == 'Quit':
                return
            else:
                break
        except:
            print("ERROR 29!!!")
    while True:
        try:
            global surname
            surname = input("Last Name: ").title()
            if len(surname) < 2:
                print("That last name is not long enough.")
            elif surname == 'Quit':
                return
            else:
                break
        except:
            print("ERROR 30!!!")
    while True:
        try:
            global username
            username = input("Username(Atleast 5 characters long): ")
            if len(username) < 5:
                print("Are you retarded!?!?")
            elif username == 'quit':
                return
            else:
                sqlUser_add = ("SELECT * FROM users;")
                dbUser_add = sqlite3.connect("Database.db")
                cursorUser_add = dbUser_add.cursor()
                cursorUser_add.execute(sqlUser_add)
                dbUsernames = cursorUser_add.fetchall()
                for usernames in dbUsernames:
                    usernamesL.append(usernames[2])
                if username in usernamesL:
                    print("That username is already taken!")
                else:
                    break
        except:
            print("ERROR 31!!!")
    while True:
        try:
            global password
            password = input("Password(8 to 20 characters long): ")
            if password == 'quit':
                return
            elif len(password) < 8:
                print("Are you retarded!?!?")
            elif len(password) > 20:
                print("WTF is wrong with you!?!?")
            else:
                break
        except:
            print("ERROR 32!!!")
    sqlUser_add = (f"INSERT INTO users (name, surname, username, password) VALUES ('{name}', '{surname}', '{username}', '{password}');")
    cursorUser_add.execute(sqlUser_add)
    dbUser_add.commit()
    dbUser_add.close()
    return
                

def gpu_application():
    dbRS = sqlite3.connect("Database.db")
    cursorRS = dbRS.cursor()
    sqlRS = (f"SELECT recent_searches FROM users WHERE username = '{username}';")
    cursorRS.execute(sqlRS)
    RS = cursorRS.fetchall()
    dbRS.close()
    num = 0
    print("\nRecent Searches: ")
    for searches in RS:
        print(f"- {searches[num]}")
        num + 1
    while True:
        try:
            if sign_in == 'quit':
                break
            else:
                print("\nOptions:")
                print("- 'Lookup' to lookup GPU(s)")
                print("- 'Add' to add a GPU to the database")
                print("- 'Delete' to delete a GPU from the database")
                print("- 'Edit' to edit a GPUs stats")
                option = input('\nSelect: ').lower()
                if option == 'lookup':
                    lookup()
                elif option == 'add':
                    add_gpu()
                elif option == 'quit':
                    break
                elif option == 'delete':
                    delete_gpu()
                elif option == 'edit':
                    gpu_edit()
                else:
                    print("That is not an option.")
        except:
            print("ERROR!!!")


def sign_in_main():
        while True:
            try:
                global sign_in
                global start_up
                start_up = 1
                print("\nOptions:")
                print("- 'Login' to login to your account")
                print("- 'Create' to create an account")
                print("- 'Guest' to login as a guest")
                sign_in = input("\nSelect: ").lower()
                if sign_in == 'login':
                    user_login()
                    if username == 'quit':
                        sign_in_main()
                    elif password == 'quit':
                        sign_in_main()
                    else:
                        gpu_application()
                elif sign_in == 'create':
                    user_create()
                    if name == 'Quit':
                        sign_in_main()
                    elif surname == 'Quit':
                        sign_in_main()
                    elif username == 'quit':
                        sign_in_main()
                    elif password == 'quit':
                        sign_in_main()
                    else:
                        gpu_application()
                elif sign_in == 'guest':
                    lookup()
                elif sign_in == 'quit':
                    return
                else:
                    print("That is not an option.")
            except:
                print("ERROR 27!!!")

    
print('Welcome to the graphics_card database!')
if start_up == 0:
    sign_in_main()
elif start_up == 1:
    print("Goodbye!")