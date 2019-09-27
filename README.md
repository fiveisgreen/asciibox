##Description
This is a tool for generating pretty ascii boxes around text to decorate your code and other artistic ascii structures. Its output only looks right on fixed width fonts such as Courier, Andale Mono, Menlo Regular, and so on. You only ever need one file: asciibox.py. 

##User Interface
Open up asciibox.py and go to the control panel. 

* Set the type of box you want by setting the "box_style" variable. You can find a list of available box styles in the __box_styles section. You can also go to the __Gallery for a more visual way of looking through box styles. In the Gallery, box styles are refered to with a hashtag, but you don't have to write the # in the box_style variable. 

* If you're making a text box, write or paste the text that you want made into an artistic box into the string "longtext". 

* Indicate if you want the text centered or left justified by setting the "centering" variable.

* Choose which type of desired comment will be used to comment out the art. If you don't want any comment marks, use "none". Options are available for various languaes comment marks. Both long comments and inline comments are supported. If you don't like any of the options here, you can use the "custom" setting, and use whatever comment mark you want, using the subsequent "custom__comment_mark" and "custom__use_short_comments" variables.

* You can put some whitespace to the left of the art, or between the the comment mark and the art. N_tabs_before_comment_mark and N_quadspaces_before_comment_mark put tabs and sets of 4 spaces respectively to the left of the art and any comment marks. N_tabs_after_comment_mark will insert tabs between the comment marks and the art. It usually looks best to have N_tabs_after_comment_mark >= 1. 

* You can set a minimum size to the output art for most boxes using the variables min_struct_width and min_struct_length. This is particularly useful if you are making a structure instead of a text box. But it can also be used to force whitespace around text in a text box. 

That's everything you should need to control and run this program. 
:-)

##Run 
Once you've set the controls, run it from the terminal:

$ python asciibox.py

This is built for Python 2.7.10, but should work in most Python2 versions. 
