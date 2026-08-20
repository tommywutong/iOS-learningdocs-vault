---
title: icon cache demo
apple_id: DTS10000581
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/icon_cache_demo/Introduction/Intro.html
archived_at: '2026-07-18T03:29:46.069924Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](icon%20cache.c.md)

# icon cache demo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Demonstrates the use of an icon cache to limit the search for icon resource to one resource file. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon System 7 |

This sample demonstrates the use of an icon cache to limit the search for icon resource to one resource file. It does this by installing an icon getter function into the cache which calls Get1(Ind)Resource instead of the usual GetResource. The application is meant to display the first suite produced by an indexed resource call. There's nothing stopping you from calling Get1Resource or anything else which might produce a handle to a member of an icon suite. There's also some jiggery-pokery having to do with my distaste for purgeable handles. Requirements: System 7 Keywords: icon, cache, optimization, performance, search

[Next](icon%20cache.c.md)

