#!/usr/bin/env python
'''
Below is a set of functions that I am brainstorming for an app that I need. I eventually want to 
make it into a simple web-page app. This will require extensive revising, as there are several 
redundancies (it is currently a monster).
'''
def get_frame():
	print "Please choose one of the following frame options: "
	print "Choose the number 1 for the 4-inch profile, "
	print "or the number 2 for the 2.3125-inch profile./n"
	frame_choice = raw_input("Type either the number 1 or the number 2.\n")
	#count = 3
	'''
	for attempt in range(3):
		print "You have", count, "attempts left.\n"
	if frame_choice in ["1", "2"]:
		return frame_choice
		break
	else:
		count = count - 1
	if count == 0:
		print "Please try again, sometime./n"
		quit()
		'''
	return frame_choice

def return_frame():
	answer = False
	frame_type = ""
	#count = 5
	while answer is False:
		frame_type = get_frame()
		if frame_type in ["1","2"]:
			answer = True
			break
		else:
			print "Wrong answer. Try again."
			#count = count - 1
			#print "you have %d tries left.\n" %(count)
	if answer is True:#Eventually place this inside the while loop
		return frame_type
	#else:
		#print "Please try again, sometime."
		#quit()

def get_frame_thickness(frame_type):
	wall_thickness = 0.000
	if frame_type == "1":
		wall_thickness = 1.039
	elif frame_type == "2":
		wall_thickness = 1.051
	print "Wall thickness: ", str(wall_thickness)
	return wall_thickness

def get_o_dims():
	o_dims = []
	o_w = raw_input("Please enter width of box as a decimal:\n")
	o_h = raw_input("Please enter height of box as a decimal:\n")
	print "Light box is %s\" W x %s\" H.\n" %(o_w, o_h)
	o_dims.append(float(o_w))
	o_dims.append(float(o_h))
	return o_dims

def get_i_dims(o_dims, frame_type):
	i_dims = list()
	wall_thickness = get_frame_thickness(frame_type)    
	for item in o_dims:
		i_dims.append(item - (2 * wall_thickness))
	return i_dims

#create a Dibond dim-retrieving function, patterned after get_i_dims() that returns full backer size
#after that, create a Dibond sheet-cutting function, based on the above and on light-bars that returns sheets

def get_dibond_dims(i_dims, frame_type):
	'''Calculates the dimensions of the Dibond on the back of the box. returns a dim list'''
	dibond_back = list()
	if frame_type == '1':
		dibond_w = i_dims[0]-.75
		dibond_h = i_dims[1]-.75
	else:
		dibond_w = i_dims[0]-.68
		dibond_h = i_dims[1]-.68		   
	dibond_back.append(dibond_w)
	dibond_back.append(dibond_h)
	return dibond_back
'''
def return_dibond_sheets(dibond_back, frame_type, light_bar_choice):
	#Do this...
	#You need to have the number of horizontal lights for this box to calculate here to 
	#break the seam
'''	
def is_ul():
	'''Asks wether light box is to be built to U.L. stndards. Returns boolean.'''
	ul = False
	answer = ""
	print "Is this a U.L. light box?"
	answer = raw_input("Enter y for yes or n for no. ")
	print "\n\n"
	answer = answer.lower()
	if answer == "y":
		ul = True
	return ul

def int_ext():
	'''Asks if light box is to be built as an interior or an exterior light box'''
	exterior = False
	answer = ""
	print "Is this light box interior or exterior?"
	answer = raw_input("Enter i for interior or e for exterior. ")
	answer = answer.lower()
	if answer == "e":
		exterior = True
	return exterior
	
def is_ext():
	'''Asks if light box is to be built as an interior or an exterior light box'''
	exterior = raw_input("is this an exterior box? Enter y for yes or n for no:\n")
	if exterior in['y', 'Y', 'n', 'N']:
		exterior = exterior.lower()
		if exterior is "y":
			ans = True
			return ans
		else:
			ans = False
			return ans
	else:
		print "Wrong input.\n"
		print "Please try again."
		quit()

