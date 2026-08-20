---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOSwingTableColumnPlugin.html
archived_at: '2026-07-15T08:13:54.678857Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOSwingTableColumnPlugin

> **__Inherits from:__**
> : EOTableColumnAssociation.TableColumnPlugin (EOInterface) : EOWidgetAssociation.WidgetPlugin (EOInterface) : Object

> **__Implements:__**
> : javax.swing.event.TableColumnModelListener:: EOWidgetAssociation.WidgetPlugin.Formatting (EOInterface):: NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

An EOSwingTableColumnPlugin object manages the individual EOColumnAssociations between a TableColumn and an EODisplayGroup.

An EOSwingTableColumnPlugin can sort the objects in the display group by the left-to-right order of the table columns. The first EOColumnAssociation to be bound to a table view automatically creates the EOSwingTableColumnPlugin; you should rarely need to do so yourself.

An EOSwingTableColumnPlugin receives data source and delegate messages from the table view, some of which it handles itself, and some of which it forwards to the appropriate EOColumnAssociations. For more information, see the EOColumnAssociation class specification.

## Interfaces Implemented

---

> : EOWidgetAssociation.WidgetPlugin.Formatting
>
> : [setValueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc643forlgc3dvmvdg64tnmf2hizls): [valueFormatter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc65tbnr2wkrtpojwwc5dumvza)
>
> :
>
> : javax.swing.event.TableColumnModelListener
>
> : [columnAdded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6y3pnr2w23sbmrsgkza): [columnMarginChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6y3pnr2w23snmfzgo2loinugc3thmvsa): [columnMoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6y3pnr2w23snn53gkza): [columnRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6y3pnr2w23ssmvww65tfmq): [columnSelectionChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6y3pnr2w23stmvwgky3unfxw4q3imfxgozle)
>
> :
>
> : NSDisposable:

## Method Types

---

> **All methods**
>
> : [EOSwingTableColumnPlugin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxa): [setTableColumnCustomizer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3xnfxgovdbmjwgkq3pnr2w23sqnr2wo2lof5zwk5cumfrgyzkdn5whk3loin2xg5dpnvuxuzls): [tableColumnCustomizer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u3xnfxgovdbmjwgkq3pnr2w23sqnr2wo2lof52gcytmmvbw63dvnvxeg5ltorxw22l2mvza): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6ytsmvqwwq3pnzxgky3unfxw4): [columnIndexInTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6y3pnr2w23sjnzsgk6cjnzkgcytmmu): [displayValueForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6zdjonygyylzkzqwy5lfizxxevtbnr2wk): [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6zlomrcwi2lunfxgo): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc6zltorqwe3djonueg33onzswg5djn5xa): [isEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc62ltivsgs5dbmjwgk): [table](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc65dbmjwgk): [tableAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc65dbmjwgkqltonxwg2lboruw63q): [valueForDisplayValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc65tbnr2wkrtpojcgs43qnrqxsvtbnr2wk): [widgetKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfinxwy5lnnzigy5lhnfxc653jmrtwk5clmv4xgvdbnnsw4)

## Constructors

---

### EOSwingTableColumnPlugin

`public EOSwingTableColumnPlugin( com.webobjects.eointerface.EOWidgetAssociation anEOWidgetAssociation, Object widget)`

Description forthcoming.

---

## Static Methods

---

### setTableColumnCustomizer

`public static void setTableColumnCustomizer( EOSwingTableColumnPlugin.TableColumnCustomizer aTableColumnCustomizer)`

Description forthcoming.

---

### tableColumnCustomizer

`public static EOSwingTableColumnPlugin.TableColumnCustomizer tableColumnCustomizer()`

Description forthcoming.

---

## Instance Methods

---

### breakConnection

`public void breakConnection()`

See the breakConnection method description in the superclass EOAssociation.

---

### columnAdded

`public void columnAdded(javax.swing.event.TableColumnModelEvent event)`

Description forthcoming.

---

### columnIndexInTable

`public int columnIndexInTable()`

Description forthcoming.

---

### columnMarginChanged

`public void columnMarginChanged(javax.swing.event.ChangeEvent event)`

Description forthcoming.

---

### columnMoved

`public void columnMoved(javax.swing.event.TableColumnModelEvent event)`

Description forthcoming.

---

### columnRemoved

`public void columnRemoved(javax.swing.event.TableColumnModelEvent event)`

Description forthcoming.

---

### columnSelectionChanged

`public void columnSelectionChanged( javax.swing.event.ListSelectionEvent event)`

Description forthcoming.

---

### displayValueForValue

`public Object displayValueForValue(Object value)`

Description forthcoming.

---

### endEditing

`public boolean endEditing()`

Description forthcoming.

---

### establishConnection

`public void establishConnection()`

See the establishConnection method description in the superclass (EOAssociation).

---

### isEditable

`public boolean isEditable()`

Description forthcoming.

---

### setValueFormatter

`public void setValueFormatter(Object formatter)`

Description forthcoming.

---

### table

`public Object table()`

Description forthcoming.

---

### tableAssociation

`public com.webobjects.eointerface.EOTableAssociation tableAssociation()`

Description forthcoming.

---

### valueForDisplayValue

`public Object valueForDisplayValue(Object value)`

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
