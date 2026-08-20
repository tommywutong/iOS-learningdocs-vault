---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOFormCell.html
archived_at: '2026-07-15T08:11:44.781322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOFormCell

> **__Inherits
> from:__**
> : javax.swing.JComponent :
> java.awt.Container :
> java.awt.Component :
> Object

> **__Implements:__**
> : EOTextAssociation.JTextComponentAccess
> : NSDisposable

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

EOFormCell objects implement entries in EOForms.An
EOFormCell has a __field component__, an editable EOTextField
into which users enter data; and a __title component__,
an uneditable EOTextField that identifies the purpose of the form
cell's field component.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

For more information on forms and form cells, see the [EOForm](EOForm.md#apple-ijeeqscbjjdei) class specification.

## Interfaces Implemented

---

> EOTextAssociation.JTextComponentAccess: [jTextComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3kkrsxq5cdn5wxa33omvxhi)
>
> NSDisposable: `dispose`

## Method Types

---

> **Accessing the field component**
> : [fieldComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3gnfswyzcdn5wxa33omvxhi)
> : [jTextComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3kkrsxq5cdn5wxa33omvxhi)
>
> **Accessing the title and
> title component**
> : [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi)
> : [title](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzi)
> : [setTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3tmv2fi2lunrsq)
> : [setTitleWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3tmv2fi2lunrsvo2leorua)
> : [titleWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkxnfshi2a)

## Instance Methods

---

### fieldComponent

`public EOTextField fieldComponent()`

Returns the receiver's field
component, the editable text field into which users enter data.

---

### jTextComponent

`public javax.swing.text.JTextComponent jTextComponent()`

Returns the receiver's field
component, the editable text field into which users enter data.

---

### setTitle

`public void setTitle(String  aString)`

Sets the receiver's title
to  _aString._ This
is a convenience method for setting the text value of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi).

---

### setTitleWidth

`public void setTitleWidth(int  width)`

Sets the width of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi). Typically
the width of the title component is handled automatically. You should
never need to invoke this method.

---

### title

`public String title()`

Returns the receiver's title. This
is a convenience method for setting the text value of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi).

---

### titleComponent

`public EOTextField titleComponent()`

Returns the receiver's title
component, the uneditable text field that identifies the purpose
of the [fieldComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3gnfswyzcdn5wxa33omvxhi).

---

### titleWidth

`public int titleWidth()`

Returns the width of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi).

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
