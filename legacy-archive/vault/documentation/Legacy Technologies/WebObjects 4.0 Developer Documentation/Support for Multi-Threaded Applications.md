---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/DeltaDoc/NewInEOF3.011.html
archived_at: '2026-07-15T07:57:54.847631Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in EOF 3.0](Table%20of%20Contents-2.md)

[!Table of Contents](Table%20of%20Contents-2.md) [!Previous Section](Raw%20Row%20Fetching.md)

# Support for Multi-Threaded Applications

Enterprise Objects Framework 3.0 provides thread-safe APIs. This means that you can now write a multi-threaded enterprise object application. (For information on multi-threading WebObjects applications, see "[What's New in WebObjects 4.0](What%27s%20New%20in%20WebObjects%204.0.md).")

The following operations are now thread-safe:

- The initial setup of the object graph in the editing context
- Making changes to the object graph in the editing context
- Database fetches
- Faulting
- Database saves

Enterprise Objects Framework 3.0 allows one thread to be active in each EOEditingContext and one thread to be active in each EODatabaseContext. In other words, multiple threads can access and modify objects concurrently in different editing contexts, but only one thread can access the database at a time (to save, fetch, or fault). Consequently, the support for multi-threaded applications can't be used to increase the level of database concurrency, but this wasn't the goal. Rather, the goal for 3.0 was to provide _thread safety_ for applications that perform other types of operations using multiple threads. To increase the level of database concurrency in your WebObjects applications, simply run multiple instances. This technique has been proven to scale very well.
The following tables describe the new API provided to support multi-threaded applications:

|  EOEditingContext (conformance to NSLocking) |  EOEditingContext (conformance to NSLocking) |
|  lock |  Locks access to the EOEditingContext to prevent other threads from accessing it. You should lock the editing context when you are making changes to the object graph, when you are fetching objects, and when you are saving objects. Only one thread is allowed per editing context tree. |
|  unlock |  Unlocks access to the EOEditingContext so that other threads may access it. |

```
```

|  EODatabaseContext (conformance to NSLocking) |  EODatabaseContext (conformance to NSLocking) |
|  lock |  Locks access to the EODatabaseContext to prevent other threads from accessing it. You typically don't have to invoke this method yourself. |
|  unlock |  Unlocks access to the EODatabaseContext. You typically don't have to invoke this method yourself. |

```
```

[!Table of Contents](Table%20of%20Contents-2.md) [!Next Section](Changes%20to%20Key-Value%20Coding.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
