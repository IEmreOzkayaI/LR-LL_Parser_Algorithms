FILE_LL = "ll.txt"
FILE_LR = "lr.txt"
FILE_INPUT = "input.txt"


def lr_print_function(i,state_stack,product,input_string,action):
    print(
           "{:<5}{:<2}{:<18}{:<2}{:<8}{:<2}{:<10}{:<2}{:<10}".format(
                        i,
                        "|",
                        "".join(s[-1]+" " for s in state_stack),
                        "|",
                        "".join(product),
                        "|",
                        "".join(input_string),
                        "|",
                        action,

                    )
                    )

def ll_print_function(i,state_stack,input_string,action):
       print(
        "{:<5}{:<2}{:<13}{:<2}{:<13}{:<2}{:<5}".format(
            i,
            "|",
            "".join(state_stack),
            "|",
            "".join(input_string),
            "|",
            action,
        )
    )

# LL grammar dosyasının okunması ve grammar kurallarının çıkarılması
with open(FILE_LL, mode="r", encoding="utf-8") as f:
    grammar_lines = f.readlines()

# grammar kurallarının parse edilerek bir sözlük oluşturulması
ll_table = {}
ll_non_terminals = []
flag = False
tokens = []
for line in grammar_lines:
    if flag == False:
        firstLine = line.strip().replace(" ", "").split(";")
        tokens = firstLine[1:]
        flag = True
    else:
        production = line.strip().replace(" ", "").split(";")
        non_terminal = production[0].strip()
        ll_non_terminals.append(non_terminal)
        for i, element in enumerate(production[1:]):
            i = i + 1
            if element:
                if production[i] != "":
                    try:
                        ll_table[(non_terminal, firstLine[i])] = production[i].split("->")[1]
                        if (production[i].split("->")[0]) == "":
                            print("\nLL grammer Error in grammar file for left side of '->' but no problem we accept directly right side of arrow. Because we assume main non terminal belongs to left side of arrow.")
                    except:
                        print("\nLL grammer Error in grammar file for direction problem '->'")

print("\nRead LL(1) parsing table from file ll.txt.")

############################################################################################################
lr_table = {}
lr_state = []
lr_goto = []
lr_action = []

with open(FILE_LR, mode="r", encoding="utf-8") as f:
    right_grammer_lines = f.readlines()
flag = False
i = 0
for line in right_grammer_lines[0].strip().replace(" ", "").split(";"):
    if (line == "action"):
        lr_action.append(
            right_grammer_lines[1].strip().replace(" ", "").split(";")[i])

    if (line == "goto"):
        lr_goto.append(right_grammer_lines[1].strip().replace(
            " ", "").split(";")[i])
    i += 1


for line in right_grammer_lines[1:]:
    if flag == False:
        firstLine = line.strip().replace(" ", "").split(";")
        flag = True
    else:
        production = line.strip().replace(" ", "").split(";")
        non_terminal = production[0].strip()
        lr_state.append(non_terminal)
        for i, element in enumerate(production[1:]):
            i = i + 1
            if element:
                if production[i] != "":
                    lr_table[(non_terminal, firstLine[i])] = production[i]

print("Read LR(1) parsing table from file lr.txt.")

############################################################################################################


########## Take inputs and hold them in different dict.##################################

# id+id*id$ => ['id', '+', 'id', '*', 'id', '$'] turn.
input_family = []
def input_parser(input_string):
    ## read tokens from ll file but if you say not detect until come specific area then okey work this.
    current_word = ""
    words = []
    for char in input_string:
        if char in tokens:
            if current_word:
                input_family.append(current_word)
                words.append(current_word)
                current_word = ""
            words.append(char)
        else:
            current_word += char

    if current_word:
        words.append(current_word)
    

    return words


################### Read input and group them.#############################################
ll_inputs = {}
lr_inputs = {}
with open(FILE_INPUT, mode="r", encoding="utf-8") as f:
    input_lines = f.readlines()


