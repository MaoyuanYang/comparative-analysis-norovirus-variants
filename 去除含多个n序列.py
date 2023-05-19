file = open('result/align/VP1-clear/3-VP1-clear.fas', 'r')
seq = []
fas = ''
line = file.readline()
while line:
    if '>' in line:
        fas = fas + ''.join(seq)
        seq = [line]
    else:
        seq.append(line)
        if line.count('n') >= 10:
            seq = []
    line = file.readline()
out = open('result/align/VP1-clear/3-VP1-clear-deleten.fas', 'w')
out.write(fas)
