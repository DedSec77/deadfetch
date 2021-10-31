from colorama import Fore
from osinfo import Variables
import platform

reset = Fore.RESET

computer1 = """
                       .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
"""

dos = r"""
             ________________________________________________
            /                                                \
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\> _                                 |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
"""

redhat = rf"""
{Fore.RED}                          _____
{Fore.RED}                   _.+sd$$$$$$$$$bs+._
{Fore.RED}               .+d$$$$$$$$$$$$$$$$$$$$$b+.                          {Fore.RED + Variables.User + "@" + Variables.distr + Fore.RESET}
{Fore.RED}            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.
{Fore.RED}          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.                     {Fore.RED + "CPU: " + reset + Variables.CPU}
{Fore.RED}        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.                   {Fore.RED +"Bit: " + reset + Variables.Bit}
{Fore.RED}       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s                  {Fore.RED +"System: " + reset + platform.system()}
{Fore.RED}     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.                {Fore.RED +"Distro: " + reset +  Variables.distr}
{Fore.RED}    .$$$$$$$$$$$$P                       T$$$$$$$$$$.               {Fore.RED +"Shell: " + reset + Variables.shell}
{Fore.RED}   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.              {Fore.RED +"Ram: " + reset + Variables.ram}
{Fore.RED}  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;             {Fore.RED +"Wm: " + reset + Variables.GUI}
{Fore.RED}  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$             {Fore.RED +"Terminal: " + reset + Variables.term}
{Fore.RED} :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$;
{Fore.RED} $$$$$$$P         `*T$$$$$b              '      `T$$$$$$
{Fore.RED}:$$$$$$$b            `*T$$$s                      :$$$$$;
{Fore.RED}:$$$$$$$$b.                                        $$$$$;
{Fore.RED}$$$$$$$$$$$b.                                     :$$$$$$
{Fore.RED}$$$$$$$$$$$$$bs.                                 .$$$$$$$
{Fore.RED}$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
{Fore.RED}:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
{Fore.RED}:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
{Fore.RED} $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
{Fore.RED} :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$;
{Fore.RED}  $$$b       `T$b+                        :$$$$$$$BUG$$
{Fore.RED}  :$P'         `"'               ,._.     ;$$$$$$$$$$$;
{Fore.RED}   \                            `*TP*     d$$P*******$
{Fore.RED}    \                                    :$$P'      /
{Fore.RED}     \                                  :dP'       /
{Fore.RED}      `.                               d$P       .'
{Fore.RED}        `.                             `'      .'
{Fore.RED}          `-.                               .-'
{Fore.RED}             `-.                         .-'
{Fore.RED}                `*+-._             _.-+*'
{Fore.RED}                      `"*-------*"'
"""

fedora = Fore.BLUE + rf"""

{Fore.BLUE}          /:-------------:\
{Fore.BLUE}       :-------------------::
{Fore.BLUE}     :-----------/{Fore.WHITE}shhOHbmp{Fore.BLUE}---:\                 {Fore.BLUE + Variables.User + "@" + Variables.distr + Fore.RESET}
{Fore.BLUE}   /-----------{Fore.WHITE}omMMMNNNMMD{Fore.BLUE}  ---:
{Fore.BLUE}  :-----------{Fore.WHITE}sMMMMNMNMP.{Fore.BLUE}    ---:               {Fore.BLUE + "CPU: " + reset + Variables.CPU}
{Fore.BLUE} :-----------:{Fore.WHITE}MMMdP{Fore.BLUE}-------    ---\              {Fore.BLUE +"Bit: " + reset + Variables.Bit}
{Fore.BLUE},------------:{Fore.WHITE}MMMd{Fore.BLUE}--------    ---:              {Fore.BLUE +"System: " + reset + platform.system()}
{Fore.BLUE}:------------:{Fore.WHITE}MMMd{Fore.BLUE}-------    .---:              {Fore.BLUE +"Distro: " + reset +  Variables.distr}
{Fore.BLUE}:----    {Fore.WHITE}oNMMMMMMMMMNho{Fore.BLUE}     .----:              {Fore.BLUE +"Shell: " + reset + Variables.shell}
{Fore.BLUE}:--     {Fore.WHITE}.+shhhMMMmhhy++{Fore.BLUE}   .------/              {Fore.BLUE +"Ram: " + reset + Variables.ram}
{Fore.BLUE}:-    -------:{Fore.WHITE}MMMd{Fore.BLUE}--------------:               {Fore.BLUE +"Wm: " + reset + Variables.GUI}
{Fore.BLUE}:-   --------/{Fore.WHITE}MMMd{Fore.BLUE}-------------;                {Fore.BLUE +"Terminal: " + reset + Variables.term}
{Fore.BLUE}:-    ------/{Fore.WHITE}hMMMy{Fore.BLUE}------------:
{Fore.BLUE}:-- :{Fore.WHITE}dMNdhhdNMMNo{Fore.BLUE}------------;
{Fore.BLUE}:---:{Fore.WHITE}sdNMMMMNds{Fore.BLUE}:------------:
{Fore.BLUE}:------:://:-------------::
{Fore.BLUE}:---------------------://
""" + Fore.RESET

