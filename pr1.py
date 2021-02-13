#! / usr / bin / env python3
# - * - кодировка: utf-8 - * -

import  sys

если  __name__  ==  '__main__' :
    A  =  список ( карта ( int , input (). Split ()))
    если  len ( A ) ! =  10 :
        print ( "Неверный размер списка" , file = sys . stderr )
        выход ( 1 )

    s  =  sum ([ a  для  a  в  A,  если  abs ( a ) <  5 ])
    печать ( и )