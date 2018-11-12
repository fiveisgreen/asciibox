#!/usr/bin/env python
# Instructions: First choose settings and insert textbox text in the control panel. Then run from the terminal:
#               $ python asciibox.py

###############################################################
# ################### Table of Contents ##################### #
#                                                             #
# __Control_Pannel    The User Interface; start here.         #
# __Hypnotoad         All Glory to the Hypnotoad              #
# __box_styles list   A list of available box styles.         #
# __Gallery           A showcase of available box styles      #
# __endgallery                                                #
#.............................................................#
# __Art_Code          The code that makes the art             #
# __endart                                                    #
# __switch            A long switch that interprets box_style #
# __Machinery         Some shady robots                       #
# __Execution         Where the program execution starts.     #
# __TODO_list         A place to plan improvements.           #
# __Credits           Who made this thing.                    #
###############################################################

###########################################################################################################################################
#    ______   ______    __   __   __________  ______     ______    __         ______      ___       __   __   __   __   _______  __       #
#   /      | /  __  \  |  \ |  | |          ||   _  \   /  __  \  |  |       |   _  \    /   \     |  \ |  | |  \ |  | |   ____||  |      #
#  |  ,----'|  |  |  | |   \|  | `---|  |---`|  |_)  | |  |  |  | |  |       |  |_)  |  /  ^  \    |   \|  | |   \|  | |  |__   |  |      #
#  |  |     |  |  |  | |  . `  |     |  |    |      /  |  |  |  | |  |       |   ___/  /  /_\  \   |  . `  | |  . `  | |   __|  |  |      #
#  |  `----.|  `--'  | |  |\   |     |  |    |  |\  \-.|  `--'  | |  `---.   |  |     /  _____  \  |  |\   | |  |\   | |  |____ |  `---.  #
#   \______| \______/  |__| \__|     |__|    | _| `.__| \______/  |______|   | _|    /__/     \__\ |__| \__| |__| \__| |_______||______|  #
#                                                                                                                                         #
#__Control_Pannel##########################################################################################################################

box_style = "starfield" 		#This determines which type of box you get. See __box_styles, __Gallery

#Put text here to be made into a box
longtext = \
"""
Insert here the text that you want 
made into an artistic text box
"""

centering = "center" 			#options: "center"=centered text with padding, "left"=left with padding, "none"

comment_style = "python" 		#Viable options: "none", "Cshort"=//, "Clong"=/*...*/, "shell"="python"="pyshort"=#, "pylong"=tripple quotes, "latex"=%, "custom"
##for use with "custom":##
custom__comment_mark = "#"      	
custom__use_short_comments = True 	#false sets long comment style like /*...*/, true sets inline comments like // in C, or # in python. 

N_tabs_before_comment_mark = 0		#number of tabs in front of everything, including comment marks
N_quadspaces_before_comment_mark = 0  	#number of 4_space indenting in front of everything, including comment mark
N_tabs_after_comment_mark = 1		#number of tabs after comment mark, but before the art. Use to create white space to the left of the art.

min_struct_width = 68 			#Minimum values for the width and length of the printed structure. Use these to add white space padding 
min_struct_length = 0			#or to just make a structure the size you want.

####################################################################################################################################
##             ,'``.._   ,'``.                                                                                                    ##
##            :,--._:)\,:,._,.:                Hypnotoad wants you to check out Patrick Gillespie's ASCII Art Generator           ## 
##            :`--,''   :`...';\             http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20         ##
##             `,'       `---'  `.                                 All Glory to the Hypnotoad!                                    ##
##             /                 :                                                                                                ##
##            /                   \                                                                                               ##
##          ,'                     :\.___,-.                                                                                      ##
##         `...,---'``````-..._    |:       \                                                                                     ##
##           (                 )   ;:    )   \  _,-.                                                                              ##
##            `.              (   //          `'    \                                                                             ##
##             :               `.//  )      )     , ;                                                                             ##
##           ,-|`.            _,'/       )    ) ,' ,'                                                                             ##
##          (  :`.`-..____..=:.-':     .     _,' ,'                                                                               ##
##           `,'\ ``--....-)='    `._,  \  ,') _ '``._                                                                            ##
##        _.-/ _ `.       (_)      /     )' ; / \ \`-.'                                                                           ##
##       `--(   `-:`.     `' ___..'  _,-'   |/   `.)                                                                              ##
##           `-. `.`.``-----``--,  .'                                                                                             ##
##             |/`.\`'        ,',');                                                                                              ##
##                 `         (/  (/                                                                                               ##
##__Hypnotoad#######################################################################################################################

#Viable __box_styles 
"none"	 			#use this to put comment marks in front of text. No art is made.
"hashbox" "hashfield" 		#use for python, shell
"Celegance" "slashfield" 	#use for C
"dotbox"
"starbox" "starfield"
"scroll1" "scroll2"
"bracketbox"
"moo"
"doubleline"
"celtic1" "celtic2" "celtic3" "celtic4"
#"xkcd"
"4dotbox"
"mathbox"
"slashes"
"diamonds" "diamonds2"
"wavy"
"8o"
"signpost"
"hearye"
"fancy1" "fancy2" "fancy3" "fancy4"
"pansies"
"gingerbread"
"christmas"
"hearts"
"ducks"
"butterflies"
"vines"
"hex"
"percentbox"
"percentfield"
#walls:
"floral"
"diamondwall" #repeat, fix
"downarrows"
"uparrows"
"wavyline"
#structures
#hashline
#slashline

#Prepare and process user interface 
centering_dict = {"center":1, "left":0, "none":2}

