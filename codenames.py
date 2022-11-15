'''
The file locations are hardcoded in because I hate you
Feel free to change them if you want, or use a variable like a normal person

This program downloads lists of associated words from https://wordassociations.net/en/words-associated-with/ and uses them to enhance your codename clues
It's actually pretty bad but if you run it in the command prompt it looks hackery and cool
I didn't use beautiful soup so expect this to break if the website is ever updated, but it doesn't look like it's been updated since like 2005 so I think we're fine
This program goes through the raw html because I'm a psycho
'''
import subprocess as s
def collect_words(url):
    f = open('main.bat', 'w')
    f.write(r'cd C:\PythonPrograms\Codenames\data' + '\n')
    game = url[::-1][0:url[::-1].find('/')][::-1]
    print(game, url)
    f.write('curl ' + url + '/nickname-input'  + ' -o ' + game + '.txt' + '\n')
    f.close()
def create(words):
    f = open('main.bat', 'w')
    f.write(r'cd C:\PythonPrograms\Codenames\data' + '\n')
    for i in range(len(words)):
        try:
            dummy = open(r'C:\PythonPrograms\Codenames\data\\' + words[i] + '1' + '.txt')
        except:
            f.write(r'curl https://wordassociations.net/en/words-associated-with/' + words[i]  + ' -o ' + words[i] + '1' + '.txt' + '\n')
    f.close()
def pages(words):
    f = open('main.bat', 'w')
    f.write(r'cd C:\PythonPrograms\Codenames\data' + '\n')
    out = []
    for i in range(len(words)):
        g = open(r'C:\PythonPrograms\Codenames\data\\' + words[i] + '1' + '.txt', encoding="utf-8").read()
        if g.find('There is no association found for') == -1 and g.find('Please make sure that the word is spelled correctly.') == -1:
            jlcr = g.find('Next') - 74 - len(words[i])
            if jlcr != -75 - len(words[i]):
                jlnt = int(g[jlcr])
                if g[jlcr - 1] in '123456789':
                    jlnt += int(g[jlcr - 1]) * 10
                out.append(jlnt)
                for z in range(2, jlnt + 1):
                    try:
                        dummy = open(r'C:\PythonPrograms\Codenames\data\\' + words[i] + str(z) + '.txt')
                    except:
                        f.write(r'curl https://wordassociations.net/en/words-associated-with/' + words[i]  + '?start=' + str((z - 1) * 100) + ' -o ' + words[i] + str(z) + '.txt' + '\n')
            else:
                out.append(1)
        else:
            out.append(0)
    return out
def read(word, lbl):
    out = []
    for label in range(1, lbl + 1):
        f = open(r'C:\PythonPrograms\Codenames\data\\' + word + str(label) + '.txt', encoding="utf-8").read()
        stop = f.find('ADJECTIVE') - 39
        ind = f.find('NOUN') + 92
        while ind < stop:
            n = ''
            while f[ind] != '"':
                n += f[ind]
                ind += 1
            if not n in out:
                out.append(n)
            ind -= int(2.5 * n.count('%'))
            ind += 50 + len(n)
        stop = f.find('VERB') - 39
        ind += 99
        while ind < stop:
            n = ''
            while f[ind] != '"':
                n += f[ind]
                ind += 1
            if not n in out:
                out.append(n)
            ind -= int(2.5 * n.count('%'))
            ind += 50 + len(n)
        stop = f.find('ADVERB') - 39
        if stop != -40:
            ind += 84
            while ind < stop:
                n = ''
                while f[ind] != '"':
                    n += f[ind]
                    ind += 1
                if not n in out:
                    out.append(n)
                ind -= int(2.5 * n.count('%'))
                ind += 50 + len(n)
            stop = f.find('facebook') - 73
            if stop != -74:
                ind += 90
                while ind < stop:
                    n = ''
                    while f[ind] != '"':
                        n += f[ind]
                        ind += 1
                    if not n in out:
                        out.append(n)
                    ind -= int(2.5 * n.count('%'))
                    ind += 50 + len(n)
        else:
            stop = f.find('facebook') - 73
            if stop != -74:
                ind += 84
                while ind < stop:
                    n = ''
                    while f[ind] != '"':
                        n += f[ind]
                        ind += 1
                    if not n in out:
                        out.append(n)
                    ind -= int(2.5 * n.count('%'))
                    ind += 50 + len(n)
    return out
def score():
    master = []
    whomst = []
    good = []
    for i in range(len(data)):
        for j in data[i]:
            if j in master:
                whomst[master.index(j)].append(combined_list[i])
            else:
                master.append(j)
                whomst.append([combined_list[i]])
    for i in range(len(master)):
        sub = 0
        for j in whomst[i]:
            if j in anti_list:
                sub += 2.1
            if j in neutral_list:
                sub += 1.1
            if j in black_list:
                sub += 10.1
        if len(whomst[i]) > 1:
            good.append((round((len(whomst[i]) - sub), 1), master[i], whomst[i]))
    good = sorted(good)
    for i in good:
        print(i)
    return master, whomst
words = input("Your Words:")
anti = input("Opponent's Words:")
neutral = input("Neutral Words:")
black = input("Black Words:")
words_list = words.split()
anti_list = anti.split()
neutral_list = neutral.split()
black_list = black.split()
combined_list = words_list + anti_list + neutral_list + black_list
# collect_words(input('url:'))
# s.call(['main.bat'])
create(combined_list)
s.call(['main.bat'])
lbls = pages(combined_list)
s.call(['main.bat'])
data = []
for i in range(len(combined_list)):
    data.append(read(combined_list[i], lbls[i]))
# print(words_list)
score()
for i in range(len(combined_list)):
    if lbls[i] == 0:
        print('Error, ' + combined_list[i] + ' not found')
print(words)
print(anti)
print(neutral)
print(black)
