---
title: 'Breadcrumb: Using CoreLocation to track user movement'
apple_id: DTS40010048
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: CoreLocation
published: '2018-05-17'
source_url: https://developer.apple.com/library/archive/samplecode/Breadcrumb/Listings/Breadcrumb_SettingsKeys_h.html
archived_at: '2026-07-27T06:57:01.857222Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Breadcrumb: Using CoreLocation to track user movement](Breadcrumb-%20Using%20CoreLocation%20to%20track%20user%20movement.md)


[Next](Breadcrumb-SettingsViewController.h.md)[Previous](Breadcrumb-CrumbPath.m.md)

# Breadcrumb/SettingsKeys.h

```
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 NSUserDefaults global keys for reading/writing user defaults.
 */

#ifndef Breadcrumb_SettingsKeys_h
#define Breadcrumb_SettingsKeys_h

// Value is a BOOL.
extern NSString * const TrackLocationInBackgroundPrefsKey;

// Value is a CLLocationAccuracy (double).
extern NSString * const LocationTrackingAccuracyPrefsKey;

// Value is a BOOL.
extern NSString * const PlaySoundOnLocationUpdatePrefsKey;

#endif
```

[Next](Breadcrumb-SettingsViewController.h.md)[Previous](Breadcrumb-CrumbPath.m.md)
