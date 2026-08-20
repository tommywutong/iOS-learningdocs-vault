---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/AppConfs4.html
archived_at: '2026-07-15T08:02:48.516903Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Application%20Configurations.md) [!Previous Section](Editing%20Context%20Configurations.md)

# Object Store Coordinator Configurations

Recall that by default, all the EOEditingContexts in an application share the same EOObjectStoreCoordinator (see["Sharing Editing Contexts and Coordinators"](Graphical%20User%20Interface%20Applications.md#apple-gm4demy)). In this default configuration, all of a coordinator's editing contexts are synchronized with one another after any of the editing contexts save changes. Also, the editing contexts share underlying database connections wherever possible. This default behavior is typically what you want, but there are a some rare situations in which you might need more than one EOObjectStoreCoordinator.

All entity names must be unique within the scope of an EOObjectStoreCoordinator, so you need multiple coordinators when your application uses more than one connection to a database and each connection uses entities with the same name. For example, the following scenarios require multiple coordinators:

- An application that performs two types of tasks-regular user tasks and administrative tasks

The different types of tasks require different connections to the database. Regular user tasks go through a database connection that uses a regular user login while administrative tasks go through a database connection that uses a special administrative login. The two connections use different connection dictionaries, but otherwise use the same models. Consequently, the each connection uses the same entities.

- A WebObjects application that requires users to log in with their own login information

In this scenario, you'd set up a database connection for each user session. Here, too, the database connections use different connection dictionaries, but otherwise use the same models.

- An application that requires multiple, simultaneous transactions open on the same database

Because the transactions use the same model (and potentially the same connection information), they require their own connections to the database.

As shown in [Figure 44](#apple-gqydgnq), using an additional coordinator influences the number of database connections your application maintains.

!

Figure 44. Multiple EOObjectStoreCoordinators

The following sections describe how to create multiple coordinators. After you create an EOObjectStoreCoordinator, it takes care of setting up its underlying network of objects as described in the sections["Inside EOObjectStoreCoordinator"](Non-Graphical%20User%20Interface%20Applications.md#apple-gm4dqma)
and ["Inside EODatabaseContext"](Non-Graphical%20User%20Interface%20Applications.md#apple-gm4dsoi).

## Setting Up Multiple Coordinators Programmatically

If you are creating your EOEditingContexts programmatically, assigning unique EOObjectStoreCoordinators wherever necessary is straightforward. You simply:
In Java:

```
EOObjectStoreCoordinator coordinator =
    new EOObjectStoreCoordinator();
EOEditingContext ec = new EOEditingContext(coordinator);
```


In Objective-C:

```
EOObjectStoreCoordinator *coordinator =
    [[[EOObjectStoreCoordinator alloc] init] autorelease];
EOEditingContext *ec = [[EOEditingContext alloc]
    initWithParentObjectStore:coordinator];
```


## Setting Up Multiple Coordinators Using Nibs

If you are unarchiving your EOEditingContexts from nib files, you can specify a unique EOObjectStoreCoordinator using the EOEditingContext method __setDefaultParentObjectStore__ (__setDefaultParentObjectStore:__ in Objective-C) as follows:
In Java:

```
EOObjectStoreCoordinator coordinator =
    new EOObjectStoreCoordinator();
EOEditingContext.setDefaultParentObjectStore(coordinator
);
NSApplication.loadNibNamed("MyNib", this);
EOEditingContext.setDefaultParentObjectStore(null);
```


In Objective-C:

```
EOObjectStoreCoordinator *coordinator =
    [[[EOObjectStoreCoordinator alloc] init] autorelease];
[EOEditingContext
    setDefaultParentObjectStore:coordinator];
[NSApplication loadNibNamed:@"MyNib" owner:self];
[EOEditingContext setDefaultParentObjectStore:nil];
```


After setting the default object store coordinator, new editing contexts (such as the one being unarchived from the nib) use the new EOObjectStoreCoordinator. After loading the nib, set the default parent object store back to the default EOObjectStoreCoordinator by sending a __setDefaultParentObjectsStore__ message with __null__ (__nil__) as the argument.

[!Table of Contents](Application%20Configurations.md) [!Next Section](Accessing%20Multiple%20Databases.md)
