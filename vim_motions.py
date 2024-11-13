# Vim Navigation and Editing Exercises

# Navigate with h, j, k, l
# Move the cursor around this comment block
# Try to move efficiently to different parts of the text

def example_function():
    # Navigate with w, b, e, ge, or W, B, E, gE
    # Move forward and backward by word in this function
    print("This is an example_function")
    print("Move between these_words efficiently")
    print("Practice jumping to specific words")

# Navigate with 0, $
# Move to the beginning and end of these lines
print("Start of the line")                                     # End of the line
print("Another line to practice")                              # Move here quickly

if 1 == 2:
    # What is the difference between using _ and 0? Try it out on this line.
    print("This is impossible")

# Navigate with gg, G but try with Ctrl+o and Ctrl+i after.
# Move to the top and bottom of the file

# Using Ctrl+o and Ctrl+i you hop forwards and backwards to your previous positions.

# Insert with i, I
# Add some text at the cursor and at the beginning of the line
# Your text here

# Append with a, A
# Add some text after the cursor and at the end of the line
print("Append text here")  # Append at the end

# Open new lines with o, O
# Add new lines above and below this one

# Undo with u, or redo with Ctr+r

# Visual mode with v, V
# Select parts of this text in character and line mode
print("Select this entire line")
print("Or just part of this line")

# Change this whole line with C
I need to be replaced with something more pythonic

# Go to invalid character, replace with a quote (f + ' + r + ")
print("invalid string')

# Go to word "ugly" and replace it with something more wholesome
# change word (c + w) or change inside word (c + i + w) or change end (c + e)
print("You are ugly!")

# Yank and paste with y, Y, p, P
# Copy this line and paste it somewhere else:
# Try copy with
# yank + around + '"'
# or
# yank + inside + b
# Pro tip: If you're confused, use v instead of y for visual mode and then yank with y (v + a + " + y).
print("Copy me and paste somewhere")


# Change with c, C
# Change parts of these lines
print("Change some words in this line")
print("Or change from the cursor to the end of the line")

# Delete with d, D
# Delete parts of these lines
print("Delete some words in this line")
print("Or delete from the cursor to the end of the line")

# Copy this whole line with yy
print("Copy all line") # Also copy the comments!

# Cut with x, X
# Remove single characters from this line
print("Remove    the   extra   spaces    in  this    line")

# Begin with visaul
# Text objects: iw, aw, is, as, ip, ap
# Practice operating on words, sentences, and paragraphs
word = "Practice"

sentence = "This is a sample sentence to practice text objects."

paragraph = """This is a paragraph.
It has multiple lines.
Practice operating on the entire paragraph."""

# Search with /, ?
# You can also search for the word under the cursor with *
# Find occurrences of 'find' in this block
print("Can you find the word find?")
print("There might be more than one find to find.")
print("Keep searching to find all instances of find.")

# Search and replace with :s
# Replace 'old' with 'new' in this line
print("This old text has some old words that should be changed from old to something else.")

# Undo and redo with u, Ctrl-r
# Make some changes and practice undoing and redoing them

# Repeat with .
# Make a change and repeat it on the lines below
print("Change me")
print("Then repeat the change here")
print("And here")

# Combine numbers with commands
# Remove all lines with only one command. Start with number, then command
print("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")
print("Line 5")

# Screen movement with Ctrl-f, Ctrl-b, zz
# Practice moving the screen and centering the cursor

# Fix tabs with >> or << or V + < or V + >
if 1 == 2
    print("I'm tabbed correctly")
        print("HeeelP! I'm not tabbed correctly")
print("I should be inside if block")
    print("I'm tabbed correctly")

# Macros are advanced but also quite simple.
# Records your input, then just perform the same action.
# Fix these print statements (for macro practice):

# Move cursor to beginning of forst line (use _ or 0)
# Start with q + w to record macro to w (you can use almost any character)
# Perform needed action to fix one line.
# Jump to next line.
# Make sure to be in normal mode, press q to stop recording
# Then press @w to execute macro (try using 5 @w, what happens?)
print("Hello, world!"
print("Python is awesome"
print("Vim makes editing fun"
print("Practice makes perfect"
print("Keep coding every day"
print("Debugging is important"
print("Always comment your code"
print("Learn new things regularly"
print("Collaborate with others"
print("Enjoy the learning process"


# Create a macro for only fixing the invalid print that are uppercase.
# Search with /
# Replace the word somehow
# You might even want to use ~ on whole line to switch between upper and lowercase.

print("I'm okay")
print("I'm also okay")
PRINT("I NEED HELP")
print("I'm fine")
PRINT("HEEEELP!")
PRINT("I CANT STOP SCREEMING!!")
print("Print above is crazy")
PRINT("KHOOORNE")

