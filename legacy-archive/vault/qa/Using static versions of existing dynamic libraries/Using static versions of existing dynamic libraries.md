---
title: Using static versions of existing dynamic libraries
apple_id: DTS10004125
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2006-10-24'
source_url: https://developer.apple.com/library/archive/qa/qa1393/_index.html
archived_at: '2026-07-18T02:30:30.470211Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1393

# Using static versions of existing dynamic libraries

## Q:  How do I link against a static version of a library when a dynamic version exists on the system?

A: How do I link against a static version of a library when a dynamic version exists on the system?

Normally, the linker goes through each path in the search paths one at a time to find a dynamic version of the library. If none is found, it goes through each of those paths looking for a static version of the same library.

The best way to explicitly control the selection of which version of the library is linked against is to keep the static and dynamic versions of the library in different directories. The library search paths must then be set to include the directories to search for your libraries, with the path to the static library preceding the path to the dynamic library. On the command line, this is done by using the `-L` linker option, followed by your directories to search. In Xcode, you use the `Library Search Paths` build setting, as shown in Figure 1.

__Figure 1__  The Library Search Paths build setting in Xcode.

!!

During the build process, use the linker flag `-search_paths_first`. In Xcode, this option is set in the `Other Linker Flags` build setting, as shown in Figure 2. This linker option causes the linker to look in each of the search paths for a dynamic library and, if none is found it looks for a static library. If there is no library found the linker continue to search the remaining paths. This method is also useful when attempting to link against static libraries of your own when there is a dynamic version of the library in the standard system library search paths.

__Figure 2__  The Other Linker Flags build setting in Xcode.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-24 | New document that illustrates how to select a static version of a library when a dynamic version of the library exists. |

