---
title: 'Five approaches to listening, observing and notifying in Cocoa. | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/06/five-approaches-to-listening-observing.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:661f1581eb33e68f'
translated: false
---

> 原文：[Five approaches to listening, observing and notifying in Cocoa. | Cocoa with Love](https://www.cocoawithlove.com/2008/06/five-approaches-to-listening-observing.html)　·　Cocoa with Love (Matt Gallagher)

Here are five different ways to implement the Observer design pattern (sometimes called Broadcaster/Listener, Publish/Subscribe or Notifications) in Objective-C and some reasons why each approach can be valuable.

This post will cover:

- Manual broadcaster and listeners
- Key Value Observing
- Notification centers
- Context notifications
- Delegates used for observing

## About Observer

The [observer design pattern](http://en.wikipedia.org/wiki/Observer_pattern) is one of the most powerful ways of maintaining abstraction between two modules. The observer design pattern involves one module that declares an event that has occurred and any number of other modules which then choose to respond to this event. It differs from the first module directly invoking the methods of a second module because the first module doesn't need to care about how many observers it has, allowing more complete abstraction between the observee and its observers.

## Manual broadcaster and listeners

The manual approach is where the broadcaster maintains an NSArray or NSSet of listeners. When it is appropriate to notify the listeners of an event, the broadcaster invokes the relevant method directly on each listener.

You will need an NSMutableArray, NSSet or maybe an NSMutableDictionary on the broadcaster class. The latter is good if you want to "key" each of your listeners by some type of event identifier. You'll also need methods on the broadcaster so that listeners can register and unregister themselves.

Sending a message to every object in an NSArray or NSSet is as simple as:

```objc
[listenersCollection
    makeObjectsPerformSelector:@selector(methodSupportedByEveryListener)];
```

See [Collections Programming Topics for Cocoa](http://developer.apple.com/documentation/Cocoa/Conceptual/Collections/Collections.html) for more.

**Advantages**: the broadcaster has complete control over its list of listeners. **Disadvantages**: manual work to add and remove listeners from the collection (especially if it is not already maintained for a different reason). More manual work if different types of message need to be broadcast.

## Key Value Observing

The NSKeyValueObserving protocol goes a long way towards making the above process significantly automatic. In many cases, the broadcaster doesn't need to do anything.

Every object in Cocoa automatically handles addObserver:forKeyPath:options:context: which allows any object to be a broadcaster. If the "setter" methods on the broadcaster follow certain rules, the "setter" method will automatically trigger the observeValueForKeyPath:ofObject:change:context: method on any listener. For example:

```objc
[source
    addObserver:destination
    forKeyPath:@"myValue"
    options:NSKeyValueChangeNewKey
    context:nil];
```

will add an observer to the "source" object so that it will send an observeValueForKeyPath:ofObject:change:context: message to destination every time the setMyValue: method is invoked.

All you need to do is have every listener register themselves with the observee and have the listeners implement observeValueForKeyPath:ofObject:change:context:.

See [NSKeyValueObserving Protocol Reference](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Protocols/NSKeyValueObserving_Protocol/Reference/Reference.html) for more.

**Advantages**: built in and automatic. Observation can be of any key path. Supports dependent notifications. **Disadvantages**: not possible for the broadcaster to know who is listening. Methods must follow naming convention for automatic observation messages to work. Listeners must be removed as observers before they are deleted, otherwise subsequent notifications will result in crashing and failure — but this is true of all approaches listed in this post.

## Notification centers

NSNotificationCenter provides an approach which is further decoupled. The typical approach used with NSNotificationCenter is that any object can send a notification to the center. At the same time, any object could be listening for notifications on that center.

Sending a notification looks like this:

```objc
[[NSNotificationCenter defaultCenter]
    postNotificationName:@"myNotificationName"
    object:broadcasterObject];
```

and registering for receiving looks like this:

```objc
[[NSNotificationCenter defaultCenter]
    addObserver:listenerObject
    selector:@selector(receivingMethodOnListener:)
    name:@"myNotificationName"
    object:nil];
```

when registering for a notification, you can specify a specific broadcaster object but you don't have to do so. You may notice the defaultCenter. In reality, this is the only center you'll use. Notifications are intended to be open to the whole application, so there is only one center.

There is also an NSDistributedNotificationCenter. This is for communicating between applications. There is only one of these on the whole computer.

See [Notification Programming Topics for Cocoa](http://developer.apple.com/documentation/Cocoa/Conceptual/Notifications/Introduction/introNotifications.html) for more.

**Advantages**: neither the sender nor receiver of notifications needs to know about the other. Can specify the exact method to receive the notification. Notification name can be any string value. **Disadvantages**: slightly more code than Key Value Observing. You still need to remove listeners before they are deleted.

## Context notifications

In the case where the property being observed is a declared property of an NSManagedObject, it is possible to listen to  NSManagedObjectContextObjectsDidChangeNotification. Technically, this is still using the NSNotification approach but it is a slightly different approach because the NSManagedObject does not manually send the notifications.

Registering for this approach looks like this:

```objc
[[NSNotificationCenter defaultCenter]
    addObserver:listenerObejct
    selector:@selector(receivingMethodOnListener:)
    name:NSManagedObjectContextObjectsDidChangeNotification
    object:observedManagedObjectContext];
```

And then in receivingMethodOnListener:, the NSInsertedObjectsKey, NSUpdatedObjectsKey and NSDeletedObjectsKey keys in the notification's userInfo will give the sets of objects which have changed.

See [NSManagedObjectContext Class Reference](http://developer.apple.com/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/Reference/Reference.html) for more.

**Advantages**: easiest way to track changes across an entire NSManagedObjectContext. **Disadvantages**: only works for Core Data and does not provide information more specific than the affected object.

## Delegates used for observing

The final observer pattern Cocoa makes easy are delegates. In a broad sense delegates are intended to handle more than simply "observations" but they don't always need to do more.

For example, all of the notifications that NSApplication and NSWindow are also sent to their delegate and could be handled there instead. Some classes send notification-like message to their delegates that are never sent as notifications. For example NSMenu, sends menuWillOpen: to its delegate but does not send an equivalent NSNotification.

To connect a delegate, just invoke:

```objc
[object setDelegate:delegateObject];
```

on an object which supports a delegate. The delegateObject can then receive any of the delegate messages it wants.

See [Cocoa Fundamentals Guide: Delegates and Data Sources](http://developer.apple.com/documentation/Cocoa/Conceptual/CocoaFundamentals/CommunicatingWithObjects/chapter_6_section_4.html) for more.

**Advantages**: detailed and specific information from classes which support it. **Disadvantages**: the class must support a delegate. Only one delegate may be connected to an object at a time.
