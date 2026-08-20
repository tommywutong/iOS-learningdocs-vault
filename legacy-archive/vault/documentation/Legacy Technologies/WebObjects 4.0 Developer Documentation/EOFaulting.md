---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOFaulting.html
archived_at: '2026-07-18T01:28:32.771743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOEnterpriseObject-2.md)
[!](EOKeyValueCoding.md)

---

# EOFaulting

__Implemented By:__
EOEnterpriseObject
EOCustomObject
EOGenericRecord

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Interface Description

The EOFaulting interface together with the EOFaultHandler class forms a general mechanism for postponing an object's initialization until its actually needed. In it's pre-initialization state, an EOFaulting object is known as a _fault_. When the object is sent a message to which it can't respond without initializing, it uses a fault handler to _fire_, or to finish initializing. Faults are most commonly used by the access layer to represent an object not yet fetched from the database, but that must nonetheless exist as an instance in the application-typically because it's the destination of a relationship. Consequently, a fault typically fires when an attempt is made to access any of its data. In this case, firing a fault involves fetching the object's data.

The default implementations of EOFaulting in EOCustomObject and EOGenericRecord are sufficient for most purposes. If you need custom faulting behavior, you typically create a subclass of EOFaultHandler to accommodate different means of converting faults into regular objects; there's rarely a need to override the default implementations of EOFaulting.

---

### Creating a Fault

In Yellow Box, you create a fault with the [EOFaultHandler](EOFaultHandler.md) method [__makeObjectIntoFault__](EOFaultHandler.md). In Java Client, you create a fault by sending an newly created object a __turnIntoFault__ message, providing an EOFaultHandler that will later help the fault to fire. This fault handler should be considered completely the private property of the fault. You shouldn't send it any messages, instead dealing exclusively with the fault.

---

### Firing a Fault

A fault is fired when it can't respond to a message without completing its initialization. Any of the object's methods that requires initialization trigger the firing, This is generally accomplished by invoking the __willRead__ method. For example, in the typical case of an object that needs to fetch it's data from a database upon firing, __willRead__ is invoked from the object's "get" methods, such as the following:

> ```
> public String roleName() {
>     willRead();
>     return roleName;
> }
> ```

The default implementations of __willRead__ provided by EOCustomObject and EOGenericRecord take care of using the object's fault handler to finish initialization. For more information on a fault handler's role, see the [EOFaultHandler](EOFaultHandler.md) class specification.

## Instance Methods

---

#### clearFault

public abstract void __clearFault__ ()

This method is available for Java Client applications only; there is no Yellow Box equivalent.

Restores the receiver to its status prior to the __turnIntoFault__ message that turned the object into a fault. Throws an exception if the receiver isn't a fault.

You rarely use this method. Rather, it's invoked by an EOFaultHandler during the process of firing the fault. For more information, see the [EOFaultHandler](EOFaultHandler.md) class specification.

---

#### isFault

public abstract boolean __isFault__ ()

This method is available for Java Client applications only; there is no Yellow Box equivalent.

Returns __true__ if _anObject_ is an EOFault, __false__ otherwise.

---

#### turnIntoFault

public abstract void __turnIntoFault__ (EOFaultHandler _aFaultHandler_)

This method is available for Java Client applications only; there is no Yellow Box equivalent.

Converts the receiver into a fault, assigning _aFaultHandler_ as the object that stores its original state and later converts the fault back into a normal object (typically by fetching data from an external repository). The receiver becomes the owner of _aFaultHandler_; you shouldn't assign it to another object.

---

#### willRead

public abstract void __willRead__ ()

Fills the receiver with values fetched from the database. Before your application attempts to message an object, you must ensure that it has been filled with its data. To do this, enterprise objects invoke the method __willRead__ prior to any attempt to access the object's state, most typically in "get" methods such as the following:

> ```
> public String roleName() {
>     willRead();
>     return roleName;
> }
> ```

---

[!](EOEnterpriseObject-2.md)
[!](EOKeyValueCoding.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
