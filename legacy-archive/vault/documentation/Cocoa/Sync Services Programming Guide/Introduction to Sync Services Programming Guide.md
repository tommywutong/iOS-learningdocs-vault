---
title: Sync Services Programming Guide
apple_id: TP40001178
resource_type: Guide
platform: macOS
topic: Data Management
technology: SyncServices
published: '2011-07-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SyncServices/SyncServices.html
archived_at: '2026-07-15T07:19:49.366711Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Why%20Use%20Sync%20Services.md)

# Introduction to Sync Services Programming Guide

Sync Services is a framework containing all the components you need to sync your applications and devices. If your application uses Sync Services, user data can be synced with other applications and devices on the same computer, or other computers over the network via MobileMe. Ideally, all Mac OS X applications should sync user data quickly and quietly in the background. Consequently, user data is available when and where the user wants it.

You should read this document if you want to sync your application’s data. Types of applications include end-user applications, tools, or servers. For example, a tool may be an interface to a device (such as a phone) or a framework that maintains persistent data. You can use existing schemas for contacts, calendars, and bookmarks. You can also extend a schema or create your own schema to sync custom objects. You can use the Sync Services API from both Objective-C and C programs.

Before using Sync Services you should understand what it is used for, what the system architecture is, and what the core classes are. Because sync sessions are implemented as finite state machines, you also need an in-depth understanding of the states and transactions within a sync session regardless of which approach you choose. The consequences of syncing incorrectly are severe—users may lose their data—so read the following conceptual articles before using this framework. In particular, you need to read [Managing Your Sync Session](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfvbuuqsfjbaucry) if you are writing your own sync methods.

- [Why Use Sync Services?](Why%20Use%20Sync%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjqfvbuuqsfjjbeqsa) explains why syncing is an important feature to end users and may become commonplace on Mac OS X.
- [Sync Services Overview](Sync%20Services%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjrfvbuuqsfjbaucry) describes the components of the sync architecture and defines syncing terms such as those used for the different sync modes.
- [Managing Your Sync Session](Managing%20Your%20Sync%20Session.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnrsfvbuuqsfjbaucry) describes the anatomy of an `ISyncSession` object. It contains details about each state in the finite state machine and the methods that can be used in each state.

A simple approach to syncing is to use a delegation model where a driver sends messages to a data source and delegate while syncing. You can also use Core Data as the persistent store for local records and to create your schema. Read the following articles to learn more about these approaches:

- [Using a Session Driver](Using%20a%20Session%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztmmbqfvjvona) describes how to use an `ISyncSessionDriver` object to control a sync session.

- [Syncing Core Data Applications](Syncing%20Core%20Data%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzsfvjvomi) describes how to create a Core Data application that syncs managed objects.

If you need more control, read the following articles that cover the low-level classes and methods you use to manage sync sessions:

- [Creating a Sync Schema](Creating%20a%20Sync%20Schema.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjtfvbuuqsfjbaucry) describes how to create your own custom schemas and contains a description of the sync schema property list.
- [Registering Schemas](Registering%20Schemas.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjufvbuuqsfjbaucry) describes how to register and unregister schemas.
- [Registering Clients](Registering%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjvfvbuuqsfjbaucry) describes how to register and unregister clients, as well as provides a description of the client description property list.
- [Syncing Relationships](Syncing%20Relationships.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjxfvbuuqsfjbaucry) describes how to add relationships to your object model and schema. It also contains tips on pushing and pulling relationships.
- [Syncing with Other Clients](Syncing%20with%20Other%20Clients.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjzfvbecssfifeukri) describes how to configure your client to sync with other clients.
- [Using Sync Anchors](Using%20Sync%20Anchors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2temzrfvjvomi) describes how to use sync anchors to improve performance and reliability.
- [Filtering Records](Filtering%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjyfvbecssfifeukri) describes how to filter the types of records your application syncs.
- [Formatting Records](Formatting%20Records.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytcnjsfvbuuqsfjjbeqsa) describes how to change the format of a record without the sync engine interpreting the change as a change to the property values.

Read this article if you want to exclude your application preferences from syncing:

- [Syncing Preferences](Syncing%20Preferences.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzufvjvomq) describes how to exclude selected preferences or all preferences of an application from syncing when the user turns this feature on.

For an in-depth description of the Sync Services API, read:

- _Sync Services Framework Reference_

If you are using or extending an Apple Applications schema, such as contacts, bookmarks or calendars, read:

- _Apple Applications Schema Reference_

If you are accessing Sync Services from a C application, refer to the _[SeeMyFriends](../../../samplecode/SeeMyFriends/SeeMyFriends.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrygm)_ sample code and this document for more information about mixing C and Objective-C:

- _[Carbon-Cocoa Integration Guide](../Carbon-Cocoa%20Integration%20Guide/Introduction%20to%20Carbon-Cocoa%20Integration%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydqojt)_
[Next](Why%20Use%20Sync%20Services.md)

