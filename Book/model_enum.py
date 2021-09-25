from enum import Enum

class Math(Enum):
    PIE=3.14

class Names(Enum):
    BOOK_NAME1="Wings of Fire"
    BOOK_NAME2="Power of Subconsious Mind"

# o/p--in python shell
# >>> from Book.model_enum import Math
# >>> Math.PIE 
# <Math.PIE: 3.14>
# >>> Math.PIE.value
# 3.14

# >>> from Book.model_enum import Names
# >>> Names.BOOK_NAME1
# <Names.BOOK_NAME1: 'Wings of Fire'>
# >>> Names.BOOK_NAME1.value
# 'Wings of Fire'
# >>> Names.BOOK_NAME2       
# <Names.BOOK_NAME2: 'Power of Subconsious Mind'>>>> Names.BOOK_NAME2.value
# 'Power of Subconsious Mind'