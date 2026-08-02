---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOFaulting.html
archived_at: '2026-07-15T08:11:38.912893Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOFaulting

> __Implemented by:__ : EODeferredFaulting
> : EOEnterpriseObject
> : EOCustomObject
> : EOGenericRecord

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The EOFaulting interface together with the EOFaultHandler
class forms a general mechanism for postponing an object's initialization
until its actually needed. In it's pre-initialization state, an EOFaulting
object is known as a _fault._ When
the object is sent a message to which it can't respond without
initializing, it uses a fault handler to _fire,_
or to finish initializing. Faults are most commonly used by the
access layer to represent an object not yet fetched from the database,
but that must nonetheless exist as an instance in the application-typically
because it's the destination of a relationship. Consequently,
a fault typically fires when an attempt is made to access any of
its data. In this case, firing a fault involves fetching the object's
data.

The default implementations of EOFaulting in EOCustomObject
and EOGenericRecord are sufficient for most purposes. If you need
custom faulting behavior, you typically create a subclass of EOFaultHandler
to accommodate different means of converting faults into regular
objects; there's rarely a need to override the default implementations
of EOFaulting.

## Creating a Fault

In Yellow Box, you create a fault with the [EOFaultHandler](EOFaultHandler.md#apple-ivhumylvnr2eqylomrwgk4q) method [makeObjectIntoFault](EOFaultHandler.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6rtbovwhisdbnzsgyzlsf5wwc23fj5rguzldorew45dpizqxk3du). In Java Client, you
create a fault by sending an newly created object a [turnIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3uovzg4sloorxumylvnr2a) message,
providing an EOFaultHandler that will later help the fault to fire.
This fault handler should be considered completely the private property
of the fault. You shouldn't send it any messages, instead dealing
exclusively with the fault.

## Firing a Fault

A fault is fired when it can't respond to a message without
completing its initialization. Any of the object's methods that
requires initialization trigger the firing, This is generally accomplished
by invoking the [willRead](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3xnfwgyutfmfsa) method.
For example, in the typical case of an object that needs to fetch
it's data from a database upon firing, `willRead` is
invoked from the object's "get" methods, such as the following:

> ```
> public String roleName() {
>     willRead();
>     return roleName;
> }
> ```

The default implementations of `willRead` provided
by EOCustomObject and EOGenericRecord take care of using the object's
fault handler to finish initialization. For more information on
a fault handler's role, see the [EOFaultHandler](EOFaultHandler.md#apple-ivhumylvnr2eqylomrwgk4q) class specification.

## Instance Methods

---

### clearFault

`public abstract void clearFault()`

(com.apple.client.eocontrol only) Restores the receiver
to its status prior to the [turnIntoFault](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpizqxk3dunfxgol3uovzg4sloorxumylvnr2a) message
that turned the object into a fault. Throws an exception if the
receiver isn't a fault.

You rarely use this method. Rather, it's invoked by an EOFaultHandler
during the process of firing the fault. For more information, see
the [EOFaultHandler](EOFaultHandler.md#apple-ivhumylvnr2eqylomrwgk4q) class specification.

---

### faultHandler

`public abstract EOFaultHandler faultHandler()`

(com.apple.client.eocontrol only)
If the receiver is a fault, returns its fault handler; otherwise
returns `nil`.

---

### isFault

`public abstract boolean isFault()`

(com.apple.client.eocontrol only) Returns `true` if
the receiver is a fault, `false` otherwise.

---

### turnIntoFault

`public abstract void turnIntoFault(EOFaultHandler aFaultHandler)`

(com.apple.client.eocontrol only) Converts the receiver
into a fault, assigning _aFaultHandler_ as
the object that stores its original state and later converts the
fault back into a normal object (typically by fetching data from
an external repository). The receiver becomes the owner of _aFaultHandler;_
you shouldn't assign it to another object.

---

### willRead

`public abstract void willRead()`

Fills the receiver with values fetched from
the database. Before your application attempts to message an object,
you must ensure that it has been filled with its data. To do this,
enterprise objects invoke the method `willRead` prior
to any attempt to access the object's state, most typically in
"get" methods such as the following:
> ```
> public String roleName() {
>     willRead();
>     return roleName;
> }
> ```

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
