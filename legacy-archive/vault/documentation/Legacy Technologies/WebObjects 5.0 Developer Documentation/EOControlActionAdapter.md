---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOInterfaceRef/Java/eointerface.swing/Classes/EOControlActionAdapter.html
archived_at: '2026-07-15T08:13:54.438051Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

# EOControlActionAdapter

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : java.awt.event.ActionListener: NSDisposable

> **__Package:__**
> : com.webobjects.eointerface.swing

---

## Class Description

---

The EOControlActionAdapter class is used to connect user interface controls to the objects that respond to actions performed on those controls. They are usually generated automatically to represent connections made in Interface Builder. For example, suppose you control-drag a connection from a "Fetch" button to a display group and that you connect the button to the display group's __fetch__ method. At runtime, an EOControlActionAdapter object is used to invoke the display group's __fetch__ method when a user clicks the Fetch button. In this example, the display group is the EOControlActionAdapter's target, "fetch" is the name of the action (method) to perform on the target, and the button is the listenee. An EOControlActionAdapter listens for the listenee (the button) to be acted upon (to be pushed). When the listenee is acted upon, the EOControlActionAdapter performs the action on its target (invokes the display group's __fetch__ method).

## Interfaces Implemented

---

> : NSDisposable
>
> : [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wecy3unfxw4qlemfyhizlsf5sgs43qn5zwk)
>
> :
>
> : java.awt.event.ActionListener
>
> : [actionPerformed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wecy3unfxw4qlemfyhizlsf5qwg5djn5xfazlsmzxxe3lfmq)
>
> :

## Method Types

---

> **All methods**
>
> : [EOControlActionAdapter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wecy3unfxw4qlemfyhizlsf5cu6q3pnz2he33mifrxi2lpnzawiylqorsxe): [setTarget](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wecy3unfxw4qlemfyhizlsf5zwk5cumfzgozlu)

## Constructors

---

### EOControlActionAdapter

`public EOControlActionAdapter( Object target, String actionName, Object listenee)`

`public EOControlActionAdapter( String actionName, Object listenee)`

Creates and returns a new EOControlActionAdapter object that performs the method identified by _actionName_ on _target_ when _listenee_ is acted upon. Raises and `llegalStateException` if _listenee_ is `null`..

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent event)`

Performs the receiver's action on its target. If target is `null`, this method simply returns. If the target doesn't implement the action method, this method prints an error message and returns.

---

### dispose

`public void dispose()`

See the description in the documentation for NSDisposable.

---

### setTarget

`public void setTarget(Object target)`

Sets the receiver's target to _target_..

---

© 2001 Apple Computer, Inc. (Last Published April 21, 2001)

[![Table of Contents](attachments/EOInterfaceRef/Java/eointerface.swing/Art/up.gif)](../../EOInterfaceTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