windows = rf'''
                   88                      88
                   ""                      88
                                           88
8b      db      d8 88 8b,dPPYba,   ,adPPYb,88  ,adPPYba,  8b      db      d8 ,adPPYba       {"CPU: " + Variables.CPU}
`8b    d88b    d8' 88 88P'   `"8a a8"    `Y88 a8"     "8a `8b    d88b    d8' I8[    ""      {"Bit: " + Variables.Bit}
 `8b  d8'`8b  d8'  88 88       88 8b       88 8b       d8  `8b  d8'`8b  d8'  `"Y8ba,        {"System: " + platform.system()}
  `8bd8'  `8bd8'   88 88       88 "8a,   ,d88 "8a,   ,a8"   `8bd8'  `8bd8'    aa    ]8I     {"Ram: " + Variables.ram}
    YP      YP     88 88       88  `"8bbdP"Y8  `"YbbdP"'      YP      YP      "YbbdP"

'''
ubuntu = Fore.YELLOW + f"""
{Fore.YELLOW}            .-.
{Fore.YELLOW}         .-'``(   )             {Fore.YELLOW + Variables.User + "@" + Variables.distr + Fore.RESET}
{Fore.YELLOW}      ,`\ \    `-`.
{Fore.YELLOW}     /   \ '``-.   `            {Fore.YELLOW + "CPU: " + reset + Variables.CPU}
{Fore.YELLOW}   .-.  ,       `___:           {Fore.YELLOW +"Bit: " + reset + Variables.Bit}
{Fore.YELLOW}  (   ) :        ___            {Fore.YELLOW +"System: " + reset + platform.system()}
{Fore.YELLOW}   `-`  `       ,   :           {Fore.YELLOW +"Distro: " + reset +  Variables.distr}
{Fore.YELLOW}     \   / ,..-`   ,            {Fore.YELLOW +"Shell: " + reset + Variables.shell}
{Fore.YELLOW}      `./ /    .-.`             {Fore.YELLOW +"Ram: " + reset + Variables.ram}
{Fore.YELLOW}         `-..-(   )             {Fore.YELLOW +"Wm: " + reset + Variables.GUI}
{Fore.YELLOW}               `-`              {Fore.YELLOW +"Terminal: " + reset + Variables.term}
""" + Fore.RESET

