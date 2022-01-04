

def change_param(groups="sample data/grupy.csv",
                 classes="sample data/zajecia.csv",
                 rooms="sample data/sale.csv",
                 lecturers="sample data/prowadzacy.csv",
                 lweight=20,
                 fun_weight=(1, 1, 1, 1),
                 FD=(3, 2, 1, 2, 3),
                 p_time=((8, 00), (12, 00)),
                 sections=3,
                 reassign="backtracking",
                 step=15,
                 max_iter=10,
                 utime=10):
    with open('./parameters.py', 'w') as f:
        f.write("# Structures files .csv\n")
        f.write("GROUPS_FILE = '{0}'\n".format(groups))
        f.write("CLASSES_FILE = '{0}'\n".format(classes))
        f.write("ROOMS_FILE = '{0}'\n".format(rooms))
        f.write("LECTURERS_FILE = '{0}'\n".format(lecturers))
        f.write("\n")
        f.write("# weights\n")
        f.write("LECTURER_WEIGHT = {0} ".format(lweight) +
                " # waga istotnosci funkcji celu prowadzacego wzgledem studenta (waga studenta = 1)\n")
        f.write("FUN_WEIGHTS = {0}  # wagi skladowych funkcji celu\n".format(fun_weight))
        f.write("WEIGHTS_FD = {0}\n".format(FD))
        f.write("PERFECT_TIME = {0}  # godziny miedzy ktorymi FP przyjmuje wartosc 0\n".format(p_time))
        f.write("\n")
        f.write("# other parameters\n")
        f.write("SECTIONS_AMOUNT = {0}\n".format(sections))
        f.write("REASSIGN_TYPE = '{0}'  # backtracking/reconstruction/replacing\n".format(reassign))
        f.write("STEP = {0}\n".format(step))
        f.write("MAX_ITER = {0}\n".format(max_iter))
        f.write("UTIME = {0}  # jednostka czasu\n".format(utime))
