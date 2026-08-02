---
title: Interface Builder User Guide
apple_id: TP40005344
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/IB_UserGuide/GestureGuide/GestureGuide.html
archived_at: '2026-07-15T07:25:01.084176Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Interface Builder User Guide](Introduction.md)


[Next](Glossary.md)[Previous](Interface%20Builder%20Customization.md)

# Interface Builder Gesture Guide

1. Control-click (or right-click) the source object and release the mouse button to display the connections panel.
2. Drag the circle next to the outlet or action you want to connect over the target object for the connection. (Hovering over an object causes it to reveal its children.) The target object should highlight to indicate a connection is possible. If it does not highlight, the target object is not of the right type and cannot be connected.
3. Release the mouse button to create the connection.
4. If you are configuring the source object’s sent action, Interface Builder displays a list of the target object’s action methods. Select the desired action method from the list to finish the connection.

1. Control-click (or right-click) the source object of the connection and do not release the mouse button.
2. While holding the mouse button, drag to the target object.
3. Release the mouse button over the target. Inter face Builder displays a prospective list of actions and outlets.
4. Select the desired outlet (of the source object) or action (of the target object) to create the connection.

1. Select the source object and open the connections inspector (Command-5).
2. Follow steps 2-4 in [Using the Connections Panel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmrtfvjvomy) to create the connection.

| Modifier key | Description |
| --- | --- |
| Command | When you hold down this key, single-clicking an object toggles its selected state. You can use this modifier key to add objects to the current selection one at a time. You can also toggle the resize behavior for windows by holding down this key; see [Design-Time Resizing Modes for Windows](Interface%20Layout.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tgnbufvbuqmjzfvjvomjz). |
| Option | After selecting an object, pressing this key and moving the mouse over a different object displays alignment information for that object relative to the selected object. Pressing the Option key during drag-and-drop operations copies the selected objects instead of moving them. |
| Shift | When pressed, single-clicking an object adds that object to the current selection. Pressing this key while resizing an object maintains the object’s aspect ratio. |
| Control | When held down, clicking a Cocoa object displays its connections panel. Holding down the Control key is equivalent to right-clicking the object and the two behaviors have the same end result. |

| Action | Gesture |
| --- | --- |
| Display inspector window | Shift-Command-I |
| Display attributes inspector | Command-1 |
| Display effects inspector | Command-2 |
| Display size inspector | Command-3 |
| Display bindings inspector | Command-4 |
| Display connections inspector | Command-5 |
| Display identity inspector | Command-6 |

| Action | Gesture |
| --- | --- |
| Display Library window | Command-Shift-L |
| Add selected item to active workspace | Return or Enter |

| Action | Gesture |
| --- | --- |
| __Location__ |  |
| Move selection by 1 pixel | Arrow (Left, Up, Right, Down) |
| Move selection by 5 pixels | Shift-Arrow |
| __Size__ |  |
| Resize selection to fit | Command-= |
| __Guides__ |  |
| Display position guides | Option (with selection) |
| Display layout rectangles | Command-L |
| Add horizontal guide | Command-Shift-_ |
| Add vertical guide | Command-Shift-| |
| __Navigation__ |  |
| Reveal selection in document window | Command-Option-Up Arrow |
| Reveal selection in Library window | Command-Option-Right Arrow |
| Display in a popup menu all of the objects currently under the mouse | Shift-Control-Click |

| Action | Gesture |
| --- | --- |
| Display icon view | Command-Option-1 |
| Display list view | Command-Option-2 |
| Display column view | Command-Option-3 |
| Reveal selection in workspace | Command-Option-Down Arrow |
| Reveal selection class in Library window | Command-Option-Double Click |

| Action | Gesture |
| --- | --- |
| __Activation__ |  |
| Activate document window | Command-0 |
| Activate document info window | Command-Option-I |
| __Selection__ |  |
| Select parent object | Command-Control-Up Arrow |
| Select child object | Command-Control-Down Arrow |
| Select next sibling object | Command-Control-Right Arrow |
| Select previous sibling object | Command-Control-Left Arrow |
| __Editing__ |  |
| Duplicate selection | Command-D |
|  | Option-Mouse Drag |
| __Navigation__ |  |
| Display declaration for selection | Command-/ |
|  | Command-Double Click |
| Display documentation for selection | Command-Option-/ |
|  | Option-Double Click |

[Next](Glossary.md)[Previous](Interface%20Builder%20Customization.md)