############################################################################
#    ______       ___       __      __      _______  ______  ____    ____  #
#   /  ____|     /   \     |  |    |  |    |   ____||   _  \ \   \  /   /  #
#  |  |  __     /  ^  \    |  |    |  |    |  |__   |  |_)  | \   \/   /   #
#  |  | |_ |   /  /_\  \   |  |    |  |    |   __|  |      /   \_    _/    #
#  |  |__| |  /  _____  \  |  `---.|  `---.|  |____ |  |\  \-.   |  |      #
#   \______| /__/     \__\ |______||______||_______|| _| `.__|   |__|      #
#                                                                          #
#__Gallery##################################################################

	#See also the file ascii.h, which has some more art.

	#	************************************	 ************************************************************
	#	*                                  *	 ************************************************************
	#	*                                  *	 ************************************************************
	#	*        This is a #starbox        *	 ******************* This is a #starfield *******************
	#	*                                  *	 ************************************************************
	#	*                                  *	 ************************************************************
	#	************************************	 ************************************************************

	#	/************************************************\	  	{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}
	#	 *                                              * 	 	{}                                {}
	#	 *          This is a #Celegance  box           * 	 	{}                                {}
	#	 *               Ideal for C/C++                * 	 	{}      This is a #bracketbox     {}
	#	 *     Needing no comment marks of it's own     * 	 	{}                                {}
	#	 *                                              * 	 	{}                                {}
	#	\************************************************/	  	{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}

	#	//////////////////////////////////////////////////
	#	//////////////////////////////////////////////////
	#	////////////// This is a #slashfield /////////////
	#	//////////////// Ideal for C/C++ /////////////////
	#	////// Needing no comment marks of it's own //////
	#	//////////////////////////////////////////////////
	#	//////////////////////////////////////////////////

	#	//////////////////////////////////////////////////////////////////////////////////////
	#	/////////////////////////////// This is a #slashfield  ///////////////////////////////
	#	/////////////// Ideal for C/C++, needing no comment marks of it's own ////////////////
	#	//////////////////////////////////////////////////////////////////////////////////////

	#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	#%%%%%%%%%%%%%%%%%%%%%%%%%%%% This is a #percentfield %%%%%%%%%%%%%%%%%%%%%%%%%%%
	#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Ideal for LaTeX %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	#	 __________________________________ 	  	::::::::::::::::::::::::::::
	#	| .______________________________. |	  	::::::::::::::::::::::::::::
	#	| |                              | |	  	::::                    ::::
	#	| |     This is a #doubleline    | |	  	:::: This is a #4dotbox ::::
	#	| |                              | |	  	::::                    ::::
	#	| |______________________________| |	  	::::::::::::::::::::::::::::
	#	|__________________________________|	  	::::::::::::::::::::::::::::

	#	/ \ / \ / \ / \ / \ / \ 	 		/ \ / \ / \ / \ / \ / \ / \ / \ 
	#	\                     / 	 		\ / \ / \ / \ / \ / \ / \ / \ / 
	#	/  This is a #slashes \ 	 		/ \                         / \ 
	#	\         box         / 	 		\ /   This is a #diamonds   \ / 
	#	/   It feels festive  \ 	 		/ \           box           / \ 
	#	\    yet important    / 	 		\ /                         \ / 
	#	/                     \ 	 		/ \ / \ / \ / \ / \ / \ / \ / \ 
	#	\ / \ / \ / \ / \ / \ / 	 		\ / \ / \ / \ / \ / \ / \ / \ / 

	#	    _                             _ 
	#	 __| |___________________________| |__
	#	(__   ___________________________   __)
	#	   | |    This is a #signpost    | |    	..................................
	#	   | |      Let it be known      | |    	:       This is a #dotbox        :
	#	   | | that it will say things,  | |    	:It is mainly used in combination:
	#	   | |   It looks best in Menlo  | |    	:        with other boxes        :
	#	 __| |___________________________| |__  	:................................:
	#	(__   ___________________________   __)
	#	   !_!                           !_!

	############################################################	  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
	#                                                          #	  %                                                %
	#                                                          #	  %                                                %
	#                   This is a #hashbox                     #	  %              This is a #percentbox             %
	#            Ideal for python, shell scripting             #	  %                Ideal for LaTeX                 %
	#                                                          #	  %                   & Erlang                     %
	#                                                          #	  %                                                %
	############################################################	  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	######################################################################################
	################################ This is a #hashfield ################################
	################## Ideal for python, shell scripting, and barriers ###################
	######################################################################################


	#	   .-------------------------------------------------------------------------.
	#	  /  .-.                      This is a scroll box                       .-.  \ 
	#	 |  /   \                       called #scroll1                         /   \  |
	#	 | |\_.  |  It is currently extendable to an unlimited number of lines |    /| |
	#	 |\|  | /|                                                             |\  | |/|
	#	 | `---' |                                                             | `---' |
	#	 |       |-------------------------------------------------------------|       |
	#	 \       |                                                             |       /
	#	  \     /                                                               \     / 
	#	   `---'                                                                 `---'  

	#	                                                                         .-.
	#	                                                                        /  .\
	#	                                                                       |\_/| |
	#	                                                                       |   |/|
	#	   .-----------------------------------------------------------------------' |
	#	  /  .-.                                                                     |
	#	 |  /   \                     This is a scroll box                           |
	#	 | |\_.  |                      called #scroll2                              |
	#	 |\|  | /|  It is currently extendable to an unlimited number of lines       |
	#	 | `---' |                                                                   |
	#	 |       |                                                                  /
	#	 |       |-----------------------------------------------------------------'
	#	 \       |                                                             
	#	  \     /                                                              
	#	   `---'              

	#	  ____________________________________    
	#	 / \                                  \   
	#	|   |                                 |   
	#	 \_ |                                 |   
	#	    |      This is a #hearye box      |   
	#	    |    use it for proclamations!    |   
	#	    |                                 |   
	#	    |                                 |   
	#	    |   ______________________________|___
	#	    |  /                                 /
	#	    \_/_________________________________/

	#	  .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.     .-.   #wavyline
	#	.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `._.'   `.

	#	   __    __        __          __    __        __          __    __        __          __    __
	#	  (//    \\)    __(//   __    (//    \\)    __(//   __    (//    \\)    __(//   __    (//    \\)  #floral
	#	  /"      / __  \\)"    \\)_  /"      / __  \\)"    \\)_  /"      / __  \\)"    \\)_  /"      / __
	#	'|-..__..-''\_''-.\__..-''  '|-..__..-''\_''-.\__..-''  '|-..__..-''\_''-.\__..-''  '|-..__..-''\
	#	(\\  \_    _(\\      _/     (\\  \_    _(\\      _/     (\\  \_    _(\\      _/     (\\  \_    //)
	#	 ""  (\\  //)""     //)      ""  (\\  //)""     //)      ""  (\\  //)""     //)      ""  (\\   ""
	#	      ""  ""        ""            ""  ""        ""            ""  ""        ""            ""

	#	________________________________________________________________________
	#	  /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\   #diamondwall
	#	 /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \ 
	#	/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \/    \
	#	\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /\    /
	#	 \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  / 
	#	__\/____\/____\/____\/____\/____\/____\/____\/____\/____\/____\/____\/__

	#	M O O * * M O O * * M O O * * M O O * * MM
	#	O                                        O
	#	O                                        O
	#	*           This is a #moo box           *
	#	*        It needs some fixing up         *
	#	M                                        M
	#	M O O * * M O O * * M O O * * M O O * * MM  

	#	   |      |      |      |      |      |      |   	 	  /|\    /|\    /|\    /|\    /|\    /|\    /|\   
	#	   |      |      |      |      |      #downarrows	  	 / | \  / | \  / | \  / | \  / | \  / | \  / | \ 
	#	   |      |      |      |      |      |      |   	 	/  |  \/  |  \/  |  \/  |  \/  |  \/  |  \/  |  \
	#	\  |  /\  |  /\  |  /\  |  /\  |  /\  |  /\  |  /	  	   |      |      |      |      |      |      |   
	#	 \ | /  \ | /  \ | /  \ | /  \ | /  \ | /  \ | / 	 	   |      |      |      |      |      | #uparrows
	#	  \|/    \|/    \|/    \|/    \|/    \|/    \|/  	 	   |      |      |      |      |      |      |   

	#	.................................................................
	#	:   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
	#	: _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
	#	:(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
	#	:  / o \    / o \    / o \    / o \    / o \    / o \    / o \  :
	#	: (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
	#	:   ,-.   .............................................   ,-.   :
	#	: _(*_*)_ :                                           : _(*_*)_ :
	#	:(_  o  _):                                           :(_  o  _):
	#	:  / o \  :        This is a #gingerbread box         :  / o \  :
	#	: (_/ \_) : It's an example of box-in-a-box technique : (_/ \_) :
	#	:   ,-.   :   using both outter and inner dotboxes    :   ,-.   :
	#	: _(*_*)_ :                                           : _(*_*)_ :
	#	:(_  o  _):                                           :(_  o  _):
	#	:  / o \  :                                           :  / o \  :
	#	: (_/ \_) :...........................................: (_/ \_) :
	#	:   ,-.      ,-.      ,-.      ,-.      ,-.      ,-.      ,-.   :
	#	: _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_  _(*_*)_ :
	#	:(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _)(_  o  _):
	#	:  / o \    / o \    / o \    / o \    / o \    / o \    / o \  :
	#	: (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_)  (_/ \_) :
	#	:...............................................................:

	#	......................................................................................
	#	:      ,~~.          ,~~.          ,~~.          ,~~.          ,~~.          ,~~.    :
	#	:     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,:
	#	:(\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  :
	#	: \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )    :
	#	:  \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /     :
	#	: ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~':
	#	:      ,~~.    ........................................................      ,~~.    :
	#	:     (  9 )-_,:                                                      :     (  9 )-_,:
	#	:(\___ )=='-'  :                 This is a #ducks box                 :(\___ )=='-'  :
	#	: \ .   ) )    :      It's an example of box-in-a-box technique       : \ .   ) )    :
	#	:  \ `-' /     :        using both outter and inner dotboxes          :  \ `-' /     :
	#	:   `~j-'      :                                                      :   `~j-'      :
	#	:     '=:      :......................................................:     '=:      :
	#	:      ,~~.          ,~~.          ,~~.          ,~~.          ,~~.          ,~~.    :
	#	:     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,:
	#	:(\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  :
	#	: \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )    :
	#	:  \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /     :
	#	: ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~':
	#	:....................................................................................:

	#	 _    .    .    _ _    .    .    _ _    .    .    _ _    .    .    _ 
	#	(@`-._ \  / _.-'@(@`-._ \  / _.-'@(@`-._ \  / _.-'@(@`-._ \  / _.-'@)
	#	 \:: .`~\/~'. ::/ \:: .`~\/~'. ::/ \:: .`~\/~'. ::/ \:: .`~\/~'. ::/ 
	#	  \"##".()."##"/   \"##".()."##"/   \"##".()."##"/   \"##".()."##"/  
	#	   >~'""||""`~<     >~'""||""`~<     >~'""||""`~<     >~'""||""`~<   
	#	  /.:::/\/\:::.\   /.:::/\/\:::.\   /.:::/\/\:::.\   /.:::/\/\:::.\  
	#	  \(@)/    \(@)/   \(@)/    \(@)/   \(@)/    \(@)/   \(@)/    \(@)/  
	#	 _ `-'.    .`-' _   `-'      `-'     `-'      `-'   _ `-'.    .`-' _ 
	#	(@`-._ \  / _.-'@)                                  @`-._ \  / _.-'@)
	#	 \:: .`~\/~'. ::/                                   \:: .`~\/~'. ::/ 
	#	  \"##".()."##"/                                     \"##".()."##"/  
	#	   >~'""||""`~<       This is a #butterflies box      >~'""||""`~<   
	#	  /.:::/\/\:::.\                                     /.:::/\/\:::.\  
	#	  \(@)/    \(@)/                                     \(@)/    \(@)/  
	#	 _ `-'.    .`-' _                                   _ `-'.    .`-' _ 
	#	(@`-._ \  / _.-'@(@`-._ \  / _.-'@(@`-._ \  / _.-'@(@`-._ \  / _.-'@)
	#	 \:: .`~\/~'. ::/ \:: .`~\/~'. ::/ \:: .`~\/~'. ::/ \:: .`~\/~'. ::/
	#	  \"##".()."##"/   \"##".()."##"/   \"##".()."##"/   \"##".()."##"/
	#	   >~'""||""`~<     >~'""||""`~<     >~'""||""`~<     >~'""||""`~<
	#	  /.:::/\/\:::.\   /.:::/\/\:::.\   /.:::/\/\:::.\   /.:::/\/\:::.\
	#	  \(@)/    \(@)/   \(@)/    \(@)/   \(@)/    \(@)/   \(@)/    \(@)/
	#	   `-'      `-'     `-'      `-'     `-'      `-'     `-'      `-'

	#	    _ _  __    _ _  __    _ _  __    _ _  __    _ _  __    _ _  __
	#	   ( | )/_/   ( | )/_/   ( | )/_/   ( | )/_/   ( | )/_/   ( | )/_/
	#	__( >O< )  __( >O< )  __( >O< )  __( >O< )  __( >O< )  __( >O< )  
	#	\_\(_|_)   \_\(_|_)   \_\(_|_)   \_\(_|_)   \_\(_|_)   \_\(_|_)   
	#	    _ _  __                                                _ _  __
	#	   ( | )/_/           This is a #pansies box              ( | )/_/
	#	__( >O< )        It's remarkably simple to encode      __( >O< )  
	#	\_\(_|_)                                               \_\(_|_)   
	#	    _ _  __    _ _  __    _ _  __    _ _  __    _ _  __    _ _  __
	#	   ( | )/_/   ( | )/_/   ( | )/_/   ( | )/_/   ( | )/_/   ( | )/_/
	#	__( >O< )  __( >O< )  __( >O< )  __( >O< )  __( >O< )  __( >O< )  
	#	\_\(_|_)   \_\(_|_)   \_\(_|_)   \_\(_|_)   \_\(_|_)   \_\(_|_)   


	#	   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._   
	#	.-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.
	#	 )                                                                           ( 
	#	(                           This is a #fancy1 box                             )
	#	 )              It has a staic width and cannot be broadended,               ( 
	#	(                         but has a variable length                           )
	#	 )                                                                           ( 
	#	(                                                                             )
	#	(___       _       _       _       _       _       _       _       _       ___)
	#	    `-._.-' (___ _) `-._.-' `-._.-' )     ( `-._.-' `-._.-' (__ _ ) `-._.-'    
	#	            ( _ __)                (_     _)                (_ ___)            
	#	            (__  _)                 `-._.-'                 (___ _)            
	#	            `-._.-'                                         `-._.-'            

	#	   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._   
	#	.-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.
	#	 )                          This is a #fancy2 box                            ( 
	#	(               It has a staic width and cannot be broadended,                )
	#	 )                        but has a variable length                          ( 
	#	(                                                                             )
	#	(___       _       _       _       _       _       _       _       _       ___)
	#	    (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)    
	#	    ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )    
	#	    (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)    
	#	    (_ ___) `-._.-'                                         `-._.-' (___ _)    
	#	    `-._.-'                                                         `-._.-'    

	#	   _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._   
	#	.-'---      - ---     --     ---   -----   - --       ----  ----   -     ---`-.
	#	 )                                                                           ( 
	#	(                           This is a #fancy2 box                             )
	#	 )              It has a staic width and cannot be broadended,               ( 
	#	(                         but has a variable length                           )
	#	 )                                                                           ( 
	#	(                                                                             )
	#	(___       _       _       _       _       _       _       _       _       ___)
	#	    `-._.-' (___ _) (__ _ ) (_   _) (__  _) ( __ _) (__  _) (__ _ ) `-._.-'    
	#	            `-._.-' (  ___) ( _  _) ( _ __) (_  __) (__ __) `-._.-'            
	#	                    `-._.-' (__  _) (__  _) (_ _ _) `-._.-'                    
	#	                            `-._.-' (_ ___) `-._.-'                            
	#	                                    `-._.-'                                    


