---
title: TransWeb
apple_id: DTS40008614
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: null
published: '2010-06-25'
source_url: https://developer.apple.com/library/archive/samplecode/TransWeb/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:27:10.546990Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TransWeb](TransWeb.md)


[Next](main.m.md)[Previous](TransWeb.md)

# ReadMe.txt

```
TransWeb

Demonstrates how to implement UIWebView with a transparent background.

To achieve this you need to make the HTML body's background color transparent by doing the following -
1) set the UIWebView's backgroundColor property to [UIColor clearColor]
2) use the UIWebView's content in the html: <body style="background-color: transparent">
3) the UIWebView's opaque property set to NO


Build Requirements
iOS 4.0 SDK


Runtime Requirements
iPhone OS 3.2 or later


Using the Sample
Launch the TransWeb project using Xcode.
To run in the simulator, set the Active SDK to Simulator. To run on a device, set the Active SDK to the appropriate Device setting.  When launched scroll vertically through the web content and observe the transparent background image.


Packaging List
main.m - Main source file for this sample.
AppDelegate.h/.m - The application's delegate to setup its window and view controller content.
MyViewController.h/.m - The main view controller controlling the web view.


Changes from Previous Versions
1.4 - Updated iTunesArtwork.
1.3 - Added iPhone OS 3.2 for deployment SDK. Updated artwork. Upgraded project to build with the iOS 4 SDK.
1.1 - Corrected UIWebView warning of "Turning off phone number detection is not supported on iPhone OS versions prior 3.0."
1.0 - First release.


Copyright (C) 2009-2010 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](TransWeb.md)