def get_lightbar():
	'''Asks user which type of light bar they want to use and returns a number accordingly'''
	ul_reg = 1
	ce = 2
	ul_thin = 3
	light_bar = 0

	print"Please enter 1 for \"U.L\" L.E.D.s, 2 for \"C.E.\" L.E.D.s, or 3 for \"Low-Profile\" L.E.D.s."
	choice = raw_input("Enter 1, 2 or 3: \n")
	if choice == "1":
		light_bar = ul_reg
	elif choice == "2":
		light_bar = ce
	else:
		light_bar = ul_thin

	return light_bar    
    
def return_light_bar_dims(light_bar_choice):
	'''Returns dimensions of lightbars that are to be used in light box'''
	bar = light_bar_choice
	width = 0.00
	height = 0.00
	dims = list()
	if bar == 1:
		width = 23.5
		height = 2.365
	elif bar == 2:
		width = 23.5
		height = 2.387
	else:
		width = 23.625
		height = 2.940
	dims.append(width)
	dims.append(height)
	return dims

def thin_light_calc_h(i_dim_width, full_light):
	quotient = i_dim_width/full_light
	full_sum = int(quotient)
	remainder = quotient - full_sum
	remainder_sum = 0.0
	if remainder < full_light and remainder >= (full_light*.75):
		remainder_sum = 0.75
	elif remainder < (full_light*.75) and remainder >= (full_light*.5):
		remainder_sum = 0.5
	elif remainder < (full_light*.5) and remainder >= (full_light*.25):
		remainder_sum = 0.25
	else:
		remainder_sum = 0.0
	return full_sum+remainder_sum
	
def reg_light_calc_h(i_dim_h, full_light):
	#consider making this function call the i_dim function
	quotient = (i_dim_h/full_light)
	full_sum = int(quotient)
	remainder = quotient - full_sum
	remainder_sum = 0.0
	if remainder >= (full_light*.6):
		remainder_sum = 1.0
	elif remainder < (full_light*.6) and remainder >= (full_light*0.1):
		remainder_sum = 0.5
	else:
		remainder_sum = 0.0
	return full_sum+remainder_sum	
	
def light_calc_v(i_dim_v, light_height):
	quotient = i_dim_v/light_height
	light_sum_v = int(quotient)
	remainder = quotient - light_sum_v
	remainder_sum = 0
	if remainder >= .5:
		remainder_sum = 1
	return light_sum_v + remainder_sum

def all_light_calc_h(i_dims, light_bar_choice):
	light_bar_dims = return_light_bar_dims(light_bar_choice)
	#i_dims = get_i_dims(o_dims, frame_type)
	h_light_bar_count = 0.0
	v_light_bar_count = light_calc_v(i_dims[1], light_bar_dims[1])
	h_v_count = list()
	if light_bar_choice == 1 or light_bar_choice == 2:
		h_light_bar_count = reg_light_calc_h(i_dims[0], light_bar_dims[0])	
	else:
		h_light_bar_count = thin_light_calc_h(i_dims[0], light_bar_dims[0])	
	h_v_count.append(h_light_bar_count)
	h_v_count.append(v_light_bar_count)
	return h_v_count

def light_calc(light_sum_h, light_sum_v):
	'''Returns the number of lights to be used in the light box. Returns a float.'''
	total_lights = light_sum_h*light_sum_v
	return total_lights
	
def reg_inverter_calc(total_lights):
	'''Returns number of A.C. to D.C. inverters, based on the number of lights. Returns a float.'''
	power_supplies = total_lights/35.00
	full_supplies = int(power_supplies)
	remainder = power_supplies-full_supplies
	if remainder >= 0.1:
		full_supplies = full_supplies+1
	return full_supplies

def thin_inverter_calc(total_lights):
	'''Returns number of A.C. to D.C. inverters, based on the number of lights. Returns a float.'''
	power_supplies = total_lights/17.00
	full_supplies = int(power_supplies)
	remainder = power_supplies-full_supplies
	if remainder >= 0.1:
		full_supplies = full_supplies+1
	return full_supplies
	
