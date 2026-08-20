---
title: LocateMe
apple_id: DTS40007801
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LocateMe/Listings/LocateMe_CLLocation_Strings_h.html
archived_at: '2026-07-18T03:13:45.999696Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LocateMe](LocateMe.md)


[Next](LocateMe-LocationDetailViewController.m.md)[Previous](LocateMe-CLLocation%2BStrings.m.md)

# LocateMe/CLLocation+Strings.h

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:

This is an Objective C category on the CLLocation class that extends the class by adding some convenience methods for presenting localized string representations of various properties.

*/

#import <CoreLocation/CoreLocation.h>

@interface CLLocation (Strings)

- (NSString *)localizedCoordinateString;
- (NSString *)localizedAltitudeString;
- (NSString *)localizedHorizontalAccuracyString;
- (NSString *)localizedVerticalAccuracyString;
- (NSString *)localizedCourseString;
- (NSString *)localizedSpeedString;

@end
```

[Next](LocateMe-LocationDetailViewController.m.md)[Previous](LocateMe-CLLocation%2BStrings.m.md)