#__endgallery

###############################################################################################
#   ___  ___       ___       ______  __    __   __   __   __   _______  ______  ____    ____  #
#  |   \/   |     /   \     /      ||  |  |  | |  | |  \ |  | |   ____||   _  \ \   \  /   /  #
#  |  \  /  |    /  ^  \   |  ,----'|  |__|  | |  | |   \|  | |  |__   |  |_)  | \   \/   /   #
#  |  |\/|  |   /  /_\  \  |  |     |   __   | |  | |  . `  | |   __|  |      /   \_    _/    #
#  |  |  |  |  /  _____  \ |  `----.|  |  |  | |  | |  |\   | |  |____ |  |\  \-.   |  |      #
#  |__|  |__| /__/     \__\ \______||__|  |__| |__| |__| \__| |_______|| _| `.__|   |__|      #
#                                                                                             #
#__Machinery###################################################################################

import os,sys
import string
import math

def long_text_to_array(thestring):
	return thestring.split('\n')
	
def max_width(lines):
	#takes a array of strings and returns the length of the longest string
	max_len = 0
	for line in lines:
		l = len(line)
		if l > max_len:
			max_len = l
	return max_len 

def printbox(commented_text_box): #WAD
	#prints commented_text_box line by line
	for line in commented_text_box:
		print line

def add_comments(text_box, comment_mark, True_short__False_long = True): #WAD
	#tacks comments onto text_box.
	#If True_short__False_long, stick comment mark in front of each line. 
	#else, wrap it in long comments. 
	#For C-style comments, set comment mark to either '/*' or '*/' and this function will handle it. 
	if True_short__False_long:
		for i in xrange(len(text_box)):# for line in text_box:
			text_box[i] = comment_mark + text_box[i] #new_text_box.append(comment_mark + line)
	else:
		front_comment_mark = comment_mark
		back_comment_mark = comment_mark
		if comment_mark == "/*" or comment_mark == "*/":
			#if in C=style comment marks:
			front_comment_mark = "/*"
			back_comment_mark = "*/"
		text_box.insert(0,front_comment_mark)
		text_box.append(back_comment_mark)

