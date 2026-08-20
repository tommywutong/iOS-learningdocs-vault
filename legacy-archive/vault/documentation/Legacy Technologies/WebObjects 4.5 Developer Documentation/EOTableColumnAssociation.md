---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTableColumnAssociation.html
archived_at: '2026-07-15T08:11:45.043898Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTableColumnAssociation

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

An EOTableColumnAssociation associates a single attribute
of all enterprise objects in its [ValueAspect](EOAssociation.md#apple-ijeugsskjfbeo)'s EODisplayGroup with
a Swing JTable TableColumn. The value of each object's attribute
is displayed in its corresponding row.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

By far the easiest way to configure EOTableColumnAssociations
is in Interface Builder, but they may also be instantiated programmatically.
Because Swing's TableColumn maintains no reference to its containing
JTable, this relationship must be explicitly specified via [setTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forkgcytmmu) before `establishConnection` is
invoked.

|  |
| --- |
| __Usable With__ |
| javax.swing.table.TableColumn |

|  |
| --- |
| __Aspects__ |
| [BoldAspect](EOAssociation.md#apple-ijeugssfincek) |  |
| [EnabledAspect](EOAssociation.md#apple-ijeugr2hivcem) | A boolean attribute of the objects, which determines whether each object's value cell is editable. Note that because EOTableViewAssociation also uses this aspect, you can use it with different keys to limit editability to the whole row or to an individual cell (column) in that row. |
| [ItalicAspect](EOAssociation.md#apple-ijeugscfi5eug) |  |
| [ValueAspect](EOAssociation.md#apple-ijeugsskjfbeo) | An attribute of the objects, displayed in each row of the TableColumn. |

## Constructors

---

### `EOTableColumnAssociation`

`public EOTableColumnAssociation(Object  aDisplayObject)`

Creates a new EOTableAssociation
to monitor and update the value in  _aDisplayObject,_
a javax.swing.table.TableColumn.

You normally
set up associations in Interface Builder, in which case you don't
need to create them programmatically. However, if you do create
them up programmatically, setting them up is a multi-step process.
After creating an association, you must bind its aspects and establish
its connections. Because Swing's TableColumn maintains no reference
to its containing JTable, this relationship must be explicitly specified
via [setTable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xc643forkgcytmmu) before [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) is
invoked

__See Also:__  [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) (EOAssociation)

---

## Static Methods

---

### `setTableColumnCustomizer`

`public static void setTableColumnCustomizer(TableColumnCustomizer  tableColumnCustomizer)`

Sets  _tableColumnCustomizer_ as
the object that determines associations' editors and renderers.
By default, an EOTableColumnAssociation's editor is the corresponding
TableColumn's editor; or, if the TableColumn doesn't have an
editor, an [EOTextColumnEditor](EOTextColumnEditor.md#apple-ijbukrcgifcus) is used. Similarly,
an EOTableColumnAssociation's renderer is the corresponding TableColumn's
renderer; or, if the TableColumn doesn't have an editor, a javax.swing.table.DefaultTableCellRenderer
is used.

---

### `tableColumnCustomizer`

`public static TableColumnCustomizer tableColumnCustomizer()`

Returns the object that specifies editors and
renderers for associations.

---

## Instance Methods

---

### format

`public java.text.Format format()`

Returns the java.lang.text.Format used to format
values bound to the receiver's `ValueAspect` for
display and editing.

---

### isEditableAtRow

`public boolean isEditableAtRow(int  row)`

Returns whether or not the property bound to
the receiver's `ValueAspect` is
editable at  _row,_ as determined by
the [EnabledAspect](EOAssociation.md#apple-ijeugr2hivcem). If this aspect is bound,
a non-zero value at  _row_ indicates
that the property may be edited. If the `EnabledAspect` is
unbound all rows are considered editable.

---

### primaryAspect

`public String primaryAspect()`

Returns `ValueAspect`.

---

### setFormat

`public void setFormat(java.text.Format  aFormat)`

Sets the java.lang.text.Format object to use
in formatting values bound to the receiver's `ValueAspect` for display
and editing.

---

### setTable

`public void breakConnection()`

Because TableColumn maintains no reference to
its containing JTable, the consumer must explicitly specify this
relationship by invoking `setTable`  _before_ `establishConnection`.
This method also assures that an instance of EOTableAssociation
exists for  _table._

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
