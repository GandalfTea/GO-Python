## Python GO Game


### Table of Contents :
   * [About](#about)
   * [Usage](#usage)
   * [GUI](#gui)
   * [TODO](#TODO)
   * [Bugs](#bugs)

&nbsp;

### About : <a name="about"></a>
Project for U30838 Programming Fundamentals. Python GO Game with PySimpleGUI. In the future, play against NN.

&nbsp;

### Highlights :
 *  2 player game of GO with a modern GUI.
 * Quick tutorial at the beginning of the game.
 * Save all moves of played game in external json file.

&nbsp;

### Usage : <a name="usage"></a>

Requires *PySimpleGUI* :
```
pip install pysimplegui
```
Run :
```
-> git clone https://github.com/GandalfTea/GO-Python
-> cd src
-> py run.py
```
Main GUI crashes if debug window is closed.


&nbsp;

### GUI Prototype : <a name="gui"></a>
![alt text](https://github.com/GandalfTea/GO-Python/blob/main/GUIPrototype.png)

&nbsp;

### TODO : <a name="TODO"></a>
	* Save captured stones in json file.
	* Implement a 'start new game' button.
	* Write every move in a doc and allow recreation of game.
	* Allow player to save a state of game and come back and try different moves.
	* Play against neural network.

&nbsp;

### Active bugs : <a name="bugs"></a>
	* Options button, next to 'X', crashes the program.
	* self-capture is not possible
	* Capture at corners is not perfect.
	* Main GUI crashes if debug window is closed.
