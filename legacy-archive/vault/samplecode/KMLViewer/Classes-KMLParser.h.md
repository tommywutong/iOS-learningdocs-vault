---
title: KMLViewer
apple_id: DTS40010046
resource_type: Sample Code
platform: iOS
topic: null
technology: MapKit
published: '2015-09-24'
source_url: https://developer.apple.com/library/archive/samplecode/KMLViewer/Listings/Classes_KMLParser_h.html
archived_at: '2026-07-18T03:13:20.486846Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [KMLViewer](KMLViewer.md)


[Next](Classes-KMLViewerViewController.h.md)[Previous](Classes-KMLViewerAppDelegate.h.md)

# Classes/KMLParser.h

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Implements a limited KML parser.
      The following KML types are supported:
              Style,
              LineString,
              Point,
              Polygon,
              Placemark.
           All other types are ignored
*/

@import MapKit;

@class KMLPlacemark;
@class KMLStyle;

@interface KMLParser : NSObject <NSXMLParserDelegate> {
    NSMutableDictionary *_styles;
    NSMutableArray *_placemarks;

    KMLPlacemark *_placemark;
    KMLStyle *_style;

    NSXMLParser *_xmlParser;
}

- (instancetype)initWithURL:(NSURL *)url;
- (void)parseKML;

@property (unsafe_unretained, nonatomic, readonly) NSArray *overlays;
@property (unsafe_unretained, nonatomic, readonly) NSArray *points;

- (MKAnnotationView *)viewForAnnotation:(id <MKAnnotation>)point;
- (MKOverlayRenderer *)rendererForOverlay:(id <MKOverlay>)overlay;

@end
```

[Next](Classes-KMLViewerViewController.h.md)[Previous](Classes-KMLViewerAppDelegate.h.md)

