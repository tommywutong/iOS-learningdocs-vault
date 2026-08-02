---
title: IKImageViewDemo
apple_id: DTS10004049
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/samplecode/IKImageViewDemo/Listings/Read_Me_txt.html
archived_at: '2026-07-18T03:12:03.416222Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IKImageViewDemo](IKImageViewDemo.md)


[Next](Document%20Revision%20History.md)[Previous](Controller.m.md)

# Read Me.txt

```
IKImageViewDemo

================================================================================
DESCRIPTION:

This small application shows how to use the ImageKit IKImageView to display a single image. After launching, the user will get a window with a sample image displayed in an IKImageView.

The sample code shows how to handle zooming (zoom-out, zoom-in, zoom-to-actual-size, and zoom-to-fit).

The application uses segmented controls to work with the different tool modes (hand-tool, selection-tool, crop-tool, and rotation-tool).

For handling the 'Save as…', the sample code is using the ImageKit IKSaveOptions to present a save panel accessory view that deals with different image settings.

================================================================================
BUILD REQUIREMENTS:

Xcode 4.6 or later

================================================================================
RUNTIME REQUIREMENTS:

OS X 10.6 or later

================================================================================
NOTES:

App Sandboxing is currently disabled for the project. 

If you enable sandboxing, the project requires the 'User Selected File' entitlement key (com.apple.security.files.user-selected.read-write) to allow for saving an edited document to a user selected destination. This information is saved in the "IKImageViewDemo.entitlements" property list file which is also included in the project. When adopting App Sandbox for the project simply simply add this file as the entitlements file.

================================================================================
REVISION HISTORY:

1.0 - Initial version
1.1 - Bug fixes, updated Layer Kit (LK) references to Core Animation (CA)
1.2 - Update to use ARC and latest Developer Tools. Fixed deprecation warnings.
1.3 - Fixed internal inconsistency with MainMenu.nib, and converted it to a .xib. Provided for sandboxing. Other miscellaneous changes.
================================================================================
Copyright (C) 2013 Apple Inc. All rights reserved.
```

[Next](Document%20Revision%20History.md)[Previous](Controller.m.md)

