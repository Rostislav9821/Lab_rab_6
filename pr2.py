#! / usr / bin / env python3
# - * - кодировка: utf-8 - * -

import  sys

если  __name__  ==  '__main__' :
    a  =  список ( карта ( int , input (). split ()))
    если  не  :
        print ( 'Заданный список пуст' , file = sys . stderr )
        выход ( 1 )

    a_min  =  a_max  =  a [ 0 ]
    i_min  =  i_max  =  0
    для  I , пункт  в  Перечислять ( ):
        если  элемент  <  a_min :
            i_min , a_min  =  i , элемент
            если  элемент  > =  a_max :
                i_max , a_max  =  i , элемент

    если  i_min  >  i_max :
        i_min , i_max  =  i_max , i_min

    count  =  0
    для  элемента  в  виде [ i_min + 1 : I_max ]:
        если  элемент  >  0 :
            count  + =  1

    печать ( количество )