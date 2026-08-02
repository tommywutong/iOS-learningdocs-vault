---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOTableColumnAssociation.html
archived_at: '2026-07-15T08:13:55.382996Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOTableColumnAssociation

> **__Inherits from:__**
> : [EOWidgetAssociation](EOWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

An EOTableColumnAssociation associates a single attribute of all enterprise objects in its ValueAspect's EODisplayGroup with a Swing JTable TableColumn . The value of each object's attribute is displayed in its corresponding row.

By far the easiest way to configure EOTableColumnAssociations is in Interface Builder, but they may also be instantiated programmatically. Because Swing's TableColumn maintains no reference to its containing JTable, this relationship must be explicitly specified via [setTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forkgcytmmu) before __establishConnection__ is invoked.

|  |
| --- |
| __Usable With__ |
| javax.swing.table.TableColumn |

|  |
| --- |
| __Aspects__ |
| BoldAspect | Description forthcoming. |
| EnabledAspect | A boolean attribute of the objects, which determines whether each object's value cell is editable. Note that because EOTableViewAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| ItalicAspect | Description forthcoming. |
| ValueAspect | An attribute of the objects, displayed in each row of the TableColumn. |

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc6zdjonyg643f)
>
> :
>
> : EOObserving:

## Method Types

---

> **All methods**
>
> : [EOTableColumnAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xa): [boldStateAtRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc6ytpnrsfg5dborsuc5csn53q): [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc6zlomrcwi2lunfxgo): [isEditableAtRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc62ltivsgs5dbmjwgkqlukjxxo): [italicStateAtRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc62lumfwgsy2torqxizkborjg65y): [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc64dsnfwwc4tzifzxazldoq): [setObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forhwe2tfmn2a): [setSortingSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forjw64tunfxgou3fnrswg5dpoi): [setTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forkgcytmmu): [setValueAtRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forlgc3dvmvaxiutpo4): [sortingSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643poj2gs3thknswyzldorxxe): [table](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc65dbmjwgk): [textColorAtRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc65dfpb2eg33mn5zec5csn53q): [valueAtRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc65tbnr2wkqlukjxxo): [widgetDidBeginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc653jmrtwk5cenfseezlhnfxekzdjoruw4zy): [widgetDidEndEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc653jmrtwk5cenfsek3teivsgs5djnztq): [widgetPluginClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc653jmrtwk5cqnr2wo2loinwgc43t)

## Constructors

---

### EOTableColumnAssociation

`public EOTableColumnAssociation(Object anObject)`

Description forthcoming.

`public EOTableColumnAssociation( Object object, Object table)`

Description forthcoming.

---

## Instance Methods

---

### boldStateAtRow

`public int boldStateAtRow(int rowIndex)`

Description forthcoming.

---

### __dispose__

`public void dispose()`

See the method description in the documentation for NSDisposable.

---

### endEditing

`public boolean endEditing()`

Description forthcoming.

---

### isEditableAtRow

`public boolean isEditableAtRow(int rowIndex)`

Returns whether or not the property bound to the receiver's `ValueAspect` is editable at _row_, as determined by the EnabledAspect. If this aspect is bound, a non-zero value at _row_ indicates that the property may be edited. If the `EnabledAspect` is unbound all rows are considered editable.

---

### italicStateAtRow

`public int italicStateAtRow(int rowIndex)`

Description forthcoming.

---

### primaryAspect

`public String primaryAspect()`

Returns EOAssociation.`ValueAspect`.

---

### setObject

`public void setObject(Object anObject)`

Description forthcoming.

---

### setSortingSelector

`public void setSortingSelector(NSSelector selector)`

Description forthcoming.

---

### setTable

`public void setTable(Object table)`

Because TableColumn maintains no reference to its containing JTable, the consumer must explicitly specify this relationship by invoking __setTable__ _before_ __establishConnection__. This method also assures that an instance of EOTableAssociation exists for _table_.

---

### setValueAtRow

`public boolean setValueAtRow( Object value, int rowIndex)`

Description forthcoming.

---

### sortingSelector

`public NSSelector sortingSelector()`

Description forthcoming.

---

### table

`public Object table()`

Description forthcoming.

---

### textColorAtRow

`public Object textColorAtRow(int rowIndex)`

Description forthcoming.

---

### valueAtRow

`public Object valueAtRow(int rowIndex)`

Description forthcoming.

---

### widgetDidBeginEditing

`public boolean widgetDidBeginEditing()`

Description forthcoming.

---

### widgetDidEndEditing

`public boolean widgetDidEndEditing()`

Description forthcoming.

---

### widgetPluginClass

`protected Class widgetPluginClass()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
