# NOTICE: DEVELOPMENT FOR THIS PROJECT HAS CEASED

**I made this a long time ago, when I was much less skilled in programming.** 

**Therefore, there is a lot of repeated code which could have been avoided by properly leveraging the 4 OOP principles.**

**Tkinter also makes it difficult to design flexibly and it's nature (a downloadable app) restricts access.**

**I may remake this project as a web application in the future.**

**Please check out my other, more recent projects on my Github which better advertise my current skillset.** 


## Simple-Chemistry-App

A small chemistry focused Windows application made using Python, currently with the following functionality:

The app displays properties (e.g. atomic mass) of the chemical elements, which are pulled from a .csv database. This is done using pandas.
You can convert between mass and molar fractions for a mixture of up to 4 compounds using the element numerical properties such as atomic masses, which are indexed using pandas. The application then outputs a pie chart with the desired compositions. Data visualisation is done via matplotlib.

The code for the project is freely available to browse in the main.py file in the repository for the project. 

To use the app, please download the latest version from my releases, install the CE_toolkit.exe file, and launch the main.exe file within the folder that is generated.

# <b>Changelog:</b>

<b>v1.2</b>

- Removed some unnecessary variables by grouping them into lists and accessing via indexing, reducing complexity. 
- Fixed a nasty bug where the properties of compound 2 were getting mixed up with compound 3 (This bug was likely introduced in v1.1)
- Changed illogical variable names (e.g. clicked11) to more logical ones (e.g. element11) 
- Grouped some functions at the top of the code as opposed to the middle. (All functions should be grouped together in future).
- Reduced line lengths to make code more legible. 
- Fixed a nasty bug that stopped compound 4 from being properly processed, due to incompatibility of float and integer data types being multiplied together. 
- Changed variable names that were very misleading in the mass/mole calculation/conversion functions. Now it is much more clear what is being calculated. 

<b>v1.1</b>

- You can now specify a mole or mass basis numerically in units of mol or grams respectively.
- Smaller program size.

<b>v1.0</b>

- Initial release. 


