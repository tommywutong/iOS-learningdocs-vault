---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOTextColumnEditor.html
archived_at: '2026-07-15T08:11:45.114057Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOTextColumnEditor

> **__Inherits
> from:__**
> : [EOColumnEditor](EOColumnEditor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33movww4rlenf2g64q)

> **__Implements:__**
> : java.awt.event.ActionListener
> : java.awt.event.FocusListener
> : javax.swing.table.TableCellEditor (EOColumnEditor)
> : javax.swing.CellEditor (javax.swing.table.TableCellEditor)

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOTextColumnEditor is a concrete subclass
of EOColumnEditor whose instances mediate
between EOTextColumnAssociations and EOTextFields (an EOTextColumnEditor's `editorComponent` is
an EOTextField).

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

For more information on the purpose of EOTextColumnEditors,
see the [EOColumnEditor](EOColumnEditor.md#apple-ijbukq2gireug) class specification.

## Interfaces Implemented

---

> java.awt.event.ActionListener: [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwcy3unfxw4udfojtg64tnmvsa)
>
> java.awt.event.FocusListener: `focusGained`
> : [focusLost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwm33dovzuy33toq)

## Method Types

---

> **Instantiation**
> : [createEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwg4tfmf2gkrlenf2g64sdn5wxa33omvxhi)
>
> **Handling events**
> : [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwcy3unfxw4udfojtg64tnmvsa)
> : [beginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwezlhnfxekzdjoruw4zy)
> : [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwk3teivsgs5djnztq)
>
> **Accessing the text field**
> : [getCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwozluinswy3cfmruxi33skzqwy5lf)
> : [isCellEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixws42dmvwgyrlenf2gcytmmu)
> : [setCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixxgzluinswy3cfmruxi33skzqwy5lf)

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent  event)`

Invokes `stopCellEditing`.

__See
Also:__  [stopCellEditing](EOColumnEditor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643un5yegzlmnrcwi2lunfxgo) ( [EOColumnEditor](EOColumnEditor.md#apple-ijbukq2gireug))

---

### `beginEditing`

`protected void beginEditing()`

Adds the receiver to its editor
component as a java.awt.event.FocusListener and as a java.awt.event.ActionListener,
and invokes `super`'s
implementation.

__See Also:__  [beginEditing](EOColumnEditor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6ytfm5uw4rlenf2gs3th) ( [EOColumnEditor](EOColumnEditor.md#apple-ijbukq2gireug))

---

### `createEditorComponent`

`protected abstract java.awt.Component createEditorComponent()`

Returns a newly instantiated
javax.swing.JTextField with a black javax.swing.border.LineBorder.

__See
Also:__  [createEditorComponent](EOColumnEditor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6y3smvqxizkfmruxi33sinxw24dpnzsw45a) ( [EOColumnEditor](EOColumnEditor.md#apple-ijbukq2gireug))

---

### `endEditing`

`protected void endEditing()`

Removes the receiver from its
editor component's focus and action listener lists, and invokes `super`'s implementation.

__See
Also:__  [endEditing](EOColumnEditor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc6zlomrcwi2lunfxgo) ( [EOColumnEditor](EOColumnEditor.md#apple-ijbukq2gireug))

---

### focusLost

`public void focusLost(java.awt.event.FocusEvent  event)`

Invokes `stopCellEditing`.

__See
Also:__  [stopCellEditing](EOColumnEditor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxwy5lnnzcwi2lun5zc643un5yegzlmnrcwi2lunfxgo) ( [EOColumnEditor](EOColumnEditor.md#apple-ijbukq2gireug))

---

### getCellEditorValue

`public Object getCellEditorValue()`

Overrides `super`'s
implementation to return the text value of the receiver's `editorComponent`,
an EOTextField.

---

### isCellEditable

`public boolean isCellEditable(java.util.EventObject  event)`

Overrides `super`'s
implementation to return `true` as
long as  _event_ is not a java.awt.event.MouseEvent with
a click count of less than two.

---

### setCellEditorValue

`public void setCellEditorValue(Object  initialValue)`

Sets the value of the receiver's
editor component, an EOTextField by default, to  _initialValue_ using
the method `setText`.

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
