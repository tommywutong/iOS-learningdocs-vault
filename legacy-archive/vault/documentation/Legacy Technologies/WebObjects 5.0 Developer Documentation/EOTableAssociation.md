---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface/Classes/EOTableAssociation.html
archived_at: '2026-07-15T08:13:55.347787Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface/Art/up.gif)](../../EOInterfaceTOC.md)

# EOTableAssociation

> **__Inherits from:__**
> : [EOWidgetAssociation](EOWidgetAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhvo2lem5sxiqltonxwg2lboruw63q) : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl) : Object

> **__Implements:__**
> : NSDisposable: EOObserving (EOControl)

> **__Package:__**
> : com.webobjects.eointerface

---

## Class Description

---

EOTableAssociation associates the contents of its SourceAspect's display group with an EOTableAssociation.TablePlugin . In general use, it should never be necessary to explicitly instantiate this class, as EOTableColumnAssociation's setTable assures that an instance exists for its _table_.

|  |
| --- |
| __Usable With__ |
| EOTable |

|  |
| --- |
| __Aspects__ |
| `EOAssociation.`EnabledAspect |  |
| `EOAssociation.`SourceAspect |  |

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxwi2ltobxxgzi)
>
> :
>
> : EOObserving:

## Method Types

---

> **Table attributes**
>
> : [boldStateAtColumnAndRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxwe33mmrjxiylumvaxiq3pnr2w23sbnzsfe33x): [italicAtColumnAndRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxws5dbnruwgqluinxwy5lnnzaw4zcsn53q): [textColorAtColumnAndRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxizlyorbw63dpojaxiq3pnr2w23sbnzsfe33x): [valueAtColumnAndRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxmylmovsuc5cdn5whk3loifxgiutpo4)
>
> **Other methods**
>
> : [EOTableAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxukt2umfrgyzkbonzw6y3jmf2gs33o): [editingTableColumnAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxwkzdjoruw4z2umfrgyzkdn5whk3loifzxg33dnfqxi2lpny): [isEditableAtColumnAndRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxws42fmruxiylcnrsuc5cdn5whk3loifxgiutpo4): [numberOfDisplayedObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxw45lnmjsxet3giruxg4dmmf4wkzcpmjvgky3uom): [primaryAspect](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u): [setSortOrderingByTableColumnOrder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxgzluknxxe5cpojsgk4tjnztue6kumfrgyzkdn5whk3loj5zgizls): [setSortsByColumnOrder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxgzluknxxe5dtij4ug33movww4t3smrsxe): [setValueAtColumnAndRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxgzlukzqwy5lfif2eg33movww4qlomrjg65y): [sortsByColumnOrder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxg33sorzue6kdn5whk3loj5zgizls): [subjectChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq): [tableDidChangeColumns](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxiylcnrsui2leinugc3thmvbw63dvnvxhg): [tableDidChangeSelection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxiylcnrsui2leinugc3thmvjwk3dfmn2gs33o): [widgetPluginClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxo2lem5sxiudmovtws3sdnrqxg4y)

## Constructors

---

### EOTableAssociation

`public EOTableAssociation(Object aDisplayObject)`

Creates a new EOTableAssociation to monitor and update the value in _aDisplayObject_, an EOTable.

In general use, it should never be necessary to explicitly instantiate this class, as EOTableColumnAssociation's setTable assures that an instance exists for its _table_.

__See Also:__ bindAspect (EOAssociation), establishConnection (EOAssociation)

---

## Instance Methods

---

### boldStateAtColumnAndRow

`public int boldStateAtColumnAndRow( int columnIndex, int rowIndex)`

Description forthcoming.

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

---

### editingTableColumnAssociation

`public EOTableColumnAssociation editingTableColumnAssociation()`

Description forthcoming.

---

### isEditableAtColumnAndRow

`public boolean isEditableAtColumnAndRow( int columnIndex, int rowIndex)`

Description forthcoming.

---

### italicAtColumnAndRow

`public int italicAtColumnAndRow( int columnIndex, int rowIndex)`

Description forthcoming.

---

### numberOfDisplayedObjects

`public int numberOfDisplayedObjects()`

Description forthcoming.

---

### primaryAspect

`public String primaryAspect()`

Returns EOAssociation.SourceAspect.

__See Also:__ primaryAspect (EOAssociation)

---

### setSortOrderingByTableColumnOrder

`public void setSortOrderingByTableColumnOrder()`

Description forthcoming.

---

### setSortsByColumnOrder

`public void setSortsByColumnOrder(boolean aBoolean)`

Description forthcoming.

---

### setValueAtColumnAndRow

`public boolean setValueAtColumnAndRow( Object value, int columnIndex, int rowIndex)`

Description forthcoming.

---

### sortsByColumnOrder

`public boolean sortsByColumnOrder()`

Description forthcoming.

---

### subjectChanged

`public void subjectChanged()`

See the subjectChanged method description in the superclass EOAssociation.

---

### tableDidChangeColumns

`public void tableDidChangeColumns()`

Description forthcoming.

---

### tableDidChangeSelection

`public void tableDidChangeSelection()`

Description forthcoming.

---

### textColorAtColumnAndRow

`public Object textColorAtColumnAndRow( int columnIndex, int rowIndex)`

Description forthcoming.

---

### valueAtColumnAndRow

`public Object valueAtColumnAndRow( int anInt, int anInt)`

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
