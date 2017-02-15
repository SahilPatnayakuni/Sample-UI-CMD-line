I have created a separate python file for task 1 and for task 2.
Both of them run from the command line so to run the task1.py file
simply navigate to the folder and type python task1.py into the command
line. Task 2 is similar in that you only need to type python task2.py "filepath"
into the command line.
This can also be opened in PyCharm, which is what I used to write it
Summary of tasks:
Task 1. A (simple) GUI interface that enable users 
a. to select one or more options (Voltage, Calcium, CalciumER) from drop-down list
b. to input a number in 'how many BRANCHTYPE' (acceptable value in the range 1-7)
c. a 'Generate' button 

Example of GUI:
Options (label) : [ dropdown list]
How many BRANCHTYPE (label): [textbox input] (with code to check valid input)
Generate (button)

Once user press the button 'Generate', it creates an output file: CptParams.par

Example: Suppose 'Voltage' and 'Calcium' are selected, and 2 is chosen as 'how many BRANCHTYPE', it generate 4 lines
COMPARTMENT_VARIABLE_TARGETS 2
BRANCHTYPE
1 Voltage Calcium
2 Voltage Calcium


Example: Suppose 'Voltage' and 'CalciumER' are selected, and 3 is chosen as 'how many BRANCHTYPE', it generate 5 lines
COMPARTMENT_VARIABLE_TARGETS 3
BRANCHTYPE
1 Voltage CalciumER
2 Voltage CalciumER
3 Voltage CalciumER



d. once 'Generate' button is clicked, the GUI now enable users to add one or more items with 3 inputs and 1 button as given

Example GUI:
ChannelName (label): [textbox] Input (label): [dropdown list with available values are those selected in (a)] Output (label): [dropdown list with available values are those selected in (a)] ChannelType (label): [dropdown list with values from 1-7]
Add (button)

Suppose in the first stage, we chose 'Voltage' and 'Calcium' as values to 'Option' label, they become two available values to the two dropdown lists in 'Input' and 'Output' labels.

Example: Now, if users input 'Na' to 'ChannelName', and select 'Voltage' as value to Input; and both 'Voltage', 'Calcium' as values to Output; and values '1', '3' to ChannelType.
Once 'Add' button is pressed, it create an output file named ChanParams.par with the following content (NOTE: square brackets are used to enclose values chosen in Input and Output labels, with comma as separator)

CHANNEL_TARGETS 2
BRANCHTYPE
1 Na [Voltage] [Voltage, Calcium]
3 Na [Voltage] [Voltage, Calcium]


Example: If users input 'Na' to 'ChannelName', and select both 'Voltage', 'Calcium' as values to Input; and both 'Voltage', 'Calcium' as values to Output; and values '1', '3' to ChannelType. Once 'Add' button is pressed, it create an output file named ChanParams.par with the following content (NOTE: square brackets are used to enclose values chosen in Input and Output labels, with comma as separator)

CHANNEL_TARGETS 2
BRANCHTYPE
1 Na [Voltage, Calcium] [Voltage, Calcium]
3 Na [Voltage, Calcium] [Voltage, Calcium]


Task 2. Write a Linux bash script (or Python script): suppose you have a few sub-folders (dataA, simA, simB, and simC) inside folder 'targetA', write a script that accept path to 'targetA' as first argument, then display only folders with prefix 'sim', and the option for user to select one folder (e.g. by displaying a number associated to that folder), for example

Select one of this:
0 simA
1 simB
2 simC
Type in the number?

Keep printing 'Type in the number?' until users select a value in the proper range (e.g. 0-2 in this case)
Once user select a folder, print out the suffix of that folder (with prefix as 'sim'), e.g. if 'simA' is selected, then print out 'A', and exit the script.