def put_A_next_to_B(A,B,space_string):
	#Merge two bricks of text A,B with B to the right of A and a filler space_string between them
	out = []
	lA = len(A)
	lB = len(B)
	minlen = min(lA,lb)
	for i in xrange(minlen):
		out.append(A[i]+space_string+B[i])
	if lA < lB:
		wA = 0
		if lA > 0:
			wA = len(A[0])
		for i in xrange(minlen,lB):
			out.append((" "*wA)+space_string+B[i])
	elif lB < lA:
		wB = 0
		if lB > 0:
			wB = len(B[0])
		for i in xrange(minlen,lA):
			out.append(A[i]+space_string+(wB*" "))
	return out
		
		
def space_pad(text, n_left=1, n_right=1, fillchar = ' '): #wad
	#tacks space to the left and right of every line, modifying the original text.
	for i in xrange(len(text)):# for line in text:
		text[i] = fillchar*n_left + text[i] + fillchar*n_right

def left_justify(text, fillchar = ' '): #wad
	#adds space to the left of the text, making the line lengths all the same. modifies the original object.
	mw = max_width(text)
	for i in xrange(len(text)): 
		diff = mw-len(text[i]) 
		if diff > 0 :
			text[i] = text[i] + diff*fillchar 

def center_justify(text, fillchar = ' '): #wad
	#adds space to the left and right of the text, making the line lengths all the same and centering the text. modifies the origional object.
	mw = max_width(text)
	for i in xrange(len(text)): 
		diff = int(mw-len(text[i]))
		if diff > 0:
			left_diff = int(math.floor(float(diff)/2.))
			right_diff = diff - left_diff
			text[i] = left_diff*fillchar + text[i] + right_diff*fillchar 

def line_pad(text, n_lines_to_add, max_width_ = -1, fillchar = ' ', T_top__F_center=False):
	#inserts lines into text, modifying the original object
	if max_width_ == -1:
		max_width_ = max_width(text)
	text_lines = len(text)
	top_lines = 0
	bot_lines = 0
	if T_top__F_center:
		top_lines = 0	
	else:
		top_lines = int(math.floor(float(n_lines_to_add)/2.))
	bot_lines = n_lines_to_add - top_lines
	for i in xrange(top_lines):
		text.insert(0, max_width_*fillchar)
	for i in xrange(bot_lines):
		text.append(max_width_*fillchar)

def inner_width(box, min_struct_width, text_width):
	top_width = 0
	left_width = 0
	rite_width = 0
	if len(box.Top_element) > 0:
		top_width =  len(box.Top_element[0])
	if len(box.Left_element) > 0:
		left_width = len(box.Left_element[0])
	if len(box.Rite_element) > 0:
		rite_width = len(box.Rite_element[0])
	min_struct_width2 = max(text_width,min_struct_width - left_width - rite_width)
	if top_width == 0:
		return min_struct_length
	n_tops = int(math.ceil(float(min_struct_width2)/float(top_width)))
	return n_tops*top_width

def inner_length(box, min_struct_length, text_length):
	#you have a box and min_struct_length, return the maximum vertical length that can fit in the box given those constraints.
	side_length =   len(box.Left_element)
	top_length =    len(box.Top_element)
	bottom_length = len(box.Bot_element)
	min_struct_length = min_struct_length - top_length - bottom_length
	min_struct_length = max(min_struct_length,text_length)
	if side_length == 0:
		return min_struct_length
	n_sides = int(math.ceil(float(min_struct_length)/float(side_length)))
	return n_sides*side_length


class box:
	fillchar = ' '
	def build_box(self,text, T_center_justify__F_left_justify):
		return [""]

class simple_box(box):
	Up_left_corner = [""]
	Up_rite_corner = [""]
	Dn_left_corner = [""]
	Dn_rite_corner = [""]
	Top_element = [""]
	Bot_element = [""]
	Left_element = [""]
	Rite_element = [""]
	min_width_interior = 0 #make these work
	min_length_interior = 0 #make these work
	pad_text = True
	def make_top_border(self,text_width):
		if len(self.Top_element) == 0:
			return [""],0
		w_element = len(self.Top_element[0])
		if w_element == 0:
			return [""],0
		n_elements = int(math.ceil(float(text_width)/w_element))
		remainder = n_elements*w_element - text_width
		border = []
		for Lline, eline, Rline in zip(self.Up_left_corner, self.Top_element, self.Up_rite_corner):
			border.append(Lline + n_elements*eline + Rline)
		return border, remainder
	def make_bottom_border(self,text_width):
		if len(self.Bot_element) == 0:
			return [""]
		w_element = len(self.Bot_element[0])
		if w_element == 0:
			return [""]
		n_elements = int(math.ceil(float(text_width)/w_element))
		#remainder = n_elements*w_element - text_width
		border = []
		for Lline, eline, Rline in zip(self.Dn_left_corner, self.Bot_element, self.Dn_rite_corner):
			border.append(Lline + n_elements*eline + Rline)
		return border#, remainder
	def make_left_border(self,text_height):
		h_element = len(self.Left_element)
		if h_element == 0:
			return [""],0
		n_elements = int(math.ceil(float(text_height)/h_element))
		remainder = n_elements*h_element - text_height
		border = []
		for i in xrange(n_elements):
			for line in self.Left_element:
				border.append(line)	
		return border, remainder
	def make_rite_border(self,text_height):
		h_element = len(self.Rite_element)
		if h_element == 0:
			return [""]
		n_elements = int(math.ceil(float(text_height)/h_element))
		#remainder = n_elements*h_element - text_height
		border = []
		for i in xrange(n_elements):
			for line in self.Rite_element:
				border.append(line)	
		return border#, remainder
	def build_box(self,text, center_text):
		if self.pad_text and center_text <= 1:
			space_pad(text)
		if center_text == 0: #{"center":1, "left":0, "none":2}
			left_justify(text, self.fillchar)
		elif center_text == 1:
			center_justify(text, self.fillchar)
		elif center_text == 2:
			pass		
		else:
			print "buildbox receives invalid center_text option", center_text 
		text_width = max_width(text)
		mw = max(text_width,self.min_width_interior)
		width_padding = mw - text_width

		text_length = len(text)
		length = max(text_length, self.min_length_interior)
		length_padding = length - text_length 

		#make borders
		box_text, lrem = self.make_top_border(mw) #lrem is the extra width that need to be added b/c the border
		bottom_border = self.make_bottom_border(mw) 
		left_border, n_lines_to_add = self.make_left_border(length) #n_lines_to_add is the extra lines that need to be added b/c the border
		rite_border = self.make_rite_border(length)

		lrem = lrem + width_padding
		n_lines_to_add = n_lines_to_add + length_padding
		#prepare text to fit in that space:
		space_pad(text, int(math.floor(float(lrem)/2.)), lrem - int(math.floor(float(lrem)/2.)), self.fillchar)			
		line_pad(text, n_lines_to_add, mw+lrem-width_padding, self.fillchar)			
		#build the box
		if len(left_border) != len(text) or len(text) != len(rite_border):
			print "build_box has a missmatch. left length ",len( left_border), "text length:",len(left_border), "right length", len(rite_border)
		for Lline, Cline, Rline in zip(left_border, text, rite_border):
			box_text.append( Lline + Cline + Rline)
		for line in bottom_border:
			box_text.append(line)
		return box_text
	""".................................................................................................
 	:      ,~~.          ,~~.          ,~~.          ,~~.          ,~~.          ,~~.          ,~~.    :
 	:     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,:
 	:(\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  :
 	: \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )    :
 	:  \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /     :
 	: ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~':
 	:      ,~~.    ......................................................................      ,~~.    :
 	:     (  9 )-_,:                                                                    :     (  9 )-_,:
 	:(\___ )=='-'  :                                                                    :(\___ )=='-'  :
 	: \ .   ) )    :         ____  ____  ______         __   ___   ___      ___         : \ .   ) )    :
 	:  \ `-' /     :        /    ||    \|      |       /  ] /   \ |   \    /  _]        :  \ `-' /     :
 	:   `~j-'      :       |  o  ||  D  )      |      /  / |     ||    \  /  [_         :   `~j-'      :
 	:     '=:      :       |     ||    /|_|  |_|     /  /  |  O  ||  D  ||    _]        :     '=:      :
 	:      ,~~.    :       |  _  ||    \  |  |      /   \_ |     ||     ||   [_         :      ,~~.    :
 	:     (  9 )-_,:       |  |  ||  .  \ |  |      \     ||     ||     ||     |        :     (  9 )-_,:
 	:(\___ )=='-'  :       |__|__||__|\_| |__|       \____| \___/ |_____||_____|        :(\___ )=='-'  :
 	: \ .   ) )    :                                                                    : \ .   ) )    :
 	:  \ `-' /     :                                                                    :  \ `-' /     :
 	:   `~j-'      :                                                                    :   `~j-'      :
 	:     '=:      :....................................................................:     '=:      :
 	:      ,~~.          ,~~.          ,~~.          ,~~.          ,~~.          ,~~.          ,~~.    :
 	:     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,     (  6 )-_,:
 	:(\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  (\___ )=='-'  :
 	: \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )     \ .   ) )    :
 	:  \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /       \ `-' /     :
 	: ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~' ~'`~'`~'`~`~':
 	:__Art_Code......................................................................................"""

