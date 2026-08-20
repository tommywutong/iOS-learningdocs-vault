---
title: CheckExecutableArchitecture
apple_id: DTS10003756
resource_type: Sample Code
platform: macOS
topic: General
technology: CoreFoundation
published: '2006-02-07'
source_url: https://developer.apple.com/library/archive/samplecode/CheckExecutableArchitecture/Introduction/Intro.html
archived_at: '2026-07-18T03:03:19.099192Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# CheckExecutableArchitecture

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-02-07 Determine whether a particular Mach-O executable contains a version suitable for executing on a given processor architecture. |
| __Build Requirements:__ | Mac OS X |
| __Runtime Requirements:__ | Mac OS X |

This sample deals with the problem of determining in advance whether a particular Mach-O executable contains a version suitable for executing on a given processor architecture. For example, an application running on an Intel-based Macintosh may wish to examine a set of potential plugins, because it suspects that some of them may be PowerPC-only and thus not suitable for loading. The code here may also be instructive and relevant for those who wish to understand the structure of Mach-O executables.

[Next](README.txt.md)

