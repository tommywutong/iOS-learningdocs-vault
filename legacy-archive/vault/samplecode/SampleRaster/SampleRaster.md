---
title: SampleRaster
apple_id: DTS40009295
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/SampleRaster/Introduction/Intro.html
archived_at: '2026-07-18T03:23:03.128254Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](README.txt.md)

# SampleRaster

|  |  |
| --- | --- |
| __Last Revision:__ | Version 4.0, 2011-09-06 Now use GCD for supply level view. Also updated to build using current Xcode 4 tools on Snow Leopard and Lion. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmrzguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6 or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

The SampleRaster project implements a CUPS printer driver that simulates a typical CMYK inkjet raster printer. The driver provides the following components:

- CUPS raster filter (rastertosample) - CUPS command filter (commandtosample) - CUPS backend (sampletopdf) - Cocoa-based printer utility application (SampleUtility.app) - Cocoa-based print dialog plugin (SampleRasterPDE.bundle) - Printer icon - ICC color profiles - iPhoto/Preview printer presets - Custom printer-state-reason keywords - On-line help - Driver information file (sample.drv) which is compiled into a PPD file (sample.ppd).

The CUPS backend is provided for testing purposes only. Most printer drivers do not require their own backend - the system-supplied backends handle all standard interfaces and network protocols for printing - and very few backends are as complicated as the sampletopdf backend.

[Next](README.txt.md)

