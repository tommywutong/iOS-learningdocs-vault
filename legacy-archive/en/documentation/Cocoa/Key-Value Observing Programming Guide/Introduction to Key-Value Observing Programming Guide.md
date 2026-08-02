---
title: Key-Value Observing Programming Guide
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html
archived_at: '2026-07-15T07:16:19.102348Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Registering%20for%20Key-Value%20Observing.md)

# Introduction to Key-Value Observing Programming Guide

Key-value observing is a mechanism that allows objects to be notified of changes to specified properties of other objects.

Key-value observing provides a mechanism that allows objects to be notified of changes to specific properties of other objects. It is particularly useful for communication between [model and controller layers](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MVC.html#//apple_ref/doc/uid/TP40008195-CH32) in an application. (In OS X, the [controller layer](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) binding technology relies heavily on key-value observing.) A [controller object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) typically observes properties of model objects, and a view object observes properties of model objects through a controller. In addition, however, a model object may observe other model objects (usually to determine when a dependent value changes) or even itself (again to determine when a dependent value changes).

You can observe properties including simple attributes, to-one relationships, and to-many relationships. Observers of to-many relationships are informed of the type of change made—as well as which objects are involved in the change.

A simple example illustrates how KVO can be useful in your application. Suppose a `Person` object interacts with an `Account` object, representing the person’s savings account at a bank. An instance of `Person` may need to be aware of when certain aspects of the `Account` instance change, such as the balance, or the interest rate.

![Art/kvo_objects_properties.png](attachments/Art/kvo_objects_properties.png)

If these attributes are public properties of `Account`, the `Person` could periodically poll the `Account` to discover changes, but this is of course inefficient, and often impractical. A better approach is to use KVO, which is akin to `Person` receiving an interrupt when a change occurs.

To use KVO, first you must ensure that the observed object, the `Account` in this case, is KVO compliant. Typically, if your objects inherit from `NSObject` and you create properties in the usual way, your objects and their properties will automatically be KVO Compliant. It is also possible to implement compliance manually. [KVO Compliance](KVO%20Compliance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tqlkciffekqkjivcq) describes the difference between automatic and manual key-value observing, and how to implement both.

Next, you must register your observer instance, the `Person`, with the observed instance, the `Account`. `Person` sends an [addObserver:forKeyPath:options:context:](https://developer.apple.com/documentation/objectivec/nsobject/1412787-addobserver) message to the `Account`, once for each observed key path, naming itself as the observer.

![Art/kvo_objects_add.png](attachments/Art/kvo_objects_add.png)

In order to receive change notifications from the `Account`, `Person` implements the [observeValueForKeyPath:ofObject:change:context:](https://developer.apple.com/documentation/objectivec/nsobject/1416553-observevalueforkeypath) method, required of all observers. The `Account` will send this message to the `Person` any time one of the registered key paths changes. The `Person` can then take appropriate action based upon the change notification.

![Art/kvo_objects_observe.png](attachments/Art/kvo_objects_observe.png)

Finally, when it no longer wants notifications, and at the very least before it is deallocated, the `Person` instance must de-register by sending the message [removeObserver:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1408054-removeobserver) to the `Account`.

![Art/kvo_objects_remove.png](attachments/Art/kvo_objects_remove.png)

[Registering for Key-Value Observing](Registering%20for%20Key-Value%20Observing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2telkciffekqkjivcq) describes the full lifecycle of registering for, receiving, and de-registering for key value observation notifications.

KVO’s primary benefit is that you don’t have to implement your own scheme to send notifications every time a property changes. Its well-defined infrastructure has framework-level support that makes it easy to adopt—typically you do not have to add any code to your project. In addition, the infrastructure is already full-featured, which makes it easy to support multiple observers for a single property, as well as dependent values.

[Registering Dependent Keys](Registering%20Dependent%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tslkciffekqkjivcq) explains how to specify that the value of a key is dependent on the value of another key.

Unlike notifications that use [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter), there is no central object that provides change notification for all observers. Instead, notifications are sent directly to the observing objects when changes are made. `NSObject` provides this base implementation of key-value observing, and you should rarely need to [override](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) these methods.

[Key-Value Observing Implementation Details](Key-Value%20Observing%20Implementation%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydolkciffekqkjivcq) describes how key-value observing is implemented.

[Next](Registering%20for%20Key-Value%20Observing.md)

