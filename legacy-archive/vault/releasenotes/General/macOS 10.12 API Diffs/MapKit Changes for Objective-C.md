---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/MapKit.html
archived_at: '2026-07-18T02:50:41.193823Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# MapKit Changes for Objective-C

### MapKit

#### MKAnnotationView.h

Added [-[MKAnnotationView initWithCoder:]](https://developer.apple.com/documentation/mapkit/mkannotationview/1827527-initwithcoder)Modified [-[MKAnnotationView initWithAnnotation:reuseIdentifier:]](https://developer.apple.com/documentation/mapkit/mkannotationview/1452779-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### MKMapItem.h

Added [MKLaunchOptionsDirectionsModeDefault](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodedefault)

#### MKPlacemark.h

Added [-[MKPlacemark initWithCoordinate:]](https://developer.apple.com/documentation/mapkit/mkplacemark/2172460-initwithcoordinate)Added [-[MKPlacemark initWithCoordinate:postalAddress:]](https://developer.apple.com/documentation/mapkit/mkplacemark/2172461-init)

#### MKPolygon.h

Modified [+[MKPolygon polygonWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452497-polygonwithcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |
| To | ``` + (instancetype)polygonWithCoordinates:(const CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |

Modified [+[MKPolygon polygonWithCoordinates:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452532-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> *)interiorPolygons ``` |
| To | ``` + (instancetype)polygonWithCoordinates:(const CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> *)interiorPolygons ``` |

Modified [+[MKPolygon polygonWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452247-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count ``` |
| To | ``` + (instancetype)polygonWithPoints:(const MKMapPoint *)points count:(NSUInteger)count ``` |

Modified [+[MKPolygon polygonWithPoints:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1451945-polygonwithpoints)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> *)interiorPolygons ``` |
| To | ``` + (instancetype)polygonWithPoints:(const MKMapPoint *)points count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> *)interiorPolygons ``` |

#### MKPolyline.h

Modified [+[MKPolyline polylineWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkpolyline/1452205-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polylineWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |
| To | ``` + (instancetype)polylineWithCoordinates:(const CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |

Modified [+[MKPolyline polylineWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkpolyline/1452773-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polylineWithPoints:(MKMapPoint *)points count:(NSUInteger)count ``` |
| To | ``` + (instancetype)polylineWithPoints:(const MKMapPoint *)points count:(NSUInteger)count ``` |

#### NSUserActivity+MKMapItem.h (Added)

Added [NSUserActivity.mapItem](https://developer.apple.com/documentation/foundation/nsuseractivity/1690596-mapitem)Added NSUserActivity(MKMapItem)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
