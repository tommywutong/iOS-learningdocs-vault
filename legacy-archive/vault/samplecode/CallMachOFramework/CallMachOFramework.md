---
title: CallMachOFramework
apple_id: DTS10001082
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-17'
source_url: https://developer.apple.com/library/archive/samplecode/CallMachOFramework/Introduction/Intro.html
archived_at: '2026-07-18T03:02:50.347321Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MIBCarbon.h.md)

# CallMachOFramework

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-17 Shows two ways of calling a Mach-O framework from a CFM application on Mac OS X. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X Mac OS X |

This sample shows two ways of calling a Mach-O framework from a CFM application on Mac OS X. Both approaches create a CFBundle for the framework and then extract pointers to functions in the framework using CFBundleGetFunctionPointerForName. The simpler approach approach just gets a pointer to the framework function, casts it to appropriate C function pointer type, and calls it. The more complex, but more general, approach uses CFMLateImport technology to bulk import functions from a framework without any messy function pointers. Requirements: Mac OS X

[Next](MIBCarbon.h.md)

