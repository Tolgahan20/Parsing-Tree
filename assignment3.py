import io
import time
import sys



def lex():  # lex function is created to get the next token
    global tokens
    global count
    global next_token
    next_token = tokens[count]
    count += 1


def unconsumed_input():  # this function is returning the input which are not read by the program
    print(tokens[(count - 1):])


# Converted Functions from Pseudo Code
def G():
    global error
    lex()
    print("G -> E")
    E()
    if ((next_token == "$") and (not(error))):
        print("success")
    else:
        print("error: unconsumed input,")
        unconsumed_input()

def E():
    if (error):
        quit()
    print("E -> T R")
    T()
    R()

def R():
    if (error):
        quit()
    if (next_token == '+'):
        print("R -> + T R")
        lex()
        T()
        R()
    elif(next_token == '-'):
        print("R -> - T R")
        lex()
        T()
        R()
    else:
        print("R -> e")

        
def T():
    if (error):
        quit()
    print("T -> F S")
    F()
    S()



def S():
    if (error):
        sys.exit()
    if (next_token == '*'):
        print("S -> * F S")
        lex()
        F()
        S()
    elif (next_token == '/'):
        print("S -> / F S")
        lex()
        F()
        S()
    else:
        print("S -> e")


def F():
    global error
    if (error):
        quit()
    if (next_token == '('):
        print("F ->( E )")
        lex()
        E()
        if (next_token == ')'):
            lex()

        else:
            error = True
            print("error: unexptected token ", next_token)
            print("error: unconsumed input, ")
            unconsumed_input()
            quit()

    elif ((next_token == "a") or (next_token == "b") or (next_token == "c") or (next_token == "d")):
        print("F -> M")
        M()

    elif ((next_token == "0") or (next_token == "1") or (next_token == "2") or (next_token == "3")):
        print("F -> N")
        N()

    else:
        error = True
        print("error: unexptected token ", next_token)
        print("error: unconsumed input,")
        unconsumed_input()


def M():
    global error
    if (error):
        quit()

    if ((next_token == "a") or (next_token == "b") or (next_token == "c") or (next_token == "d")):
        print("M ->", next_token)
        lex()

    else:
        error = True
        print("error: unexptected token ", next_token)
        print("error: unconsumed input,")
        unconsumed_input()


def N():
    global error
    if (error):
        quit()
    if((next_token == "0") or (next_token == "1") or (next_token == "2") or (next_token == "3")):
        print("N ->", next_token)
        lex()
    else:
        error = True
        print("error: unexptected token ", next_token)



if __name__ == '__main__': #main function where we run our program
  #global declerations
  global count
  global error
  global tokens
  global next_token

  error = False
  count = 0
  tokens = []
  next_token = '%'

  #reading file
  f = open('input1.txt', 'r')
  program = f.read()
  splitted = program.split(' ') #splitting the input

  tokens = []
  token = []

  for i in splitted:
      token += i.split('\n') #checking the whitespace and new lines
  for x in token:
      if x != '':
          tokens += x
  G() #running function G initially