def total_inverter_count(total_lights, light_bar_choice):
	'''Returns number of A.C. to D.C. inverters, based on the number of lights. Returns a float.'''
	inverter_count = 0
	if light_bar_choice == 1 or light_bar_choice ==2:
		inverter_count = reg_inverter_calc(total_lights)
	else:
		inverter_count = thin_inverter_calc(total_lights)
	return inverter_count		
	
def print_light_count(light_sum_h, light_sum_v):
	'''Prints out the total number of lights in the light box.'''
	total_h = light_sum_h
	full = int(total_h)
	partial = total_h - full
	str_full = str(full)
	str_partial = str(partial)
	if full == 1:
		print"This light box has one full column of lights with", str(light_sum_v), "bars"
	elif full > 1:
		print"This light box has", str(full), "full columns of lights with", str(light_sum_v), "bars"	
	if partial > 0:
		print" and one", str_partial, "column with", str(light_sum_v), "bars." 
	print"Total:", str(light_sum_h*light_sum_v), "bars."
	
def get_light_count_x(i_dim_width, lightbar_width):
	'''Calculates the number of light bars and sections that will fit horizontally within a light box.'''
	quotient = i_dim_width/lightbar_width
	int_quotient = int(quotient)
	diff = quotient - int_quotient
	light_count_x = 0.0
	addnum = 0
	if (lightbar_width == 23.5):
		if diff > 0.6:
			addnum = 1.0
		elif (diff >= 0.2) and (diff <= 0.6):
			addnum = 0.5
		else:
			addnum = 0.0
	else:
		if diff >= 0.75:
			addnum = 0.75
		elif (diff >= 0.5) and (diff < 0.75):
			addnum = 0.5
		elif (diff >= 0.25) and (diff < 0.5):
			addnum = 0.25
		else:
			addnum = 0.0
	
	light_count_x = int_quotient + addnum
	return light_count_x	

def overlapped_light_column_calc(i_dims, light_count_x, light_type):
	'''Called when the lights exceed inner dims and must overlap to fit within box.
	Returns a 2-item list of light columns and num of overlapped lights.'''
	return_info_list = list()#[0] is a list of column widths; [1] is the number of overlapped lights
	column_width_list = list()
	light_type = int(light_type)
	lightbar_width = 23.5
	first_ul_overlap = 1.852
	first_ce_overlap = 1.775
	dist_betw_ul_leds = 1.968
	dist_betw_ce_leds = 1.975
	width_moved = 0.0
	full_columns = int(light_count_x)
	half_columns = light_count_x - full_columns
	combo_column_width = 0.0
	new_width = lightbar_width*light_count_x # Starts as initial width, but is reduced
	overlapped_leds = 0	
	'''This will return a list of 1 or more columns.'''
	while new_width > i_dims:
		if overlapped_leds == 0:
			if light_type == 1:
				new_width = new_width - first_ul_overlap
				overlapped_leds = overlapped_leds + 1
			elif light_type == 2:
				new_width = new_width - first_ce_overlap
				overlapped_leds = overlapped_leds + 1				
		else:
			if light_type == 1:
				new_width = new_width - dist_betw_ul_leds
				overlapped_leds = overlapped_leds + 1
			elif light_type == 2:
				new_width = new_width - dist_betw_ce_leds
				overlapped_leds = overlapped_leds + 1
	#Combine overlapped column and get its combined width
	if half_columns > 0:
		#Combine a new column using the half-column with an adjacent full column - return width
		full_columns = (full_columns - 1)
		combo_column_width = (new_width - (full_columns*lightbar_width))
	else:
		#combine the last full column with the previous full column - return width
		full_columns = (full_columns - 2)
		combo_column_width = (new_width - (full_columns*lightbar_width))
	columns = (full_columns + 1) #add num of columns and one for the combo column
	#Add column widths to list of column widths
	for column in range(full_columns):
		column_width_list.append(lightbar_width)
		
	column_width_list.append(combo_column_width)
	return_info_list.append(column_width_list)
	return_info_list.append(overlapped_leds)
	print return_info_list
	return return_info_list

#Create a light_count_y that works the same as x, but is vertically oriented

