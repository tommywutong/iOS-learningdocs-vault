---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/EOControlActionAdapter.html
archived_at: '2026-07-15T08:11:44.629090Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# EOControlActionAdapter

> **__Inherits
> from:__**
> : Object

> **__Implements:__**
> : java.awt.event.ActionListener
> : NSDisposable

> **__Package:__**
> : com.apple.client.eointerface

---

## Class Description

---

The EOControlActionAdapter class is used to
connect user interface controls to the objects that respond to actions
performed on those controls. They are usually generated automatically
to represent connections made in Interface Builder. For example,
suppose you control-drag a connection from a "Fetch" button
to a display group and that you connect the button to the display
group's `fetch` method. At runtime, an
EOControlActionAdapter object is used to invoke the display group's `fetch` method when
a user clicks the Fetch button. In this example, the display group
is the EOControlActionAdapter's __target__, "fetch"
is the name of the __action__ (method) to perform
on the target, and the button is the __listenee__.
An EOControlActionAdapter listens for the listenee (the button)
to be acted upon (to be pushed). When the listenee is acted upon,
the EOControlActionAdapter performs the action on its target (invokes
the display group's `fetch` method).

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.yellow.eointerface package. |

## Interfaces Implemented

---

> NSDisposable: `dispose`

## Constructors

---

### EOControlActionAdapter

`public EOControlActionAdapter(
Object  target,
String  actionName,
Object  listenee)`

`public EOControlActionAdapter(
String  actionName,
Object  listenee)`

Creates and returns a new EOControlActionAdapter
object that performs the method identified by  _actionName_ on  _target_ when  _listenee_ is
acted upon. Raises an `illegalStateException` if  _listenee_ is `null`.

---

## Instance Methods

---

### actionPerformed

`public void actionPerformed(java.awt.event.ActionEvent  event)`

Performs
the receiver's action on its target. If target is `null`,
this method simply returns. If the target doesn't implement the
action method, this method prints an error message and returns.

---

### setTarget

`public void setTarget(Object  target)`

Sets the receiver's target
to  _target._

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
