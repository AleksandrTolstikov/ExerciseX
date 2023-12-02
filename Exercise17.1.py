class Department: # Отдел, который является общим для мастера и станочника
    pass

class Master(Department): # Мастер, который контролирует выпуск деталей
    pass

class Machine_Operator(Department): # Станочник, который производит детали
    pass

class Detail: # Деталь, которая является общей для вала и лопатки
    pass

class Shaft(Detail): # Вал, один из видов детали
    pass

class Spatula(Detail): # Лопатка, одна из видов детали
    pass

class Production: # Производство, общее для всех классов
    pass

class Plan: # План, который необходимо предоставить мастеру
    pass
