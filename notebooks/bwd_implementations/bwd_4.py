# -------------------- variable and constant definitions
CONST000 = 2.00000000000000
CONST001 = 2.25000000000000
CONST002 = 4.50000000000000
CONST003 = 6.70820393249937
CONST004 = 8.87411967464942
CONST005 = 9.48683298050514
CONST006 = 6.27495019900557
CONST007 = 10.0623058987491
CONST008 = 12.0000000000000
CONST009 = 18.8248505970167
CONST010 = 20.1246117974981
CONST011 = 26.6223590239483
CONST012 = 28.4604989415154
CONST013 = 37.6497011940334
CONST014 = 40.2492235949962
CONST015 = -9.00000000000000
CONST016 = -8.87411967464942
CONST017 = -37.6497011940334
CONST018 = -6.70820393249937
CONST019 = -26.6223590239483
CONST020 = -21.3453742061366
CONST021 = -20.1246117974981
CONST022 = -18.8248505970167
CONST023 = -18.0000000000000
CONST024 = -14.2302494707577
CONST025 = -10.0623058987491
CONST026 = -7.11512473537885
CONST027 = -6.27495019900557
CONST028 = -3.35410196624968
VAR00 = g_7
VAR01 = y**3
VAR02 = g_8
VAR03 = g_5
VAR04 = g_6
VAR05 = y**2
VAR06 = g_4
VAR07 = x**3
VAR08 = z**3
VAR09 = g_1
VAR10 = z
VAR11 = x
VAR12 = g_2
VAR13 = x**2
VAR14 = z**2
VAR15 = g_0
VAR16 = g_3
VAR17 = y
# -------------------- kernel implementations
g_x = CONST017*VAR00*VAR10*VAR11*VAR17 + CONST024*VAR03*VAR10*VAR11*VAR17 + VAR02*(-CONST016*VAR07 + CONST019*VAR11*VAR14) + VAR04*(-CONST018*VAR07 + CONST021*VAR05*VAR11) + VAR06*(CONST000*VAR11*(CONST001*VAR14 + CONST015*VAR05) + CONST002*VAR07) + VAR09*VAR17*(CONST022*VAR13 - CONST022*VAR14) + VAR12*(-CONST021*VAR05*VAR10 + CONST025*VAR10*VAR13 + CONST028*VAR08) + VAR15*(-CONST016*VAR08 + CONST019*VAR10*VAR13) + VAR16*(CONST005*VAR01 + CONST020*VAR13*VAR17 + CONST026*VAR14*VAR17)
g_y = CONST000*VAR04*VAR17*(CONST025*VAR13 - CONST025*VAR14) + CONST014*VAR10*VAR11*VAR12*VAR17 + VAR00*(CONST022*VAR10*VAR13 - CONST027*VAR08) + VAR03*(CONST026*VAR08 + VAR10*(CONST012*VAR05 + CONST026*VAR13)) + VAR06*(CONST008*VAR01 + CONST023*VAR13*VAR17 + CONST023*VAR14*VAR17) + VAR09*(-CONST022*VAR11*VAR14 + CONST027*VAR07) + VAR16*(CONST026*VAR07 + VAR11*(CONST012*VAR05 + CONST026*VAR14))
g_z = -CONST017*VAR09*VAR10*VAR11*VAR17 + CONST024*VAR10*VAR11*VAR16*VAR17 + VAR00*VAR17*(CONST022*VAR13 - CONST022*VAR14) + VAR02*(-CONST016*VAR08 + CONST019*VAR10*VAR13) + VAR03*(CONST005*VAR01 + CONST020*VAR14*VAR17 + CONST026*VAR13*VAR17) + VAR04*(CONST018*VAR08 - CONST021*VAR05*VAR10) + VAR06*(CONST002*VAR08 + CONST002*VAR10*VAR13 + CONST023*VAR05*VAR10) + VAR12*(CONST028*VAR07 + VAR11*(-CONST021*VAR05 + CONST025*VAR14)) + VAR15*(CONST016*VAR07 - CONST019*VAR11*VAR14)
