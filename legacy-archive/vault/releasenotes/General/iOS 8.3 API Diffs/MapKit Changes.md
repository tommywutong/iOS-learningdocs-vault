---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/MapKit.html
archived_at: '2026-07-18T02:56:26.653693Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# MapKit Changes

## MapKit

Removed MKAnnotation.setCoordinate(CLLocationCoordinate2D)Added MKCoordinateRegion.init()Added MKCoordinateRegion.init(center: CLLocationCoordinate2D, span: MKCoordinateSpan)Added MKCoordinateSpan.init()Added MKCoordinateSpan.init(latitudeDelta: CLLocationDegrees, longitudeDelta: CLLocationDegrees)Added MKMapPoint.init()Added MKMapPoint.init(x: Double, y: Double)Added MKMapRect.init()Added MKMapRect.init(origin: MKMapPoint, size: MKMapSize)Added MKMapSize.init()Added MKMapSize.init(width: Double, height: Double)Added MKTileOverlayPath.init()Added MKTileOverlayPath.init(x: Int, y: Int, z: Int, contentScaleFactor: CGFloat)Modified MKCoordinateRegion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKCoordinateRegion {     var center: CLLocationCoordinate2D     var span: MKCoordinateSpan } ``` |
| To | ``` struct MKCoordinateRegion {     var center: CLLocationCoordinate2D     var span: MKCoordinateSpan     init()     init(center center: CLLocationCoordinate2D, span span: MKCoordinateSpan) } ``` |

Modified MKCoordinateSpan [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKCoordinateSpan {     var latitudeDelta: CLLocationDegrees     var longitudeDelta: CLLocationDegrees } ``` |
| To | ``` struct MKCoordinateSpan {     var latitudeDelta: CLLocationDegrees     var longitudeDelta: CLLocationDegrees     init()     init(latitudeDelta latitudeDelta: CLLocationDegrees, longitudeDelta longitudeDelta: CLLocationDegrees) } ``` |

Modified MKErrorCode.DirectionsNotFound

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapPoint [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKMapPoint {     var x: Double     var y: Double } ``` |
| To | ``` struct MKMapPoint {     var x: Double     var y: Double     init()     init(x x: Double, y y: Double) } ``` |

Modified MKMapRect [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKMapRect {     var origin: MKMapPoint     var size: MKMapSize } ``` |
| To | ``` struct MKMapRect {     var origin: MKMapPoint     var size: MKMapSize     init()     init(origin origin: MKMapPoint, size size: MKMapSize) } ``` |

Modified MKMapSize [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKMapSize {     var width: Double     var height: Double } ``` |
| To | ``` struct MKMapSize {     var width: Double     var height: Double     init()     init(width width: Double, height height: Double) } ``` |

Modified MKMapView.annotationsInMapRect(MKMapRect) -> Set<NSObject>!

|  | Declaration |
| --- | --- |
| From | ``` func annotationsInMapRect(_ mapRect: MKMapRect) -> NSSet! ``` |
| To | ``` func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>! ``` |

Modified MKTileOverlayPath [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKTileOverlayPath {     var x: Int     var y: Int     var z: Int     var contentScaleFactor: CGFloat } ``` |
| To | ``` struct MKTileOverlayPath {     var x: Int     var y: Int     var z: Int     var contentScaleFactor: CGFloat     init()     init(x x: Int, y y: Int, z z: Int, contentScaleFactor contentScaleFactor: CGFloat) } ``` |

Modified MKAnnotationCalloutInfoDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MKAnnotationCalloutInfoDidChangeNotification: NSString! ``` |
| To | ``` let MKAnnotationCalloutInfoDidChangeNotification: String ``` |

Modified MKErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` var MKErrorDomain: NSString! ``` |
| To | ``` let MKErrorDomain: String ``` |

Modified MKLaunchOptionsCameraKey

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsCameraKey: NSString! ``` |
| To | ``` let MKLaunchOptionsCameraKey: String ``` |

Modified MKLaunchOptionsDirectionsModeDriving

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsDirectionsModeDriving: NSString! ``` |
| To | ``` let MKLaunchOptionsDirectionsModeDriving: String ``` |

Modified MKLaunchOptionsDirectionsModeKey

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsDirectionsModeKey: NSString! ``` |
| To | ``` let MKLaunchOptionsDirectionsModeKey: String ``` |

Modified MKLaunchOptionsDirectionsModeWalking

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsDirectionsModeWalking: NSString! ``` |
| To | ``` let MKLaunchOptionsDirectionsModeWalking: String ``` |

Modified MKLaunchOptionsMapCenterKey

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsMapCenterKey: NSString! ``` |
| To | ``` let MKLaunchOptionsMapCenterKey: String ``` |

Modified MKLaunchOptionsMapSpanKey

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsMapSpanKey: NSString! ``` |
| To | ``` let MKLaunchOptionsMapSpanKey: String ``` |

Modified MKLaunchOptionsMapTypeKey

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsMapTypeKey: NSString! ``` |
| To | ``` let MKLaunchOptionsMapTypeKey: String ``` |

Modified MKLaunchOptionsShowsTrafficKey

|  | Declaration |
| --- | --- |
| From | ``` let MKLaunchOptionsShowsTrafficKey: NSString! ``` |
| To | ``` let MKLaunchOptionsShowsTrafficKey: String ``` |

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
