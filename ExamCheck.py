def read_candidate_answers():
    outfile=open('answers.txt','r')
    answer_list=outfile.read().split()
    return answer_list

def read_correct_answers():
    file=open('correct.txt', 'r')
    correct_list=file.read().split()
    return correct_list

#def correct_answers():
 #   correct_list = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
  #                  'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
   # return correct_list


#def open_answer():
 #   answer_list = []
  #  for i in range(0, 20):
   #     ele = input()
    #    answer_list.append(ele)
    #return answer_list


def check(correct_list, answers_list):
    count = 0
    print(correct_list)
    print(answers_list)
    wrong_answers = []
    for i in range(20):
        if correct_list[i] == answers_list[i]:
            count += 1
        else:
            wrong_answers.append(i)
            count += 0
    if count < 15:
        print('You failed')
    else:
        print('You passed')
    print('The number of correctly answers question is', count)
    print('The number of incorrectly answers question is', 20 - count)
    print('The question numbers of the incorrectly answers are', wrong_answers)


def main():
    correct_list = read_correct_answers()
    answers_list = read_candidate_answers()
    check(correct_list, answers_list)


if __name__ == "__main__":
    main()
