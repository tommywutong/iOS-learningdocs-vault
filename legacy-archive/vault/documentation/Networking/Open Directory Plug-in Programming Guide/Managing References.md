---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/ManagingReferences/ManagingReferences.html
archived_at: '2026-07-27T06:57:05.795901Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Standard%20Record%20and%20Attribute%20Types.md)[Previous](Calling%20OS%20X%20Functions.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Managing References

Open Directory allocates Directory Service references, such as Open Directory node references, open record references, and attribute list value references, and passes them to the appropriate plug-in as part of a process request. Plug-ins can use these references to keep track of their own data. When a reference becomes invalid, such as when an Open Directory node is closed, the plug-in must free any memory that is associated with the now invalid reference.

[Next](Standard%20Record%20and%20Attribute%20Types.md)[Previous](Calling%20OS%20X%20Functions.md)
