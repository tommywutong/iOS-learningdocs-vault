---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.cocoa/Classes/EOCocoaTableViewPlugin.html
archived_at: '2026-07-15T08:13:54.078715Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.cocoa/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOCocoaTableViewPlugin

> **__Inherits from:__**
> : [EOTableAssociation.TablePlugin (EOInterface)](EOTableAssociation.TablePlugin.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhviylcnrsuc43tn5rwsylunfxw4lsumfrgyzkqnr2wo2lo) : EOWidgetAssociation.WidgetPlugin (EOInterface) : Object

> **__Implements:__**
> : NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.cocoa

---

## Class Description

---

An EOCocoaTableViewPlugin object manages the individual EOColumnAssociations between an NSTableView and an EODisplayGroup.

An EOCocoaTableViewPlugin can sort the objects in the display group by the left-to-right order of the table columns. The first EOColumnAssociation to be bound to a table view automatically creates the EOCocoaTableViewPlugin; you should rarely need to do so yourself.

An EOCocoaTableViewPlugin receives data source and delegate messages from the table view, some of which it handles itself, and some of which it forwards to the appropriate EOColumnAssociations. For more information, see the EOColumnAssociation class specification.

|  |
| --- |
| __Usable With__ |
| NSTableView (com.apple.cocoa.application.NSTableView). |

|  |
| --- |
| __Aspects__ |
| `source` | Bound to the EODisplayGroup providing objects. This aspect doesn't use a key. |
| `enabled` | A boolean attribute of the objects, which determines whether each object's row is editable. Note that because EOColumnAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| `textColor` | An NSColor attribute of the objects, which determines the color of text for each object's row in the NSTableView. |
| `bold` | A boolean attribute of the objects, which determines whether each objects row is displayed in bold or regular weight text. |
| `italic` | A boolean attribute of the objects, which determines whether each objects row is displayed in italic or normal angle text. |

|  |
| --- |
| __Object Keys Taken__ |
| `dataSource` | An EOTableViewAssociation responds to some data source messages and forwards others to the appropriate EOColumnAssociation. |
| `delegate` | An EOTableViewAssociation forwards delegate messages to the appropriate EOColumnAssociations. |
| `target` | Reserved, but not used. |

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5sgs43qn5zwk)
>
> :

## Method Types

---

> **All methods**
>
> : [EOCocoaTableViewPlugin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5cu6q3pmnxwcvdbmjwgkvtjmv3va3dvm5uw4): [associationForColumnAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5qxg43pmnuwc5djn5xem33sinxwy5lnnzaxislomrsxq): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5rhezlbnnbw63tomvrxi2lpny): [editingColumnIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5swi2lunfxgoq3pnr2w23sjnzsgk6a): [editingRowIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5swi2lunfxgoutpo5ew4zdfpa): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5sxg5dbmjwgs43iinxw43tfmn2gs33o): [existingTableAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5sxq2ltoruw4z2umfrgyzkbonzw6y3jmf2gs33o): [numberOfColumns](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5xhk3lcmvze6zsdn5whk3loom): [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof5zwk3dfmn2gs33ojfxgizlymvzq): [tableColumnAssociationForColumnAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof52gcytmmvbw63dvnvxec43tn5rwsylunfxw4rtpojbw63dvnvxec5cjnzsgk6a): [updateSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof52xazdborsvgzlmmvrxi2lpnzew4zdfpbsxg): [updateTableContents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof52xazdborsviylcnrsug33oorsw45dt): [valueChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof53gc3dvmvbwqylom5swi): [widgetKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwg33bkrqwe3dfkzuwk52qnr2wo2lof53wszdhmv2ewzlzonkgc23fny)

## Constructors

---

### EOCocoaTableViewPlugin

`public EOCocoaTableViewPlugin( com.webobjects.eointerface.EOWidgetAssociation anEOWidgetAssociation, Object anObject)`

Creates a new EOCocoaTableViewPlugin to manage EOColumnAssociations associated with _aDisplayObject_, an NSTableView.

You normally set up associations with the Interface Builder application, in which case you don't need to create them programmatically. However, if you do create them up programmatically, setting them up is a multi-step process. After creating an association, you must bind its aspects and establish its connections.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### associationForColumnAtIndex

`public com.webobjects.eointerface.EOTableColumnAssociation associationForColumnAtIndex(int index)`

Description forthcoming.

---

### breakConnection

`public void breakConnection()`

See the breakConnection method description in the superclass EOAssociation.

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

---

### editingColumnIndex

`public int editingColumnIndex()`

Description forthcoming.

---

### editingRowIndex

`public int editingRowIndex()`

Description forthcoming.

---

### establishConnection

`public void establishConnection()`

See the establishConnection method description in the superclass (EOAssociation).

---

### existingTableAssociation

`public com.webobjects.eointerface.EOTableAssociation existingTableAssociation()`

Description forthcoming.

---

### numberOfColumns

`public int numberOfColumns()`

Description forthcoming.

---

### selectionIndexes

`public int[] selectionIndexes()`

Description forthcoming.

---

### tableColumnAssociationForColumnAtIndex

`public com.webobjects.eointerface.EOTableColumnAssociation tableColumnAssociationForColumnAtIndex(int columnIndex)`

Description forthcoming.

---

### updateSelectionIndexes

`public void updateSelectionIndexes(int[] selectedRowIndexes)`

Description forthcoming.

---

### updateTableContents

`public void updateTableContents(int numberOfRows)`

Description forthcoming.

---

### valueChanged

`public void valueChanged()`

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
