---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSNotification.html
archived_at: '2026-07-15T08:13:56.323738Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSNotification

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSCoding: java.io.Serializable

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSNotification objects encapsulate information so that it can be broadcast to other objects by an [NSNotificationCenter](NSNotificationCenter.md#apple-inauqrsfjbcuu) object.

## Notifications and their Rationale

The standard way to pass information between objects is message passing-one object invokes the method of another object. However, message passing requires that the object sending the message know who the receiver is and what messages it responds to. At times, this tight coupling of two objects is undesirable-most notably because it would join together two otherwise independent subsystems. For these cases, a broadcast model is introduced: An object posts a notification, which is dispatched to the appropriate observers through an NSNotificationCenter object, or simply notification center.

An NSNotification object (referred to as a notification) contains a name, an object, and a dictionary. The name is a tag identifying the notification. The object is any object that the poster of the notification wants to send to observers of that notification (typically, it is the object that posted the notification). The dictionary stores other related objects if any.

Any object may post a notification. Other objects can register themselves as observers to receive notifications when they are posted. The object posting the notification, the object included in the notification, and the observer of the notification may all be different objects or the same object. Objects that post notifications need not know anything about the observers. On the other hand, observers need to know at least the notification name and keys to the dictionary if provided.

NSNotification objects are immutable objects.

## Notification Centers

The notification center manages the sending and receiving of notifications. When an object wants to receive a certain notification, it registers itself with the notification center. When an object has a notification to send, it sends it to the notification center. When the notification center receives a notification, it passes that notification along to all objects registered to receive it. (See the [NSNotificationCenter](NSNotificationCenter.md#apple-inauqrsfjbcuu) class specification for more on posting notifications.)

This notification model frees an object from concern about what objects it should send information to. Any object may simply post a notification without knowing what objects-if any-are receiving the notification. However, objects receiving notifications do need to know at least the notification name if not the type of information the notification contains. The notification center takes care of broadcasting notifications to registered observers. Another benefit of this model is to allow multiple objects to listen for notifications, which would otherwise be cumbersome.

You can create a notification object with the constructor. However, you don't usually create your own notifications directly. The NSNotificationCenter method [postNotification](NSNotificationCenter.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3qn5zxittporuwm2ldmf2gs33o) allows you to conveniently post a notification without creating it first.

## Notification and Delegation

Using the notification system is similar to using delegates, but it has these advantages:

- Any number of objects may receive the notification, not just the delegate object. This precludes returning a value.
- An object may receive any message you like from the notification center, not just the predefined delegate methods.
- The object posting the notification does not even have to know the observer exists.

## Creating Subclasses

You can subclass NSNotification to contain information in addition to the notification name, object, and dictionary. This extra data must be agreed upon between notifiers and observers.

## Interfaces Implemented

---

> : NSCoding
>
> : [classForCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc6y3mmfzxgrtpojbw6zdfoi): [encodeWithCoder](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc6zlomnxwizkxnf2gqq3pmrsxe)
>
> :

## Method Types

---

> **Constructors**
>
> : [NSNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc6tstjzxxi2lgnfrwc5djn5xa)
>
> **Obtaining information about a notification**
>
> : [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc63tbnvsq): [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc633cnjswg5a): [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc65ltmvzes3tgn4)
>
> **Methods inherited from Object**
>
> : [equals](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc6zlrovqwy4y): [hashCode](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc62dbonueg33emu): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc65dpkn2he2lom4)
>
> **Decoding the notification**
>
> : [decodeObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttporuwm2ldmf2gs33of5sgky3pmrsu6ytkmvrxi)

## Constructors

---

### NSNotification

`public NSNotification( String aName, Object anObject)`

Creates a notification object that associates the name _aName_ with the object _anObject_ and contains an empty userInfo dictionary. The _aName_ parameter may not be `null`.

`public NSNotification( String aName, Object anObject, NSDictionary userInfo)`

Returns a notification object that associates the name _aName_ with the object _anObject_ and the dictionary of arbitrary data _userInfo_. The dictionary _userInfo_ may be `null`; if so, the new notification contains an empty userInfo dictionary. _aName_ may not be `null`.

---

## Static Methods

---

### decodeObject

`public static Object decodeObject(NSCoder coder)`

Creates an NSNotification from the data in _coder_.

__See Also:__ [NSCoding](NSCoding.md#apple-ineucskcizbeq)

---

## Instance Methods

---

### __classForCoder__

`public Class classForCoder()`

Conformance with [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [classForCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwg3dbonzum33sinxwizls) in the interface specification for NSCoding.

---

### encodeWithCoder

`public void encodeWithCoder(NSCoder aNSCoder)`

Conformance with [NSCoding](NSCoding.md#apple-ineucskcizbeq). See the method description of [encodeWithCoder](NSCoding.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstinxwi2lom4xwk3tdn5sgkv3jorueg33emvza) in the interface specification for NSCoding.

---

### equals

`public boolean equals(Object anObject)`

Compares the receiving NSNotification object to _anObject_. If _anObject_ is an NSNotification and the contents of _anObject_ are equal to the contents of the receiver, this method returns true. If not, it returns false. Two notifications are equal if their names, objects, and dictionaries are equal.

__See Also:__ [name](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc63tbnvsq), [object](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc633cnjswg5a), [userInfo](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc65ltmvzes3tgn4)

---

### hashCode

`public int hashCode()`

Provide an appropriate hash code useful for storing the receiver in a hash-based data structure.

---

### name

`public String name()`

Returns the name of the notification. Examples of this might be "PortIsInvalid". Typically, you invoke this method on the notification object passed to your notification-handler method. (You specify a notification-handler method when you register to receive the notification.)

Notification names can be any string. To avoid name collisions, however, you might want to use a prefix that's specific to your application.

---

### object

`public Object object()`

Returns the object associated with the notification. This is often the object that posted this notification. It may be `null`.

Typically, you invoke this method on the notification object passed in to your notification-handler method. (You specify a notification-handler method when you register to receive the notification.)

---

### toString

`public String toString()`

Returns a string representation of the receiver including its name, object, and dictionary.

---

### userInfo

`public NSDictionary userInfo()`

Returns the NSDictionary associated with the notification. The NSDictionary stores any additional objects that objects receiving the notification might use. For example a PortIsInvalid notification may provide the port number in the dictionary. The NSDictionary is empty if no userInfo dictionary was specified when the notification was created.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
