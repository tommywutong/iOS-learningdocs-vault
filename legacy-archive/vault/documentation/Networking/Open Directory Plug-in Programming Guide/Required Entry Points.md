---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/RequiredEntryPoints/RequiredEntryPoints.html
archived_at: '2026-07-27T06:57:05.771040Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Processing%20Open%20Directory%20Requests.md)[Previous](Runtime%20Environment.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Required Entry Points

Every Open Directory plug-in must provide the entry points described in this section. The entry points are listed below in the order in which they are typically called.

- `Initialize`, called by Open Directory so that the plug-in can initialize itself.
- `Validate`, called by Open Directory when plug-ins are loaded in order to pass to each plug-in a unique value that the plug-in uses to identify itself when it calls Open Directory callback routines in order to register and unregister directory nodes or to write information in an Open Directory log file.
- `SetPluginState`, called by Open Directory to notify the plug-in of a change in state. For example, this entry point would be called to enable or disable the plug-in.
- `PeriodicTask`, called by Open Directory on a regular basis so that the plug-in can perform periodic tasks.
- `ProcessRequest`, called by Open Directory to pass requests from Open Directory clients.
- `Shutdown`, called by Open Directory to tell the plug-in that Open Directory is shutting down. For example, this entry point would be called when the system shuts down. The plug-in should release memory and perform any other tasks to prepare itself for shutdown.

[Next](Processing%20Open%20Directory%20Requests.md)[Previous](Runtime%20Environment.md)
