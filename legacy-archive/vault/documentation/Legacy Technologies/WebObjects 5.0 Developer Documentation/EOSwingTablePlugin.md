---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOSwingTablePlugin.html
archived_at: '2026-07-15T08:13:54.700468Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOSwingTablePlugin

> **__Inherits from:__**
> : [EOTableAssociation.TablePlugin (EOInterface)](EOTableAssociation.TablePlugin.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhviylcnrsuc43tn5rwsylunfxw4lsumfrgyzkqnr2wo2lo) : EOWidgetAssociation.WidgetPlugin (EOInterface) : Object

> **__Implements:__**
> : javax.swing.event.ListSelectionListener: javax.swing.event.TableColumnModelListener: NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

Documentation for this class is forthcoming.

## Interfaces Implemented

---

> : javax.swing.event.ListSelectionListener
>
> : [valueChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxxmylmovsug2dbnztwkza)
>
> :
>
> : javax.swing.event.TableColumnModelListener
>
> : [columnAdded](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwg33movww4qlemrswi): [columnMarginChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwg33movww4tlbojtws3sdnbqw4z3fmq): [columnMoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwg33movww4tlpozswi): [columnRemoved](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwg33movww4utfnvxxmzle): [columnSelectionChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwg33movww4u3fnrswg5djn5xeg2dbnztwkza)
>
> :
>
> : NSDisposable:

## Method Types

---

> **All methods**
>
> : [EOSwingTablePlugin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxukt2to5uw4z2umfrgyzkqnr2wo2lo): [breakConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwe4tfmfvug33onzswg5djn5xa): [editingColumnIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwkzdjoruw4z2dn5whk3lojfxgizly): [editingRowIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwkzdjoruw4z2sn53us3temv4a): [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwk43umfrgy2ltnbbw63tomvrxi2lpny): [existingTableAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxwk6djon2gs3thkrqwe3dfifzxg33dnfqxi2lpny): [numberOfColumns](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxw45lnmjsxet3ginxwy5lnnzzq): [selectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxxgzlmmvrxi2lpnzew4zdfpbsxg): [tableColumnAssociationForColumnAtIndex](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxxiylcnrsug33movww4qltonxwg2lboruw63sgn5zeg33movww4qlujfxgizly): [updateSelectionIndexes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxxk4demf2gku3fnrswg5djn5xes3temv4gk4y): [updateTableContents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxxk4demf2gkvdbmjwgkq3pnz2gk3tuom): [valueChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxxmylmovsug2dbnztwkza): [widgetKeysTaken](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn3ws3thkrqwe3dfkbwhkz3jnyxxo2lem5sxis3fpfzviyllmvxa)

## Constructors

---

### EOSwingTablePlugin

`public EOSwingTablePlugin( com.webobjects.eointerface.EOWidgetAssociation anEOWidgetAssociation, Object widget)`

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

`public void valueChanged(javax.swing.event.ListSelectionEvent event)`

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
