---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/ProcessingConcurrentRequests/ProcessingConcurrentRequests.html
archived_at: '2026-07-27T06:57:05.783239Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Open%20Directory%20Callbacks.md)[Previous](Processing%20Open%20Directory%20Requests.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Processing Concurrent Requests

Open Directory is multi-threaded, so plug-ins must be thread-safe. Plug-ins may be called multiple times by multiple applications. For example, the following requests may occur at the same time:

- Application A makes a request that takes a long length of time to complete.
- Application B makes a request that takes a short length of time to complete.
- Application C makes a request that takes a medium length of time to complete.

Open Directory passes requests to the responsible plug-in as the requests come in and does not manage or serialize requests in any way. The plug-in is responsible for handling multiple concurrent requests in any way that it deems appropriate. It may choose to process Application A’s request first and Application B’s request last, process the requests serially, or use some other algorithm for determining the order in which to process concurrent requests.

[Next](Open%20Directory%20Callbacks.md)[Previous](Processing%20Open%20Directory%20Requests.md)