debian = Fore.RED + rf"""
{Fore.RED}         _sudZUZ#Z#XZo=_            {Fore.RED + Variables.User + "@" + Variables.distr + Fore.RESET}
{Fore.RED}      _jmZZ2!!~---~!!X##wa
{Fore.RED}   .<wdP~~            -!YZL,        {Fore.RED + "CPU: " + reset + Variables.CPU}
{Fore.RED}  .mX2'       _%aaa__     XZ[.      {Fore.RED +"Bit: " + reset + Variables.Bit}
{Fore.RED}  oZ[      _jdXY!~?S#wa   ]Xb;      {Fore.RED +"System: " + reset + platform.system()}
{Fore.RED} _#e'     .]X2(     ~Xw|  )XXc      {Fore.RED +"Distro: " + reset +  Variables.distr}
{Fore.RED}..2Z`      ]X[.       xY|  ]oZ(     {Fore.RED +"Shell: " + reset + Variables.shell}
{Fore.RED}..2#;      )3k;     _s!~   jXf`     {Fore.RED +"Ram: " + reset + Variables.ram}
{Fore.RED} 1Z>      -]Xb/    ~    __#2(       {Fore.RED +"Wm: " + reset + Variables.GUI}
{Fore.RED} -Zo;       +!4ZwaaaauZZXY'         {Fore.RED +"Terminal: " + reset + Variables.term}
{Fore.RED}  *#[,        ~-?!!!!!!-~
{Fore.RED}   XUb;.
{Fore.RED}    )YXL,,
{Fore.RED}      +3#bc,
{Fore.RED}        -)SSL,,
{Fore.RED}           ~~~~~
""" + Fore.RESET

popos = Fore.BLUE + f"""
             /////////////                                                                                      {Fore.BLUE + Variables.User + "@" + Variables.distr + Fore.RESET + Fore.BLUE}
         /////////////////////
      ///////{Fore.WHITE}*767{Fore.BLUE}////////////////                                                        {Fore.BLUE + "CPU: " + reset + Variables.CPU  + Fore.BLUE}
    //////{Fore.WHITE}7676767676*{Fore.BLUE}//////////////                                                      {Fore.BLUE +"Bit: " + reset + Variables.Bit  + Fore.BLUE}
   /////{Fore.WHITE}76767{Fore.BLUE}//{Fore.WHITE}7676767{Fore.BLUE}//////////////                                                     {Fore.BLUE +"System: " + reset + platform.system()  + Fore.BLUE}
  /////{Fore.WHITE}767676{Fore.BLUE}///{Fore.WHITE}*76767{Fore.BLUE}///////////////                                                    {Fore.BLUE +"Distro: " + reset +  Variables.distr  + Fore.BLUE}
 ///////{Fore.WHITE}767676{Fore.BLUE}///{Fore.WHITE}76767.{Fore.BLUE}///{Fore.WHITE}7676*{Fore.BLUE}///////                                                   {Fore.BLUE +"Shell: " + reset + Variables.shell  + Fore.BLUE}
/////////{Fore.WHITE}767676{Fore.BLUE}//{Fore.WHITE}76767{Fore.BLUE}///{Fore.WHITE}767676{Fore.BLUE}////////                                                  {Fore.BLUE +"Ram: " + reset + Variables.ram  + Fore.BLUE}
//////////{Fore.WHITE}76767676767{Fore.BLUE}////{Fore.WHITE}76767{Fore.BLUE}/////////                                                  {Fore.BLUE +"Wm: " + reset + Variables.GUI  + Fore.BLUE}
///////////{Fore.WHITE}76767676{Fore.BLUE}//////{Fore.WHITE}7676{Fore.BLUE}//////////                                                  {Fore.BLUE +"Terminal: " + reset + Variables.term  + Fore.BLUE}
////////////{Fore.WHITE},7676,{Fore.BLUE}///////{Fore.WHITE}767{Fore.BLUE}///////////
/////////////{Fore.WHITE}*7676{Fore.BLUE}///////{Fore.WHITE}76{Fore.BLUE}////////////
///////////////{Fore.WHITE}7676{Fore.BLUE}////////////////////
 ///////////////{Fore.WHITE}7676///{Fore.WHITE}767{Fore.BLUE}////////////
  //////////////////////{Fore.WHITE}'{Fore.BLUE}////////////
   //////{Fore.WHITE}.7676767676767676767,{Fore.BLUE}//////
    /////{Fore.WHITE}767676767676767676767{Fore.BLUE}/////
      ///////////////////////////
         /////////////////////
             /////////////"""


