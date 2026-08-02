---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/Guide/AppConfs2.html
archived_at: '2026-07-18T01:19:14.117853Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Developer's Guide](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

[!Table of Contents](Application%20Configurations.md) [!Previous Section](Graphical%20User%20Interface%20Applications.md)

# Non-Graphical User Interface Applications

Command line tools, background processes, and other non-graphical user interface applications have a very similar configuration to that of applications with an interface. However, they don't use display groups, and they typically don't use EODatabaseDataSources either.

!

Figure 37. Typical Configuration of a Non-Graphical-User-Interface Application

In an application that doesn't have a graphical user interface, your code must initiate the creation of the network of the behind-the-scenes objects. This creation process is typically begun when you allocate and initialize an EOEditingContext.

## Creating an Editing Context

You create an EOEditingContext the same way you'd create any other object:
In Java:

```
EOEditingContext editingContext = new EOEditingContext();
```


In Objective-C:

```
EOEditingContext *editingContext =
        [[EOEditingContext alloc] init];
```


Both of the examples above create a new editing context and connect it to an EOObjectStoreCoordinator. By default, the editing context is connected to the default object store coordinator as determined by EOObjectStoreCoordinator's __defaultCoordinator__ static method (class method in Objective-C).

!

Figure 38. Allocating and Initializing an EOEditingContext

The first time __defaultCoordinator__ is invoked, it creates an EOObjectStoreCoordinator. Subsequent invocations return the same instance. Consequently, all the editing contexts in an application are connected to EODatabaseContext objects through the same EOObjectStoreCoordinator by default.
The remaining objects in the network are created on demand. When a database operation is initiated with a message to an editing context, the request is passed on to its object store coordinator. In the case of a nested editing context configuration, the message is passed down the object network until reaches the editing context's root object store-usually an EOObjectStoreCoordinator.
For example, an __objectsWithFetchSpecification__ message sent to an EOEditingContext percolates through its parent object stores until it reaches the coordinator as shown in [Figure 39](#apple-gm4dona).

!

Figure 39. How Messages Percolate Down to an EOObjectStoreCoordinator

## Inside EOObjectStoreCoordinator

When an EOObjectStoreCoordinator receives a message requiring interaction with the database, it attempts to locate an EOCooperatingObjectStore-usually an EODatabaseContext-that can handle the request. The coordinator generally builds its list of cooperating stores on demand as follows:

- When a coordinator needs to forward a request to a database, it checks to see if it has an cooperating stores in its list that can handle the interaction. If it finds one, it uses it.
- If the coordinator does not have a cooperating store to handle the interaction (either because none of its cooperating stores can handle this specific database request or because the coordinator doesn't have any cooperating stores), it posts a CooperatingObjectStoreNeeded notification (EOCooperatingObjectStoreNeeded in Objective-C) so that another object can register a new cooperating store. After posting the notification, the coordinator checks its list of cooperating stores a second time. If it finds an available store (because an object registered a new one in response to the notification), it uses the newly registered store.

In a typical Enterprise Objects Framework application, an EOObjectStoreCoordinator's cooperating stores are EODatabaseContexts. The EODatabaseContext class registers for the CooperatingObjectStoreNeeded notification, and provides the coordinator with a new database context that can accommodate the request. Consequently, you don't have to provide cooperating stores to a coordinator yourself unless you're using a subclass of EOCooperatingObjectStore that isn't an EODatabaseContext.

- Once the coordinator has a cooperating store to use, it forwards the request to the store.

__Note:__  In the case of an application with a graphical user interface, an EODatabaseDataSource generally forces a connection to an EOCooperatingObjectStore when it's unarchived from a nib or component. Thus, the EOObjectStoreCoordinator may never post a CooperatingObjectStoreNeeded notification.

## Inside EODatabaseContext

An EODatabaseContext performs a database operation using an EODatabaseChannel. When a database context receives a message that requires database interaction (such as __objectsWithFetchSpecification__), it attempts to obtain a channel to perform the corresponding database operation as follows:

- If the database context has a registered channel that isn't busy (that is, a channel that doesn't have a fetch in progress), it uses the available channel.
- If the EODatabaseContext doesn't have an available channel (either because all the channels are busy or because the context doesn't have any channels), it posts a DatabaseChannelNeededNotification (EODatabaseChannelNeededNotification in Objective-C) so that another object can register a new channel. After posting the notification, the context checks its list of registered channels a second time. If it finds an available channel (because an object registered a new channel), it uses the newly registered channel.
- If the database context doesn't have any registered channels after posting a DatabaseChannelNeededNotification, it creates one, puts it in its list of registered channels, and uses the new channel to perform the database operation.

__Note:__  By default, an EODatabaseContext has one EODatabaseChannel, but you can register additional channels programmatically. For more information, see the chapter["Connecting to a Database"](Connecting%20to%20a%20Database.md#apple-gyztomi).

## Substituting a Custom EOCooperatingObjectStore

There are two approaches to providing a custom EOCooperatingObjectStore to an EOObjectStoreCoordinator:

- Tell EODatabaseContext what class to register.

If the EOCooperatingObjectStore is a subclass of EODatabaseContext, you can simply tell EODatabaseContext to register instances of the subclass instead of EODatabaseContext instances. Use the EODatabaseContext static method __setContextClassToRegister__ (__setContextClassToRegister:__ class method in Objective-C) to specify your subclass.

- Register the custom EOCooperatingObjectStore yourself.

To register your own cooperating store, add yourself as an observer of CooperatingObjectStoreNeeded notifications. When you receive a notification, create an instance of your custom store and use the EOObjectStoreCoordinator method __addCooperatingObjectStore__ (__addCooperatingObjectStore:__ in Objective-C) to register your cooperating store with the coordinator. To prevent EODatabaseContext from registering competing object stores, invoke the EODatabaseContext static method __setContextClassToRegister__ with __null__ (__nil__ in Objective-C) as the argument.

For more information, see the EODatabaseContext class specification in the _Enterprise Objects Framework Reference_.

[!Table of Contents](Application%20Configurations.md) [!Next Section](Editing%20Context%20Configurations.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
