---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/CallingMacOSXFunctions/CallingMacOSXFunctions.html
archived_at: '2026-07-27T06:57:05.793126Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Managing%20References.md)[Previous](Open%20Directory%20Callbacks.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Calling OS X Functions

Open Directory plug-ins can call any OS X function but to reduce memory usage and make porting to other platforms easier, Open Directory plug-ins should restrict themselves to the System and CoreFoundation frameworks and use other frameworks only when there is a compelling reason to do so. (For example, the Open Directory LDAP plug-in uses the LDAP library.)

Open Directory plug-ins themselves should not display any human interface (HI). Only a plug-in’s separate configuration application or Directory Access plug-in should display HI.

[Next](Managing%20References.md)[Previous](Open%20Directory%20Callbacks.md)
