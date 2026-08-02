---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOFormCell.html
archived_at: '2026-07-15T08:13:54.466451Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOFormCell

> **__Inherits from:__**
> : javax.swing.JComponent : java.awt.Container : java.awt.Component : Object

> **__Implements:__**
> : EOTextComponentAccess: NSDisposable: java.io.Serializable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

EOFormCell objects implement entries in EOForms.An EOFormCell has a __field component__, an editable EOTextField into which users enter data; and a __title component__, an uneditable EOTextField that identifies the purpose of the form cell's field component.

For more information on forms and form cells, see the EOForm class specification.

## Interfaces Implemented

---

> : EOTextAssociation.JTextComponentAccess
>
> : [textComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3umv4hiq3pnvyg63tfnz2a)
>
> :
>
> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3enfzxa33tmu)
>
> :

## Method Types

---

> **All methods**
>
> : [EOFormCell](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl2fj5dg64tninswy3a): [fieldComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3gnfswyzcdn5wxa33omvxhi): [setTitle](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3tmv2fi2lunrsq): [setTitleWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3tmv2fi2lunrsvo2leorua): [title](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzi): [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi): [titleWidth](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkxnfshi2a)

## Constructors

---

### EOFormCell

`public EOFormCell()`

Description forthcoming.

---

## Instance Methods

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

---

### fieldComponent

`public EOTextField fieldComponent()`

Returns the receiver's field component, the editable text field into which users enter data.

---

### setTitle

`public void setTitle(String title)`

Sets the receiver's title to _title_. This is a convenience method for setting the text value of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi)..

---

### setTitleWidth

`public void setTitleWidth(int width)`

Sets the width of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi). Typically the width of the title component is handled automatically. You should never need to invoke this method.

---

### textComponent

`public javax.swing.text.JTextComponent textComponent()`

Returns the receiver's field component, the editable text field into which users enter data.

---

### title

`public String title()`

Returns the receiver's title. This is a convenience method for setting the text value of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi)..

---

### titleComponent

`public EOTextField titleComponent()`

Returns the receiver's title component, the uneditable text field that identifies the purpose of the [fieldComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3gnfswyzcdn5wxa33omvxhi)..

---

### titleWidth

`public int titleWidth()`

Returns the width of the receiver's [titleComponent](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpizxxe3kdmvwgyl3unf2gyzkdn5wxa33omvxhi)..

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
