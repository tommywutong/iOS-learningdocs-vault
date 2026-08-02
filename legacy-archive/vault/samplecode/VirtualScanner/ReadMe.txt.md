---
title: VirtualScanner
apple_id: DTS40011006
resource_type: Sample Code
platform: macOS
topic: General
technology: ImageCaptureCore
published: '2012-06-12'
source_url: https://developer.apple.com/library/archive/samplecode/VirtualScanner/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:28:01.630327Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VirtualScanner](VirtualScanner.md)


[Next](Includes-EntryPoints.h.md)[Previous](VirtualScanner.md)

# ReadMe.txt

```
### VirtualScanner ###

===========================================================================
DESCRIPTION:

This is a sample project that shows how to create an Image Capture scanner device module.  It uses 'canned' information, built from the included ScannerProperties.plist, to create a virtual scanner device.  The test.tiff file will be used to simulate the image from the scanner bed or document feeder.  Developers can use this project as a starting point for creating their own scanner device module.  Entry points are defined and documented as to what procedures will need to be implemented to get basic functionality out of the scanner.  Any actual communication to hardware can be completed using the skeleton functions in the VirtualScanner class.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X 10.6 or later.

===========================================================================
RUNTIME REQUIREMENTS:

This application will run under Mac OS X 10.6 or later, and will register a new device when running
from XCode automatically to allow for debugging of entry points.  There is no need to install the test software anywhere specific for creating and testing purposes.

Device modules will need to be installed for production at the location "/Library/Image Capture/Devices/".

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2011 Apple Inc. All rights reserved.
```

[Next](Includes-EntryPoints.h.md)[Previous](VirtualScanner.md)

