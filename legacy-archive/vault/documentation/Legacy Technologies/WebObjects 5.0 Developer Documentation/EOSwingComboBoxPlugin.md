---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOSwingComboBoxPlugin.html
archived_at: '2026-07-15T08:13:54.579836Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOSwingComboBoxPlugin

> **__Inherits from:__**
> : EOValueSelectionAssociation.ValueSelectionPlugin (EOInterface) : EOWidgetAssociation.WidgetPlugin (EOInterface) : Object

> **__Implements:__**
> : java.awt.event.ActionListener: EOWidgetAssociation.WidgetPlugin.Formatting (EOInterface): NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

An EOSwingComboBoxPlugin object displays an attribute or to-one relationship value in an JComboBox. The items in the combo box can be entered manually, or for a relationship, constructed dynamically from values supplied by an EODisplayGroup. EOSwingComboBoxPlugin is very similar to the EOSwingPopUpButtonPlugin.

## Examples

There are three basic ways to configure a combo box and it's association. Each is described below.

### Selecting a String from a Static List

Suppose you have a Movie display group and you want to provide a combo box for setting the rating from a static list of strings. In this example, a Movie object's rating is a string property rather than a relationship to a Rating object). To do this, in Interface Builder, type the list of ratings into the combo box. Control-drag a connection from the combo box to the Movie display group. Choose EOSwingComboBoxPlugin in the Connections inspector, and bind the selectedTitle aspect to the "rating" key.

### Selecting a String from a Dynamic List

This example is similar to the previous one, except in this example, a Movie object's rating is chosen from strings in a Rating database table. There's a Rating EODisplayGroup that fetches the ratings into Rating objects, and the combo box is filled from the "ratingString" property of the rating display group's Rating objects. To do this, in Interface Builder, control-drag a connection from the combo box to the Ratings display group. Choose EOSwingComboBoxPlugin in the Connections inspector, and bind the titles aspect to the "ratingString" key. Similarly, control-drag a connection from the combo box to the Movie display group. Again choose EOSwingComboBoxPlugin in the Connections inspector, and bind the selectedTitle aspect to the "rating" key.

### Selecting the Destination of a To-One Relationship

Suppose you have a list of employees and want to assign each employee a department. In terms of the object model, you want to assign a Department object as the destination of an Employee object's __department__ relationship. To do this, in Interface Builder, control-drag a connection from the combo box to a Department display group. Choose EOSwingComboBoxPlugin in the Connections inspector, and bind the titles aspect to the "name" key. Similarly, control-drag a connection from the combo box to the Employee display group. Again choose EOSwingComboBoxPlugin in the Connections inspector, and bind the selectedObject to the "department" key.

If the selectedObject aspect is bound and the user types a value that doesn't match any of those currently in the list, an error panel is displayed.

## Interfaces Implemented

---

> : NSDisposable:
>
> : EOWidgetAssociation.WidgetPlugin.Formatting
>
> : [setValueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rponsxivtbnr2wkrtpojwwc5dumvza): [valueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rpozqwy5lfizxxe3lbor2gk4q)
>
> :
>
> : java.awt.event.ActionListener
>
> : [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rpmfrxi2lpnzigk4tgn5zg2zle)
>
> :

## Method Types

---

> **All methods**
>
> : [EOSwingComboBoxPlugin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rpivhvg53jnztug33nmjxue33ykbwhkz3jny): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rpmjzgkyllinxw43tfmn2gs33o): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rpmvzxiylcnruxg2cdn5xg4zldoruw63q): [selectionIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rponswyzldoruw63sjnzsgk6a): [setSelectionIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rponsxiu3fnrswg5djn5xes3temv4a): [setTitlesFromObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rponsxivdjorwgk42gojxw2t3cnjswg5dt): [titles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rporuxi3dfom): [widgetKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thinxw2ytpijxxqudmovtws3rpo5uwiz3forfwk6ltkrqwwzlo)

## Constructors

---

### EOSwingComboBoxPlugin

`public EOSwingComboBoxPlugin( com.webobjects.eointerface.EOWidgetAssociation anEOWidgetAssociation, Object widget)`

Description forthcoming.

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent anActionEvent)`

Description forthcoming.

---

### breakConnection

`public void breakConnection()`

See the breakConnection method description in the superclass EOAssociation.

---

### establishConnection

`public void establishConnection()`

See the establishConnection method description in the superclass (EOAssociation).

---

### selectionIndex

`public int selectionIndex()`

Description forthcoming.

---

### setSelectionIndex

`public void setSelectionIndex( int selectionIndex, boolean enabled)`

Description forthcoming.

---

### setTitlesFromObjects

`public void setTitlesFromObjects(Object[] objects)`

Description forthcoming.

---

### setValueFormatter

`public void setValueFormatter(Object formatter)`

Description forthcoming.

---

### titles

`public String[] titles()`

Description forthcoming.

---

### valueFormatter

`public Object valueFormatter()`

Description forthcoming.

---

### widgetKeysTaken

`public String[] widgetKeysTaken()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
