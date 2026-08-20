---
title: 'SeismicXML: Using NSXMLParser to parse XML documents'
apple_id: DTS40007323
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2016-01-08'
source_url: https://developer.apple.com/library/archive/samplecode/SeismicXML/Listings/SeismicXML_APLEarthquakeTableViewCell_h.html
archived_at: '2026-07-18T03:23:39.726920Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SeismicXML: Using NSXMLParser to parse XML documents](SeismicXML-%20Using%20NSXMLParser%20to%20parse%20XML%20documents.md)


[Next](SeismicXML-APLEarthQuakeSource.h.md)[Previous](SeismicXML-APLViewController.m.md)

# SeismicXML/APLEarthquakeTableViewCell.h

```objc

/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Table view cell to display an earthquake.
 */

@import UIKit;

@class APLEarthquake;

@interface APLEarthquakeTableViewCell : UITableViewCell

- (void)configureWithEarthquake:(APLEarthquake *)earthquake;

@end
```

[Next](SeismicXML-APLEarthQuakeSource.h.md)[Previous](SeismicXML-APLViewController.m.md)

