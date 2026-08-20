---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/StoreCompTable.html
archived_at: '2026-07-15T07:52:23.319706Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](StorageStratsIntro.md)

## Comparison of Storage Options

The following table summarizes the pros and cons of each of the state storage options. These options are discussed in more detail in the next section, "[A Closer Look at Storage Strategies](CloserLookAtStrats.md#apple-guytkma)," but seeing an overall comparison might save you time in deciding which options to explore.

|  |  State in Server |  State in Page |  State in Cookies |  Custom Storage |
|  Simplicity |  Simplest approach; WebObject's default. |  Relatively simple, but can involve design changes to application. |  Relatively simple. |  More complex. |
|  Security |  Secure since state is on server and accessed by encrypted session IDs. |  Since data is passed to client, opens possibility that data could be modified by user. |  Since data is passed to client, opens possibility that data could be modified by user. |  If stored on server, can be as secure or more secure than state-in-server. |
|  Scalability |  Can consume lots of memory. Also, can't use load balancing once state is established in a particular application instance. |  More scalable since any application instance can handle a request (because state is bundled with each request). Applications don't grow when new sessions are added. |  Not very scalable. Cookie specification limits capacity to 4K bytes per cookie, but some browsers have further limitations. |  Depends on design of storage. If file system or database used for storage, can scale to accommodate almost any need. |
|  Reliability |  Least reliable, since if the server crashes, state is lost. |  More reliable, since a server crash doesn't affect state stored on client. |  More reliable, since a server crash doesn't affect state stored on client. |  Can be extremely reliable if state is stored in server file system or database. |
|  Other |  |  Performance can suffer  if lots of data is passed back and forth between client and server. State can become out of sync, especially when using frames. |  Client can refuse to accept cookies. |  |

```
```

[!Table of Contents](StateTOC.md) [!Next Section](CloserLookAtStrats.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
