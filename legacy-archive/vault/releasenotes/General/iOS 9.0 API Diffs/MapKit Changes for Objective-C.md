---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/MapKit.html
archived_at: '2026-07-18T02:56:34.667996Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MapKit Changes for Objective-C

### MapKit

#### MKAnnotationView.h

Added [MKAnnotationView.detailCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452543-detailcalloutaccessoryview)

#### MKDirectionsRequest.h

Modified [MKDirectionsRequest.destination](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433146-destination)

|  | Declaration |
| --- | --- |
| From | ``` - (MKMapItem *)destination ``` |
| To | ``` @property(nonatomic, strong, nullable) MKMapItem *destination ``` |

Modified [MKDirectionsRequest.source](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433144-source)

|  | Declaration |
| --- | --- |
| From | ``` - (MKMapItem *)source ``` |
| To | ``` @property(nonatomic, strong, nullable) MKMapItem *source ``` |

#### MKDirectionsResponse.h

Added [MKETAResponse.distance](https://developer.apple.com/documentation/mapkit/mketaresponse/1452164-distance)Added [MKETAResponse.expectedArrivalDate](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/1451881-expectedarrivaldate)Added [MKETAResponse.expectedDepartureDate](https://developer.apple.com/documentation/mapkit/mketaresponse/1452644-expecteddeparturedate)Added [MKETAResponse.transportType](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/1452616-transporttype)Modified [MKDirectionsResponse.routes](https://developer.apple.com/documentation/mapkit/mkdirections/response/1452071-routes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *routes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<MKRoute *> *routes ``` |

Modified [MKRoute.advisoryNotices](https://developer.apple.com/documentation/mapkit/mkroute/1452359-advisorynotices)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *advisoryNotices ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *advisoryNotices ``` |

Modified [MKRoute.steps](https://developer.apple.com/documentation/mapkit/mkroute/1452173-steps)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *steps ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<MKRouteStep *> *steps ``` |

#### MKDirectionsTypes.h

Added [MKDirectionsTransportTypeTransit](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/1452697-transit)

#### MKLocalSearchResponse.h

Modified [MKLocalSearchResponse.mapItems](https://developer.apple.com/documentation/mapkit/mklocalsearchresponse/1451939-mapitems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *mapItems ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<MKMapItem *> *mapItems ``` |

#### MKMapCamera.h

Added [+[MKMapCamera cameraLookingAtCenterCoordinate:fromDistance:pitch:heading:]](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411079-cameralookingatcentercoordinate)

#### MKMapItem.h

Added [MKMapItem.timeZone](https://developer.apple.com/documentation/mapkit/mkmapitem/1452431-timezone)Added [MKLaunchOptionsDirectionsModeTransit](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodetransit)Modified [-[MKMapItem openInMapsWithLaunchOptions:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452239-openinmapswithlaunchoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)openInMapsWithLaunchOptions:(NSDictionary *)launchOptions ``` |
| To | ``` - (BOOL)openInMapsWithLaunchOptions:(NSDictionary<NSString *,id> * _Nullable)launchOptions ``` |

Modified [+[MKMapItem openMapsWithItems:launchOptions:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452207-openmapswithitems)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)openMapsWithItems:(NSArray *)mapItems launchOptions:(NSDictionary *)launchOptions ``` |
| To | ``` + (BOOL)openMapsWithItems:(NSArray<MKMapItem *> * _Nonnull)mapItems launchOptions:(NSDictionary<NSString *,id> * _Nullable)launchOptions ``` |

#### MKMapView.h

Added [MKMapView.showsCompass](https://developer.apple.com/documentation/mapkit/mkmapview/1451879-showscompass)Added [MKMapView.showsScale](https://developer.apple.com/documentation/mapkit/mkmapview/1452343-showsscale)Added [MKMapView.showsTraffic](https://developer.apple.com/documentation/mapkit/mkmapview/1452433-showstraffic)Modified [-[MKMapView addAnnotations:]](https://developer.apple.com/documentation/mapkit/mkmapview/1451889-addannotations)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAnnotations:(NSArray *)annotations ``` |
| To | ``` - (void)addAnnotations:(NSArray<id<MKAnnotation>> * _Nonnull)annotations ``` |

Modified [-[MKMapView addOverlays:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452335-addoverlays)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOverlays:(NSArray *)overlays ``` |
| To | ``` - (void)addOverlays:(NSArray<id<MKOverlay>> * _Nonnull)overlays ``` |

Modified [-[MKMapView addOverlays:level:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452518-addoverlays)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOverlays:(NSArray *)overlays level:(MKOverlayLevel)level ``` |
| To | ``` - (void)addOverlays:(NSArray<id<MKOverlay>> * _Nonnull)overlays level:(MKOverlayLevel)level ``` |

Modified [MKMapView.annotations](https://developer.apple.com/documentation/mapkit/mkmapview/1452593-annotations)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *annotations ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<id<MKAnnotation>> *annotations ``` |

Modified [-[MKMapView annotationsInMapRect:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452279-annotations)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)annotationsInMapRect:(MKMapRect)mapRect ``` |
| To | ``` - (NSSet<id<MKAnnotation>> * _Nonnull)annotationsInMapRect:(MKMapRect)mapRect ``` |

Modified [MKMapView.overlays](https://developer.apple.com/documentation/mapkit/mkmapview/1452784-overlays)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *overlays ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<id<MKOverlay>> *overlays ``` |

Modified [-[MKMapView overlaysInLevel:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452757-overlays)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)overlaysInLevel:(MKOverlayLevel)level ``` |
| To | ``` - (NSArray<id<MKOverlay>> * _Nonnull)overlaysInLevel:(MKOverlayLevel)level ``` |

Modified [-[MKMapView removeAnnotations:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452130-removeannotations)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAnnotations:(NSArray *)annotations ``` |
| To | ``` - (void)removeAnnotations:(NSArray<id<MKAnnotation>> * _Nonnull)annotations ``` |

Modified [-[MKMapView removeOverlays:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452719-removeoverlays)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeOverlays:(NSArray *)overlays ``` |
| To | ``` - (void)removeOverlays:(NSArray<id<MKOverlay>> * _Nonnull)overlays ``` |

Modified [MKMapView.selectedAnnotations](https://developer.apple.com/documentation/mapkit/mkmapview/1452570-selectedannotations)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *selectedAnnotations ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<id<MKAnnotation>> *selectedAnnotations ``` |

Modified [-[MKMapView showAnnotations:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452309-showannotations)

|  | Declaration |
| --- | --- |
| From | ``` - (void)showAnnotations:(NSArray *)annotations animated:(BOOL)animated ``` |
| To | ``` - (void)showAnnotations:(NSArray<id<MKAnnotation>> * _Nonnull)annotations animated:(BOOL)animated ``` |

Modified [-[MKMapViewDelegate mapView:didAddAnnotationViews:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452311-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView didAddAnnotationViews:(NSArray *)views ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView didAddAnnotationViews:(NSArray<MKAnnotationView *> * _Nonnull)views ``` |

Modified [-[MKMapViewDelegate mapView:didAddOverlayRenderers:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452609-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView didAddOverlayRenderers:(NSArray *)renderers ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView didAddOverlayRenderers:(NSArray<MKOverlayRenderer *> * _Nonnull)renderers ``` |

#### MKOverlayPathRenderer.h

Modified [MKOverlayPathRenderer.lineDashPattern](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452493-linedashpattern)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *lineDashPattern ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *lineDashPattern ``` |

#### MKPinAnnotationView.h

Added [+[MKPinAnnotationView greenPinColor]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452568-greenpincolor)Added [MKPinAnnotationView.pinTintColor](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452042-pintintcolor)Added [+[MKPinAnnotationView purplePinColor]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452110-purplepincolor)Added [+[MKPinAnnotationView redPinColor]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1451990-redpincolor)Modified [MKPinAnnotationView.pinColor](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452530-pincolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MKPinAnnotationColorGreen](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor/green)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MKPinAnnotationColorPurple](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor/purple)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [MKPinAnnotationColorRed](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor/mkpinannotationcolorred)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### MKPlacemark.h

Modified [-[MKPlacemark initWithCoordinate:addressDictionary:]](https://developer.apple.com/documentation/mapkit/mkplacemark/1451895-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoordinate:(CLLocationCoordinate2D)coordinate addressDictionary:(NSDictionary *)addressDictionary ``` |
| To | ``` - (instancetype _Nonnull)initWithCoordinate:(CLLocationCoordinate2D)coordinate addressDictionary:(NSDictionary<NSString *,id> * _Nullable)addressDictionary ``` |

#### MKPolygon.h

Modified [MKPolygon.interiorPolygons](https://developer.apple.com/documentation/mapkit/mkpolygon/1452521-interiorpolygons)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *interiorPolygons ``` |
| To | ``` @property(readonly, nullable) NSArray<MKPolygon *> *interiorPolygons ``` |

Modified [+[MKPolygon polygonWithCoordinates:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452532-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |
| To | ``` + (instancetype _Nonnull)polygonWithCoordinates:(CLLocationCoordinate2D * _Nonnull)coords count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> * _Nullable)interiorPolygons ``` |

Modified [+[MKPolygon polygonWithPoints:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1451945-polygonwithpoints)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |
| To | ``` + (instancetype _Nonnull)polygonWithPoints:(MKMapPoint * _Nonnull)points count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> * _Nullable)interiorPolygons ``` |

#### MKTypes.h

Added [MKMapTypeHybridFlyover](https://developer.apple.com/documentation/mapkit/mkmaptype/hybridflyover)Added [MKMapTypeSatelliteFlyover](https://developer.apple.com/documentation/mapkit/mkmaptype/mkmaptypesatelliteflyover)

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
