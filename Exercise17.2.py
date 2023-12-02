class Department:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Department('(self.name)')"

class Machine_Operator(Department):
    def __repr__(self):
        return f"Machine_Operator('(self.name)')"

class Detail:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Detail('(self.name)')"

class Shaft(Detail):
    def __repr__(self):
        return f"Shaft('(self.name)')"

class Spatula(Detail):
    def __repr__(self):
        return f"Spatula('(self.name)')"

class Production:
    def __init__(self,
                     name,
                     masters=None,
                     machine_operators=[],
                     shafts=[],
                     spatulas=[]):
            self.name = name
            self.masters = masters
            self.machine_operators = machine_operators
            self.shafts = shafts
            self.spatulas = spatulas

    def __repr__(self):
        return f"Production('{self.name}, ...')"

class Master(Department):
    def __repr__(self):
        return f"Master('(self.name)')"

    def receive_plan(self, plan):
        try:
            self.plans += [plan]
        except AttributeError:
            self.plans = [plan]

    def enum_plans(self):
        for x in self.plans:
            yield x

class Plan:
    def __init__(self,
                     name,
                     machine_operator,
                     shaft):
            self.name =name
            self.machine_operator = machine_operator
            self.shaft = shaft            

    def __repr__(self):
        return f"Plan('{self.name}, ...')"

if __name__ == '__main__':
   department = Department('Дима')
   ivan = Master('Иван')
   petr = Machine_Operator('Петр')
   shaft1 = Shaft('Вал ротора двигателя PD')
   shaft2 = Shaft('Вал ротора двигателя PS')
   spatula1 = Spatula('Лопатки турбины двигателя PD')
   spatula2 = Spatula('Лопатки турбины двигателя PS')
   pd = Production(
       name = 'Двигатель PD',
       masters = ivan,
       machine_operators = [petr],
       shafts = [shaft1, shaft2],
       spatulas = [spatula1, spatula2])
   plan_a = Plan(
       name = 'Вал ротора двигателя PD',
       machine_operator = petr,
       shaft = shaft1)
   plan_b = Plan(
       name = 'Вал ротора двигателя PS',
       machine_operator = petr,
       shaft = shaft2)
   ivan.receive_plan(plan_a)
   ivan.receive_plan(plan_b)
   print(list(ivan.enum_plans()))
