---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/RevisionHistory.html
archived_at: '2026-07-27T06:57:05.844753Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Previous](Client%20Side%20Buffer%20Parsing.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Document Revision History

This table describes the changes to _Open Directory Plug-in Programming Guide_.

| __Date__ | __Notes__ |
| 2015-03-09 | Moved to Retired Documents Library. |
| 2006-05-23 | Moved reference information to the new document "Open Directory Reference." |
| 2005-04-29 | Updated for OS X v10.4. Changed "Rendezvous" to "Bonjour." Changed title from "Open Directory Plug-ins." |

[Previous](Client%20Side%20Buffer%20Parsing.md)