def build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ulcorner, fill_char = ' '): 
	box_obj = simple_box()
	box_obj.fillchar = fill_char
	box_obj.Up_left_corner = ulcorner
	#box_obj.Up_left_corner = [ulcorner]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Dn_left_corner = box_obj.Up_left_corner
	box_obj.Dn_rite_corner = box_obj.Dn_left_corner
	box_obj.Top_element = box_obj.Up_left_corner
	box_obj.Bot_element = box_obj.Top_element
	box_obj.Left_element = box_obj.Up_left_corner
	box_obj.Rite_element = box_obj.Left_element
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_starbox(text, center_text,min_struct_width, min_struct_length): #starbox
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["*"])

def build_textbox_starfield(text, center_text,min_struct_width, min_struct_length): #starfield
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["*"],"*")

def build_textbox_diamonds(text, center_text,min_struct_width, min_struct_length): #diamonds
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["/ \ ","\ / "])

def build_textbox_pansies(text, center_text,min_struct_width, min_struct_length): #pansies
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, [\
"    _ _  __",\
"   ( | )/_/",\
"__( >O< )  ",\
"\_\(_|_)   "])

def build_textbox_Celegance(text, center_text,min_struct_width, min_struct_length): #Celegance
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["/*"]
	box_obj.Up_rite_corner = ["*\\"]
	box_obj.Dn_left_corner = ["\\*"]
	box_obj.Dn_rite_corner = ["*/"]
	box_obj.Top_element = ["*"]
	box_obj.Bot_element = box_obj.Top_element
	box_obj.Left_element = [" *"]
	box_obj.Rite_element = ["* "]
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_slashfield(text, center_text,min_struct_width, min_struct_length): #slashfield
	box_obj = simple_box()
	box_obj.fillchar = '/'
	box_obj.Up_left_corner = ["//"]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Dn_left_corner = box_obj.Up_left_corner
	box_obj.Dn_rite_corner = box_obj.Dn_left_corner
	box_obj.Top_element = ['/']
	box_obj.Bot_element = box_obj.Top_element
	box_obj.Left_element = box_obj.Up_left_corner
	box_obj.Rite_element = box_obj.Left_element
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_dotbox(text, center_text,min_struct_width, min_struct_length, pad_text = True): #dotbox
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.pad_text = pad_text #turn to false for outter boxes.
	box_obj.Up_left_corner = ["."]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Dn_left_corner = [':']
	box_obj.Dn_rite_corner = box_obj.Dn_left_corner
	box_obj.Top_element = ['.']
	box_obj.Bot_element = box_obj.Top_element
	box_obj.Left_element = [':']
	box_obj.Rite_element = box_obj.Left_element
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_gingerbread(text, center_text,min_struct_width, min_struct_length): #gingerbread
	#uses box-in-a-box techniques
	gbread_box = simple_box()
	gbread_box.fillchar = ' '
	gbread_box.Up_left_corner = [\
"   ,-.   ",\
" _(*_*)_ ",\
"(_  o  _)",\
"  / o \  ",\
" (_/ \_) "]
	gbread_box.Up_rite_corner = gbread_box.Up_left_corner
	gbread_box.Dn_left_corner = gbread_box.Up_left_corner
	gbread_box.Dn_rite_corner = gbread_box.Dn_left_corner
	gbread_box.Top_element = gbread_box.Up_left_corner
	gbread_box.Bot_element = gbread_box.Top_element
	gbread_box.Left_element = gbread_box.Up_left_corner
	gbread_box.Rite_element = gbread_box.Left_element
        gbread_box.min_length_interior = 0
	gbread_box.min_width_interior = 0
	gbread_box.pad_text = False 
	inner_text_box = build_textbox_dotbox(text,center_text,\
		inner_width(gbread_box, min_struct_width-2,max_width(text)+2),\
		inner_length(gbread_box, min_struct_length-2,len(text)+2) )
	no_centering_index = centering_dict["none"]
	middle_text_box = gbread_box.build_box(inner_text_box,no_centering_index) 
	return build_textbox_dotbox(middle_text_box,no_centering_index,0,0)

def build_textbox_ducks(text, center_text,min_struct_width, min_struct_length): #ducks
	#uses box-in-a-box techniques
	gbread_box = simple_box()
	gbread_box.fillchar = ' '
	gbread_box.Up_left_corner = [\
"      ,~~.    ",\
"     (  6 )-_,",\
"(\___ )=='-'  ",\
" \ .   ) )    ",\
"  \ `-' /     ",\
" ~'`~'`~'`~`~'"]
	gbread_box.Up_rite_corner = gbread_box.Up_left_corner
	gbread_box.Dn_left_corner = gbread_box.Up_left_corner
	gbread_box.Dn_rite_corner = gbread_box.Dn_left_corner
	gbread_box.Top_element = gbread_box.Up_left_corner
	gbread_box.Bot_element = gbread_box.Top_element
	gbread_box.Left_element = [\
"      ,~~.    ",\
"     (  9 )-_,",\
"(\___ )=='-'  ",\
" \ .   ) )    ",\
"  \ `-' /     ",\
"   `~j-'      ",\
"     '=:      "]
	gbread_box.Rite_element = gbread_box.Left_element
        gbread_box.min_length_interior = 0
	gbread_box.min_width_interior = 0
	gbread_box.pad_text = False 
	inner_text_box = build_textbox_dotbox(text,center_text,\
		inner_width(gbread_box, min_struct_width-2,max_width(text)+2),\
		inner_length(gbread_box, min_struct_length-2,len(text)+2) )
	no_centering_index = centering_dict["none"]
	middle_text_box = gbread_box.build_box(inner_text_box,no_centering_index) 
	return build_textbox_dotbox(middle_text_box,no_centering_index,0,0)

def build_textbox_hashbox(text, center_text,min_struct_width, min_struct_length): #hashbox
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["#"])

def build_textbox_hashfield(text, center_text,min_struct_width, min_struct_length): #hashfield
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["#"],"#")

def build_textbox_percentbox(text, center_text,min_struct_width, min_struct_length): #hashbox
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["%"])

def build_textbox_percentfield(text, center_text,min_struct_width, min_struct_length): #hashfield
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["%"],"%")

def build_textbox_bracketbox(text, center_text,min_struct_width, min_struct_length): #bracketbox
	return build_textbox_single_element(text, center_text,min_struct_width, min_struct_length, ["{}"])

