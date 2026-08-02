---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.38.html
archived_at: '2026-07-15T08:10:00.387482Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](When%20to%20Revert%20or%20Undo%20in%20an%20Editing%20Context.md) [!](Using%20Nested%20Editing%20Contexts.md)

#   Setting the Delegates of Database Contexts and Adaptor Contexts

##  Synopsis

Describes how to set the delegates for EODatabaseContexts, EOAdaptorContexts, and their channels.

##  Discussion

The delegates for EODatabaseContexts, EOAdaptorContexts, and their channels receive messages that, if they properly implement the corresponding methods, enable them to generate custom primary keys, fine-tune the behavior of batch faulting, satisfy a fetch request from a local cache, and accomplish a variety of other tasks (see the reference documentation for
EODatabaseContext.DelegateDelegation
). Because EODatabaseContexts, EODatabaseChannels, and related objects are created dynamically, it's a little tricky to set their delegates. The mechanism that you use to set delegates for these objects is notification.

When an EOCooperatingObjectStore is added to the EOObjectStoreCoordinator, the coordinator posts an
EOCooperatingObjectStoreWasAdded
notification. Since EODatabaseContexts are subclasses of EOCooperatingObjectStore, this notification is posted whenever a database context is created and added to the coordinator. To catch this notification, just set up an observing object that listens for the
EOCooperatingObjectStoreWasAdded
notification.

Whenever the designated method of the observing object is invoked via notification, the coordinator is passed in as the notification object. Given the coordinator, you can traverse all the cooperating object stores and set delegates for them.

When you set the delegate of an EODatabaseContext object, that delegate object is propagated to all of the EODatabaseContext's EODatabaseChannels. An EOAdaptorChannel is always created along with the creation of an EODatabaseChannel and an EOAdaptorContext is always created along with creation of an EODatabaseContext; the EODatabaseContext and EODatabaseChannel always keep a reference to these adaptor objects. Through these relationships, a delegate can access EOAdaptorContexts and EOAdaptorChannels from its EODatabaseContext or EODatabaseChannel.

The following code shows how to register for
EOCooperatingObjectStoreWasAdded
notifications in the Session constructor, and then how to set the delegate for each EODatabaseContext. (EOCooperatingObjectStores).

####  Java Code

```

public Session() {
    super();
    try {
        // Create a selector that can be used to define         // a callback to our addedObjectStore method
        Class params[]={Class.forName("com.apple.yellow.foundation.NSNotification")};
        Selector selector=new NSSelector("addedObjectStore", params);

        // Register as a CooperatingObjectStoreWasAdded         // observer with our callback
        NSNotificationCenter.defaultCenter().addObserver(this,selector,            EOObjectStoreCoordinator.CooperatingObjectStoreWasAdded, null);
    }
    catch(Exception e) {
        logString(e.toString());
    }
}
public void addedObjectStore(NSNotification notification)
{
    EOObjectStoreCoordinator coordinator=        (EOObjectStoreCoordinator) notification.object();
    NSArray stores=coordinator.cooperatingObjectStores();
    NSEnumerator anEnum=(NSEnumerator) stores.objectEnumerator();
       // make sure all of our stores have our this object as its delegate.
    while (anEnum.hasMoreElements()) {

        EODatabaseContext store=(EODatabaseContext) anEnum.nextElement();
        store.setDelegate(this);
        logString("Setting delegate of "+store);
    }
}
```

####  Objective-C Code

```objc

- init {
    self = [super init];
    [[NSNotificationCenter defaultCenter] addObserver: self         selector:@selector(addedObjectStore:)         name:EOCooperatingObjectStoreWasAdded object:nil];
    return self;
}
- (void) addedObjectStore: (NSNotification *)notification
{
    EOObjectStoreCoordinator *coordinator=[notification object];
    NSArray *stores=[coordinator cooperatingObjectStores];
   // make sure all of our stores have our this object as its delegate.
    [stores makeObjectsPerformSelector: @selector(setDelegate:)         withObject: self];
}
```


##  See Also

- 

  EODatabaseContext class specification in the _Enterprise Objects Framework Reference_
- 

  EOAdaptorContext class specification in the _Enterprise Objects Framework Reference_
- 

  EOObjectStoreCoordinator class specification in the _Enterprise Objects Framework Reference_
- 

  EOCooperatingObjectStore class specification in the _Enterprise Objects Framework Reference_
- 

  NSNotificationCenter class specification in the _Foundation Framework Reference_
- 

  NSNotification class specification in the _Foundation Framework Reference_

##  Questions

- 

  How do I dynamically set the delegate for an EODatabaseContext, an EOAdaptorContext, or their related channels?

##  Keywords

- 

  Delegate
- 

  Notification
- 

  Adaptor
- 

  Database
- 

  Context
- 

  Channel

##  Revision History

23 July, 1998. David Scheck. First Draft.

17 November, 1998. Terry Donoghue. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](When%20to%20Revert%20or%20Undo%20in%20an%20Editing%20Context.md) [!](Using%20Nested%20Editing%20Contexts.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