def get_frame_dims(frame_type):
	frame_list = list()
	frame_thickness = 0.0
	od2db = 0.0
	id2db = 0.0
	if frame_type == 1:
		frame_thickness = 1.039
		id2db = .496
		od2db = 1.534
	else:
		frame_thickness = 1.051
		id2db = .534
		od2db = 1.585
	frame_list = [frame_thickness, od2db, id2db]
	return frame_list

def overlap_sections_h(box_width, od2lightbar, db2lightbar, column_list, lightbar_width):
	'''Takes a list of columns (one with an overlap) and gives a list of sections'''
	num_columns = len(column_list)
	columns = column_list #Copies the list
	last_column = 0.0
	first_column = 0.0
	single_column = 0.0
	sections = list()
	remaining_columns = num_columns
	od2lightbar_r = True
	od2lightbar_l = True
	if len(columns) >= 3: #If there are at least 3 single columns to work with
		if (columns[-1] + db2lightbar) <= 48:# This should be true in any case
			last_column = colums[-1] + od2lightbar
			del columns[-1]#deletes the last item
			od2lightbar_r = False
		else:
			print "Overlap column is too wide. Fix this...\n"
		if (db2lightbar+columns[0]+columns[1]) <= 48:
			first_column = (od2lightbar + columns[0] + columns[1])
			del columns[0]#deletes the 0 element
			del columns[0]#deletes the following 0 element
			sections.append(first_column)
			od2lightbar_l = False
		else:
			first_column = (od2lightbar + columns[0])#Makes first column from one light column
			del columns[0]#deletes the 0 element
			sections.append(first_column)
			od2lightbar_l = False
	#Maybe make sure that the frame-sides have been bumped from the list
	evencolumns = len(columns)/2#This is how many pairs of even columns are in the list
	for pairedcolumns in range(evencolumns):
		sections.append(lightbar_width*2)#add paired columns to section list
	if len(columns)%2 != 0:#If there was an odd number of columns - add that single one to list
		sections.append(lightbar_width)
	sections.append(last_column)
	return sections

def overlap_sections_h_new(box_width, od2lightbar, db2lightbar, column_list, lightbar_width):
	'''Takes a list of columns (one with an overlap) and gives a list of sections'''
	num_columns = len(column_list)
	columns = column_list #Copies the list
	last_column = 0.0
	first_column = 0.0
	single_column = 0.0
	sections = list()
	remaining_columns = num_columns
	od2lightbar_r = True
	od2lightbar_l = True
	
	if len(columns) == 1:
		if (columns[0] + (2*db2lightbar)) <= 48:
			sections.append(box_width)
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
	elif len(columns) == 2:
		if (columns[0] + columns[1] + (2*db2lightbar)) <= 48:
			sections.append(box_width)
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
		else:
			first_column = (columns[0]+od2lightbar)
			last_column = (columns[1]+od2lightbar)
			sections.append(first_column)
			sections.append(last_column)
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
	if len(columns) >= 3: #If there are at least 3 single columns to work with
		if (columns[-1] + db2lightbar) <= 48:# This should be true in any case
			last_column = colums[-1] + od2lightbar
			del columns[-1]#deletes the last item
			od2lightbar_r = False
		else:
			print "Overlap column is too wide. Fix this...\n"
		if (db2lightbar+columns[0]+columns[1]) <= 48:
			first_column = (od2lightbar + columns[0] + columns[1])
			del columns[0]#deletes the 0 element
			del columns[0]#deletes the following 0 element
			sections.append(first_column)
			od2lightbar_l = False
		else:
			first_column = (od2lightbar + columns[0])#Makes first column from one light column
			del columns[0]#deletes the 0 element
			sections.append(first_column)
			od2lightbar_l = False
			#Ends of box have been addressed, now move on to center sections
	#Maybe make sure that the frame-sides have been bumped from the list
	evencolumns = len(columns)/2#This is how many pairs of even columns are in the list
	for pairedcolumns in range(evencolumns):
		sections.append(lightbar_width*2)#add paired columns to section list
	if len(columns)%2 != 0:#If there was an odd number of columns - add that single one to list
		sections.append(lightbar_width)
	sections.append(last_column)
	return sections

