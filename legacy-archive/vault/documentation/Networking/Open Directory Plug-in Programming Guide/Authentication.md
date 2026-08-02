---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/Authentication/Authentication.html
archived_at: '2026-07-27T06:57:05.801914Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Property%20List%20for%20an%20Open%20Directory%20Plug-in.md)[Previous](Standard%20Record%20and%20Attribute%20Types.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Authentication

If an Open Directory plug-in is going to support authentication, at minimum, it should support node native, change password, and set password as root methods. Other authentication methods are optional. It is up to the plug-in to determine which node native authentication allows cleartext authentication.

[Next](Property%20List%20for%20an%20Open%20Directory%20Plug-in.md)[Previous](Standard%20Record%20and%20Attribute%20Types.md)
