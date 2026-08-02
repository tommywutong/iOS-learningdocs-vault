---
title: 'SeismicXML: Using NSXMLParser to parse XML documents'
apple_id: DTS40007323
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: null
published: '2016-01-08'
source_url: https://developer.apple.com/library/archive/samplecode/SeismicXML/Listings/SeismicXML_APLParseOperation_h.html
archived_at: '2026-07-18T03:23:39.888106Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SeismicXML: Using NSXMLParser to parse XML documents](SeismicXML-%20Using%20NSXMLParser%20to%20parse%20XML%20documents.md)


[Next](SeismicXML-APLEarthquake.h.md)[Previous](LICENSE.txt.md)

# SeismicXML/APLParseOperation.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The NSOperation class used to perform the XML parsing of earthquake data.
 */


@interface APLParseOperation : NSOperation

@property (copy, readonly) NSData *earthquakeData;

- (instancetype)initWithData:(NSData *)parseData NS_DESIGNATED_INITIALIZER;

+ (NSString *)AddEarthQuakesNotificationName;       // NSNotification name for sending earthquake data back to the app delegate
+ (NSString *)EarthquakeResultsKey;                 // NSNotification userInfo key for obtaining the earthquake data

+ (NSString *)EarthquakesErrorNotificationName;     // NSNotification name for reporting errors
+ (NSString *)EarthquakesMessageErrorKey;           // NSNotification userInfo key for obtaining the error message

@end
```

[Next](SeismicXML-APLEarthquake.h.md)[Previous](LICENSE.txt.md)

