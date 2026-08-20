---
title: Dynamic Library Programming Topics
apple_id: TP40001869
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/DynamicLibraries/100-Articles/LoggingDynamicLoaderEvents.html
archived_at: '2026-07-15T07:24:27.356055Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dynamic Library Programming Topics](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Run-Path%20Dependent%20Libraries.md)

# Logging Dynamic Loader Events

As you develop and use dynamic libraries, you may want to know when certain events occur. For example, you want to know when the dynamic loader binds a particular undefined external symbol or how long it took for an application to launch.

This article identifies the environment variables you can set and the type of dynamic loader logging they activate.

[Table 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanzxfvjvomq) lists the environment variables that turn on logging by the dynamic loader.

__Table 1__  Environment variables that effect dynamic loader logging

| Environment variable | Description |
| `DYLD_PRINT_LIBRARIES` | Logs when images are loaded. |
| `DYLD_PRINT_LIBRARIES_POST_LAUNCH` | Logs when images are loaded as a result of a dlopen call. Includes a dynamic libraries’ dependent libraries. |
| `DYLD_PRINT_APIS` | Logs the invocation that causes the dynamic loader to return the address of a symbol. |
| `DYLD_PRINT_STATISTICS` | Logs statistical information on an application’s launch process, such as how many images were loaded, when the application finishes launching. |
| `DYLD_PRINT_INITIALIZERS` | Logs when the dynamic loader calls initializer and finalizer functions. |
| `DYLD_PRINT_SEGMENTS` | Logs when the dynamic loader maps a segment of a dynamic library to the current process’s address space. |
| `DYLD_PRINT_BINDINGS` | Logs when the dynamic loader binds an undefined external symbol with its definition. |

[Next](Document%20Revision%20History.md)[Previous](Run-Path%20Dependent%20Libraries.md)

