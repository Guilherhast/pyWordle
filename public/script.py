from js import document, window, navigator, XMLHttpRequest
from pyodide import create_proxy
import unicodedata

#Global variables
word = ""
params = ""
norm_word = ""


#TODO
#Delete it after change the front end
#TEMP
fake_result = ['Y', '', 'N','N','N']

#Help functions
def normalize(text):
    nfkd_form = unicodedata.normalize('NFKD', text)
    norm = nfkd_form.encode('ASCII', 'ignore')
    ans = norm.decode('utf8')
    return ans.upper()


#TODO
#Make this function calculate the colors.
#It should return a vector with same len as word
#If entry[i] matches with word[i] result[i] should be 'G'
#If entry[i] is in word result[i] should be 'Y'
#Else entry[i] should be ''
def calc_colors(entry):
    global norm_word
    global fake_result
    for i in range(len(fake_result)):
        if fake_result[i] == 'Y':
            fake_result[i]='G'
        if fake_result[i] == '':
            fake_result[i]='Y'
        if fake_result[i] == 'N':
            fake_result[i]=''
    return fake_result

#Api
#TODO
#Make a function to request the
#daily word from the api.
#For this use: XMLHttpRequest
#https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
def get_word():
    return 'Front'.upper()
#Game functions
def row_check(row):
    entry = get_entry(row)
    ans = calc_colors(entry)
    mark_answer(row,ans)
    if ans == ['G','G','G','G','G']:
        show_win_screen()
    else:
        disable_row(row)
        add_row()

def show_win_screen():
    global word
    ms = document.getElementById("mainStack")
    winScreen = document.getElementById("winScreen")
    h2 = winScreen.getElementsByTagName("h2")[0]
    h2.innerText = word.upper()
    ms.classList.add('hidden')
    winScreen.classList.remove('hidden')
    pass

#Dom manipulation
def disable_row(row):
    for i in row.children:
        i.disabled = 'true'

def get_entry(row):
    text = []
    inputs = row.getElementsByTagName('input')
    for i in inputs:
        text.append(i.value)
    return text

def mark_answer(row, answer):
    winMsg = document.getElementById("winMsg")
    inputs = row.getElementsByTagName('input')
    winMsg.innerHTML += '<br>\n'
    for i in range(len(answer)):
        if answer[i] == 'G':
            inClass = 'bg-green'
            inputs[i].classList.add(inClass)
            winMsg.innerHTML += '🟩'
        elif answer[i] == 'Y':
            inClass = 'bg-yellow'
            inputs[i].classList.add(inClass)
            winMsg.innerHTML += '🟨'
        else:
            winMsg.innerHTML += '⬛'

def create_input():
    i =  document.createElement('input')
    i.type = 'text'
    i.setAttribute('maxlength',  1)
    i.setAttribute('onfocus',  'this.select()')
    i.addEventListener('input', proxy_on_input)
    i.addEventListener('keydown', proxy_on_key_down)
    return i


def add_row():
    global word
    row = document.createElement('div')
    row.classList.add('entryRow')

    for i in range(len(word)):
        row.append(create_input())

    btn = document.createElement('button')
    btn.type='submit'
    btn.innerHTML = '&gt;'
    btn.addEventListener('click', proxy_check)

    row.append(btn)

    stack = document.getElementById('mainStack')
    stack.append(row)

    row.getElementsByTagName("input")[0].focus()
    pass


#Pre proxies
def check_answer(e):
    row_check(e.target.parentElement)

def copy(e):
    winMsg = document.getElementById("winMsg")
    navigator.clipboard.writeText(winMsg.innerText)

def on_input(e):
    if e.inputType == 'insertText' or e.inputType == 'insertCompositionText':
        e.target.value = e.data[-1].upper()
        nextEl =  e.target.nextElementSibling
        nextEl.focus()

def on_key_down(e):
  if e.key.upper() == "BACKSPACE":
      e.target.value = ''
      e.target.previousElementSibling.focus()

#Proxies
proxy_check = create_proxy(check_answer)
proxy_copy = create_proxy(copy)
proxy_on_input = create_proxy(on_input)
proxy_on_key_down = create_proxy(on_key_down)

#System functions
def init():
    global params
    global word
    global norm_word

    try:
        params = window.location.href.split('?')[1]
    except:
        params = ''

    btnCopy = document.getElementById("btnCopy")
    btnCopy.addEventListener('click',proxy_copy)

    winMsg = document.getElementById("winMsg")
    url = window.location.href
    winMsg.innerHTML += "<br>\n<a href='%s'>%s</a>" % (url,url)

    word = get_word()
    norm_word = normalize(word)


def main():
    init()
    add_row()

if __name__ == '__main__':
    main()