def sections_h(box_width, od2lightbar, db2lightbar, column_list, lightbar_width):
	'''Takes a list of columns from one to many (no overlaps), and gives a list of sections'''
	num_columns = len(column_list)
	columns = column_list #Copies the list
	last_column = 0.0
	first_column = 0.0
	sections = list()
	od2lightbar_r = True
	od2lightbar_l = True
	'''od2lightbar should have an attribute to show that it is still present'''
	remaining_columns = num_columns
	if len(columns) == 1:
		if (columns[0] + (2*db2lightbar)) <= 48:
			sections.append(box_width)
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
	elif len(columns) == 2:
		if (columns[0] + columns[1] + (2*db2lightbar)) <= 48:
			sections.append(box_width)
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
		else:
			first_column = (columns[0]+od2lightbar)
			last_column = (columns[1]+od2lightbar)
			sections.append(first_column)
			sections.append(last_column)
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
	elif len(columns) == 3:
		if (column[-1] < column[1]) and ((column[-1]+column[1]+db2lightbar) <= 48)):
			#combine the two last columns and frame into the last section
			#combine the first column and frame into the 1st section
			last_column = (columns[-1]+columns[-2]+od2lightbar)
			first_column = (columns[0]+od2lightbar)
			sections.append(first_column)
			sections.append(last_column)
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
		elif (column[0]+column[1]+db2lightbar) <= 48:
			#combine the two first columns and frame into the last section
			first_column = (columns[0]+columns[1]+od2lightbar)
			sections.append(first_column)
			last_column = (columns[-1]+od2lightbar)
			sections.append(last_column)#Append the last column (with frame) to list
			od2lightbar_l = False
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
		else:
			#take first section and last section, and then take the middle section
			#This will most likely never happen
			first_column = (columns[0]+columns[1]+od2lightbar)
			sections.append(first_column)
			od2lightbar_l = False
			del columns[0]#Delete first column (with frame)
			last_column = (columns[-1]+od2lightbar)
			del columns[-1]#Delete last column (with frame)
			sections.append.(columns[0])#Append the remaining/center column in list
			sections.append(last_column)#Append last column with frame
			od2lightbar_r = False
			#sections of light box have been collected into a list. Function finished!
	elif len(columns) >= 4: #If there are at least 4 single columns to work with
		if (columns[-1] + columns[-2] + db2lightbar) <= 48:#Knock out last_column
			last_column = (columns[-1] + columns[-2] + od2lightbar)#Makes 2 light bar column
			del columns[-1]#deletes the last item
			del columns[-1]#deletes the new last item
			remaining_columns = remaining_columns - 2
			od2lightbar_r = False
		else:
			last_column = (columns[-1] + od2lightbar)#Makes a column from one light bar width
			del columns[-1]#deletes the last item
			remaining_columns = remaining_columns - 1
			od2lightbar_r = False
		if (db2lightbar+columns[0]+columns[1]) <= 48:#Knock out first_column
			first_column = (od2lightbar + columns[0] + columns[1])#Makes 2 light bar column
			del columns[0]#deletes the 0 element
			del columns[0]#deletes the new 0 element
			remaining_columns = remaining_columns - 2
			od2lightbar_l = False
		else:
			first_column = (od2lightbar + columns[0])#Makes first column from one light column
			del columns[0]#deletes the 0 element
			remaining_columns = remaining_columns - 1
			od2lightbar_l = False
		sections.append(first_column)
	#By this point both first and last columns should be identified and first column is in the list
	count = 0
	if od2lightbar_l is False and od2lightbar_r is False:
		if (len(columns) >= 2):#This applies to several sections left over
			pairedcolumnsremaining = len(columns)/2#This is how many pairs of even columns remaining in list
			for pairedcolumns in range(pairedcolumnsremaining):
				sections.append(lightbar_width*2)#add paired columns to section list
				count = count + 2
		for items in range(count):
			del columns[0]#deletes the 0 element/deletes a column for each one added to the section list
		if len(columns)%2 != 0:#If there was an odd number of columns left-(one)-add that to list
			sections.append(lightbar_width)
			del columns[0]#deletes the 0 element, which should be the final remaining element
			remaining_columns - remaining_columns - 1
	sections.append(last_column)
	#sections of light box have been collected into a list. Function finished!
	return sections	#return the list of sections that were combined from columns
	
