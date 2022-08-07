from numpy import random

def store(a = []):                                 # for storing the values of the playes #
     def closure():
         return (a)
     return closure

def storeI(a = []):
     def closure():
         return (a)
     return closure

def count(i = [0]):
     def closure():
         return (i)
     return closure

def countI(i = [0]):
     def closure():
         return (i)
     return closure

                                   #############################  storing the values   ########################### 
                                   
                                   
def sourav(oppIn = None):
         i = count()
         tCnt = i()
         lEle = tCnt[len(tCnt)-1]
         tCnt.append((lEle)+1)
         cnt = count(tCnt)
         currCn = cnt()
         curCnt = currCn[len(currCn)-1]

         oppResp = store()
         if (oppIn != None):
                 tOppResp = oppResp()
                 tOppResp.append(oppIn)
                 opResp = store(tOppResp)
                 cOverallResp = opResp()
         else:
                 cOverallResp = []
         if (curCnt < 3):
                 return "D"
         else:
                 if "D" in cOverallResp[curCnt-3:curCnt]:
                         return "D"
                 else:
                         return "C"

                                        ################### storing values for I term ###########################
                                        
                                        
def souravI(oppIn = None):
         i = countI()
         tCnt = i()
         lEle = tCnt[len(tCnt)-1]
         tCnt.append((lEle)+1)
         cnt = countI(tCnt)
         currCn = cnt()
         curCnt = currCn[len(currCn)-1]

         oppResponse = storeI()
         if (oppIn != None):
                 tOppResp = oppResponse()
                 tOppResp.append(oppIn)
                 opResp = storeI(tOppResp)
                 curOverallResp = opResp()
         else:
                 cOverallResp = []
         if (curCnt < 3):
                 return "C"
         else:
                 if "C" in cOverallResp[curCnt-3:curCnt]:
                         return "C"
                 else:
                         return "D"


def random1(oppIn = None):
     return random.choice(["C", "D"])

def counter(i=[0]):
     def closure():
         return (i)
     return closure

def score_p(i=[]):
     def closure():
         return (i)
     return closure

def score_o(i=[]):
     def closure():
         return (i)
     return closure

def counterTr(i=[0]):
     def closure():
         return (i)
     return closure

def score_pTr(i=[]):
     def closure():
         return (i)
     return closure

def score_oTr(i=[]):
     def closure():
         return (i)
     return closure

                                                 ##############for scores ###############################
                                                 
                                                 
def score(my_input=None,op_input=None):
     my_counter = 0
     op_counter = 0
     for my_inp, op_inp in zip(my_input, op_input):
         if (my_inp == "C" and op_inp =="C"):
             my_counter = my_counter + 20
             op_counter = op_counter + 20
         elif (my_inp == "C" and op_inp =="D"):
             my_counter = my_counter + 0
             op_counter = op_counter + 30
         elif (my_inp == "D" and op_inp =="C"):
             my_counter = my_counter + 30
             op_counter = op_counter + 0
         elif (my_inp == "D" and op_inp =="D"):
             my_counter = my_counter + 10
             op_counter = op_counter + 10
     return(my_counter-op_counter)
                                                   ######################Starterg Dominanty#############################
                                                   
                                                   
def sourav(opp_move = None):
     cn = counterTr()
     cn_temp = cn()
     i = cn_temp[len(cn_temp)-1]
     cn_temp.append(i+1)
     ct = counterTr(cn_temp)

     if  i == 0:
             my_move = "D"
             score_pTr([my_move])

     elif i > 0:

             my_moves = score_pTr()
             op_moves = score_oTr()

             my_moves_list = my_moves()
             op_moves_list = op_moves()

             if (i == 1):
                 score_cal = score(my_moves_list, [opp_move])
             else:
                 score_cal = score(my_moves_list, op_moves_list)

             if  score_cal > 0:
                 my_move = "C"
             else:
                 my_move = "D"

             my_moves_list.append(my_move)
             op_moves_list.append(opp_move)
             my_m = score_pTr(my_moves_list)
             op_m = score_oTr(op_moves_list)

     return my_move
 

                                                ############ Main Code ############
                                                
                                                
dispatcher = {'random1' : random1, 'sourav' : sourav}

function_list = [ 'random1','sourav']


def dispatch(name, *args, **kwargs):
     return dispatcher[name](*args, **kwargs)

match_count = [0] * len(function_list)
total_score = [0] * len(function_list)
total_wins = [0] * len(function_list)

cont = 0


while(cont < 500):
         n = 10
         i = 0

         randomly_selected_functions = random.choice(function_list, size = (2))

         index_fun1 = function_list.index(randomly_selected_functions[0])
         index_fun2 = function_list.index(randomly_selected_functions[1])

         match_count[index_fun1] += 1
         match_count[index_fun2] += 1

         out1 = dispatch(randomly_selected_functions[0])
         out2 = dispatch(randomly_selected_functions[1])
         p1 = 0
         p2 = 0
         while(i < n):
                 if(out1 == out2 and out1 == "C"):
                         p1 = p1 + 20
                         p2 = p2 + 20
                 elif(out1 == out2 and out1 == "D"):
                         p1 = p1 + 10
                         p2 = p2 + 10
                 elif(out1 != out2 and out1 == "D"):
                         p1 = p1 + 30
                 else:
                         p2 = p2 + 30
                 out1T = dispatch(randomly_selected_functions[0], out2)
                 out2 = dispatch(randomly_selected_functions[1], out1)
                 out1 = out1T
                 i+=1
         total_score[index_fun1] += p1
         total_score[index_fun2] += p2
         if (p1 > p2):
             total_wins[index_fun1] += 1
         else:
             total_wins[index_fun2] += 1

         cont += 1
avg_score = [x / y for x, y in zip(total_score, match_count)]
print("Winner function is :",
function_list[avg_score.index(max(avg_score))], "!!! and score of winner is :", round(max(avg_score), 3))


print("\nAll scores:")
print("Matches Played - Average Score - Total Wins - % wins - Function")
for a, b, c, d in sorted(zip(function_list, match_count, avg_score, total_wins), key = lambda x: x[2], reverse = True):
         print(b, " - ", round(c, 2), " - ", d, " - ", (round(d/b * 100, 2)) , " - ", a)
