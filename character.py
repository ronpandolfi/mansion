import numpy as np
import dice

femalefirstnames = ['Abigale', 'Abby', 'Ada', 'Adella', 'Agnes', 'Allie', 'Almira', 'Almyra', 'Alva', 'Amelia', 'Ann',
                    'Annie', 'Arrah', 'Beatrice', 'Becky', 'Bernice', 'Bess', 'Bessie', 'Beth', 'Betsy', 'Charity',
                    'Charlotte', 'Claire', 'Constance', 'Cynthia', 'Dorothy', 'Edith', 'Edna', 'Edwina', 'Ella',
                    'Eleanor', 'Ellie', 'Elizabeth', 'Eliza', 'Liza', 'Lizzy', 'Elvira', 'Emma', 'Esther', 'Ethel',
                    'Ettie', 'Eudora', 'Eva', 'Fidelia', 'Frances', 'Flora', 'Florence', 'Geneve', 'Genevieve',
                    'Georgia', 'Gertrude', 'Gertie', 'Gladys', 'Grace', 'Hannah', 'Hattie', 'Helen', 'Helene',
                    'Henrietta', 'Hettie', 'Hester', 'Hope', 'Hortence', 'Isabell', 'Isabella', 'Jane', 'Jennie',
                    'Jessamine', 'Josephine', 'Judith', 'Julia', 'Juliet', 'Katherine', 'Kate', 'Laura', 'Leah',
                    'Lenora', 'Letitia', 'Lila', 'Lilly', 'Lorena', 'Lorraine', 'Lottie', 'Louise', 'Louisa', 'Lucy',
                    'Lulu', 'Lydia', 'Mahulda', 'Margaret', 'Mary', 'Martha', 'Matilda', 'Mattie', 'Maude', 'Maxine',
                    'Maxie', 'Mercy', 'Mildred', 'Minerva', 'Missouri', 'Molly', 'Myrtle', 'Nancy', 'Natalie', 'Nellie',
                    'Nelly', 'Nettie', 'Nora', 'Orpha', 'Patsy', 'Parthena', 'Peggy', 'Permelia', 'Phoebe', 'Philomena',
                    'Polly', 'Preshea', 'Rachel', 'Rebecca', 'Rhoda', 'Rhody', 'Rowena', 'Rufina', 'Ruth', 'Samantha',
                    'Sally', 'Sarah', 'Sarah Ann', 'Savannah', 'Selina', 'Sophronia', 'Stella', 'Theodosia',
                    'Vertiline', 'Verd', 'Victoria', 'Virginia', 'Ginny', 'Vivian', 'Winnifred', 'Winnie', 'Zona',
                    'Zylphia']
malefirstnames = ['Aaron']


class character(object):
    def __init__(self, name='Player 1', hp=10, luck=5, strength=5, knowledge=5, temper=5, will=5):
        self.name = name
        self.hp = hp
        self.luck = luck
        self.strength = strength
        self.knowledge = knowledge
        self.temper = temper
        self.will = will

        self._curse = 0
        self._exhaustion = 0
        self._trepidity = 0  # focus
        self._anger = 0
        self._madness = 0  # sanity


class player(character):
    pass


def npc(character):
    pass


def randomnpc():
    hp = 6 + dice.d6()
    stats = np.sum(dice.d6(0, 6, (2, 5)), axis=0)
    name = np.random.choice(femalefirstnames)
    return npc(name, hp, *stats)
