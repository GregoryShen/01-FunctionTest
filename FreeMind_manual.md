## Introduction



## Demonstration of some features



Creating and deleting nodes



Editing node text



Formatting a node



Using physical styles



Highlighting nodes with clouds



Adding hyperlinks



## Adding Icons

* A node can have several icons.
  * It can have the same icon more than once
* To add icons to a node, select a node and click one of the icons displayed in the left toolbar.
* To remove one icon, press red cross at the top of the icon toolbar.
* To remove all icons, press trash can icon at the top of the icon toolbar.
* To add a new icon to a node without using the left toolbar, press Alt + I
* Currently, it is not easy to extend the icons present in FreeMind(See FreeMind's wiki for an explanation). This will probably change in the next release.
* To hide or show the icon toolbar, in the context menu at the background use Toggle Left Toolbar. The icon toolbar is called left toolbar there.
* The icons as attached to this node are included, and more.
* Icon tweaks
  * If you press SHIFT while adding an icon from the icon toolbar, all other icons are removed from this node before adding the new one
  * If you press CONTROL while clicking on an icon, the first occurrence of this icon will be removed.

## Adding graphical links

* To create a graphical link between two nodes, drag a node and drop it to another node holding both shift and control keys; release the mouse button before releasing shift and control keys.
* Alternatively, you can select two nodes using Ctrl and to choose "Add graphical link" from the "Insert" menu or its shortcut Ctrl+L
* Context Menu
  * To change the color of the link, use link context menu, by right-clicking the graphical link.
  * To change the arrows of the link, use link context menu.
  * To delete a link, use link context menu.
  * To navigate to one of the end nodes of the link, use link context menu.
* To change the routing of an arrow link, drag it and move it
* An example of graphical link follows
* Example
  * Link to another part
  * Node with folded subnode
    * subnode
  * Another link

## Searching

* To find text in a node and all its descendant nodes, press Ctrl + F or in the "edit" menu use Find.
* To find the next match of your search, press Ctrl +Ｇ or in the "edit" menu Find Next.
* To search the whole map, select the central node by pressing Escape before searching.
* The search is a breadth-first search. This is because the deeper a node, the greater the detail described in the node.
* Search will only search the selected node and its descendants. To search the entire mind map, either select the central node directly, or press \<ESC> before searching to automatically search from the central node.
* If you enter multiple words into the find dialog, then each word must occur (but not necessarily in that order)
* If you want to search for a given sentence then put it into quotation marks.
  * Example
    * one
      * one one
      * one two
    * two
      * two one
      * two two
  * Searching for ...
    * one one (without quotations), you'll get four hits.
    * one two (without quotations), you'll get two hits.
    * "one one", you'll get only one hit.
* New interactive search
  * Using CONTROL+SHIFT+F you'll see the new search and replace dialog
  * It searches the whole mindmap
  * It supports regular expressions
  * It finds when you type.


## Selecting multiple nodes

* To select multiple nodes, hold control or shift while clicking.
* To add single nodes to already selected nodes, hold control when clicking.
* To select a continuous range of nodes, hold shift when clicking, or hold shift while moving around with arrow keys.
* To select a complete subtree, hold AltGr while clicking, or hold shift while moving with arrow keys from a node to its parent. Finally Ctrl+Shift+A does the same via the keyboard.
* To cancel the selection of multiple nodes, click on the map background or onto an unselected node.

## Dragging and dropping

* You can move nodes around using drag and drop.
* To drop a node as a child, position the cursor at the outer part of the node while dropping.
* To copy nodes rather than move, hold control while dragging, or drag with middle mouse button.
* To edit an existing map, drag its file and drop it on the background of FreeMind; this works at least in Microsoft Windows operating system.
* If you have selected multiple nodes, all are being moved or copied.
* You can drop data from external applications, like files on Microsoft Windows operating system, or pieces of text selected in a browser.

Copying and pasting



Moving around



Folding and unfolding



Changing to a different mind map



Scrolling the map

Zooming

Using undo

Exporting to HTML

Exporting as bitmap or vector picture

Exporting to other XML formats

Importing folder structure

Importing Internet Explorer favorites

Importing MindManager X5 mind map

Integration with Word or Outlook

Setting preferneces

Printing

Using rich text by means of HTML in nodes

Using pictures in nodes

Using experimental file locking

New features in version 0.9.0

New features in version 1.0.0



