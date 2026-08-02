---
title: CFM_MachO_CFM
apple_id: DTS10001083
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-17'
source_url: https://developer.apple.com/library/archive/samplecode/CFM_MachO_CFM/Introduction/Intro.html
archived_at: '2026-07-18T03:02:28.217300Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CFM%20Application-CFMMachOCFM.c.md)

# CFM_MachO_CFM

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-17 CFM application calls Mach-O routine, passing in a fixed up CFM function pointer as a callback parameter. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Mac OS X Mac OS X 10.1 |

This sample demonstrates how to call a Mach-O function which takes a callback function pointer as a parameter. The main CFM application readies the callback function by calling a routine MachOFunctionPointerForCFMFunctionPointer() which generates power pc assembly glue to call the passed in function pointer. This generated glue is then passed to the Mach-O routine as the callback parameter. Requirements: Mac OS X 10.1 Keywords: Carbon CFM Mach-O Macho Bundle

[Next](CFM%20Application-CFMMachOCFM.c.md)

