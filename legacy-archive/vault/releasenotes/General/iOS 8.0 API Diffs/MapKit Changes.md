---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/MapKit.html
archived_at: '2026-07-18T02:55:58.845246Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# MapKit Changes

## MapKit

MKAnnotation.hModified [-[MKAnnotation setCoordinate:]](https://developer.apple.com/documentation/mapkit/mkannotation/1429528-setcoordinate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MKAnnotationView.hModified [-[MKAnnotationView initWithAnnotation:reuseIdentifier:]](https://developer.apple.com/documentation/mapkit/mkannotationview/1452779-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAnnotation:(id<MKAnnotation>)annotation reuseIdentifier:(NSString *)reuseIdentifier ``` |
| To | ``` - (instancetype)initWithAnnotation:(id<MKAnnotation>)annotation reuseIdentifier:(NSString *)reuseIdentifier ``` |

MKCircle.hModified [+[MKCircle circleWithCenterCoordinate:radius:]](https://developer.apple.com/documentation/mapkit/mkcircle/1411076-init)

|  | Declaration |
| --- | --- |
| From | ``` + (MKCircle *)circleWithCenterCoordinate:(CLLocationCoordinate2D)coord radius:(CLLocationDistance)radius ``` |
| To | ``` + (instancetype)circleWithCenterCoordinate:(CLLocationCoordinate2D)coord radius:(CLLocationDistance)radius ``` |

Modified [+[MKCircle circleWithMapRect:]](https://developer.apple.com/documentation/mapkit/mkcircle/1411072-circlewithmaprect)

|  | Declaration |
| --- | --- |
| From | ``` + (MKCircle *)circleWithMapRect:(MKMapRect)mapRect ``` |
| To | ``` + (instancetype)circleWithMapRect:(MKMapRect)mapRect ``` |

MKCircleRenderer.hModified [-[MKCircleRenderer initWithCircle:]](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/1452547-initwithcircle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCircle:(MKCircle *)circle ``` |
| To | ``` - (instancetype)initWithCircle:(MKCircle *)circle ``` |

MKCircleView.hModified [-[MKCircleView initWithCircle:]](https://developer.apple.com/documentation/mapkit/mkcircleview/1623524-initwithcircle)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCircle:(MKCircle *)circle ``` |
| To | ``` - (instancetype)initWithCircle:(MKCircle *)circle ``` |

MKDirectionsRequest.hModified [-[MKDirectionsRequest initWithContentsOfURL:]](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433158-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |

MKGeometry.hRemoved [-[NSValue MKCoordinateSpanValue]](https://developer.apple.com/documentation/foundation/nsvalue/1452516-mkcoordinatespanvalue)Removed [-[NSValue MKCoordinateValue]](https://developer.apple.com/documentation/foundation/nsvalue/1452495-mkcoordinatevalue)Added [NSValue.MKCoordinateSpanValue](https://developer.apple.com/documentation/foundation/nsvalue/1452516-mkcoordinatespanvalue)Added [NSValue.MKCoordinateValue](https://developer.apple.com/documentation/foundation/nsvalue/1452495-mkcoordinatevalue)MKLocalSearch.hModified [-[MKLocalSearch initWithRequest:]](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452759-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithRequest:(MKLocalSearchRequest *)request ``` |
| To | ``` - (instancetype)initWithRequest:(MKLocalSearchRequest *)request ``` |

MKMapItem.hModified [-[MKMapItem initWithPlacemark:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452285-initwithplacemark)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPlacemark:(MKPlacemark *)placemark ``` |
| To | ``` - (instancetype)initWithPlacemark:(MKPlacemark *)placemark ``` |

Modified [MKLaunchOptionsCameraKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionscamerakey)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 7.1 |

MKMapView.hModified [-[MKMapViewDelegate mapView:annotationView:calloutAccessoryControlTapped:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616211-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:annotationView:didChangeDragState:fromOldState:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452229-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didAddAnnotationViews:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452311-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didAddOverlayRenderers:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452609-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didAddOverlayViews:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616206-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didChangeUserTrackingMode:animated:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616202-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didDeselectAnnotationView:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452707-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didFailToLocateUserWithError:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452211-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didSelectAnnotationView:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452393-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:didUpdateUserLocation:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452086-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:regionDidChangeAnimated:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452345-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:regionWillChangeAnimated:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452571-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:rendererForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:viewForAnnotation:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapView:viewForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1616210-mapview)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapViewDidFailLoadingMap:withError:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452327-mapviewdidfailloadingmap)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapViewDidFinishLoadingMap:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452291-mapviewdidfinishloadingmap)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapViewDidFinishRenderingMap:fullyRendered:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451897-mapviewdidfinishrenderingmap)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapViewDidStopLocatingUser:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452715-mapviewdidstoplocatinguser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapViewWillStartLoadingMap:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452744-mapviewwillstartloadingmap)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapViewWillStartLocatingUser:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452171-mapviewwillstartlocatinguser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKMapViewDelegate mapViewWillStartRenderingMap:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451970-mapviewwillstartrenderingmap)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MKOverlay.hModified [-[MKOverlay canReplaceMapContent]](https://developer.apple.com/documentation/mapkit/mkoverlay/1452399-canreplacemapcontent)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKOverlay intersectsMapRect:]](https://developer.apple.com/documentation/mapkit/mkoverlay/1452138-intersectsmaprect)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MKOverlayRenderer.hModified [-[MKOverlayRenderer initWithOverlay:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451915-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithOverlay:(id<MKOverlay>)overlay ``` |
| To | ``` - (instancetype)initWithOverlay:(id<MKOverlay>)overlay ``` |

MKOverlayView.hModified [-[MKOverlayView initWithOverlay:]](https://developer.apple.com/documentation/mapkit/mkoverlayview/1613884-initwithoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithOverlay:(id<MKOverlay>)overlay ``` |
| To | ``` - (instancetype)initWithOverlay:(id<MKOverlay>)overlay ``` |

MKPlacemark.hModified [-[MKPlacemark initWithCoordinate:addressDictionary:]](https://developer.apple.com/documentation/mapkit/mkplacemark/1451895-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCoordinate:(CLLocationCoordinate2D)coordinate addressDictionary:(NSDictionary *)addressDictionary ``` |
| To | ``` - (instancetype)initWithCoordinate:(CLLocationCoordinate2D)coordinate addressDictionary:(NSDictionary *)addressDictionary ``` |

MKPolygon.hModified [+[MKPolygon polygonWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452497-polygonwithcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` + (MKPolygon *)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |
| To | ``` + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |

Modified [+[MKPolygon polygonWithCoordinates:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452532-init)

|  | Declaration |
| --- | --- |
| From | ``` + (MKPolygon *)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |
| To | ``` + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |

Modified [+[MKPolygon polygonWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452247-init)

|  | Declaration |
| --- | --- |
| From | ``` + (MKPolygon *)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count ``` |
| To | ``` + (instancetype)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count ``` |

Modified [+[MKPolygon polygonWithPoints:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1451945-polygonwithpoints)

|  | Declaration |
| --- | --- |
| From | ``` + (MKPolygon *)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |
| To | ``` + (instancetype)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |

MKPolygonRenderer.hModified [-[MKPolygonRenderer initWithPolygon:]](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/1448129-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPolygon:(MKPolygon *)polygon ``` |
| To | ``` - (instancetype)initWithPolygon:(MKPolygon *)polygon ``` |

MKPolygonView.hModified [-[MKPolygonView initWithPolygon:]](https://developer.apple.com/documentation/mapkit/mkpolygonview/1614141-initwithpolygon)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPolygon:(MKPolygon *)polygon ``` |
| To | ``` - (instancetype)initWithPolygon:(MKPolygon *)polygon ``` |

MKPolylineRenderer.hModified [-[MKPolylineRenderer initWithPolyline:]](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452074-initwithpolyline)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPolyline:(MKPolyline *)polyline ``` |
| To | ``` - (instancetype)initWithPolyline:(MKPolyline *)polyline ``` |

MKPolylineView.hModified [-[MKPolylineView initWithPolyline:]](https://developer.apple.com/documentation/mapkit/mkpolylineview/1618189-initwithpolyline)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPolyline:(MKPolyline *)polyline ``` |
| To | ``` - (instancetype)initWithPolyline:(MKPolyline *)polyline ``` |

MKReverseGeocoder.hModified [-[MKReverseGeocoder initWithCoordinate:]](https://developer.apple.com/documentation/mapkit/mkreversegeocoder/1618471-initwithcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCoordinate:(CLLocationCoordinate2D)coordinate ``` |
| To | ``` - (instancetype)initWithCoordinate:(CLLocationCoordinate2D)coordinate ``` |

MKTileOverlay.hModified [-[MKTileOverlay initWithURLTemplate:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452705-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURLTemplate:(NSString *)URLTemplate ``` |
| To | ``` - (instancetype)initWithURLTemplate:(NSString *)URLTemplate ``` |

MKTileOverlayRenderer.hModified [-[MKTileOverlayRenderer initWithTileOverlay:]](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/1452303-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTileOverlay:(MKTileOverlay *)overlay ``` |
| To | ``` - (instancetype)initWithTileOverlay:(MKTileOverlay *)overlay ``` |

MKUserTrackingBarButtonItem.hModified [-[MKUserTrackingBarButtonItem initWithMapView:]](https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem/1620146-initwithmapview)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMapView:(MKMapView *)mapView ``` |
| To | ``` - (instancetype)initWithMapView:(MKMapView *)mapView ``` |

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
