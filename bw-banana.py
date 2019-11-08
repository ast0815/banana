#!/usr/bin/env python
# encoding: utf8
from time import sleep
import sys
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--message', '-m', help="what to say", default="IT'S PEANUT BUTTER JELLY TIME!1!")
parser.add_argument('prog', help="program to call with banana argument", nargs='*', default=['echo'])
args = parser.parse_args()

banana = []
prog = args.prog
message = args.message

#0
banana.append(r"""                                   
                                   
                                   
                  ww               
                 M~~0              
                 M  !Mw            
                 M    !M'          
              _*MM**,  !M'         
              0*0*  #   4'         
               *0MMM_jg'4'         
                @wmm~~P'4'         
                _M_*m~  4'         
         _mmy_ _#~~    qM'jmm_,    
         #  ~M M~     wM'4C' "[    
         ~mm#~wM    ,g0  jMWm/'    
           ,0wMw,,ww0~Bwmf'        
          wMM~~~~~~~~MMMw          
         H,,,~~M   #~~',,4'        
          ~~~~~~   ~~~~~~'         """)

#1
banana.append(r"""                                   
                                   
                  ,w               
                 #~~#              
                 #  !M_            
                 #    ~N           
              ,^#~^^,  /M'         
              #=#=  #   4'         
               ^#^^^__g 4'         
                Pw^^ _! 4'         
                _B_^^   4'         
       _--y_    #~~     J'  jm--,  
       L  ~#   m#      j~  "C' _[  
       "mmMMy wM      4Mm_jmMmm/'  
            ~~#~    w@~ "~~        
            pMMM  #~*q             
          ww8v       *www          
         Q    ~M   *~    J'        
          ~~~~~     ~~~~~'         """)

#2
banana.append(r"""                 ww                
                #  4               
               w#  ~B              
               M    !M             
  ,^ML,      j^~^,!^^M_       wM^\,
  L _jf      # ^ # ` 4M       L_ _f
   ^^~L_,     #^^ !^^_Z     _jP^^' 
        ^^m_, #^^^^^,!M _jn^'      
            ^^#^___^  4^^'         
              #       4            
              #      q*            
              #     ,J             
              #     #~             
              #my,w0~              
               M~~~Z               
              #~   ~B              
           www#w   _#www           
         E~   wM   4w   ~Z'        
         ~~~~~       ~~~~~         """)

#3
banana.append(r"""                                   
               ww                  
              #  #                 
             M~  #w                
            0~    #                
           w0***w*@M,              
   _,      M# ! # * #    ___,      
  f -Mf    Mj*** **#    *M' q'     
  LjwMf    M9j*****0    4MyjJ'     
      My,  # ~*jjj*0  _pM'         
       ~@**#j  ~~~ #**@~           
           ~#      #               
            Mw     #               
             Mg, ,,#               
              MMmMMM               
             w#    *w              
           wwM      #www           
         #~,,,~M   #~,,,~M'        
         ~~~~~~     ~~~~~~'        """)

#4
banana.append(r"""                                   
                                   
                                   
               ww                  
              M~~M                 
            wM9  #                 
           #9    #                 
          @9  j**MM*,              
          8   #  *0*0              
          8 mjjMMM0M               
          8 HL~mmwM                
          8  ~mm_#_                
     _mmy_Mg    ~~B_ _pmm_         
     F  ~f My     ~B 4~  4'        
     ~mWMT  0w,    *w~Bmm/'        
         ~#w#~Mww,,w0w0,           
          wMMM~~~~~~~~RMw          
         #,,,~~M   #~~',,4'        
          ~~~~~~   ~~~~~~'         """)

#5

#6
banana.append(r"""                ww                 
               M  #                
              #~  *w               
             #~    4               
_/^^L,      _#^^^,!~^_      _wM^\, 
4n _wf      M# ^ # ` 4      4U, _f 
  ^^ML_,    Ej^^^ !^#     __j@^^'  
       ^^w, @9,^^^^^# __jr^'       
          ^^8  ^___^#^^            
            8       #              
            ^y      #              
             #,     #              
             ~#,    #              
              ~My,wm@              
               M~~~Z               
              #~   ~B              
           www#w   _#www           
         E~   wM   4w   ~Z'        
         ~~~~~       ~~~~~         """)

#7
banana.append(r"""                                   
                  ww               
                 M  #              
                wM  !M             
                #    !0            
              j*M*w***0w           
       __,    # * # ! #M'     __,  
      f  Me    M**'***_Z'   qM' \e 
      \jjM8    M*****_!M'   4MLj,' 
          Mg_  MM_jj*~ 4' _jM'     
           ~@**M ~~~  _ZM*@~       
               M      #~           
               M     qM            
               M,, ,wM             
               MMMmM0              
              wM    *w             
           www#      *ww           
         #~,,,~M   #~,,,~M'        
         ~~~~~~     ~~~~~~'        """)

for i in range(10):
    for b in banana:
        subprocess.call(prog + [b+'\n'+message])
        sleep(0.1)
