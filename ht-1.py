# class Iron(object):
#     tempPlavl = 1538
#     tempZatv = 1537
#     tempIspar = 2862
#
#     def agg_state(self, t):
#         if t >= self.tempIspar:
#             return 'испарение'
#         elif self.tempPlavl >= t < self.tempIspar:
#             return 'Плавление'
#         else:
#             print('затвердевание')
#             return 'затвердевание'
#
#
# a = Iron()
# print(a.agg_state(1500))

class Element(object):

    tmp_plavl = 0
    tmp_zatv = 0
    tmp_ispar = 0

    def agg_state(self, t, temp_scale):
        if temp_scale == 'C':
            if t <= self.tmp_zatv:
                return 'затвердевание'
            elif self.tmp_zatv <= t < self.tmp_ispar:
                return 'Плавление'
            else:
                return 'испарение'
        else:
            tmp = self.convers_tmp(t, temp_scale)
            if tmp <= self.tmp_zatv:
                return 'затвердевание'
            elif self.tmp_zatv <= tmp < self.tmp_ispar:
                return 'Плавление'
            else:
                return 'испарение'


    def convers_tmp(self, t, temp_sc):
        if temp_sc == 'F':
            tmp = (t - 32) // 9 * 5
        else:
            tmp = t - 273.15
        print(tmp, ' C')
        return tmp


# C - цельсий
# F - фаренгейт
# K - кельвин
class Iron(Element):

    tmp_plavl = 1538
    tmp_zatv = 1537
    tmp_ispar = 2862


tr = Iron()
print(tr.agg_state(3480, 'K'))
