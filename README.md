# LR-LL_Parser_Algorithms
LEFT AND RIGHT MOST DERIVATION

You are asked to write a Python program for left and right most derivation. <br/>
For this purpose, your program should take three inputs. First is “ll.txt” which contains LL(1)<br/>
parsing table for left most derivation. Second is “lr.txt” which contains LR(1) parsing table for<br/>
right most derivation. Third is “input.txt” which contains input strings (could be more than 2)<br/>
you should process with their corresponding tables. You should use the following variables to<br/>
store file names.<br/>
FILE_LL = “ll.txt”<br/>
FILE_LR = “lr.txt”<br/>
FILE_INPUT = “input.txt”<br/>
These variables contains names of the files you must read. Their default value should<br/>
be the values given here, not different or personalized. In addition, you should NOT use<br/>
global addressing for these files (e.g. C:\user\student\Desktop\input.txt). You should<br/>
only use their names so that they are searched on local folder only.<br/>
Example files for ll.txt, lr.txt and input.txt are also given. You can examine them and change<br/>
them to test your software. Your program will be graded by using different parsing tables and<br/>
inputs, so make sure that your program works for all parsing tables and inputs, not just one.<br/>
Assuming your program takes the given example files as input, you are expected to generate an<br/>
output on console (not in a file) like given on the page below (the text given inside parenthesis<br/>
is for information only, you are not required to print it out but you can if you wish):<br/>
<hr/>
Read LL(1) parsing table from file ll.txt.<br/>
Read LR(1) parsing table from file lr.txt.<br/>
Read input strings from file input.txt.<br/>
Processing input string id+id*id$ for LL(1) parsing table.<br/><br/>
NO | STACK | INPUT | ACTION<br/>
1 | $ | id+id*id$ | E->TA<br/>
2 | $AT | id+id*id$ | T->FB<br/>
3 | $ABF | id+id*id$ | F->id<br/>
4 | $ABid | id+id*id$ | Match and remove id<br/>
5 | $AB | +id*id$ | B->ϵ<br/>
6 | $A | +id*id$ | A->+TA<br/>
7 | $AT+ | +id*id$ | Match and remove +<br/>
8 | $AT | id*id$ | T->FB<br/>
9 | $ABF | id*id$ | F->id<br/>
10 | $ABid | id*id$ | Match and remove id<br/>
11 | $AB | *id$ | B->*FB<br/>
12 | $ABF* | *id$ | Match and remove *<br/>
13 | $ABF | id$ | F->id<br/>
14 | $ABid | id$ | Match and remove id<br/>
15 | $AB | $ | B->ϵ<br/>
16 | $A | $ | A->ϵ<br/>
17 | $ | $ | ACCEPTED<br/><br/>
Processing input string acd$ for LR(1) parsing table.<br/>
NO | STATE STACK | READ | INPUT | ACTION<br/>
1 | 1 | a | acd$ | Shift to state 3<br/>
2 | 1 3 | c | acd$ | Shift to state 6<br/>
3 | 1 3 6 | d | acd$ | Shift to state 5<br/>
4 | 1 3 6 5 | $ | acd$ | Reverse B->d<br/>
5 | 1 3 6 | B | acB$ | Shift to state 7<br/>
6 | 1 3 6 7 | $ | acB$ | Reverse B->cB<br/>
7 | 1 3 | B | aB$ | Shift to state 4<br/>
8 | 1 3 4 | $ | aB$ | Reverse S->aB<br/>
9 | 1 | S | S$ | Shift to state 2<br/>
10 | 1 2 | $ | S$ | ACCEPTED<br/><br/>
Processing input string +id*id$ for LL(1) parsing table.<br/>
NO | STACK | INPUT | ACTION<br/>
1 | $ | +id*id$ | E->TA<br/>
2 | $AT | +id*id$ | REJECTED<br/> (T does not have an action/step for +)<br/><br/>
Processing input string cd$ for LR(1) parsing table.<br/>
NO | STATE STACK | READ | INPUT | ACTION<br/>
1 | 1 | c | cd$ | REJECTED (State 1 does not have an action/step for c)<br/><br/>
<hr/>
You should try to make your output as orderly as possible but do not spend days or weeks just<br/>
for small aesthetic improvements to the console output.<br/>
Correct execution and output will be very important for your grade, if your program does not<br/>
work correctly, your grade will be very low. In addition, your program should NOT import any<br/>
libraries or external packages, adding these and using alternative and easier methods and<br/>
algorithms for this assignment, will make your grade zero. If you really believe that this<br/>
assignment is not possible to do without external libraries, discuss it with me on class forums or<br/>
lab sessions.<br/><br/>
As you may have seen, there is a special character at your input files called Epsilon (ϵ). Make<br/>
sure your program detects this character correctly. Uppercase and lowercase version of this<br/>
character is shown in the links below.<br/>
https://www.compart.com/en/unicode/U+03B5<br/>
https://www.compart.com/en/unicode/U+03F5<br/>
Your input files uses spaces to make it more readable and table like, however this is not a<br/>
requirement. You should eliminate empty spaces when you read these files because input strings<br/>
“E->TA” and “E -> T A” are functionally equivalent in this context and you should consider<br/>
them as the same too.<br/>
