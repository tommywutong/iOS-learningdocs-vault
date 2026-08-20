---
title: DropPrint USB
apple_id: DTS10000288
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/DropPrint_USB/Introduction/Intro.html
archived_at: '2026-07-18T03:07:20.619506Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](DropShell.c.md)

# DropPrint USB

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-26 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

DropPrint USB demonstrates a method for identifying attached USB printers which are supported by the Apple USBPrinterClass driver and to send data to these printers. This sample program works with printers supported by the Apple USBPrinterDriver. One requirement is that the printer must respond to the "1284 Get Capability String" request. The Apple USBPrinterDriver uses the response to this request to register an entry in the Name Registry. This sample searches for these strings to display the names of the available printers. Keywords: print, USB

[Next](DropShell.c.md)

