---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.cocoa/Classes/EOCocoaRadioMatrixPlugin.html
archived_at: '2026-07-15T08:13:54.008421Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.cocoa/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOCocoaRadioMatrixPlugin

> **__Inherits from:__**
> : EOValueSelectionAssociation.ValueSelectionPlugin (EOInterface) : EOWidgetAssociation.WidgetPlugin (EOInterface) : Object

> **__Implements:__**
> : EOWidgetAssociation.WidgetPlugin.Formatting: (EOInterface): NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.cocoa

---

## Class Description

---

An EOCocoaRadioMatrixPlugin allows you to populate an NSMatrix's cells. EOCocoaRadioMatrixPlugin supports connections for both cell titles and icons, depending on the matrix's prototype cell. You define the prototype in Interface Builder (to display an icon only, text only, or both).

|  |
| --- |
| __Usable With__ |
| NSMatrix (com.apple.cocoa.application.NSMatrix) |

|  |
| --- |
| __Aspects__ |
| `selectedTitle` | An attribute of the selected object whose values can be represented as strings. |
| `selectedTag` | An integer attribute of the selected object. |
| `enabled` | A boolean attribute of the selected object, which determines whether the matrix is enabled. |

|  |
| --- |
| __Object Keys Taken__ |
| `target` | When the user chooses an item in the matrix, the EORadioMatrixAssociation updates the selected object's property with the item's title or tag. |

## Examples

Suppose that you want to display actors' names and pictures in an NSMatrix. Start with a TalentPhoto display group (where a TalentPhoto object has a relationship to its Talent object). In Interface Builder, create a button containing both an image and text. Then, alternate(option)-drag to create a matrix of buttons. Control-drag from the matrix to the photo display group. In the Connections inspector, choose EOCocoaRadioMatrixPlugin, and bind the __image__ aspect to the __photo__ attribute. Repeat, binding the __title__ aspect to the __talent.lastName__ attribute.

Note that you can group the matrix in a scroll view. An EOCocoaRadioMatrixPlugin will automatically manage the size of the matrix for this (for vertical scrolling only).

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc6zdjonyg643f)
>
> :
>
> : EOWidgetAssociation.WidgetPlugin.Formatting
>
> : [setValueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc643forlgc3dvmvdg64tnmf2hizls): [valueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc65tbnr2wkrtpojwwc5dumvza)
>
> :

## Method Types

---

> **All methods**
>
> : [EOCocoaRadioMatrixPlugin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxa): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc6ytsmvqwwq3pnzxgky3unfxw4): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc6zltorqwe3djonueg33onzswg5djn5xa): [selectionIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc643fnrswg5djn5xes3temv4a): [setSelectionIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc643forjwk3dfmn2gs33ojfxgizly): [setTitlesFromObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc643forkgs5dmmvzum4tpnvhwe2tfmn2hg): [titles](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc65djorwgk4y): [widgetKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkjqwi2lpjvqxi4tjpbigy5lhnfxc653jmrtwk5clmv4xgvdbnnsw4)

## Constructors

---

### EOCocoaRadioMatrixPlugin

`public EOCocoaRadioMatrixPlugin( com.webobjects.eointerface.EOWidgetAssociation anEOWidgetAssociation, Object widget)`

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

`public void setSelectionIndex( int value, boolean enabled)`

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