for input_string in input_lines:
    if (input_string.strip().replace(" ", "").split(";")[0]) == "LL":
        ll_inputs[len(ll_inputs)] = input_parser(
            input_string.strip().replace(" ", "").split(";")[1]
        )
    if (input_string.strip().replace(" ", "").split(";")[0]) == "LR":
        lr_inputs[len(lr_inputs)] = input_string.strip().replace(
            " ", "").split(";")[1]


print("Read input strings from file input.txt.")

############################################################################################################

############## Reverse coming inputs ###################################
def reverse_input_ll(sentence):
    rev = []
    long = len(sentence) + 1
    board = len(sentence) + 1
    for i in range(1, len(sentence) + 1):
        val = i
        if tokens.__contains__(sentence[-i:board]):
            rev.append(sentence[-i:board])
        elif (ll_non_terminals.__contains__(sentence[-i:board])):
            rev.append(sentence[-i:board])
            board = -i
        else:
            continue

    return rev


def reverse_input_lr(sentence):
    rev = []
    long = len(sentence) + 1
    board = len(sentence) + 1
    for i in range(1, len(sentence) + 1):
        val = i
        part = sentence[-i:board]
        if (lr_action.__contains__(sentence[-i:board]) or lr_goto.__contains__(sentence[-i:board])):
            rev.append(sentence[-i:board])
            board = -i
        else:
            continue

    return rev


def count_strings_in_array(main_string, string_array):
    count = 0
    for s in main_string:
        if s in string_array:
            count += 1
    return count




##################### LL(1) PARSER ALGORITHM ########################################
def ll_parser(input_string, ll_table):
    stack = ["$"]
    i = 1
    print("\n")
    print(
        "{:<5}{:<15}{:<15}{:<20}".format(
            "NO", "|     STACK", "|     INPUT", "|   ACTION"
        )
    )

    action=str(list(ll_table.keys())[0][0]) + "->" + str(list(ll_table.values())[0])
    ll_print_function(i, stack,input_string,action)

    reversed_type = reverse_input_ll(ll_table.get(list(ll_table.keys())[0]))
    for char in reversed_type:
        stack.append(char)

    copy_stack = []
    copy_input = ""
    while len(stack) > 0 :
        top = stack[-1]
        current_input = input_string[0]

        if top == current_input:
            copy_stack = stack.copy()
            copy_input = input_string.copy()
            input_string.pop(0)
            stack.pop()
            if top == "$":
                i += 1
                ll_print_function(i, copy_stack,copy_input,"ACCEPTED")
                continue
            else:
                i += 1
                ll_print_function(i, copy_stack,copy_input,"Match and remove " + top)
                continue
        elif (top, current_input) in ll_table:
            i += 1
            production = ll_table[(top, current_input)]
            action = top + "->" + production

            ll_print_function(i, stack,input_string,action)

            stack.pop() # Remove printed key from stack

            if input_family.__contains__(production): # like id or + or * or $ etc.
                stack.append(production)
            elif production == "ϵ": 
                continue
            else: #like AT -> TA REVERSE operation
                reversed_type = reverse_input_ll(production)
                if reversed_type == []: 
                    # if it doesn't contain non-terminal or terminal char then it is error.
                    # Because this pattern is not in grammar.
                    i+=1
                    ll_print_function(i, stack,input_string,
                    "REJECTED ( "+ "".join(production)+ " it is not suitable pattern for " + "".join
                    (top)+" "+  "".join(current_input) + " )")
                    break
                else:
                    for char in reversed_type:
                        stack.append(char)
        else:
            i+=1
            ll_print_function(i, stack,input_string,"REJECTED ( "+ "".join
                (top)+ " does not have an action/step for "+ "".join(current_input) + " )")    
            break


