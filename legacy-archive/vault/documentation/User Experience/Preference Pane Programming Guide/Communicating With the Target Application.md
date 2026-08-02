---
title: Preference Pane Programming Guide
apple_id: 10000110i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PreferencePanes/Tasks/Communication.html
archived_at: '2026-07-18T02:12:29.478075Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preference Pane Programming Guide](Introduction.md)


[Next](Implementing%20a%20Preference%20Pane%20Help%20Menu.md)[Previous](Using%20Preference%20Services.md)

# Communicating With the Target Application

In some situations you need to communicate directly with the target application rather than rely solely on the preference file. This section describes how to use two methods—distributed objects and distributed notifications—to achieve this.

Distributed objects allow one application to communicate with an object in another application. You can use distributed objects only in Cocoa applications.

The application that owns the object, the target application in this case, makes the object available to other applications by vending the object with code such as

```
id serverObject; // Assume this exists.
NSConnection *theConnection;

theConnection = [NSConnection defaultConnection];
[theConnection setRootObject:serverObject];
[theConnection registerName:@“MyServer”];
```

where `serverObject` is an object that defines a set of methods for external use. These methods can provide low-level “get” and “set” accessors for the application settings or higher-level queries and requests. To gain access to the object, another application, such as your preference pane, executes code such as

```
NSConnection *theConnection;
id remoteObject;

theConnection = [NSConnection connectionWithRegisteredName:@“MyServer”
            host:nil];
remoteObject = [[theConnection rootProxy] retain];
```

where `remoteObject` is now a proxy object representing the vended object. Interaction with the object occurs normally:

```
x = [remoteObject defaultWidth];
[remoteObject setBackgroundColor:[NSColor redColor]];
```


Distributed notifications allow an application to broadcast a message to any number of other applications without needing to know who those other applications are, or even if the other applications exist. Every application type—Cocoa, Carbon, BSD—can use distributed notifications.

An application, the target application in this case, expresses an interest in receiving a broadcasted message by registering itself with the system’s distributed notification center, identifying exactly what message, or notification type, it wants to receive. The notification type is defined by an arbitrary string agreed upon by the sender and receiver of the notification. As an example, Cocoa’s NSWindow class defines the notification type [NSWindowWillCloseNotification](https://developer.apple.com/documentation/appkit/nswindowwillclosenotification), which a window object broadcasts when its window closes. Any other object can register to receive this notification. (This notification, however, is internal to a single application and is not distributed to the rest of the system.)

In addition to the message, the application can identify the particular object sending the message. When the sender and receiver are in the same application—in other words, using nondistributed notifications—the observed object can be anything. When using distributed notifications, though, the object must be a string (CFString or NSString). A useful choice for the observed string is the bundle identifier of the target application.

In registering for the notification, the application provides a callback to be executed when it receives the notification. The application then proceeds with its duties. To receive the notification, the application must enter a Core Foundation run loop. This occurs for both the Cocoa run loop and Carbon event manager.

To register to receive a notification, a Cocoa application executes code such as the following:

```
NSString *observedObject = @“com.mycompany.example.PrefpaneTarget”;
NSDistributedNotificationCenter *center =
            [NSDistributedNotificationCenter defaultCenter];
[center addObserver: self
            selector: @selector(callbackWithNotification:)
            name: @“My Notification”
            object: observedObject];
```

The observer argument is the object on which the callback method is invoked. The callback method, identified by the `selector` argument and implemented by the observer object, has a signature of

```objc
- (void)callbackWithNotification:(NSNotification *)myNotification;
```

The NSNotification object passed to this method contains the specific object and notification message received.

The analogous code for a Carbon or BSD application using Core Foundation is

```
void *observer;
CFStringRef observedObject =
            CFSTR(“com.mycompany.example.PrefpaneTarget”);
CFNotificationCenterRef center =
            CFNotificationCenterGetDistributedCenter();
CFNotificationCenterAddObserver(center, observer, myCallbackFntn,
            CFSTR(“My Notification”), observedObject,
            CFNotificationSuspensionBehaviorDeliverImmediately);
```

with a callback function prototype of

```
(void)myCallbackFntn(CFNotificationCenterRef center, void *observer,
            CFStringRef notificationName, const void *observedObject,
            CFDictionaryRef userInfo);
```

Because the callback is a function instead of a method invocation, the `observer` argument is any additional data (in the form of a pointer) that you want to pass to the callback function.

Next, the broadcasting application—your preference pane—sends the notification. It calls the system’s notification center, tells the center what notification to send, and optionally passes a dictionary containing additional information. The dictionary can be used to pass the modified preferences directly to the application. Or, the preference pane can choose not to use the dictionary and instead write the changes out to disk. The notification is then used to tell the application to update its preferences from the disk.

Cocoa code to send the notification looks like this:

```
NSString *observedObject = @“com.mycompany.example.PrefpaneTarget”;
NSDistributedNotificationCenter *center =
            [NSDistributedNotificationCenter defaultCenter];
[center postNotificationName: @“My Notification”
            object: observedObject
            userInfo: nil /* no dictionary */
            deliverImmediately: YES];
```

The Core Foundation code looks like this:

```
CFStringRef observedObject =
            CFSTR(“com.mycompany.example.PrefpaneTarget”);
CFNotificationCenterRef center =
            CFNotificationCenterGetDistributedCenter();
CFNotificationCenterPostNotification(center, CFSTR(“My Notification”),
            observedObject, NULL /* no dictionary */, TRUE);
```

The notification center looks up all the applications that registered to receive the given notification type from the particular `observedObject`. It then notifies each application’s run loop of the notification and gives it a copy of the dictionary. The selected callback function or method is executed during the application’s next pass through its run loop.

When using Preference Services, be certain to flush changes to the disk with the appropriate synchronize functions before sending notifications of changes. Otherwise, due to the caching performed by Preference Services, the disk may not accurately reflect the changes when the target receives the notification. Likewise, the target application must resynchronize its preferences after receiving the notification.

[Next](Implementing%20a%20Preference%20Pane%20Help%20Menu.md)[Previous](Using%20Preference%20Services.md)

