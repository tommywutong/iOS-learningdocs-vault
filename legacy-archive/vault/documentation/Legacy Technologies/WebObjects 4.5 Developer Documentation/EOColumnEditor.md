---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOColumnEditor.html
archived_at: '2026-07-15T08:11:44.594103Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOColumnEditor

> **__Inherits
> from:__**
> : Object

> **__Implements:__**
> : javax.swing.table.TableCellEditor
> : javax.swing.CellEditor (javax.swing.table.TableCellEditor)

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOColumnEditor is an abstract class that implements
generalized cell editing management for javax.swing.JTables. Swing
specifies that JTable cell editing is performed by an object implementing
the javax.swing.table.TableCellEditor interface. EOColumnEditor
implements this interface in a generalized way, and concrete subclasses
such as EOTextColumnEditor perform component-specific instantiation
and event communication.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

The most important function of an EOColumnEditor instance
is mediating between its Component and the EOTableColumnAssociation
that's bound to the edited column. This mediation enables the validation
of edited values that associations are required to perform.

Create a subclass of EOColumnEditor if you want to use a Component
for JTable editing for which no EOColumnEditor is implemented.

## Interfaces Implemented

---

> javax.swing.table.TableCellEditor: `addCellEditorListener` (javax.swing.CellEditor)
> : `cancelCellEditing` (javax.swing.CellEditor)
> : [getCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6z3forbwk3dmivsgs5dpojlgc3dvmu)
> : `getTableCellEditorComponent`
> : [isCellEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc62ltinswy3cfmruxiylcnrsq)
> : `removeCellEditorListener` (javax.swing.CellEditor)
> : [shouldSelectCell](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643in52wyzctmvwgky3uinswy3a)
> : [stopCellEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643un5yegzlmnrcwi2lunfxgo)

## Method Types

---

> **Instantiation**
> : [createEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6y3smvqxizkfmruxi33sinxw24dpnzsw45a)
> : [editingTableColumnAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlenf2gs3thkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xa)
> : [editorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlenf2g64sdn5wxa33omvxhi)
> : [setCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643forbwk3dmivsgs5dpojlgc3dvmu)
> : [setEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643forcwi2lun5zeg33nobxw4zlooq)
>
> **Event handling**
> : [beginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6ytfm5uw4rlenf2gs3th)
> : [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlomrcwi2lunfxgo)

## Instance Methods

---

### `beginEditing`

`protected void beginEditing()`

Invoked from [shouldSelectCell](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643in52wyzctmvwgky3uinswy3a) and `getTableCellEditorComponent` to
inform the receiver that editing has been requested and should begin
(`shouldSelectCell` is invoked only by mouse
clicks). EOColumnEditor's implementation sends [associationDidBeginEditing](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfseezlhnfxekzdjoruw4zy) to
the EODisplayGroup of the EOTableColumnAssociation that's bound
to the receiver's TableColumn; so subclasses should invoke `super`'s
implementation before activating their Component.

---

### `createEditorComponent`

`protected abstract java.awt.Component createEditorComponent()`

Creates and returns a Component to perform the
editing-a JTextField or JComboBox, for example. Invoked in EOColumnEditor's
constructor, this method must be overridden by every subclass in
order to create and return the Component it manages.

---

### editingTableColumnAssociation

`protected com.apple.client.eointerface.EOTableColumnAssociation editingTableColumnAssociation()`

Returns the EOTableColumnAssociation
that's bound to the column being edited, which is cached
in EOColumnEditor's implementation of [shouldSelectCell](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643in52wyzctmvwgky3uinswy3a) and `getTableCellEditorComponent`.

---

### editorComponent

`public java.awt.Component editorComponent()`

Returns the receiver's Component-a
user interface control that implements the editing mechanism. EOColumnEditor
caches the Component in the constructor (in the method [createEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6y3smvqxizkfmruxi33sinxw24dpnzsw45a), which
is invoked from the constructor).

---

### `endEditing`

`protected void endEditing()`

Invoked from `cancelCellEditing` and [stopCellEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643un5yegzlmnrcwi2lunfxgo) to
inform the receiver that it should end editing. EOColumnEditor's
implementation sends [associationDidEndEditing](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfsek3teivsgs5djnztq) to
the EODisplayGroup of the EOTableColumnAssociation that's bound
to the receiver's TableColumn. Subclasses should invoke `super`'s
implementation after deactivating their Component.

---

### getCellEditorValue

`public Object getCellEditorValue()`

Returns the receiver's [editorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlenf2g64sdn5wxa33omvxhi). EOColumnEditor's
implementation simply returns `null`,
so subclasses must override this method.

---

### isCellEditable

`public boolean isCellEditable(java.util.EventObject  event)`

Returns `true` if  _event_ is
an event that should trigger editing, `false` otherwise. EOColumnEditor's implementation
simply returns `false`.
Subclasses must override this method.

---

### `setCellEditorValue`

`protected abstract void setCellEditorValue(Object  initialValue)`

Invoked from `getTableCellEditorComponent` to
assign  _initialValue_ as the receiver's [editorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlenf2g64sdn5wxa33omvxhi). Subclasses
must override this method.

---

### setEditorComponent

`public void setEditorComponent(java.awt.Component  editorComponent)`

Sets the receiver's editor
component to  _editorComponent._ Invoked
by the constructor, where  _editorComponent_ is
the Component returned from [createEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6y3smvqxizkfmruxi33sinxw24dpnzsw45a).

---

### shouldSelectCell

`public boolean shouldSelectCell(java.util.EventObject  event)`

Returns `true` if
event represents a legitimate selection trigger, or `false` otherwise. EOColumnEditor's implementation
invokes [beginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6ytfm5uw4rlenf2gs3th) and
returns `true`.

---

### stopCellEditing

`public boolean stopCellEditing()`

Informs the
receiver that it should stop editing. EOColumnEditor's implementation
invokes [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlomrcwi2lunfxgo) and
returns `true`.

|  |
| --- |
| __Note:__ Validation failures aren't handled with this method. The boolean return value is ignored. |

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