##################### LR(1) PARSER ALGORITHM ########################################
def lr_parser(input_string, lr_table):
    input_stack = []
    temp_stack = []
    state_stack = []
    
    state_stack.append(lr_state[0])
    counter = 0
    input_stack = reverse_input_lr(input_string)
    print("\n")
    print(
        "{:<5}{:<20}{:<10}{:<12}{:<20}".format(
            "NO", "|   STATE  STACK", "|   READ", "|   INPUT", "|   ACTION"
        )
    )

    while len(input_stack) > 0:
        product = input_stack.pop()
        temp_stack.append(product)
        new_state = ""
        action_output = ""

        if (state_stack[-1], product) in lr_table:
            if product == "$":
                temp_stack.pop();
                control_state = lr_table[(state_stack[-1], product)]
                if control_state.upper() == "ACCEPT" :
                   counter+=1
                   lr_print_function(counter,state_stack,product,input_string,"ACCEPTED")
                   break
                elif not(lr_state.__contains__(control_state)):
                    input_stack.append(product)
                    control_state = control_state.split("->")
                    ## control any pattern exist to right side.
                    pattern_count = 0;
                    control_pattern= []
                    isFind=False;
                    for element in temp_stack[::-1]:
                        control_pattern.append(element);
                        pattern_count +=1
                        c=control_pattern[::-1]
                        if "".join(control_pattern[::-1]) == control_state[1]:
                            while pattern_count > 0:
                                temp_stack.pop()
                                pattern_count-=1
                            input_stack.append(control_state[0])
                            isFind=True
                    if isFind==False:
                        counter+=1
                        lr_print_function(counter,state_stack,product,input_string,"REJECTED ( Input string doesn't contain " + "".join(control_state[1]) +" pattern )")
                        break
                else:
                    counter+=1
                    lr_print_function(counter,state_stack,product,input_string,"REJECTED ( Specified cell "+ "".join(state_stack[-1])+ " and $ contains state name )")
                    break

            ## if it is not $ and also if it is a terminal and after made changes for $ , turn right to left control.       
            if (lr_table[(state_stack[-1], product)]) in lr_table.values():
                new_state = lr_table[(state_stack[-1], product)]
                if lr_action.__contains__(product):
                     if product == "$":
                        action_output ="Reverse " + new_state
                     else:
                        action_output = "Shift to state " + new_state[-1]
                elif lr_goto.__contains__(product):
                    action_output = "Change to state " + new_state[-1]
                else:
                    action_output = new_state
                counter += 1
                lr_print_function(counter,state_stack,product,input_string,action_output)

                if product == "$":
                    i=0;
                    while i < count_strings_in_array(control_state[1],lr_action + lr_goto):
                        state_stack.pop()
                        i+=1
                    input_string=input_string.replace(control_state[1], control_state[0])
                else:   
                    state_stack.append(new_state)
            else:
                counter+=1
                lr_print_function(counter,state_stack,product,input_string,"REJECTED ( "+ "".join
                (state_stack[-1])+ " does not have an action/step for "+ "".join(product) + " )")
                break
            
        else:
            counter+=1
            lr_print_function(counter,state_stack,product,input_string,"REJECTED ( "+ "".join
            (state_stack[-1])+ " does not have an action/step for "+ "".join(product) + " )")
            break
            


##################################### Turn All LL(1) inputs to LL(1) parser.#####################################
###################################### Turn All LR(1) inputs to LR(1) parser.#####################################

for i in range(max(len(ll_inputs.values()), len(lr_inputs.values()))):
    if i < len(ll_inputs.values()):
        input_string = list(ll_inputs.values())[i]
        print("\n\nProcessing input string "+ "".join(input_string) +" for LL(1) parsing table.")
        ll_parser(input_string, ll_table)
    if i < len(lr_inputs.values()):
            input_string = list(lr_inputs.values())[i]
            print("\n\nProcessing input string "+ "".join(input_string) +" for LR(1) parsing table.")
            lr_parser(input_string, lr_table)
