---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSNotificationCenter.html
archived_at: '2026-07-15T08:13:56.342259Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSNotificationCenter

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSNotificationCenter object (or simply, notification center) is essentially a notification dispatch table. It notifies all observers of notifications meeting specific criteria. This information is encapsulated in [NSNotification](NSNotification.md#apple-ijduorkhjjauu) objects, also known as notifications. Client objects register themselves as observers of specific notifications posted by other objects. When an event occurs, an object posts an appropriate notification to the notification center. (See the [NSNotification](NSNotification.md#apple-ijduorkhjjauu) class specification for more on notifications.) The notification center dispatches a message to each registered observer, passing the notification as the sole argument. It is possible for the posting object and the observing object to be the same.

Each task has a default notification center that you access with the [defaultCenter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttporuwm2ldmf2gs33oinsw45dfoixwizlgmf2wy5cdmvxhizls) static method.

NSNotificationCenter is implemented using weak references (see Sun's documentation for java.lang.ref.\* for details). Thus, if the default NSNotificationCenter is the last object in your application with a reference to either an object registered to receive notifications or an object being observed, the object will be garbage collected.

## Registering to Receive Notifications

There are two ways to register to receive notifications.

If an object wishes to register itself to receive all notifications from all objects, it should send the [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3bmrse63lonfzwg2lfnz2e6yttmvzhmzls) method, specifying the message the notification should send.

Otherwise, an object registers itself to receive a notification by sending the [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3bmrse6yttmvzhmzls) method, specifying the message the notification should send, the name of the notification it wants to receive, and about which object. However, the observer need not specify both the name and the object. If it specifies only the object, it will receive all notifications containing that object. If the object specifies only a notification name, it will receive that notification every time it's posted, regardless of the object associated with it.

It is possible for an observer to register to receive more than one message for the same notification. In such a case, the observer will receive all messages it is registered to receive for the notification, but the order in which it receives them cannot be determined.

## Method Types

---

> **Constructors**
>
> : [NSNotificationCenter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel2oknhg65djmzuwgylunfxw4q3fnz2gk4q)
>
> **Accessing the default center**
>
> : [defaultCenter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5hfgttporuwm2ldmf2gs33oinsw45dfoixwizlgmf2wy5cdmvxhizls)
>
> **Adding and removing observers**
>
> : [addObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3bmrse6yttmvzhmzls): [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3bmrse63lonfzwg2lfnz2e6yttmvzhmzls): [removeObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3smvww65tfj5rhgzlsozsxe): [removeOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3smvww65tfj5ww42ltmnuwk3tuj5rhgzlsozsxe)
>
> **Posting notifications**
>
> : [postNotification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3qn5zxittporuwm2ldmf2gs33o)

## Constructors

---

### NSNotificationCenter

`protected NSNotificationCenter()`

Standard no-arg constructor. For use by subclasses only.

---

## Static Methods

---

### defaultCenter

`public static NSNotificationCenter defaultCenter()`

Returns the current task's notification center, which is used for system notifications.

---

## Instance Methods

---

### addObserver

`public synchronized void addObserver( Object anObserver, NSSelector aSelector, String notificationName, Object anObject)`

Registers _anObserver_ to receive notifications with the name _notificationName_ and/or containing _anObject_. When a notification of name _notificationName_ containing the object _anObject_ is posted, _anObserver_ receives an _aSelector_ message with this notification as the argument. The method for the selector specified in _aSelector_ must have one and only one argument. _anObject_ or _notificationName_ can be `null`, but not both:

|  |  |  |
| --- | --- | --- |
| __anObject__ | __notificationName__ | __Action__ |
| `null` | _notificationName_ | The notification center notifies the observer of all notifications with the name _notificationName_. |
| _anObject_ | `null` | The notification center notifies the observer of all notifications with an object matching _anObject_. |
| `null` | null | Do not invoke this method specifying `null` for both _notificationName_ and _anObject_. Instead, use [addOmniscientObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xegzloorsxel3bmrse63lonfzwg2lfnz2e6yttmvzhmzls). |

---

### __addOmniscientObserver__

`public synchronized void addOmniscientObserver( Object anObserver, NSSelector aSelector)`

Registers _anObserver_ to receive all notifications from all objects. When a notification is posted, _anObserver_ receives an _aSelector_ message with this notification as the argument. The method for the selector specified in _aSelector_ must have exactly one argument. Omniscient observers can significantly degrade performance and should be used with care.

---

### postNotification

`public void postNotification( String notificationName, Object anObject, NSDictionary userInfo)`

Creates a notification with the name _notificationName_, associates it with the object _anObject_ and dictionary _userInfo_, and posts it to the notification center.

This method is the preferred method for posting notifications. _anObject_ is typically the object posting the notification. It may be `null`. _userInfo_ also may be `null`.

`public void postNotification( String notificationName, Object anObject)`

Creates a notification with the name _notificationName_, associates it with the object _anObject_, and posts it to the notification center. _anObject_ is typically the object posting the notification. It may be `null`.

`public void postNotification(NSNotification notification)`

Posts _notification_ to the notification center. You can create _notification_ with the [NSNotification](NSNotification.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjzxxi2lgnfrwc5djn5xc6tstjzxxi2lgnfrwc5djn5xa) constructor.

---

### removeObserver

`public void removeObserver(Object anObserver)`

Same as `removeObserver(anObserver, null, null)`.

`public synchronized void removeObserver( Object anObserver, String notificationName, Object anObject)`

Removes _anObserver_ as the observer of notifications with the name _notificationName_ and object _anObject_ from the notification center. This method interprets `null` parameters as wildcards:

|  |  |
| --- | --- |
| __removeObserver Parameters__ | __Action__ |
| `null`, _notificationName_, _anObject_ | Removes all observers of _notificationName_ containing _anObject_. |
| _anObserver_, `null`, _anObject_ | Removes _anObserver_ as an observer of all notifications containing _anObject_. |
| _anObserver_, _notificationName_, `null` | Removes _anObserver_ as an observer of _notificationName_ containing any object. |
| _anObserver_, `null`, `null` | Removes all notifications containing _anObserver_. |
| `null`, _notificationName_, `null` | Removes all observers of _notificationName_. |
| `null`, `null`, _anObject_ | Removes all observers of _anObject_. |

Recall that the object a notification contains is usually the object that posted the notification.

---

### __removeOmniscientObserver__

`public synchronized void removeOmniscientObserver(Object anObserver)`

Unregisters _anObserver_ as an observer of all notifications.

---

### __toString__

`public String toString()`

Returns a String representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
