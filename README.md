## Description
![Description_img](/images/Description_signpost.png)

Have a look through the [Gallery](https://github.com/fiveisgreen/asciibox/blob/405cfb94ffce55853db93fe5a8fb4aa2f45d1e32/asciibox3.py#L124-L408)

## Useage Option 1: Open up asciibox3.py and go to the _control_panel. 

* Set the type of box you want by setting the "box_style" variable. You can find a list of available box styles in the __box_styles section. You can also go to the __Gallery for a more visual way of looking through box styles. In the Gallery, box styles are refered to with a hashtag, but you don't have to write the # in the box_style variable. 

* If you're making a text box, write or paste the text that you want made into an artistic box into the string "longtext". 

* Indicate if you want the text centered or left justified by setting the "centering" variable.

* Choose which type of desired comment will be used to comment out the art. If you don't want any comment marks, use "none". Options are available for various languaes comment marks. Both long comments and inline comments are supported. If you don't like any of the options here, you can use the "custom" setting, and use whatever comment mark you want, using the subsequent "custom__comment_mark" and "custom__use_short_comments" variables.

* You can put some whitespace to the left of the art, or between the the comment mark and the art. N_tabs_before_comment_mark and N_quadspaces_before_comment_mark put tabs and sets of 4 spaces respectively to the left of the art and any comment marks. N_tabs_after_comment_mark will insert tabs between the comment marks and the art. It usually looks best to have N_tabs_after_comment_mark >= 1. 

* You can set a minimum size to the output art for most boxes using the variables min_struct_width and min_struct_length. This is particularly useful if you are making a structure instead of a text box. But it can also be used to force whitespace around text in a text box. 

### Run 
Once you've set the controls, run it from the terminal:
$ python asciibox3.py


![Divider](/images/Floral_divider.PNG)

# Usage Option 2: Command line options
There are command line options giving accesss to everything on the control pannel. 

Ways to find and set the box style:
* -g (--gallery) Display the gallery. This helps in choosing a box style

* -l (--list) Prints a list of box styles

* -s (--style) Specifies the box style. 

Ways to read in text
* -t (--text) [textbox text] Enter textbox text as command line arguments. Text can be in quotes or not, either way. This overrides -f.

* -i (--interactive) Enter textbox text in a stdin interactive session. Exit the interactive session by writing .q on a new line, then enter.

* -f (--file) [filename] Read textbox text from file. Make sure to manually enter carriage returns between lines. 

* -m (--comment) Defines comment style. Options (case insensitive): 'none' applies no comment mark. 'Cshort' gives singe line C/C++/Java style comments. 'Clong' gives the /*..*/ multiline comments. 'shell'='python'='pyshort' all give pound sign comments. 'pylong' puts text in tripple, 'latex' gives percent sign comments. 'custom' [CustomCommentMark] allows you to specify any text as a comment-mark-like prefix. Ex: --custom '@'.

* -c (--centering) Options: Defines text centering within the box. Options: 'none','center' centers text with space padding, 'left' aligns left with left space padding.

* -b (--beforetabs) [int] Number of tabs in front of everything, including comment marks

* -B (--beforequads) [int] Number of quads (sets of 4 space) indenting in front of everything, including comment mark

* -a (--aftertabs) [int] Number of tabs after comment mark, but before the art. Use to create white space to the left of the art.

* -x (--width) [int] Minimum values for the width of the printed structure. Use these to add white space padding

* -y (--length) [int] Minimum values for the length of the printed structure. Use these to add white space padding


That's everything you should need to control and run this program. 
:-)

### Run 
$./asciibox3.py -g

$./asciibox3.py -l

$./asciibox3.py -s hashbox -t weeeee -y5

$./asciibox3.py -s 4dotbox -f foo.txt

## Python Compatability
asciibox.py was built for Python 2.7.10, but and should work in most Python2 versions. If not, replace xrange with range.
asciibox.py was built for Python 3.7.3.

