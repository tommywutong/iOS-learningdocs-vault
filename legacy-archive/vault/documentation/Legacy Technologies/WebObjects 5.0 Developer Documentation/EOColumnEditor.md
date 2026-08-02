---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOColumnEditor.html
archived_at: '2026-07-15T08:13:54.145462Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md) 

# EOColumnEditor

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : javax.swing.table.TableCellEditor

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

EOColumnEditor is an abstract class that implements generalized cell editing management for javax.swing.JTables. Swing specifies that JTable cell editing is performed by an object implementing the javax.swing.table.TableCellEditor interface. EOColumnEditor implements this interface in a generalized way, and concrete subclasses such as EOTextColumnEditor perform component-specific instantiation and event communication.

The most important function of an EOColumnEditor instance is mediating between its Component and the EOTableColumnAssociation that's bound to the edited column. This mediation enables the validation of edited values that associations are required to perform.

Create a subclass of EOColumnEditor if you want to use a Component for JTable editing for which no EOColumnEditor is implemented.

## Interfaces Implemented

---

> : javax.swing.table.TableCellEditor
>
> : [addCellEditorListener](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6ylemrbwk3dmivsgs5dpojggs43umvxgk4q): [cancelCellEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6y3bnzrwk3cdmvwgyrlenf2gs3th): [getCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6z3forbwk3dmivsgs5dpojlgc3dvmu): [getTableCellEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6z3forkgcytmmvbwk3dmivsgs5dpojbw63lqn5xgk3tu): [isCellEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc62ltinswy3cfmruxiylcnrsq): [removeCellEditorListener](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc64tfnvxxmzkdmvwgyrlenf2g64smnfzxizlomvza): [shouldSelectCell](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643in52wyzctmvwgky3uinswy3a): [stopCellEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643un5yegzlmnrcwi2lunfxgo)
>
> :

## Method Types

---

> **All methods**
>
> : [EOColumnEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6rkpinxwy5lnnzcwi2lun5za): [beginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6ytfm5uw4rlenf2gs3th): [createEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6y3smvqxizkfmruxi33sinxw24dpnzsw45a): [editingTableColumnAssociation](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlenf2gs3thkrqwe3dfinxwy5lnnzaxg43pmnuwc5djn5xa): [editorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlenf2g64sdn5wxa33omvxhi): [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlomrcwi2lunfxgo): [fireEditingCanceled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6ztjojsukzdjoruw4z2dmfxggzlmmvsa): [fireEditingStopped](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6ztjojsukzdjoruw4z2torxxa4dfmq): [isCellEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc62ltinswy3cfmruxiylcnrsq): [setCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643forbwk3dmivsgs5dpojlgc3dvmu): [setEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643forcwi2lun5zeg33nobxw4zlooq)

## Constructors

---

### EOColumnEditor

`public EOColumnEditor()`

Description forthcoming.

---

## Instance Methods

---

### addCellEditorListener

`public void addCellEditorListener(javax.swing.event.CellEditorListener aCellEditorListener)`

Description forthcoming.

---

### beginEditing

`protected void beginEditing()`

Description forthcoming.

---

### cancelCellEditing

`public void cancelCellEditing()`

Description forthcoming.

---

### createEditorComponent

`protected abstract java.awt.Component createEditorComponent()`

Description forthcoming.

---

### editingTableColumnAssociation

`public com.webobjects.eointerface.EOTableColumnAssociation editingTableColumnAssociation()`

Returns the EOTableColumnAssociation that's bound to the column being edited, which is cached in EOColumnEditor's implementation of [shouldSelectCell](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643in52wyzctmvwgky3uinswy3a) and __getTableCellEditorComponent__..

---

### editorComponent

`public java.awt.Component editorComponent()`

Returns the receiver's Component-a user interface control that implements the editing mechanism. EOColumnEditor caches the Component in the constructor (in the method [createEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6y3smvqxizkfmruxi33sinxw24dpnzsw45a), which is invoked from the constructor).

---

### endEditing

`protected void endEditing()`

Description forthcoming.

---

### fireEditingCanceled

`protected void fireEditingCanceled()`

Description forthcoming.

---

### fireEditingStopped

`protected void fireEditingStopped()`

Description forthcoming.

---

### getCellEditorValue

`public Object getCellEditorValue()`

Returns the receiver's [editorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlenf2g64sdn5wxa33omvxhi). EOColumnEditor's implementation simply returns `null`, so subclasses must override this method.

---

### getTableCellEditorComponent

`public java.awt.Component getTableCellEditorComponent( javax.swing.JTable aJTable, Object initialValue, boolean isSelected, int rowIndex, int columnIndex)`

Description forthcoming.

---

### isCellEditable

`public boolean isCellEditable(java.util.EventObject event)`

Description forthcoming.

---

### removeCellEditorListener

`public void removeCellEditorListener(javax.swing.event.CellEditorListener aCellEditorListener)`

Description forthcoming.

---

### setCellEditorValue

`protected abstract void setCellEditorValue(Object value)`

Description forthcoming.

---

### setEditorComponent

`public void setEditorComponent(java.awt.Component editorComponent)`

Description forthcoming.

---

### shouldSelectCell

`public boolean shouldSelectCell(java.util.EventObject event)`

Description forthcoming.

---

### stopCellEditing

`public boolean stopCellEditing()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
