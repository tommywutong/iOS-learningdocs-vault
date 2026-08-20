---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/MapKit.html
archived_at: '2026-07-15T07:34:46.790484Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# MapKit Changes

## MapKit

MKAnnotation.hModified [-[MKAnnotation setCoordinate:]](https://developer.apple.com/documentation/mapkit/mkannotation/1429528-setcoordinate)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MKAnnotationView.hModified [MKAnnotationView.annotation](https://developer.apple.com/documentation/mapkit/mkannotationview/1452613-annotation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id<MKAnnotation> annotation ``` |
| To | ``` @property(nonatomic, strong) id<MKAnnotation> annotation ``` |

Modified [MKAnnotationView.image](https://developer.apple.com/documentation/mapkit/mkannotationview/1452094-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSImage *image ``` |
| To | ``` @property(nonatomic, strong) NSImage *image ``` |

Modified [-[MKAnnotationView initWithAnnotation:reuseIdentifier:]](https://developer.apple.com/documentation/mapkit/mkannotationview/1452779-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAnnotation:(id<MKAnnotation>)annotation reuseIdentifier:(NSString *)reuseIdentifier ``` |
| To | ``` - (instancetype)initWithAnnotation:(id<MKAnnotation>)annotation reuseIdentifier:(NSString *)reuseIdentifier ``` |

Modified [MKAnnotationView.leftCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452423-leftcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) NSView *leftCalloutAccessoryView ``` |
| To | ``` @property(strong, nonatomic) NSView *leftCalloutAccessoryView ``` |

Modified [MKAnnotationView.rightCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452233-rightcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) NSView *rightCalloutAccessoryView ``` |
| To | ``` @property(strong, nonatomic) NSView *rightCalloutAccessoryView ``` |

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

MKDirections.hModified [-[MKDirections initWithRequest:]](https://developer.apple.com/documentation/mapkit/mkdirections/1452197-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

MKDirectionsRequest.hModified [-[MKDirectionsRequest initWithContentsOfURL:]](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433158-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |

MKGeometry.hRemoved [-[NSValue MKCoordinateSpanValue]](https://developer.apple.com/documentation/foundation/nsvalue/1452516-mkcoordinatespanvalue)Removed [-[NSValue MKCoordinateValue]](https://developer.apple.com/documentation/foundation/nsvalue/1452495-mkcoordinatevalue)Added [NSValue.MKCoordinateSpanValue](https://developer.apple.com/documentation/foundation/nsvalue/1452516-mkcoordinatespanvalue)Added [NSValue.MKCoordinateValue](https://developer.apple.com/documentation/foundation/nsvalue/1452495-mkcoordinatevalue)MKLocalSearch.hModified [-[MKLocalSearch initWithRequest:]](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452759-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithRequest:(MKLocalSearchRequest *)request ``` | -- |
| To | ``` - (instancetype)initWithRequest:(MKLocalSearchRequest *)request ``` | yes |

MKMapItem.hAdded [MKLaunchOptionsCameraKey](https://developer.apple.com/documentation/mapkit/mklaunchoptionscamerakey)Modified [-[MKMapItem initWithPlacemark:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452285-initwithplacemark)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPlacemark:(MKPlacemark *)placemark ``` |
| To | ``` - (instancetype)initWithPlacemark:(MKPlacemark *)placemark ``` |

Modified [MKMapItem.placemark](https://developer.apple.com/documentation/mapkit/mkmapitem/1452134-placemark)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) MKPlacemark *placemark ``` |
| To | ``` @property(nonatomic, readonly) MKPlacemark *placemark ``` |

Modified [MKMapItem.url](https://developer.apple.com/documentation/mapkit/mkmapitem/1452746-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSURL *url ``` |
| To | ``` @property(nonatomic, strong) NSURL *url ``` |

MKMapSnapshotter.hModified [-[MKMapSnapshotter initWithOptions:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452090-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

MKMapView.hAdded [MKMapView.showsScale](https://developer.apple.com/documentation/mapkit/mkmapview/1452343-showsscale)Modified [MKMapView.delegate](https://developer.apple.com/documentation/mapkit/mkmapview/1452115-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<MKMapViewDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak) id<MKMapViewDelegate> delegate ``` |

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

MKMultiPoint.hRemoved MKMultiPoint.pointsAdded [-[MKMultiPoint points]](https://developer.apple.com/documentation/mapkit/mkmultipoint/1452425-points)MKOverlay.hModified [-[MKOverlay canReplaceMapContent]](https://developer.apple.com/documentation/mapkit/mkoverlay/1452399-canreplacemapcontent)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[MKOverlay intersectsMapRect:]](https://developer.apple.com/documentation/mapkit/mkoverlay/1452138-intersectsmaprect)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MKOverlayPathRenderer.hModified [MKOverlayPathRenderer.fillColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452668-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSColor *fillColor ``` |
| To | ``` @property(strong) NSColor *fillColor ``` |

Modified [MKOverlayPathRenderer.strokeColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452175-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSColor *strokeColor ``` |
| To | ``` @property(strong) NSColor *strokeColor ``` |

MKOverlayRenderer.hModified [-[MKOverlayRenderer initWithOverlay:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451915-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithOverlay:(id<MKOverlay>)overlay ``` | -- |
| To | ``` - (instancetype)initWithOverlay:(id<MKOverlay>)overlay ``` | yes |

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

MKPolylineRenderer.hModified [-[MKPolylineRenderer initWithPolyline:]](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452074-initwithpolyline)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithPolyline:(MKPolyline *)polyline ``` |
| To | ``` - (instancetype)initWithPolyline:(MKPolyline *)polyline ``` |

MKTileOverlay.hModified [-[MKTileOverlay initWithURLTemplate:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452705-init)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithURLTemplate:(NSString *)URLTemplate ``` | -- |
| To | ``` - (instancetype)initWithURLTemplate:(NSString *)URLTemplate ``` | yes |

MKTileOverlayRenderer.hModified [-[MKTileOverlayRenderer initWithTileOverlay:]](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/1452303-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithTileOverlay:(MKTileOverlay *)overlay ``` |
| To | ``` - (instancetype)initWithTileOverlay:(MKTileOverlay *)overlay ``` |

MKUserLocation.hModified [MKUserLocation.heading](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452721-heading)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic, retain) CLHeading *heading ``` |
| To | ``` @property(readonly, nonatomic) CLHeading *heading ``` |

Modified [MKUserLocation.location](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452415-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) CLLocation *location ``` |
| To | ``` @property(readonly, nonatomic) CLLocation *location ``` |

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