def get_dbpanels_h(sections, od2db):
	'''Takes a list of sections and returns a list of dibond panels'''
	section_list = sections
	dbpanels_h = list()
	if section_list > 2:
		dbpanels_h.append(section_list[0]-od2db)#Append the first Dibond section, minus the frame
		del section_list[0]
		for section in range(len(section_list)-1):
			dbpanels_h.append(section)#Append each section without a frame to the list
		dbpanels_h.append(section_list[-1]-od2db)#Append the last Dibond section, minus the frame
	elif section_list == 2:
		dbpanels_h.append(section_list[0]-od2db)#Append the first Dibond section, minus the frame
		dbpanels_h.append(section_list[-1]-od2db)#Append the last Dibond section, minus the frame
	else:
		dbpanels_h.append(section_list[0]-(od2db*2))#Append the sole Dibond section, minus the frames
	return dbpanels_h

def single_section(lightbox_width, od2db):
	'''To be used if the Dibond is <= 48" wide.'''
	section_width = list()
	if (lightbox_width - (2*od2db)) <= 48:
		section_width.append(lightbox_width)
		return section_width
	else:
		print "Lightbox will consist of more than one horizontal section.\n"
			
def get_sections_x(frame_type, o_dims):
	'''Takes 2 parameters and returns a list containing 2 lists - 1:sections, 2:dibond panels'''
	'''TO DO:
		PRINT OUT A LIST OF POSSIBLE SECTION POINTS, FROM LEFT SIDE
		PRINT OUT A LIST OF SUGGESTED SECTION AND DIBOND WIDTHS, FROM LEFT
		PRINT OPTIMAL CENTER POINTS, BASED ON SECTIONS'''
	max_dim = (16*12)#printer can only print 16' wide graphics
	section = 0.0
	dbpanel = 0.0
	output_list = list()
	h_sections = list()
	dibond_panels_w = list()
	start_point = 0.0 #The start point for each section, starts at 0. Width is added each time.
	remaining_box_width = o_dims[0]
	
	'''get frame dims from functions below'''
	light_bar_choice = get_lightbar()
	light_bar_dims = return_light_bar_dims(light_bar_choice)
	frame_list = get_frame_dims(int(frame_type))#returns list: frame_thickness, od2db, id2db
	frame_thickness = frame_list[0]
	od2db = frame_list[1]
	id2db = frame_list[2]
	
	remaining_dibond_w = o_dims[0] - (od2db*2)
	db2lightbar = 0.0
	od2lightbar = 0.0
	full_light_w = light_bar_dims[0]
	#light_h = light_bar_dims[1] #Height of a light bar and wire for one light unit		
	i_dims = (o_dims[0] - (2*frame_thickness))
	'''get width of all light bars inside box'''
	light_count_x = get_light_count_x(i_dims, full_light_w)
	width_of_lights = (light_count_x * full_light_w)
	light_column_list = list()
	new_width_of_lights = 0.0
	overlapped_light_count = 0
	od2lightbar = (o_dims[0] - width_of_lights)/2
	db2lightbar = od2lightbar - od2db
	light_overlap_list = list()
	h_sect_count = 0 #Counts sections from L to R
	full_columns = 0
	partial_column = 0.0
	overlapped_lights = False
	if width_of_lights > i_dims:
		#Alters width of lights to reflect the overlapping of bars...
		#The last bar will be combined with previous column.
		#Find out if lights are ce or ul before executing the next line
		print "Overlap of Lights Required..."
		overlapped_lights = True
		light_overlap_list = overlapped_light_column_calc(i_dims, light_count_x, light_bar_choice)
		light_column_list = light_overlap_list[0]
		for columnwidth in light_column_list:
			new_width_of_lights = new_width_of_lights + columnwidth#Width of lights with overlap
		
		overlapped_light_count = light_overlap_list[1]#int contents of 2nd list of 2-item list
		od2lightbar = (o_dims[0] - new_width_of_lights)/2
		db2lightbar = od2lightbar - od2db
		'''Now call the function that generates sections for overlapped lights'''
	else:
		full_columns = int(light_count_x)
		for column in range(full_columns):
			light_column_list.append(full_light_w)
		if full_columns < light_count_x:
			partial_column = light_count_x - full_columns
			light_column_list.append((partial_column * full_light_w))
		'''Now call the function that generates sections for non-overlapped lights'''
		
	print "Width of Lights Within Box: ", new_width_of_lights
	print "Dist From Edge to Light Bar: ", od2lightbar
 	print "Dist From Dibond Edge to Light Bar: ", db2lightbar
	print "Original Width of Light Bars: ", width_of_lights
	print "Inner Width of Light Box: ", i_dims
	print "Column Widths: ", light_column_list
	'''*******************************************************************'''
	'''The following while loop should be obsolete after using the new functions'''
	#horizontal calcs below:
	
	if overlapped_lights is True:
		if len(light_column_list) == 1:
			section = single_section(lightbox_width, od2db)# this is fine
			h_sections.append(section)
		else:
			 sections_h(remaining_box_width, od2lightbar, db2lightbar, light_column_list, full_light_w)
		'''
		elif len(light_column_list) == 2:
			# make a function that takes care of only two columns
		elif len(light_column_list) >= 3:
			#This should be either >= 3 or == 3
			'''
	else:
		h_sections = 
		'''
		if len(light_column_list) == 1:
			section = single_section(lightbox_width, od2db)# this is fine
			h_sections.append(section)		
		elif len(light_column_list) == 2:
			# make a function that takes care of only two columns
		elif len(light_column_list) == 2:
			# make a function that takes care of only two columns
			'''		
		
	while remaining_box_width > 0:
		'''Create a new function for a condition where the Dibond is < 48.'''
		if remaining_dibond_w <= 48 and h_sect_count == 0: # if the dibond between the frame sides <= 48: one horizontal section
			section = remaining_box_width
			h_sections.append(section)
			dbpanel = (section - (od2db * 2))
			dibond_panels_w.append(dbpanel)
			remaining_box_width = remaining_box_width - section
			remaining_dibond_w = remaining_dibond_w - dbpanel
			start_point = section
			h_sect_count = h_sect_count + 1
			print "A"
			#Now move on to vertical sectioning, if necessary
		elif remaining_dibond_w > 48 and h_sect_count == 0:  
			if (db2lightbar + (full_light_w * 2)) <= 48:
				section = (od2lightbar + (full_light_w * 2))
				h_sections.append(section)
				dbpanel = (section - od2db)
				print "B1", dbpanel
				dibond_panels_w.append(dbpanel)
				print "B1", dibond_panels_w
				remaining_box_width = remaining_box_width - section
				remaining_dibond_w = (remaining_dibond_w - dbpanel)
				start_point = section
				h_sect_count = h_sect_count + 1 
				print "B1"
			elif (db2lightbar + (full_light_w * 2)) > 48:
				section = (od2lightbar + full_light_w)
				print "B2", section
				print "OD2L",od2lightbar, "FLW", full_light_w
				h_sections.append(section)
				dbpanel = (section - od2db)
				print "B2", dbpanel
				dibond_panels_w.append(dbpanel)
				print "B2", dibond_panels_w
				remaining_box_width = remaining_box_width - section
				remaining_dibond_w = (remaining_dibond_w - dbpanel)
				start_point = section
				h_sect_count = h_sect_count + 1	
				print "B2"	
		elif (remaining_box_width > ((full_light_w * 2) + od2lightbar)) and (h_sect_count > 0):
			section = (full_light_w * 2)
			h_sections.append(section)
			dbpanel = section
			print "C", dbpanel
			dibond_panels_w.append(dbpanel)
			print "C", dibond_panels_w
			remaining_box_width = (remaining_box_width - section)
			remaining_dibond_w = (remaining_dibond_w - dbpanel)
			start_point = section
			h_sect_count = h_sect_count + 1
			print "C"
		elif (remaining_box_width <= ((full_light_w * 2) + od2lightbar)) and (h_sect_count > 0):
			section = remaining_box_width
			print "D", section
			h_sections.append(section)
			print "OD2L",od2lightbar, "FLW", full_light_w 
			dbpanel = (section - od2db)
			print "D", dbpanel
			dibond_panels_w.append((dbpanel))
			print "D", dibond_panels_w
			remaining_box_width = remaining_box_width - section
			remaining_dibond_w = (remaining_dibond_w - dbpanel)
			start_point = section
			h_sect_count = h_sect_count + 1
			#there should be nothing left after this
			print "D"
	output_list.append(h_sections)
	output_list.append(dibond_panels_w)
	return output_list

