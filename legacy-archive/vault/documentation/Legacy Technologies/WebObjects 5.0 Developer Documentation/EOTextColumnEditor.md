---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOTextColumnEditor.html
archived_at: '2026-07-15T08:13:54.782764Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOTextColumnEditor

> **__Inherits from:__**
> : [EOColumnEditor](EOColumnEditor.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33movww4rlenf2g64q) : Object

> **__Implements:__**
> : java.awt.event.ActionListener: java.awt.event.FocusListener

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

EOTextColumnEditor is a concrete subclass of EOColumnEditor whose instances mediate between EOTextColumnAssociations and EOTextFields (an EOTextColumnEditor's __editorComponent__ is an EOTextField).

For more information on the purpose of EOTextColumnEditors, see the EOColumnEditor class specification.

## Interfaces Implemented

---

> : java.awt.event.ActionListener
>
> : [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwcy3unfxw4udfojtg64tnmvsa)
>
> :
>
> : java.awt.event.FocusListener
>
> : [focusGained](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwm33dovzuoyljnzswi): [focusLost](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwm33dovzuy33toq)
>
> :

## Method Types

---

> **All methods**
>
> : [EOTextColumnEditor](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixukt2umv4hiq3pnr2w23sfmruxi33s): [beginEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwezlhnfxekzdjoruw4zy): [createEditorComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwg4tfmf2gkrlenf2g64sdn5wxa33omvxhi): [endEditing](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwk3teivsgs5djnztq): [getCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixwozluinswy3cfmruxi33skzqwy5lf): [isCellEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixws42dmvwgyrlenf2gcytmmu): [setCellEditorValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkrsxq5cdn5whk3loivsgs5dpoixxgzluinswy3cfmruxi33skzqwy5lf)

## Constructors

---

### EOTextColumnEditor

`public EOTextColumnEditor()`

Description forthcoming.

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent event)`

Description forthcoming.

---

### beginEditing

`protected void beginEditing()`

Description forthcoming.

---

### createEditorComponent

`protected java.awt.Component createEditorComponent()`

Description forthcoming.

---

### endEditing

`protected void endEditing()`

Description forthcoming.

---

### focusGained

`public void focusGained(java.awt.event.FocusEvent event)`

Description forthcoming.

---

### focusLost

`public void focusLost(java.awt.event.FocusEvent event)`

Description forthcoming.

---

### getCellEditorValue

`public Object getCellEditorValue()`

Overrides `super`'s implementation to return the text value of the receiver's __editorComponent__, an EOTextField.

---

### isCellEditable

`public boolean isCellEditable(java.util.EventObject event)`

Overrides `super`'s implementation to return `true` as long as _event_ is not a java.awt.event.MouseEvent with a click count of less than two.

---

### setCellEditorValue

`public void setCellEditorValue(Object anObject)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
