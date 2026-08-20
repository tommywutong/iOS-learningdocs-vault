---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/StandardRecordandAttributeTypes/StandardRecordandAttributeTypes.html
archived_at: '2026-07-27T06:57:05.799042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Authentication.md)[Previous](Managing%20References.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Standard Record and Attribute Types

Plug-ins should support the standard record and attribute types described in “Record Type Constants” in the Reference chapter as appropriate for the data that the directory system provides and in accordance with the needs of OS X. Plug-ins should also honor the meta types described in that section. (Meta types are types that are created dynamically, such as a user’s current location.) Plug-ins should map the standard record and attribute types to the plug-in’s native record and attribute types.

Plug-ins can support as many native record and attribute types as they want.

[Next](Authentication.md)[Previous](Managing%20References.md)