def create_lightbar():
	"""Generates a lightbar instance from the Lightbar class"""
	light_choice = ''
	print "Please choose an L.E.D. light type from the following options:"
	print "Type the number 1 for a regular, U.L. approved, 23.5\" L.E.D. light"
	print "Type the number 2 for a C.E.-style, 23.5\" long light L.E.D. light."
	print "Type the number 3 for U.L. approved, 23.625\" long, low-profile L.E.D. lights.\n"
	light_choice = raw_input("Please enter either 1, 2 or 3: \n")
	if light_choice in ["1", "2", "3"]:
		light_choice = int(light_choice)
	else:
		print "Bad choice."
		quit()
	if light_choice in [1,3]:
		ul = True
	else:
		ul = False	
	#ul = is_ul()
	ext = is_ext()
	light_bar = Lightbar(light_choice, ul, ext)
	return light_bar

class Lightbar:
	"""An L.E.D. bar of varying dims and qualities."""
	"""This class needs to generate light bar height, as well"""
	def __init__(self, type, is_ul, ext):
		self.type = type # 1 for UL reg, 2 for CE, 3 for UL Low-Profile - from a function
		self.is_ul = True # value is given as true, until otherwise indicated
		self.exterior = False
		
	def get_divisions(self):
		# returns number of divisions that light bar can be broken into (2 or 4)
		if self.type == 1 or self.type == 2:
			divisions = 2
		else:
			divisions = 4
		return divisions
		
	def assign_dims(self):
		#assigns and returns dimensions of instantiation based on type of light bar
		if self.type == 1 or self.type == 2:
			full = 23.5
		else:
			full = 23.625
		return full
		
	def section_length(self):
		#Returns section lengths
		divs = self.get_divisions()
		full = self.assign_dims()
		section_len = full/divs
		return section_len
		
	def ul_bool(self):
		ul = True
		if type == 2:
			ul = False
		else: 
			ul = True
		return ul
	
