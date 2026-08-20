---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/StoreCompTable.html
archived_at: '2026-07-15T07:47:54.901090Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](StorageStratsIntro.md)

# Comparison of Storage Options

These options are discussed in more detail in later sections, but seeing an overall comparison might save you time in deciding which options to explore.

Table 1: __Comparing Storage Schemes__

| feature | State in server | State in page | State in cookies | Custom storage |
| --- | --- | --- | --- | --- |
| __Simplicity__ | Simplest approach; WebObject's default. | Relatively simple, but can involve design changes to application. | Relatively simple. | More complex. |
| __Security__ | Secure since state is on server and accessed by encrypted session IDs. | Since data is passed to client, opens possibility that data could be modified by user. | Since data is passed to client, opens possibility that data could be modified by user. | If stored on server, can be as secure or more secure than state-in-server. |
| __Scalability__ | Can consume lots of memory. Also, can't use round-robin request handling once state is established in a particular application instance. | More scalable since any application instance can handle a request (because state is bundled with each request). Applications don't grow when new sessions are added. | Not very scalable. Cookie specification limits capacity to 4K bytes per cookie, but some browsers have further limitations. | Depends on design of storage. If filesystem or database used for storage, can scale to accommodate almost any need. |
| __Reliability__ | Least reliable since if the server crashes, state is lost. | More reliable since a server crash doesn't affect state stored on client. | More reliable since a server crash doesn't affect state stored on client. | Can be extremely reliable if state is stored in server file system or database. |
| __Other__ |  | Performance can suffer if lots of data is passed back and forth between client and server. State can become out of sync, especially when using frames. | Client can refuse to accept cookies. |  |

If you know you want to use WebObjects' default server-side storage mechanism, read the "[State in the Server](StateInServer.md)" section below and then you can skip to "[Controlling Session State](ControllingSessionState.md)" for information about managing the memory requirements of your application. If you want to examine the other storage options in more detail, continue with "[A Closer Look at Storage Strategies](CloserLookAtStrats.md)".

[!Table of Contents](ManagingState.book.md)
[!Next Section](CloserLookAtStrats.md)