arch = Fore.CYAN + rf"""
{Fore.CYAN}                   ▄                        {Fore.CYAN + Variables.User + "@" + Variables.distr + Fore.RESET}
{Fore.CYAN}                  ▟█▙
{Fore.CYAN}                 ▟███▙                      {Fore.CYAN + "CPU: " + reset + Variables.CPU}
{Fore.CYAN}                ▟█████▙                     {Fore.CYAN +"Bit: " + reset + Variables.Bit}
{Fore.CYAN}               ▟███████▙                    {Fore.CYAN +"System: " + reset + platform.system()}
{Fore.CYAN}              ▂▔▀▜██████▙                   {Fore.CYAN +"Distro: " + reset +  Variables.distr}
{Fore.CYAN}             ▟██▅▂▝▜█████▙                  {Fore.CYAN +"Shell: " + reset + Variables.shell}
{Fore.CYAN}            ▟█████████████▙                 {Fore.CYAN +"Ram: " + reset + Variables.ram}
{Fore.CYAN}           ▟███████████████▙                {Fore.CYAN +"Wm: " + reset + Variables.GUI}
{Fore.CYAN}          ▟█████████████████▙               {Fore.CYAN +"Terminal: " + reset + Variables.term}
{Fore.CYAN}         ▟███████████████████▙
{Fore.CYAN}        ▟█████████▛▀▀▜████████▙
{Fore.CYAN}       ▟████████▛      ▜███████▙
{Fore.CYAN}      ▟█████████        ████████▙
{Fore.CYAN}     ▟██████████        █████▆▅▄▃▂
{Fore.CYAN}    ▟██████████▛        ▜█████████▙
{Fore.CYAN}   ▟██████▀▀▀              ▀▀██████▙
{Fore.CYAN}  ▟███▀▘                       ▝▀███▙
{Fore.CYAN} ▟▛▀                               ▀▜▙
""" + Fore.RESET


gentoo = Fore.MAGENTA + rf"""
         -/oyddmdhs+:.
     -odNMMMMMMMMNNmhy+-`
   -yNMMMMMMMMMMMNNNmmdhy+-
 `omMMMMMMMMMMMMNmdmmmmddhhy/`
 omMMMMMMMMMMMNhhyyyohmdddhhhdo`
.ydMMMMMMMMMMdhs++so/smdddhhhhdm+`              {Fore.MAGENTA + Variables.User + "@" + Variables.distr + Fore.RESET  + Fore.MAGENTA}
 oyhdmNMMMMMMMNdyooydmddddhhhhyhNd.
  :oyhhdNNMMMMMMMNNNmmdddhhhhhyymMh             {Fore.MAGENTA + "CPU: " + reset + Variables.CPU  + Fore.MAGENTA}
    .:+sydNMMMMMNNNmmmdddhhhhhhmMmy             {Fore.MAGENTA +"Bit: " + reset + Variables.Bit  + Fore.MAGENTA}
       /mMMMMMMNNNmmmdddhhhhhmMNhs:             {Fore.MAGENTA +"System: " + reset + platform.system()  + Fore.MAGENTA}
    `oNMMMMMMMNNNmmmddddhhdmMNhs+`              {Fore.MAGENTA +"Distro: " + reset +  Variables.distr  + Fore.MAGENTA}
  `sNMMMMMMMMNNNmmmdddddmNMmhs/.                {Fore.MAGENTA +"Shell: " + reset + Variables.shell  + Fore.MAGENTA}
 /NMMMMMMMMNNNNmmmdddmNMNdso:`                  {Fore.MAGENTA +"Ram: " + reset + Variables.ram  + Fore.MAGENTA}
+MMMMMMMNNNNNmmmmdmNMNdso/-                     {Fore.MAGENTA +"Wm: " + reset + Variables.GUI  + Fore.MAGENTA}
yMMNNNNNNNmmmmmNNMmhs+/-`                       {Fore.MAGENTA +"Terminal: " + reset + Variables.term  + Fore.MAGENTA}
/hMMNNNNNNNNMNdhs++/-`
`/ohdmmddhys+++/:.`
  `-//////:--.
""" + Fore.RESET