def main():
	print"Welcome to the light box app!"
	print"Get ready for some fun!!!\n"
  frame_type = return_frame() #asks for either 4" (a) or 2 5/16" (b) type profiles
  o_dims = get_o_dims() #2-item list of exterior dims of light box 
  ##i_dims = get_i_dims(o_dims, frame_type) #2-item list of interior dims
  #light_bar_choice = get_lightbar(frame_type) #choice of 1 (ul reg), 2 (ce) or 3 (low-profile)
  ##light_bar = create_lightbar()#Creates from the Lightbar class
  #light_bar_dims = return_light_bar_dims(light_bar_choice) #2-item list of bar w and h
  ##h_v_light_bar_count = reg_thin_light_calc_h(o_dims, frame_type, light_bar_choice)
  #exterior_lights = int_ext() #Are lights interior or exterior? 
  ##total_light_count = light_calc(h_v_light_bar_count[0], h_v_light_bar_count[1])
  ##print_light_count(h_v_light_bar_count[0], h_v_light_bar_count[1])
  ##power_inverters = total_inverter_count(total_light_count, light_bar_choice) 
  #light_bar_dims = return_light_bar_dims(light_bar_choice)
  sections = get_sections_x(frame_type, o_dims)
  print sections
  print "The End..."

if __name__ == "__main__":
  main()
