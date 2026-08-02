---
title: Server Notification Center Programming Guide
apple_id: TP40008593
resource_type: Guide
platform: macOS
topic: System Administration
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/NSServerNotificationCenterProgrammingGuide/RequestingDistributedNotificationsWithNSServerNotificationCenter/RequestingDistributedNotificationsWithNSServerNotificationCenter.html
archived_at: '2026-07-15T08:18:24.999487Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Server Notification Center Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

# ServerNotificationCenter Distributed Notifications

The `ServerNotificationCenter` framework provides an API for receiving distributed notifications. This service allows application developers to register with a server and subsequently receive notices from that server whenever something changes. It also allows developers to post notifications to a server for other users to receive.

`ServerNotificationCenter` is built on top of the Extensible Messaging and Presence Protocol (XMPP), which is also the foundation of other protocols such as Jabber.

At a high level, XMPP provides a means for servers to communicate with one another, allowing a user associated with one server to receive notifications posted by a different server.

To use these notifications, the user must have an account on a server that supports XMPP, henceforth referred to as the user’s notification server. (This is generally the user’s Mobile Me account.) When an application subscribes to notifications from a remote server, it does so by telling the user’s notification server that it wants to subscribe. The user’s notification server then informs the remote server.

Using a server as a notification proxy provides four benefits:

- Firewalls cause fewer problems (and particularly firewalls that do network address translation). The remote server need not be able to reach the user’s machine directly.
- Dynamic IP numbers are no problem. There is no need to reregister with thousands of servers when your IP number changes. The client merely needs to reconnect to the notification server.
- The notification server can queue up messages while a user is offline.
- Notification messages can be coalesced. If more than one user of a given notification server subscribes to the same notification, the remote server can deliver that notification to those users with a single message instead of sending out one per client.

Before you can use server notifications, first configure the notification daemon on your computer.

First, if your server supports SSL authentication, enable SSL for that server by issuing this command:

```
notificationconf usessl hostname
```

Substitute the actual hostname in place of _hostname_.

Next, provide the notification daemon with login credentials for the server. To do this, enter the following command:

```
notificationconf setpass hostname username
```

The `notificationconf` command prompts you for the password that corresponds with the specified username, then stores a username/password pair in your keychain for future use.

Finally, create a node on the server for each notification you intend to send and receive. To do this, issue the following command:

```
notificationconf createnode hostname nodename username
```


Before you subscribe to notifications, first create an object (of your choosing) that contains an instance method to call when a notification is received. That method should take a single parameter that is a pointer to an `NSNotification` object.

For example:

```objc
@interface TestObj : NSObject {}
@end

@implementation TestObj
- (void) notificationReceived:(NSNotification *)notification
{
    NSServerNotificationCenter *center = [notification object];
    NSString *serviceJID = [center serviceHost];
    NSLog(@"Notification received on service %@: %@", serviceJID, notification);

    NSDictionary *myDictionary = [notification userInfo];
}
@end
```

If you are familiar with the `NSNotification` API, you should notice one key difference: the sending object is always the server notification center object itself rather than an object passed to the `postNotification` method.

Next, subscribe to the notification. You do this by first calling one of the `centerForService` methods to obtain a notification center specific to a given hostname. Then, you call one of the `addObserver` methods to begin receiving a particular notification.

For example:

```
/* Create some data objects and an object that will receive the notifications. */
NSString* notificationName = @"MyNotificationName";
NSString* hostName = @"notificationhost.example.org";
TestObj *MyObject = [[TestObj alloc] init];

/* Create the notification center */
NSServerNotificationCenter* center = [NSServerNotificationCenter centerForService:hostName];

/* Subscribe to a notification */
[center addObserver:MyObject selector:@selector(notificationReceived:) name:notificationName object:nil];
```


Posting server notifications is similar to posting local notifications using `NSNotificationCenter` with one exception: you pass `nil` as the source object to any method that takes such a parameter. The reasons for this are twofold. First, specific objects have no meaning on another machine. Second, the API overloads the `object` accessor of `NSNotification` to store a pointer to the corresponding `NSServerNotificationCenter` object itself. This allows you to easily determine the source hostname, notification name, and so on.

Before you post notifications, first create a notification center object.

```
/* Create some data objects. */
NSString* notificationName = @"MyNotificationName";
NSString* hostName = @"notificationhost.example.org";
NSDictionary* myDictionary = <# userInfo Dictionary #>

/* Create the notification center */
NSServerNotificationCenter* center = [NSServerNotificationCenter centerForService:hostName];
```

Once you have created a notification center object, you can post a notification like this:

```
/* Post a notification */
[center postNotificationName:notificationName object:nil userInfo:myDictionary];
```

[Next](Document%20Revision%20History.md)[Previous](Introduction.md)