def build_textbox_doubleline(text, center_text,min_struct_width, min_struct_length): #doubleline
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = [" __","| ."]
	box_obj.Up_rite_corner = ["__ ",". |"]
	box_obj.Dn_left_corner = ["| |","|__"]
	box_obj.Dn_rite_corner = ["| |","__|"]
	box_obj.Top_element = ["_","_"]
	box_obj.Bot_element = box_obj.Top_element
	box_obj.Left_element = ["| |"]
	box_obj.Rite_element = box_obj.Left_element
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_signpost(text, center_text,min_struct_width, min_struct_length): #signpost
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["    _ "," __| |","(__   "]
	box_obj.Up_rite_corner = [" _ ","| |__","   __)"]
	box_obj.Dn_left_corner = [" __| |","(__   ","   !_!"]
	box_obj.Dn_rite_corner = ["| |__","   __)","!_!"]
	box_obj.Top_element = [" ","_","_"]
	box_obj.Bot_element = ["_","_"," "]
	box_obj.Left_element = ["   | |"]
	box_obj.Rite_element = ["| |   "]
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_celtic3(text, center_text,min_struct_width, min_struct_length): #celtic3
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["  ______"," / \    ","|   |   "," \_ |   "]
	box_obj.Up_rite_corner = ["___    ", "   \\   ","   |   ","   |   "]
	box_obj.Dn_left_corner = ["    |   ","    |   ","    |   ","    |  /","    \_/_"]
	box_obj.Dn_rite_corner = ["   |   ","   |   ","___|___","      /","_____/"]
	box_obj.Top_element = ["_"," "," "," "]
	box_obj.Bot_element = [" "," ","_"," ","_"]
	box_obj.Left_element = ["    |   "]
	box_obj.Rite_element = ["   |   "]
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 


def build_textbox_4dotbox(text, center_text,min_struct_width, min_struct_length): #4dotbox
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["::::","::::"]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Dn_left_corner = box_obj.Up_left_corner
	box_obj.Dn_rite_corner = box_obj.Dn_left_corner
	box_obj.Top_element = [":",":"]
	box_obj.Bot_element = box_obj.Top_element
	box_obj.Left_element = ["::::"]
	box_obj.Rite_element = box_obj.Left_element
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_slashes(text, center_text,min_struct_width, min_struct_length): #slashes
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["/ "]
	box_obj.Up_rite_corner = ["\\"]
	box_obj.Dn_left_corner = ["\\ "]
	box_obj.Dn_rite_corner = ["/"]
	box_obj.Top_element = ["\ / "]
	box_obj.Bot_element = ["/ \ "]
	box_obj.Left_element = ["\ ","/ "]
	box_obj.Rite_element = ["/ ","\ "]
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_butterflies(text, center_text,min_struct_width, min_struct_length): #butterflies
	#simple butterflies. I don't want to use this pattern too much, 
	#butterflies ought to be more diverse, make this an xkcd pattern.
	#also you're missing the ends of the antenee on the bototm row
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = [\
  " _    .    .    _",\
  "(@`-._ \  / _.-'@",\
  " \:: .`~\/~'. ::/",\
 '  \\"##".()."##"/ ',\
"""   >~'""||""`~<  """,\
  "  /.:::/\/\:::.\ ",\
  "  \(@)/    \(@)/ ",\
  " _ `-'.    .`-' _"]
	box_obj.Up_rite_corner = [\
  " _    .    .    _ ",\
  "(@`-._ \  / _.-'@)",\
  " \:: .`~\/~'. ::/ ",\
 '  \\"##".()."##"/  ',\
"""   >~'""||""`~<   """,\
  "  /.:::/\/\:::.\  ",\
  "  \(@)/    \(@)/  ",\
  " _ `-'.    .`-' _ "]
	box_obj.Dn_left_corner = [\
  "(@`-._ \  / _.-'@",\
  " \:: .`~\/~'. ::/",\
 '  \\"##".()."##"/ ',\
"""   >~'""||""`~<  """,\
  "  /.:::/\/\:::.\ ",\
  "  \(@)/    \(@)/ ",\
  "   `-'      `-'  "]
	box_obj.Dn_rite_corner = [\
  "(@`-._ \  / _.-'@)",\
  " \:: .`~\/~'. ::/",\
 '  \\"##".()."##"/',\
"""   >~'""||""`~<""",\
  "  /.:::/\/\:::.\\",\
  "  \(@)/    \(@)/",\
  "   `-'      `-'"]
	box_obj.Top_element = [
  " _    .    .    _",\
  "(@`-._ \  / _.-'@",\
  " \:: .`~\/~'. ::/",\
 '  \\"##".()."##"/ ',\
"""   >~'""||""`~<  """,\
  "  /.:::/\/\:::.\ ",\
  "  \(@)/    \(@)/ ",\
  "   `-'      `-'  "]
	box_obj.Bot_element = box_obj.Dn_left_corner
	box_obj.Left_element = [\
  "(@`-._ \  / _.-'@)",\
  " \:: .`~\/~'. ::/ ",\
 '  \\"##".()."##"/  ',\
"""   >~'""||""`~<   """,\
  "  /.:::/\/\:::.\  ",\
  "  \(@)/    \(@)/  ",\
  " _ `-'.    .`-' _ "]
	box_obj.Rite_element = [\
  "@`-._ \  / _.-'@)",\
  "\:: .`~\/~'. ::/ ",\
 ' \\"##".()."##"/  ',\
"""  >~'""||""`~<   """,\
  " /.:::/\/\:::.\  ",\
  " \(@)/    \(@)/  ",\
  "_ `-'.    .`-' _ "]
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_scroll1(text, center_text,min_struct_width,min_struct_length): #scroll1
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["   .------"]
	box_obj.Up_rite_corner = ["------."]
	box_obj.Dn_left_corner = [\
" |       |",\
" \       |",\
"  \     / ",\
"   `---'  "]
	box_obj.Dn_rite_corner = [\
"|       |",\
"|       /",\
" \     / ",\
"  `---'  "]
	box_obj.Top_element = ["-"]
	box_obj.Bot_element = ["-"," "," "," "]
	box_obj.Left_element = ["  /  .-.  ",\
" |  /   \ ",\
" | |\_.  |",\
" |\|  | /|",\
" | `---' |"]
	box_obj.Rite_element = ["  .-.  \ ",\
" /   \  |",\
"|    /| |",\
"|\  | |/|",\
"| `---' |"]
	stretch = max(max(0, len(text) - 6) , min_struct_length - 11) 
	for i in xrange(stretch):
		box_obj.Left_element.append(" |       |")
		box_obj.Rite_element.append("|       |")
        box_obj.min_length_interior = 0
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_scroll2(text, center_text,min_struct_width,min_struct_length): #scroll2

	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = [\
"          ",\
"          ",\
"          ",\
"          ",\
"   .------"]
	box_obj.Up_rite_corner = [\
"  .-.",\
" /  .\\",\
"|\_/| |",\
"|   |/|",\
"----' |"] 
	box_obj.Dn_left_corner = [\
" |       |", \
" \       |", \
"  \     / ", \
"   `---'  "]
	box_obj.Dn_rite_corner = ["----'","","",""]
	box_obj.Top_element = [" "," "," "," ","-"]
	box_obj.Bot_element = ["-"," "," "," "]
	box_obj.Left_element = [\
"  /  .-.  ", \
" |  /   \ ", \
" | |\_.  |", \
" |\|  | /|", \
" | `---' |", \
" |       |"]
	box_obj.Rite_element = [\
"      |",\
"      |",\
"      |",\
"      |",\
"      |"]
	stretch = max(max(0, len(text) - 6), min_struct_length - 15) 
	for i in xrange(stretch):
		box_obj.Left_element.append(" |       |")
		box_obj.Rite_element.append("      |")
	box_obj.Rite_element.append("     /")
        box_obj.min_length_interior = 0
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_moo(text, center_text,min_struct_width, min_struct_length): #moo
	#this needs some fixing up.
	box_obj = simple_box()
	box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["M"]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Dn_left_corner = box_obj.Up_left_corner
	box_obj.Dn_rite_corner = box_obj.Up_left_corner
	box_obj.Top_element = [" O O * * M"]
	box_obj.Bot_element = box_obj.Top_element
	box_obj.Left_element = ["O","O","*","*","M"]
	box_obj.Rite_element = box_obj.Left_element
        box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return box_obj.build_box(text, center_text) 

