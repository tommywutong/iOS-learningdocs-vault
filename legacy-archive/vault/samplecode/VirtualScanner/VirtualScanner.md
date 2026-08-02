---
title: VirtualScanner
apple_id: DTS40011006
resource_type: Sample Code
platform: macOS
topic: General
technology: ImageCaptureCore
published: '2012-06-12'
source_url: https://developer.apple.com/library/archive/samplecode/VirtualScanner/Introduction/Intro.html
archived_at: '2026-07-18T03:28:01.281733Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# VirtualScanner

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2012-06-12 More documentation and bug fixes when creating ICA raw files. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcmbqgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6 or later |
| __Runtime Requirements:__ | This application will run under Mac OS X 10.6 or later, and will register a new device when running from XCode automatically to allow for debugging of entry points. There is no need to install the test software anywhere specific for creating and testing purposes. Device modules will need to be installed for production at the location "/Library/Image Capture/Devices/". |

This is a sample project that shows how to create an Image Capture scanner device module. It uses 'canned' information, built from the included ScannerProperties.plist, to create a virtual scanner device. The test.tiff file will be used to simulate the image from the scanner bed or document feeder. Developers can use this project as a starting point for creating their own scanner device module. Entry points are defined and documented as to what procedures will need to be implemented to get basic functionality out of the scanner. Any actual communication to hardware can be completed using the skeleton functions in the VirtualScanner class.

[Next](ReadMe.txt.md)

