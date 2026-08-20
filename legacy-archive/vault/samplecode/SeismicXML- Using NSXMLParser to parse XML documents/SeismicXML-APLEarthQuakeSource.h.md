---
title: 'SeismicXML: Using NSXMLParser to parse XML documents'
apple_id: DTS40007323
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2016-01-08'
source_url: https://developer.apple.com/library/archive/samplecode/SeismicXML/Listings/SeismicXML_APLEarthQuakeSource_h.html
archived_at: '2026-07-18T03:23:39.640775Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SeismicXML: Using NSXMLParser to parse XML documents](SeismicXML-%20Using%20NSXMLParser%20to%20parse%20XML%20documents.md)


[Next](SeismicXML-APLEarthQuakeSource.m.md)[Previous](SeismicXML-APLEarthquakeTableViewCell.h.md)

# SeismicXML/APLEarthQuakeSource.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Data source object responsible for initiating the download of the XML data and parses the Earthquake objects at view load time.
 */

@import Foundation;

@interface APLEarthQuakeSource : NSObject

@property (readonly) NSMutableArray *earthquakes;
@property (readonly) NSError *error;

- (void)startEarthQuakeLookup;

@end
```

[Next](SeismicXML-APLEarthQuakeSource.m.md)[Previous](SeismicXML-APLEarthquakeTableViewCell.h.md)

