---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/OpenDirectoryCallbacks/OpenDirectoryCallbacks.html
archived_at: '2026-07-27T06:57:05.789870Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Calling%20OS%20X%20Functions.md)[Previous](Processing%20Concurrent%20Requests.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Open Directory Callbacks

Open Directory provides three callback routines for plug-ins to call:

- `DSDebugLog`. Writes an entry in the Open Directory log file. All records written by all Open Directory plug-ins are written to the same log file in the order by which Open Directory receives them.
- `DSRegisterNode`. Registers a node so that it is available for use by applications that make Open Directory calls.
- `DSUnregisterNode`. Unregisters a node that was previously registered.

The Open Directory callback routines are described in detail in the section Open Directory Callbacks” in the Reference section.

[Next](Calling%20OS%20X%20Functions.md)[Previous](Processing%20Concurrent%20Requests.md)
