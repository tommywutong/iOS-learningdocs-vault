---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.cocoa/Classes/EOCocoaPopUpButtonPlugin.html
archived_at: '2026-07-15T08:13:53.983758Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.cocoa/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOCocoaPopUpButtonPlugin

> **__Inherits from:__**
> : EOValueSelectionAssociation.ValueSelectionPlugin (EOInterface) : EOWidgetAssociation.WidgetPlugin (EOInterface) : Object

> **__Implements:__**
> : EOWidgetAssociation.WidgetPlugin.Formatting: (EOInterface): NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.cocoa

---

## Class Description

---

An EOCocoaPopUpButtonPlugin object displays an attribute or to-one relationship value in an NSPopUpButton (Cocoa).

The items in the NSPopUpButton can be entered manually, or for a relationship, constructed dynamically from values supplied by the destination entity's EODisplayGroup. The value displayed by the NSPopUpButton can be bound by one of three aspects: __selectedTitle__, which is useful for values representable as strings; __selectedIndex__, for integer values; and __selectedObject__, for the destination object of a relationship.

|  |
| --- |
| __Usable With__ |
| NSPopUpButton (Cocoa) |

|  |
| --- |
| __Aspects__ |
| `titles` | An attribute of the objects in an EODisplayGroup whose values can be represented as strings. |
| `selectedTitle` | An attribute of the selected object whose values can be represented as strings. |
| `selectedIndex` | An integer attribute of the selected object. |
| `selectedObject` | A to-one relationship of the selected object; the value displayed is that for the attribute bound to the __titles__ aspect. |
| `enabled` | A boolean attribute of the selected object, which determines whether the NSPopUpButton is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| `target` | When the user chooses an item in the pop-up list, the EOPopUpAssociation updates the selected object's property with the item's title, tag, or object. |

## Examples

There are several basic ways to configure a combo box and it's association. They are described below.

### Selecting a String from a Static List

Suppose you have a Movie display group and you want to provide a pop-up list for setting the rating from a static list of strings. In this example, a Movie object's rating is a string property rather than a relationship to a Rating object. To do this, in Interface Builder, type the list of ratings into the pop-up list. Control-drag a connection from the pop-up list to the Movie display group. Then bind the `selectedTitle` aspect to the "rating" key. With this configuration, if an object's string attribute value isn't in the pop-up list, it's temporarily added while the object is selected.

### Selecting a String from a Dynamic List

This example is similar to the previous one, except in this example, a Movie object's rating is chosen from strings in a Rating database table. There's a Rating EODisplayGroup that fetches the ratings into Rating objects, and the pop-up list is filled from the "ratingString" property of the rating display group's Rating objects. To do this, in Interface Builder, control-drag a connection from the pop-up list to the Ratings display group. Then bind the `titles` aspect to the "ratingString" key. Similarly, control-drag a connection from the pop-up list to the Movie display group, and bind the `selectedTitle` aspect to the "rating" key.

### Selecting an Integer Tag from a Static List

Suppose you have a Customer enterprise object whose credit card type (Visa, MasterCard, and so on) is indicated by an integer tag. You want a user to be able to choose a customer's card type from a pop-up list. To do this, in Interface Builder, set the credit card names and tags for the pop-up list. Control-drag a connection from the pop-up list to the Customer display group. Then bind the `selectedIndex` aspect to the "cardType" key. You can also allow for a general "other" value by defining a special tag and setting it in the EOCocoaPopUpButtonPlugin. Credit card tags from the database not matching any in the pop-up list are then displayed as the "other" value. (It would also make sense to disable the pop-up list in this case, to avoid writing the meaningless tag back to the database.)

### Selecting the Destination of a To-One Relationship

Suppose you have a list of employees and want to assign each employee a department. In terms of the object model, you want to assign a Department object as the destination of an Employee object's __department__ relationship. To do this, in Interface Builder, control-drag a connection from the pop-up list to a Department display group. Then bind the `titles` aspect to the "name" key. Similarly, control-drag a connection from the pop-up list to the Employee display group, and bind the `selectedObject` to the "department" key. This fills the pop-up list with the names of departments, and causes the name of the selected Employee's Department to be selected in the pop-up list.

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc6zdjonyg643f)
>
> :
>
> : EOWidgetAssociation.WidgetPlugin.Formatting
>
> : [setValueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc643forlgc3dvmvdg64tnmf2hizls): [valueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc65tbnr2wkrtpojwwc5dumvza)
>
> :

## Method Types

---

> **All methods**
>
> : [EOCocoaPopUpButtonPlugin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxa): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc6ytsmvqwwq3pnzxgky3unfxw4): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc6zltorqwe3djonueg33onzswg5djn5xa): [selectionIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc643fnrswg5djn5xes3temv4a): [setSelectionIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc643forjwk3dfmn2gs33ojfxgizly): [setTitlesFromObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc643forkgs5dmmvzum4tpnvhwe2tfmn2hg): [titles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc65djorwgk4y): [widgetKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkbxxavlqij2xi5dpnzigy5lhnfxc653jmrtwk5clmv4xgvdbnnsw4)

## Constructors

---

### EOCocoaPopUpButtonPlugin

`public EOCocoaPopUpButtonPlugin( com.webobjects.eointerface.EOWidgetAssociation anEOWidgetAssociation, Object widget)`

Description forthcoming.

---

## Instance Methods

---

### breakConnection

`public void breakConnection()`

See the breakConnection method description in the superclass EOAssociation.

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

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

`public void setSelectionIndex( int value, boolean isEnabled)`

Description forthcoming.

---

### setTitlesFromObjects

`public void setTitlesFromObjects(Object[] objects[])`

Description forthcoming.

---

### setValueFormatter

`public void setValueFormatter(Object anObject)`

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

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.cocoa/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
