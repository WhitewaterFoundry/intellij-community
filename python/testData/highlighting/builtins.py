# bg is always black.
# effect is white
# func decl: red bold
# class decl: blue bold
# predefined decl: green bold

<info descr="null" type="INFORMATION" foreground="0x00ff00" background="0x000000" effectcolor="0xffffff" effecttype="BOXED" fonttype="1">len</info>("")
len = [] # redefine
len # no highlight

class <info descr="null" type="INFORMATION">A</info>(<info descr="null" type="INFORMATION" foreground="0x00ff00" background="0x000000" effectcolor="0xffffff" effecttype="BOXED" fonttype="1">object</info>):

  <info descr="null" type="INFORMATION" foreground="0x00ff00" background="0x000000" effectcolor="0xffffff" effecttype="BOXED" fonttype="1">@</info><info descr="null" type="INFORMATION">classmethod</info>
  def <info descr="null" type="INFORMATION">foo</info>(cls):
    pass

try:
  1/0
except <info descr="null" type="INFORMATION" foreground="0x00ff00" background="0x000000" effectcolor="0xffffff" effecttype="BOXED" fonttype="1">ArithmeticError</info>:
  pass