apple =  Fore.GREEN + f"""
            .:'           {Fore.GREEN + Variables.User + "@" + platform.system() + reset + Fore.GREEN}
         __ :'__
      .'`  `-'  ``.       {Fore.RED + "CPU: " + reset + Variables.CPU + Fore.RED}
     :          .-'       {Fore.YELLOW + "Bit: " + reset + Variables.Bit + Fore.YELLOW}
     :         :          {"System: " + reset + platform.system() + Fore.YELLOW}
      :         `-;       {Fore.BLUE + "Shell: " + reset + Variables.shell + Fore.BLUE}
       `.__.-.__.'        {"Ram: " + reset + Variables.ram}
""" + Fore.RESET




# Сука ты коннченая, козлина ты ебанныая, ты сука сучара блять

raspberry = Fore.GREEN + rf"""
   .~~.   .~~.      {Variables.User + "@" + Variables.distr + Fore.RESET + Fore.GREEN}
   '. \ ' ' / .
   .~ .~~~..~.      {Fore.RED + "CPU: " + reset + Variables.CPU  + Fore.RED}
  : .~.'~'.~. :     {Fore.RED +"Bit: " + reset + Variables.Bit  + Fore.RED}
 ~ (   ) (   ) ~    {Fore.RED +"System: " + reset + platform.system()  + Fore.RED}
( : '~'.~.'~' : )   {Fore.RED +"Distro: " + reset +  Variables.distr  + Fore.RED}
 ~ .~ (   ) ~. ~    {Fore.RED +"Shell: " + reset + Variables.shell  + Fore.RED}
  (  : '~' :  )     {Fore.RED +"Ram: " + reset + Variables.ram  + Fore.RED}
   '~ .~~~. ~'      {Fore.RED +"Wm: " + reset + Variables.GUI  + Fore.RED}
                    {Fore.RED +"Terminal: " + reset + Variables.term  + Fore.RED}
""" + Fore.RESET

manjaro = Fore.GREEN + rf"""
{Fore.GREEN}██████████████████  ████████    {Variables.User + "@" + Variables.distr + Fore.RESET + Fore.GREEN}
{Fore.GREEN}██████████████████  ████████    
{Fore.GREEN}██████████████████  ████████    {Fore.GREEN + "CPU: " + reset + Variables.CPU  + Fore.GREEN}    
{Fore.GREEN}██████████████████  ████████    {Fore.GREEN +"Bit: " + reset + Variables.Bit  + Fore.GREEN}
{Fore.GREEN}████████            ████████    {Fore.GREEN +"System: " + reset + platform.system()  + Fore.GREEN}
{Fore.GREEN}████████  ████████  ████████    {Fore.GREEN +"Distro: " + reset +  Variables.distr  + Fore.GREEN}
{Fore.GREEN}████████  ████████  ████████    {Fore.GREEN +"Shell: " + reset + Variables.shell  + Fore.GREEN}
{Fore.GREEN}████████  ████████  ████████    {Fore.GREEN +"Ram: " + reset + Variables.ram  + Fore.GREEN}
{Fore.GREEN}████████  ████████  ████████    {Fore.GREEN +"Wm: " + reset + Variables.GUI  + Fore.GREEN}
{Fore.GREEN}████████  ████████  ████████    {Fore.GREEN +"Terminal: " + reset + Variables.term  + Fore.GREEN}
{Fore.GREEN}████████  ████████  ████████
{Fore.GREEN}████████  ████████  ████████
{Fore.GREEN}████████  ████████  ████████
{Fore.GREEN}████████  ████████  ████████
"""