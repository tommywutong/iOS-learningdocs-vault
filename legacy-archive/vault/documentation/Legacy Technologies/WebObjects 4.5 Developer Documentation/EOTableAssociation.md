---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTableAssociation.html
archived_at: '2026-07-15T08:11:45.026530Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTableAssociation

> **__Inherits
> from:__**
> : [EOAssociation](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuc43tn5rwsylunfxw4) : EODelayedObserver (EOControl)
> : Object

> **__Implements:__**
> : javax.swing.event.ListSelectionListener
> : EOObserving (EODelayedObserver)
> : NSDisposable (EOAssociation)

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOTableAssociation associates the contents of its [SourceAspect](EOAssociation.md#apple-ijeugsseizfeo)'s display group with
an EOTable (an object that places a javax.swing.JTable in a scroll
view). In general use, it should never be necessary to explicitly
instantiate this class, as EOTableColumnAssociation's [setTable](EOTableColumnAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forkgcytmmu) assures that an instance
exists for its  _table._

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

|  |
| --- |
| __Usable With__ |
| EOTable |

|  |
| --- |
| __Aspects__ |
| `EOAssociation.` [EnabledAspect](EOAssociation.md#apple-ijeugr2hivcem) |  |
| `EOAssociation.` [SourceAspect](EOAssociation.md#apple-ijeugsseizfeo) |  |

## Interfaces Implemented

---

> javax.swing.event.ListSelectionListener: [valueChanged](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxxmylmovsug2dbnztwkza)

## Constructors

---

### EOTableAssociation

`public EOTableAssociation(Object  aDisplayObject)`

Creates a new EOTableAssociation to monitor
and update the value in  _aDisplayObject,_
an EOTable.

In general use, it should never be necessary to
explicitly instantiate this class, as EOTableColumnAssociation's [setTable](EOTableColumnAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forkgcytmmu) assures that an instance
exists for its  _table._

__See
Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4)), [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

## Static Methods

---

### instanceForTable

`public static EOTableAssociation instanceForTable(Object  table)`

Invoked from EOTableColumnAssociation's [setTable](EOTableColumnAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forkgcytmmu) to ensure that an EOTableAssociation
has been created for  _table._

---

## Instance Methods

---

### addColumnAssociation

`public void addColumnAssociation(EOTableColumnAssociation  aTableColumnAssociation)`

Adds  _aTableColumnAssociation_ to
the receiver's set of EOTableColumnAssociations. If
the receiver's [SourceAspect](EOAssociation.md#apple-ijeugsseizfeo) is unbound, this method
binds it to _aTableColumnAssociation_'s
display group and then invokes [establishConnection](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny).

---

### breakConnection

`public void breakConnection()`

See the [breakConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe4tfmfvug33onzswg5djn5xa) method description
in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

### editingAssociation

`public EOTableColumnAssociation editingAssociation()`

Returns the EOTableColumnAssociation bound to
the column being edited in the receiver's display object, if any.

---

### establishConnection

`public void establishConnection()`

See the [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) method
description in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

### isUsableWithObject

`public boolean isUsableWithObject(Object  candidate)`

Returns `true` if  _candidate_ is
an instance of EOTable and its [jTable](EOTable.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dff5vfiylcnrsq) is an instance of JTable,  _false_ otherwise.

__See
Also:__  [isUsableWithObject](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxws42vonqwe3dfk5uxi2cpmjvgky3u) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

### primaryAspect

`public String primaryAspect()`

Returns [SourceAspect](EOAssociation.md#apple-ijeugsseizfeo).

__See
Also:__  [primaryAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxa4tjnvqxe6kbonygky3u) ( [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4))

---

### removeColumnAssociation

`public void removeColumnAssociation(EOTableColumnAssociation  aTableColumnAssociation)`

Removes  _aTableColumnAssociation_ from
the receiver's set of EOTableColumnAssociations. If  _aTableColumnAssociation_ is
the last of the receiver's column associations, it prepares itself
for garbage collection.

---

### subjectChanged

`public void subjectChanged()`

See the [subjectChanged](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq) method description
in the superclass [EOAssociation](EOAssociation.md#apple-ivhuc43tn5rwsylunfxw4).

---

### valueChanged

`public void valueChanged(com.sun.java.swing.event.ListSelectionEvent  event)`

EOTableAssociation listens to its display object's
TableModel in order to synchronize the selection indices of its [SourceAspect](EOAssociation.md#apple-ijeugsseizfeo)'s EODisplayGroup with
those of the model. This method represents the association's implementation
of the ListSelectionListener interface.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
