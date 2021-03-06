#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                               July 21, 2021
ENGI 2420 FA21  
Prof. M. Diaz-Maldonado


Problem 1.46: Ideal Gas Law
Estimate the density of Mar's atmosphere via the ideal gas law by
assuming that the atmosphere is composed of pure carbon dioxide (CO2).


Copyright (c) 2021 Misael Diaz-Maldonado

This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] B Munson, D Young, T Okiishi, and W Huebsch, Fundamentals of
    Fluid Mechanics, 8th edition
[1] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition
"""


"""
Given:
Mar's atmospheric conditions:
molecular weight of CO2,    kg/mol
ideal gas constant,         J / (mol K)
pressure,                   Pa
temperature,                K
"""

MW = 44.0e-3
R  =  8.314
P  =  900.0
T  = -50 + 273.15

"""
Solution:
density of Mar's atmosphere, kg/m^3, by the ideal gas law
"""

rho_Mars = MW * P / (R * T)

"""
Given:
Earth's atmospheric conditions:
molecular weight of air,    kg/mol
pressure,                   Pa
temperature,                K
"""

MW = 28.9e-3
P  = 101.6e3
T  = 18 + 273.15

"""
Solution:
density of Earth's atmosphere, kg/m^3
"""

rho_Earth = MW * P / (R * T)


ans = (
    f"\n\nProblem 1.46: Martian Atmopheric Density\n"
    f"density of Mars' atmosphere:    {rho_Mars:8.4f} kg/m^3\n"
    f"density of Earth's atmosphere:  {rho_Earth:8.4f} kg/m^3\n"
    f"Earth to Mars density ratio:    {rho_Earth/rho_Mars:8.4f}\n"
)
print(ans)
