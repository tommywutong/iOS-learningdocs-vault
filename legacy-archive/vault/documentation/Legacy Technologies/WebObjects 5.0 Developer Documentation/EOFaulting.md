---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOFaulting.html
archived_at: '2026-07-15T08:13:47.983486Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOFaulting

> __Implemented by:__ : EODeferredFaulting:: EOEnterpriseObject:: EOCustomObject:: EOGenericRecord:

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The EOFaulting interface together with the EOFaultHandler class forms a general mechanism for postponing an object's initialization until its actually needed. In it's pre-initialization state, an EOFaulting object is known as a _fault_. When the object is sent a message to which it can't respond without initializing, it uses a fault handler to _fire_, or to finish initializing. Faults are most commonly used by the access layer to represent an object not yet fetched from the database, but that must nonetheless exist as an instance in the application-typically because it's the destination of a relationship. Consequently, a fault typically fires when an attempt is made to access any of its data. In this case, firing a fault involves fetching the object's data.

The default implementations of EOFaulting in EOCustomObject and EOGenericRecord are sufficient for most purposes. If you need custom faulting behavior, you typically create a subclass of EOFaultHandler to accommodate different means of converting faults into regular objects; there's rarely a need to override the default implementations of EOFaulting.

## Creating a Fault

You create a fault with the EOFaultHandler method makeObjectIntoFault. In Java Client, you create a fault by sending an newly created object a [turnIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3uovzg4sloorxumylvnr2a) message, providing an EOFaultHandler that will later help the fault to fire. This fault handler should be considered completely the private property of the fault. You shouldn't send it any messages, instead dealing exclusively with the fault.

## Firing a Fault

A fault is fired when it can't respond to a message without completing its initialization. Any of the object's methods that requires initialization trigger the firing, This is generally accomplished by invoking the [willRead](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3xnfwgyutfmfsa) method. For example, in the typical case of an object that needs to fetch it's data from a database upon firing, __willRead__ is invoked from the object's "get" methods, such as the following:

> ```
> public String roleName() {
>     willRead();
>     return roleName;
> }
> ```

The default implementations of __willRead__ provided by EOCustomObject and EOGenericRecord take care of using the object's fault handler to finish initialization. For more information on a fault handler's role, see the EOFaultHandler class specification.

## Instance Methods

---

### clearFault

`public abstract void clearFault()`

Restores the receiver to its status prior to the [turnIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3uovzg4sloorxumylvnr2a) message that turned the object into a fault. Throws an exception if the receiver isn't a fault.

You rarely use this method. Rather, it's invoked by an EOFaultHandler during the process of firing the fault. For more information, see the EOFaultHandler class specification.

---

### faultHandler

`public abstract EOFaultHandler faultHandler()`

If the receiver is a fault, returns its fault handler; otherwise returns `nil`.

---

### isFault

`public abstract boolean isFault()`

Returns __true__ if the receiver is a fault, __false__ otherwise.

---

### turnIntoFault

`public abstract void turnIntoFault(EOFaultHandler aFaultHandler)`

(Java Client only) Converts the receiver into a fault, assigning _aFaultHandler_ as the object that stores its original state and later converts the fault back into a normal object (typically by fetching data from an external repository). The receiver becomes the owner of _aFaultHandler_; you shouldn't assign it to another object.

---

### willRead

`public abstract void willRead()`

Fills the receiver with values fetched from the database. Before your application attempts to message an object, you must ensure that it has been filled with its data. To do this, enterprise objects invoke the method __willRead__ prior to any attempt to access the object's state, most typically in "get" methods such as the following:
> ```
> public String roleName() {
>     willRead();
>     return roleName;
> }
> ```

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
