---
title: 'AVLocationPlayer: Using AVFoundation Metadata Reading APIs'
apple_id: TP40014495
resource_type: Sample Code
platform: macOS
topic: null
technology: AVFoundation
published: '2015-04-30'
source_url: https://developer.apple.com/library/archive/samplecode/AVLocationPlayer/Listings/README_md.html
archived_at: '2026-07-18T03:00:18.137675Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVLocationPlayer: Using AVFoundation Metadata Reading APIs](AVLocationPlayer-%20Using%20AVFoundation%20Metadata%20Reading%20APIs.md)


[Next](AVLocationPlayer-AAPLDocument.h.md)[Previous](AVLocationPlayer-main.m.md)

# README.md

```
# Using AVFoundation metadata reading APIs to draw recorded location on map view

This sample shows the use of AVAssetReaderOutputMetadataAdaptor to read location metadata from a movie file containing this information. The location data is then plotted on MKMapView to present the location path where the video was recorded. This sample also shows the use of AVPlayerItemMetadataOutput to show current location on the drawn path during playback.

## Requirements

Building and Linking with MapKit Framework for OS X:
————————————————————————————————————————————————————
If you don’t have the right entitlements to use MapKit framework, at runtime you will not see map detail and you will get this message in the console:

“Your Application has attempted to access the Map Kit API. You cannot access this API without an entitlement. You may receive an entitlement from the Mac Developer Program for use by you only with your Mac App Store Apps. For more information about Apple's Mac Developer Program, please visit developer.apple.com.”

In the Portal: 
1) Create an AppID with “Maps” enabled for both Development and Distribution.
2) Create the Mac Provisioning Profiles for Development and Distribution, that use this new AppID.

Then in Xcode:
3) Set the target’s CFBundleIdentifier to match the new AppID.
4) Select the appropriate “Team” for your target, in the “General” tab, under the “Identity” section.
5) In the “Capabilities” tab, turn on “App Sandbox” and “Maps”.  This will create and include an entitlements file in your project called “AVLocationPlayer.entitlements” in order to link and run with MapKit.framework.

### Build

Xcode 5.0 or later, Mac OS X v10.10 or later

### Runtime

Mac OS X v10.10 or later

Copyright (C) 2014 Apple Inc. All rights reserved.
```

[Next](AVLocationPlayer-AAPLDocument.h.md)[Previous](AVLocationPlayer-main.m.md)