def build_barrier_floral(min_struct_width): #floral
	box_obj = simple_box()
	box_obj.Up_left_corner = ["","","","","","",""]
	box_obj.Up_rite_corner = [\
"   __    __",\
"  (//    \\\\)",\
'  /"      / __',\
"'|-..__..-''\\",\
"(\\\  \_    //)",\
' ""  (\\\\   ""',\
'      ""']
	box_obj.Top_element = [\
"   __    __        __       ",\
"  (//    \\\\)    __(//   __  ",\
'  /"      / __  \\\\)"    \\\\)_',\
"'|-..__..-''\_''-.\__..-''  ",\
'(\\\\  \_    _(\\\\      _/     ',\
' ""  (\\\\  //)""     //)     ',\
'      ""  ""        ""      ']
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Dn_rite_corner)
	return_text = box_obj.build_box("", centering_dict["none"])
	return_text.remove("") 
	return return_text

def build_barrier_diamondwall(min_struct_width): #diamondwall
	box_obj = simple_box()
	box_obj.Up_left_corner = ["","","","","","",""]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Top_element = [\
"______",\
"  /\  ",\
" /  \ ",\
"/    \\",\
"\    /",\
" \  / ",\
"__\/__"]
	box_obj.min_width_interior = min_struct_width
	return_text = box_obj.build_box("", centering_dict["none"])
	return_text.remove("") 
	return return_text

def build_barrier_uparrows(min_struct_width): #uparrows
	box_obj = simple_box()
	box_obj.Up_left_corner = ["","","","","",""]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Top_element = [\
"   |   ",\
"   |   ",\
"   |   ",\
"\  |  /",\
" \ | / ",\
"  \|/  "]
	box_obj.min_width_interior = min_struct_width
	return_text = box_obj.build_box("", centering_dict["none"])
	return_text.remove("") 
	return return_text

def build_barrier_downarrows(min_struct_width): #downarrows
	box_obj = simple_box()
	box_obj.Up_left_corner = ["","","","","",""]
	box_obj.Up_rite_corner = box_obj.Up_left_corner
	box_obj.Top_element = [\
"  /|\  ",\
" / | \ ",\
"/  |  \\",\
"   |   ",\
"   |   ",\
"   |   "]
	box_obj.min_width_interior = min_struct_width
	return_text = box_obj.build_box("", centering_dict["none"])
	return_text.remove("") 
	return return_text

def build_barrier_wavyline(min_struct_width): #wavyline
	box_obj = simple_box()
	box_obj.Up_left_corner = ["",""]
	box_obj.Up_rite_corner = [\
"  .-.  ",\
".'   `."]
	box_obj.Top_element = [\
"  .-.   ",\
".'   `._"]
	box_obj.min_width_interior = min_struct_width  -  max_width(box_obj.Left_element) - max_width(box_obj.Rite_element)
	return_text = box_obj.build_box("", centering_dict["none"])
	return_text.remove("") 
	return return_text

def build_textbox_fancy1(text, center_text,min_struct_length): #fancy1
	box_obj = simple_box()
	#box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["  ",".-"]
	box_obj.Up_rite_corner = ["  ","-."]
	box_obj.Dn_left_corner = ["(_","  ","  ","  ","  "]
	box_obj.Dn_rite_corner = ["_)","  ","  ","  ","  "]
	box_obj.Top_element = [\
" _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._ ",\
"'---      - ---     --     ---   -----   - --       ----  ----   -     ---`"]
	box_obj.Bot_element = [\
"__       _       _       _       _       _       _       _       _       __",\
"  `-._.-' (___ _) `-._.-' `-._.-' )     ( `-._.-' `-._.-' (__ _ ) `-._.-'  ",\
"          ( _ __)                (_     _)                (_ ___)          ",\
"          (__  _)                 `-._.-'                 (___ _)          ",\
"          `-._.-'                                         `-._.-'          "]
	box_obj.Left_element = [" )","( "]
	box_obj.Rite_element = ["( "," )"]
	box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_fancy2(text, center_text,min_struct_length): #fancy2
	box_obj = simple_box()
	#box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["  ",".-"]
	box_obj.Up_rite_corner = ["  ","-."]
	box_obj.Dn_left_corner = ["(_","  ","  ","  ","  ","  "]
	box_obj.Dn_rite_corner = ["_)","  ","  ","  ","  ","  "]
	box_obj.Top_element = [\
" _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._ ",\
"'---      - ---     --     ---   -----   - --       ----  ----   -     ---`"]
	box_obj.Bot_element = [\
"__       _       _       _       _       _       _       _       _       __",\
"  (__  _) ( __ _) (__  _) (__ _ ) `-._.-' ( _ __) (_  __) (_ __ ) (_  __)  ",\
"  ( _ __) (_  __) (__ __) `-._.-'         `-._.-' (__ __) (__  _) (__ _ )  ",\
"  (__  _) (_ _ _) `-._.-'                         `-._.-' (_ _ _) (_  __)  ",\
"  (_ ___) `-._.-'                                         `-._.-' (___ _)  ",\
"  `-._.-'                                                         `-._.-'  "]
	box_obj.Left_element = [" )","( "]
	box_obj.Rite_element = ["( "," )"]
	box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	return box_obj.build_box(text, center_text) 

def build_textbox_fancy3(text, center_text,min_struct_length): #fancy3
	box_obj = simple_box()
	#box_obj.fillchar = ' '
	box_obj.Up_left_corner = ["  ",".-"]
	box_obj.Up_rite_corner = ["  ","-."]
	box_obj.Dn_left_corner = ["(_","  ","  ","  ","  ","  "]
	box_obj.Dn_rite_corner = ["_)","  ","  ","  ","  ","  "]
	box_obj.Top_element = [\
" _.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._ ",\
"'---      - ---     --     ---   -----   - --       ----  ----   -     ---`"]
	box_obj.Bot_element = [\
"__       _       _       _       _       _       _       _       _       __",\
"  `-._.-' (___ _) (__ _ ) (_   _) (__  _) ( __ _) (__  _) (__ _ ) `-._.-'  ",\
"          `-._.-' (  ___) ( _  _) ( _ __) (_  __) (__ __) `-._.-'          ",\
"                  `-._.-' (__  _) (__  _) (_ _ _) `-._.-'                  ",\
"                          `-._.-' (_ ___) `-._.-'                          ",\
"                                  `-._.-'                                  "]

	box_obj.Left_element = [" )","( "]
	box_obj.Rite_element = ["( "," )"]
	box_obj.min_length_interior = min_struct_length - len( box_obj.Top_element) - len(box_obj.Bot_element)
	return box_obj.build_box(text, center_text) 





#__endart


######################################################################     .----------.
#     _____ ____    __    ____  __   __________   ______  __    __   #     |   ____   |
#    /     |\   \  /  \  /   / |  | |          | /      ||  |  |  |  #     |  |.--.|  |
#   |   (--` \   \/    \/   /  |  | `---|  |---`|  ,----'|  |__|  |  #     |  ||  ||  |
#    \   \    \            /   |  |     |  |    |  |     |   __   |  #     |  ||__||  |
#  .--)   |    \    /\    /    |  |     |  |    |  `----.|  |  |  |  #     |  ||\ \|  |
#  |_____/      \__/  \__/     |__|     |__|     \______||__|  |__|  #     |  |\ \_\  |
#                                                                    #     |  |_\[_]  |
######################################################################     |          |
#__switch                                                                  '----------'

