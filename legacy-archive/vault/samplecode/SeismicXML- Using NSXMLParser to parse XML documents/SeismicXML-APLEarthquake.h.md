---
title: 'SeismicXML: Using NSXMLParser to parse XML documents'
apple_id: DTS40007323
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2016-01-08'
source_url: https://developer.apple.com/library/archive/samplecode/SeismicXML/Listings/SeismicXML_APLEarthquake_h.html
archived_at: '2026-07-18T03:23:39.820140Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SeismicXML: Using NSXMLParser to parse XML documents](SeismicXML-%20Using%20NSXMLParser%20to%20parse%20XML%20documents.md)


[Next](SeismicXML-APLViewController.h.md)[Previous](SeismicXML-APLParseOperation.h.md)

# SeismicXML/APLEarthquake.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The model class that stores the information about an earthquake.
 */

@import Foundation;

@interface APLEarthquake : NSObject

// Magnitude of the earthquake on the Richter scale.
@property (nonatomic) float magnitude;
// Name of the location of the earthquake.
@property (nonatomic, strong) NSString *location;
// Date and time at which the earthquake occurred.
@property (nonatomic, strong) NSDate *date;
// Latitude and longitude of the earthquake.
@property (nonatomic) double latitude;
@property (nonatomic) double longitude;

@end
```

[Next](SeismicXML-APLViewController.h.md)[Previous](SeismicXML-APLParseOperation.h.md)

