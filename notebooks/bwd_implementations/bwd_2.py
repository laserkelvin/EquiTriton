# -------------------- variable and constant definitions
CONST000 = 3.87298334620742
CONST001 = 4.47213595499958
CONST002 = -2.23606797749979
CONST003 = -3.87298334620742
VAR00 = g_1
VAR01 = g_3
VAR02 = g_4
VAR03 = g_0
VAR04 = z
VAR05 = x
VAR06 = g_2
VAR07 = y
# -------------------- kernel implementations
g_x = CONST002*VAR05*VAR06 - CONST003*VAR00*VAR07 + CONST003*VAR02*VAR05 - CONST003*VAR03*VAR04
g_y = CONST001*VAR06*VAR07 - CONST003*VAR00*VAR05 - CONST003*VAR01*VAR04
g_z = CONST002*VAR04*VAR06 - CONST003*VAR01*VAR07 - CONST003*VAR02*VAR04 - CONST003*VAR03*VAR05