def get_box(box_style ,comment_mark, True_short__False_long, center_text, text, indenting_string, min_struct_width, min_struct_length):
	#the main UI function.
	#will take in a int box_style indicating which type of box you want, a string for a comment mark,
	# and a bool indicating whether you're using long or short 
	#we expect the build_textbox family of functions to turn the string into an array of strings of pretty text boxes.
	text_box = [""]
	do_add_comment_mark = True
	box_style = box_style.strip("#") #in case the user forgets and puts in the hash.
	#get the main textbox
	if box_style == "none":
		text_box = text
	elif box_style == "floral":
		text_box = build_barrier_floral(min_struct_width)
	elif box_style == "diamondwall":
		text_box = build_barrier_diamondwall(min_struct_width)
	elif box_style == "diamonds":
		text_box = build_textbox_diamonds(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "pansies":
		text_box = build_textbox_pansies(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "downarrows":
		text_box = build_barrier_downarrows(min_struct_width)
	elif box_style == "uparrows":
		text_box = build_barrier_uparrows(min_struct_width)
	elif box_style == "wavyline":
		text_box = build_barrier_wavyline(min_struct_width)
	elif box_style == "starbox":
		text_box = build_textbox_starbox(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "starfield":
		text_box = build_textbox_starfield(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "gingerbread":
		text_box = build_textbox_gingerbread(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "ducks" or box_style == "duckbox":
		text_box = build_textbox_ducks(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "bracketbox":
		text_box = build_textbox_bracketbox(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "slashfield":
		text_box = build_textbox_slashfield(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "dotbox":
		text_box = build_textbox_dotbox(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "hashfield":
		text_box = build_textbox_hashfield(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "hashbox":
		text_box = build_textbox_hashbox(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "percentbox":
		text_box = build_textbox_percentbox(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "signpost":
		text_box = build_textbox_signpost(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "percentfield":
		text_box = build_textbox_percentfield(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "doubleline":
		text_box = build_textbox_doubleline(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "4dotbox":
		text_box = build_textbox_4dotbox(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "hearye":
		text_box = build_textbox_hearye(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "slashes":
		text_box = build_textbox_slashes(text,center_text,min_struct_width, min_struct_length)
	elif (box_style == "moo" or box_style == "moobox"):
		text_box = build_textbox_moo(text,center_text,min_struct_width, min_struct_length)
	elif box_style == "Celegance":
		text_box = build_textbox_Celegance(text,center_text,min_struct_width, min_struct_length)
		do_add_comment_mark = False #C++ comment marks are built into the box.
	elif box_style == "scroll1":
		text_box = build_textbox_scroll1(text,center_text,min_struct_width,min_struct_length)
	elif box_style == "scroll2":
		text_box = build_textbox_scroll2(text,center_text,min_struct_width,min_struct_length)
	elif box_style == "butterflies":
		text_box = build_textbox_butterflies(text,center_text,min_struct_width,min_struct_length)
	elif box_style == "fancy1":
		text_box = build_textbox_fancy1(text,center_text,min_struct_length)
	elif box_style == "fancy2":
		text_box = build_textbox_fancy2(text,center_text,min_struct_length)
	elif box_style == "fancy3":
		text_box = build_textbox_fancy3(text,center_text,min_struct_length)
	else: 
		print "Error! I don't recognize box_name ", box_style
		return
	#append comment marks in front of it
	add_comments(text_box, comment_mark, True_short__False_long)
	add_comments(text_box, indenting_string, True)
	return text_box

##########################################################################################
#   ______ ___   ___  _______   ______  __    __   __________  __    ______    __   __   #
#  |   ___|\  \ /  / |   ____| /      ||  |  |  | |          ||  |  /  __  \  |  \ |  |  #
#  |  |__   \  V  /  |  |__   |  ,----'|  |  |  | `---|  |---`|  | |  |  |  | |   \|  |  #
#  |   __|   >   <   |   __|  |  |     |  |  |  |     |  |    |  | |  |  |  | |  . `  |  #
#  |  |___  /  .  \  |  |____ |  `----.|  `--'  |     |  |    |  | |  `--'  | |  |\   |  #
#  |______|/__/ \__\ |_______| \______| \______/      |__|    |__|  \______/  |__| \__|  #
#                                                                                        #
#__Execution##############################################################################

#[comment mark, True = use short comment; False = use long comments
comment_mark_dict = {\
"none":["",True], \
"Cshort": ["//",True], "Clong": ["/*",False], \
"shell": ["#",True], \
"python": ["#",True], "pyshort": ["#",True], "pylong": ['"""',False], \
"latex": ["%",True],\
"custom":[custom__comment_mark,custom__use_short_comments]}

text_list = long_text_to_array(longtext)

center_text = centering_dict[centering]
box_style.strip('#')
box_style = box_style.lower()
use_short_comments = comment_mark_dict[comment_style][1]
comment_mark =  comment_mark_dict[comment_style][0] + N_tabs_after_comment_mark*'\t'
indenting_string = N_tabs_before_comment_mark*'\t' + N_quadspaces_before_comment_mark*'    '

#make and print the box
printbox(get_box(box_style, comment_mark, use_short_comments, center_text, text_list,  indenting_string, min_struct_width, min_struct_length))

###################################################################
#   _______ ____  _____   ____       _      _____  _____ _______  #
#  |__   __/ __ \|  __ \ / __ \     | |    |_   _|/ ____|__   __| #
#     | | | |  | | |  | | |  | |    | |      | | | (___    | |    #
#     | | | |  | | |  | | |  | |    | |      | |  \___ \   | |    #
#     | | | |__| | |__| | |__| |    | |____ _| |_ ____) |  | |    #
#     |_|  \____/|_____/ \____/     |______|_____|_____/   |_|    #
#                                                                 #
#__TODO_list#######################################################

# --> Enable this to accept an input file.
# --> The Beginning is needs more art.
# --> Add more art, particularly from Code/Tools/ascii.h
# --> Write more headers in big font 
# --> fix the inner dot width in duckbox
# --> fix the #moo box

#####################################################
#    _____ _____  ______ _____ _____ _______ _____  #
#   / ____|  __ \|  ____|  __ \_   _|__   __/ ____| #
#  | |    | |__) | |__  | |  | || |    | | | (___   #
#  | |    |  _  /|  __| | |  | || |    | |  \___ \  #
#  | |____| | \ \| |____| |__| || |_   | |  ____) | #
#   \_____|_|  \_\______|_____/_____|  |_| |_____/  #
#                                                   #
#__Credits###########################################
#
#             ^+xw*"""^q_  0 p" F  F _F  p^^"___jM   j  F              F
#               _,,__   q x" [  F J_ J  P  w""""_  _,"  9  _m^`"*____x"    _____
#          v,,_w"   "M_ @ `, ",_!u_9__L F #  r^""^^"    f j"      "      _*"   "6_
#              _,,__  B 9_ "v,_Zp*"""""^@u# P _m^"^u,a*"  j   ____       9       ""
#            _F    `4 A_ "*-ap"            ^Lj" _smu,    _* ,-"   9_   _wf
#          ^^"__,,_ jL  -- m<                5j! ____*-*^   &       """"     ___
#            p"    9p`^u,av'    Written by    `,*""""q_   _x" _aa,_        p^" ""u
#          ,r  _____!L___,M   Anthony Barker   Lsr--x_"^^`" qP     9      J      `M
#            y^    "_    _J      GNU GPLv3     L_,,_ ?_    _#       ^v- -^"
#           _F  __,_`^---"jr       2017       j___ ""y""^^""_,-r-u_
#          r^ j!    ?s_, *"jp                g""""^q_b_    _F     "p      j^^""-w
#             L  _,wma_  _x"jN__          __d"""^c  F  "-^""  _    "c____j'      L
#            j" J"    """  _F 99Nu______g**L_""s  4 A,    _P"""^q_    ""         "-
#          m^  j_  _-^""mw^" _' # 9"N""L ^, "s  b #   "--^"      0
#               @ j"   _v-wa+" ," j  #  p  r j qF "q_   _*-wu_   9,     y^`"^w_
#            _,!  0_  f   _m-**" _F _F  L _FjP ?,    "^""    "u    "---^      j
#          """     # J   j"   p"""p-^ x^ p" d_   -q__a-mw_    j               `L
#                 V  `q  #   f   j   4   b   ^,   __      6_  ?,     _,__       "--
#          *`^ww-"     F 9L_ b   1   4   `u_   "-^""*,    jh    ^-xm*"   9z
#                     )    0 `+a_ W__ 9,___"^^"+_     L   0                k
#              _x-*v+"     9    0   "b    "_    "p   _0   `&    ___       d_
#
# 
# Most art is sourced from Christopher Johnson's webpage https://asciiart.website//index.php
# Art-text is produced by Patrick Gillespie's ASCII Art Generator; see __Hypnotoad for the link.
##########################################################################################
