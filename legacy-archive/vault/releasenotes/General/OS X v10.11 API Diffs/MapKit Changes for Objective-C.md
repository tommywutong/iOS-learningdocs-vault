---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/MapKit.html
archived_at: '2026-07-18T02:53:09.518488Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MapKit Changes for Objective-C

### MapKit

#### MKAnnotation.h

Modified [MKAnnotation.subtitle](https://developer.apple.com/documentation/mapkit/mkannotation/1429520-subtitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *subtitle ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *subtitle ``` |

Modified [MKAnnotation.title](https://developer.apple.com/documentation/mapkit/mkannotation/1429522-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *title ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *title ``` |

#### MKAnnotationView.h

Added [MKAnnotationView.detailCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452543-detailcalloutaccessoryview)Modified [MKAnnotationView.annotation](https://developer.apple.com/documentation/mapkit/mkannotationview/1452613-annotation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) id<MKAnnotation> annotation ``` |
| To | ``` @property(nonatomic, strong, nullable) id<MKAnnotation> annotation ``` |

Modified [MKAnnotationView.image](https://developer.apple.com/documentation/mapkit/mkannotationview/1452094-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSImage *image ``` |
| To | ``` @property(nonatomic, strong, nullable) NSImage *image ``` |

Modified [-[MKAnnotationView initWithAnnotation:reuseIdentifier:]](https://developer.apple.com/documentation/mapkit/mkannotationview/1452779-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAnnotation:(id<MKAnnotation>)annotation reuseIdentifier:(NSString *)reuseIdentifier ``` |
| To | ``` - (instancetype _Nonnull)initWithAnnotation:(id<MKAnnotation> _Nullable)annotation reuseIdentifier:(NSString * _Nullable)reuseIdentifier ``` |

Modified [MKAnnotationView.leftCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452423-leftcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, nonatomic) NSView *leftCalloutAccessoryView ``` |
| To | ``` @property(strong, nonatomic, nullable) NSView *leftCalloutAccessoryView ``` |

Modified [MKAnnotationView.reuseIdentifier](https://developer.apple.com/documentation/mapkit/mkannotationview/1452060-reuseidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *reuseIdentifier ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *reuseIdentifier ``` |

Modified [MKAnnotationView.rightCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452233-rightcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong, nonatomic) NSView *rightCalloutAccessoryView ``` |
| To | ``` @property(strong, nonatomic, nullable) NSView *rightCalloutAccessoryView ``` |

#### MKCircle.h

Modified [+[MKCircle circleWithCenterCoordinate:radius:]](https://developer.apple.com/documentation/mapkit/mkcircle/1411076-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)circleWithCenterCoordinate:(CLLocationCoordinate2D)coord radius:(CLLocationDistance)radius ``` |
| To | ``` + (instancetype _Nonnull)circleWithCenterCoordinate:(CLLocationCoordinate2D)coord radius:(CLLocationDistance)radius ``` |

Modified [+[MKCircle circleWithMapRect:]](https://developer.apple.com/documentation/mapkit/mkcircle/1411072-circlewithmaprect)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)circleWithMapRect:(MKMapRect)mapRect ``` |
| To | ``` + (instancetype _Nonnull)circleWithMapRect:(MKMapRect)mapRect ``` |

#### MKCircleRenderer.h

Modified [MKCircleRenderer.circle](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/1452413-circle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKCircle *circle ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKCircle *circle ``` |

Modified [-[MKCircleRenderer initWithCircle:]](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/1452547-initwithcircle)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCircle:(MKCircle *)circle ``` |
| To | ``` - (instancetype _Nonnull)initWithCircle:(MKCircle * _Nonnull)circle ``` |

#### MKDirections.h

Modified [-[MKDirections calculateDirectionsWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mkdirections/1452078-calculate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)calculateDirectionsWithCompletionHandler:(MKDirectionsHandler)completionHandler ``` |
| To | ``` - (void)calculateDirectionsWithCompletionHandler:(MKDirectionsHandler _Nonnull)completionHandler ``` |

Modified [-[MKDirections calculateETAWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mkdirections/1452736-calculateeta)

|  | Declaration |
| --- | --- |
| From | ``` - (void)calculateETAWithCompletionHandler:(MKETAHandler)completionHandler ``` |
| To | ``` - (void)calculateETAWithCompletionHandler:(MKETAHandler _Nonnull)completionHandler ``` |

Modified [-[MKDirections initWithRequest:]](https://developer.apple.com/documentation/mapkit/mkdirections/1452197-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRequest:(MKDirectionsRequest *)request ``` |
| To | ``` - (instancetype _Nonnull)initWithRequest:(MKDirectionsRequest * _Nonnull)request ``` |

#### MKDirectionsRequest.h

Modified [MKDirectionsRequest.arrivalDate](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433148-arrivaldate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDate *arrivalDate ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDate *arrivalDate ``` |

Modified [MKDirectionsRequest.departureDate](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433155-departuredate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDate *departureDate ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDate *departureDate ``` |

Modified [MKDirectionsRequest.destination](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433146-destination)

|  | Declaration |
| --- | --- |
| From | ``` - (MKMapItem *)destination ``` |
| To | ``` @property(nonatomic, strong, nullable) MKMapItem *destination ``` |

Modified [-[MKDirectionsRequest initWithContentsOfURL:]](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433158-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithContentsOfURL:(NSURL *)url ``` |
| To | ``` - (instancetype _Nonnull)initWithContentsOfURL:(NSURL * _Nonnull)url ``` |

Modified [+[MKDirectionsRequest isDirectionsRequestURL:]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433150-isdirectionsrequesturl)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)isDirectionsRequestURL:(NSURL *)url ``` |
| To | ``` + (BOOL)isDirectionsRequestURL:(NSURL * _Nonnull)url ``` |

Modified [-[MKDirectionsRequest setDestination:]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433157-setdestination)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDestination:(MKMapItem *)destination ``` |
| To | ``` - (void)setDestination:(MKMapItem * _Nullable)destination ``` |

Modified [-[MKDirectionsRequest setSource:]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433156-setsource)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSource:(MKMapItem *)source ``` |
| To | ``` - (void)setSource:(MKMapItem * _Nullable)source ``` |

Modified [MKDirectionsRequest.source](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433144-source)

|  | Declaration |
| --- | --- |
| From | ``` - (MKMapItem *)source ``` |
| To | ``` @property(nonatomic, strong, nullable) MKMapItem *source ``` |

#### MKDirectionsResponse.h

Added [MKETAResponse.distance](https://developer.apple.com/documentation/mapkit/mketaresponse/1452164-distance)Added [MKETAResponse.expectedArrivalDate](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/1451881-expectedarrivaldate)Added [MKETAResponse.expectedDepartureDate](https://developer.apple.com/documentation/mapkit/mketaresponse/1452644-expecteddeparturedate)Added [MKETAResponse.transportType](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/1452616-transporttype)Modified [MKDirectionsResponse.destination](https://developer.apple.com/documentation/mapkit/mkdirections/response/1451981-destination)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKMapItem *destination ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKMapItem *destination ``` |

Modified [MKDirectionsResponse.routes](https://developer.apple.com/documentation/mapkit/mkdirections/response/1452071-routes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *routes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<MKRoute *> *routes ``` |

Modified [MKDirectionsResponse.source](https://developer.apple.com/documentation/mapkit/mkdirectionsresponse/1452261-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKMapItem *source ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKMapItem *source ``` |

Modified [MKETAResponse.destination](https://developer.apple.com/documentation/mapkit/mketaresponse/1452611-destination)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKMapItem *destination ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKMapItem *destination ``` |

Modified [MKETAResponse.source](https://developer.apple.com/documentation/mapkit/mketaresponse/1451947-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKMapItem *source ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKMapItem *source ``` |

Modified [MKRoute.advisoryNotices](https://developer.apple.com/documentation/mapkit/mkroute/1452359-advisorynotices)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *advisoryNotices ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *advisoryNotices ``` |

Modified [MKRoute.name](https://developer.apple.com/documentation/mapkit/mkroute/1452684-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *name ``` |

Modified [MKRoute.polyline](https://developer.apple.com/documentation/mapkit/mkroute/1451943-polyline)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKPolyline *polyline ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKPolyline *polyline ``` |

Modified [MKRoute.steps](https://developer.apple.com/documentation/mapkit/mkroute/1452173-steps)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *steps ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<MKRouteStep *> *steps ``` |

Modified [MKRouteStep.instructions](https://developer.apple.com/documentation/mapkit/mkroutestep/1452447-instructions)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *instructions ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *instructions ``` |

Modified [MKRouteStep.notice](https://developer.apple.com/documentation/mapkit/mkroutestep/1452347-notice)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *notice ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *notice ``` |

Modified [MKRouteStep.polyline](https://developer.apple.com/documentation/mapkit/mkroute/step/1452223-polyline)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKPolyline *polyline ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKPolyline *polyline ``` |

#### MKDirectionsTypes.h

Added [MKDirectionsTransportTypeTransit](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/1452697-transit)

#### MKDistanceFormatter.h

Modified [-[MKDistanceFormatter distanceFromString:]](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452766-distance)

|  | Declaration |
| --- | --- |
| From | ``` - (CLLocationDistance)distanceFromString:(NSString *)distance ``` |
| To | ``` - (CLLocationDistance)distanceFromString:(NSString * _Nonnull)distance ``` |

Modified [MKDistanceFormatter.locale](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452235-locale)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSLocale *locale ``` |
| To | ``` @property(copy, atomic) NSLocale * _Null_unspecified locale ``` |

Modified [-[MKDistanceFormatter stringFromDistance:]](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1451994-string)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)stringFromDistance:(CLLocationDistance)distance ``` |
| To | ``` - (NSString * _Nonnull)stringFromDistance:(CLLocationDistance)distance ``` |

#### MKGeodesicPolyline.h

Modified [+[MKGeodesicPolyline polylineWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/1452314-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polylineWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |
| To | ``` + (instancetype _Nonnull)polylineWithCoordinates:(CLLocationCoordinate2D * _Nonnull)coords count:(NSUInteger)count ``` |

Modified [+[MKGeodesicPolyline polylineWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/1452053-polylinewithpoints)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polylineWithPoints:(MKMapPoint *)points count:(NSUInteger)count ``` |
| To | ``` + (instancetype _Nonnull)polylineWithPoints:(MKMapPoint * _Nonnull)points count:(NSUInteger)count ``` |

#### MKGeometry.h

Modified [+[NSValue valueWithMKCoordinate:]](https://developer.apple.com/documentation/foundation/nsvalue/1452193-valuewithmkcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithMKCoordinate:(CLLocationCoordinate2D)coordinate ``` |
| To | ``` + (NSValue * _Nonnull)valueWithMKCoordinate:(CLLocationCoordinate2D)coordinate ``` |

Modified [+[NSValue valueWithMKCoordinateSpan:]](https://developer.apple.com/documentation/foundation/nsvalue/1452333-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithMKCoordinateSpan:(MKCoordinateSpan)span ``` |
| To | ``` + (NSValue * _Nonnull)valueWithMKCoordinateSpan:(MKCoordinateSpan)span ``` |

Modified [MKMapRectDivide()](https://developer.apple.com/documentation/mapkit/1452231-mkmaprectdivide)

|  | Declaration |
| --- | --- |
| From | ``` void MKMapRectDivide (     MKMapRect rect,     MKMapRect *slice,     MKMapRect *remainder,     double amount,     CGRectEdge edge ); ``` |
| To | ``` void MKMapRectDivide (     MKMapRect rect,     MKMapRect * _Nonnull slice,     MKMapRect * _Nonnull remainder,     double amount,     CGRectEdge edge ); ``` |

Modified [MKStringFromMapPoint()](https://developer.apple.com/documentation/mapkit/1451962-mkstringfrommappoint)

|  | Declaration |
| --- | --- |
| From | ``` NSString * MKStringFromMapPoint (     MKMapPoint point ); ``` |
| To | ``` NSString * _Nonnull MKStringFromMapPoint (     MKMapPoint point ); ``` |

Modified [MKStringFromMapRect()](https://developer.apple.com/documentation/mapkit/1451996-mkstringfrommaprect)

|  | Declaration |
| --- | --- |
| From | ``` NSString * MKStringFromMapRect (     MKMapRect rect ); ``` |
| To | ``` NSString * _Nonnull MKStringFromMapRect (     MKMapRect rect ); ``` |

Modified [MKStringFromMapSize()](https://developer.apple.com/documentation/mapkit/1452351-mkstringfrommapsize)

|  | Declaration |
| --- | --- |
| From | ``` NSString * MKStringFromMapSize (     MKMapSize size ); ``` |
| To | ``` NSString * _Nonnull MKStringFromMapSize (     MKMapSize size ); ``` |

#### MKLocalSearch.h

Modified [-[MKLocalSearch initWithRequest:]](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452759-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRequest:(MKLocalSearchRequest *)request ``` |
| To | ``` - (instancetype _Nonnull)initWithRequest:(MKLocalSearchRequest * _Nonnull)request ``` |

Modified [-[MKLocalSearch startWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452652-startwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startWithCompletionHandler:(MKLocalSearchCompletionHandler)completionHandler ``` |
| To | ``` - (void)startWithCompletionHandler:(MKLocalSearchCompletionHandler _Nonnull)completionHandler ``` |

#### MKLocalSearchRequest.h

Modified [MKLocalSearchRequest.naturalLanguageQuery](https://developer.apple.com/documentation/mapkit/mklocalsearchrequest/1452353-naturallanguagequery)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *naturalLanguageQuery ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *naturalLanguageQuery ``` |

#### MKLocalSearchResponse.h

Modified [MKLocalSearchResponse.mapItems](https://developer.apple.com/documentation/mapkit/mklocalsearchresponse/1451939-mapitems)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *mapItems ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<MKMapItem *> *mapItems ``` |

#### MKMapCamera.h

Added [+[MKMapCamera cameraLookingAtCenterCoordinate:fromDistance:pitch:heading:]](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411079-cameralookingatcentercoordinate)Modified [+[MKMapCamera camera]](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411085-camera)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)camera ``` |
| To | ``` + (instancetype _Nonnull)camera ``` |

Modified [+[MKMapCamera cameraLookingAtCenterCoordinate:fromEyeCoordinate:eyeAltitude:]](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411092-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)cameraLookingAtCenterCoordinate:(CLLocationCoordinate2D)centerCoordinate fromEyeCoordinate:(CLLocationCoordinate2D)eyeCoordinate eyeAltitude:(CLLocationDistance)eyeAltitude ``` |
| To | ``` + (instancetype _Nonnull)cameraLookingAtCenterCoordinate:(CLLocationCoordinate2D)centerCoordinate fromEyeCoordinate:(CLLocationCoordinate2D)eyeCoordinate eyeAltitude:(CLLocationDistance)eyeAltitude ``` |

#### MKMapItem.h

Added [MKMapItem.timeZone](https://developer.apple.com/documentation/mapkit/mkmapitem/1452431-timezone)Added [MKLaunchOptionsDirectionsModeTransit](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodetransit)Modified [-[MKMapItem initWithPlacemark:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452285-initwithplacemark)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPlacemark:(MKPlacemark *)placemark ``` |
| To | ``` - (instancetype _Nonnull)initWithPlacemark:(MKPlacemark * _Nonnull)placemark ``` |

Modified [+[MKMapItem mapItemForCurrentLocation]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452002-mapitemforcurrentlocation)

|  | Declaration |
| --- | --- |
| From | ``` + (MKMapItem *)mapItemForCurrentLocation ``` |
| To | ``` + (MKMapItem * _Nonnull)mapItemForCurrentLocation ``` |

Modified [MKMapItem.name](https://developer.apple.com/documentation/mapkit/mkmapitem/1452339-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *name ``` |

Modified [-[MKMapItem openInMapsWithLaunchOptions:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452239-openinmapswithlaunchoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)openInMapsWithLaunchOptions:(NSDictionary *)launchOptions ``` |
| To | ``` - (BOOL)openInMapsWithLaunchOptions:(NSDictionary<NSString *,id> * _Nullable)launchOptions ``` |

Modified [+[MKMapItem openMapsWithItems:launchOptions:]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452207-openmapswithitems)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)openMapsWithItems:(NSArray *)mapItems launchOptions:(NSDictionary *)launchOptions ``` |
| To | ``` + (BOOL)openMapsWithItems:(NSArray<MKMapItem *> * _Nonnull)mapItems launchOptions:(NSDictionary<NSString *,id> * _Nullable)launchOptions ``` |

Modified [MKMapItem.phoneNumber](https://developer.apple.com/documentation/mapkit/mkmapitem/1452088-phonenumber)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *phoneNumber ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *phoneNumber ``` |

Modified [MKMapItem.placemark](https://developer.apple.com/documentation/mapkit/mkmapitem/1452134-placemark)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKPlacemark *placemark ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKPlacemark *placemark ``` |

Modified [MKMapItem.url](https://developer.apple.com/documentation/mapkit/mkmapitem/1452746-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, strong) NSURL *url ``` |
| To | ``` @property(nonatomic, strong, nullable) NSURL *url ``` |

#### MKMapSnapshot.h

Modified [MKMapSnapshot.image](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/snapshot/1452701-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSImage *image ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSImage *image ``` |

#### MKMapSnapshotOptions.h

Modified [MKMapSnapshotOptions.camera](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452082-camera)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) MKMapCamera *camera ``` |
| To | ``` @property(nonatomic, copy, nonnull) MKMapCamera *camera ``` |

#### MKMapSnapshotter.h

Modified [-[MKMapSnapshotter initWithOptions:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452090-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithOptions:(MKMapSnapshotOptions *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithOptions:(MKMapSnapshotOptions * _Nonnull)options ``` |

Modified [-[MKMapSnapshotter startWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452479-start)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startWithCompletionHandler:(MKMapSnapshotCompletionHandler)completionHandler ``` |
| To | ``` - (void)startWithCompletionHandler:(MKMapSnapshotCompletionHandler _Nonnull)completionHandler ``` |

Modified [-[MKMapSnapshotter startWithQueue:completionHandler:]](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452419-start)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startWithQueue:(dispatch_queue_t)queue completionHandler:(MKMapSnapshotCompletionHandler)completionHandler ``` |
| To | ``` - (void)startWithQueue:(dispatch_queue_t _Nonnull)queue completionHandler:(MKMapSnapshotCompletionHandler _Nonnull)completionHandler ``` |

#### MKMapView.h

Added [MKMapView.showsTraffic](https://developer.apple.com/documentation/mapkit/mkmapview/1452433-showstraffic)Modified [-[MKMapView addAnnotation:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452069-addannotation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAnnotation:(id<MKAnnotation>)annotation ``` |
| To | ``` - (void)addAnnotation:(id<MKAnnotation> _Nonnull)annotation ``` |

Modified [-[MKMapView addAnnotations:]](https://developer.apple.com/documentation/mapkit/mkmapview/1451889-addannotations)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAnnotations:(NSArray *)annotations ``` |
| To | ``` - (void)addAnnotations:(NSArray<id<MKAnnotation>> * _Nonnull)annotations ``` |

Modified [-[MKMapView addOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1451964-addoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOverlay:(id<MKOverlay>)overlay ``` |
| To | ``` - (void)addOverlay:(id<MKOverlay> _Nonnull)overlay ``` |

Modified [-[MKMapView addOverlay:level:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452635-addoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addOverlay:(id<MKOverlay>)overlay level:(MKOverlayLevel)level ``` |
| To | ``` - (void)addOverlay:(id<MKOverlay> _Nonnull)overlay level:(MKOverlayLevel)level ``` |

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

Modified [MKMapView.camera](https://developer.apple.com/documentation/mapkit/mkmapview/1452277-camera)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) MKMapCamera *camera ``` |
| To | ``` @property(nonatomic, copy, nonnull) MKMapCamera *camera ``` |

Modified [-[MKMapView convertCoordinate:toPointToView:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452694-convertcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)convertCoordinate:(CLLocationCoordinate2D)coordinate toPointToView:(NSView *)view ``` |
| To | ``` - (CGPoint)convertCoordinate:(CLLocationCoordinate2D)coordinate toPointToView:(NSView * _Nullable)view ``` |

Modified [-[MKMapView convertPoint:toCoordinateFromView:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452503-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (CLLocationCoordinate2D)convertPoint:(CGPoint)point toCoordinateFromView:(NSView *)view ``` |
| To | ``` - (CLLocationCoordinate2D)convertPoint:(CGPoint)point toCoordinateFromView:(NSView * _Nullable)view ``` |

Modified [-[MKMapView convertRect:toRegionFromView:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452305-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (MKCoordinateRegion)convertRect:(CGRect)rect toRegionFromView:(NSView *)view ``` |
| To | ``` - (MKCoordinateRegion)convertRect:(CGRect)rect toRegionFromView:(NSView * _Nullable)view ``` |

Modified [-[MKMapView convertRegion:toRectToView:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452055-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (CGRect)convertRegion:(MKCoordinateRegion)region toRectToView:(NSView *)view ``` |
| To | ``` - (CGRect)convertRegion:(MKCoordinateRegion)region toRectToView:(NSView * _Nullable)view ``` |

Modified [MKMapView.delegate](https://developer.apple.com/documentation/mapkit/mkmapview/1452115-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, weak) id<MKMapViewDelegate> delegate ``` |
| To | ``` @property(nonatomic, weak, nullable) id<MKMapViewDelegate> delegate ``` |

Modified [-[MKMapView dequeueReusableAnnotationViewWithIdentifier:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452672-dequeuereusableannotationviewwit)

|  | Declaration |
| --- | --- |
| From | ``` - (MKAnnotationView *)dequeueReusableAnnotationViewWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (MKAnnotationView * _Nullable)dequeueReusableAnnotationViewWithIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [-[MKMapView deselectAnnotation:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1451988-deselectannotation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deselectAnnotation:(id<MKAnnotation>)annotation animated:(BOOL)animated ``` |
| To | ``` - (void)deselectAnnotation:(id<MKAnnotation> _Nullable)annotation animated:(BOOL)animated ``` |

Modified [-[MKMapView exchangeOverlay:withOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452491-exchangeoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)exchangeOverlay:(id<MKOverlay>)overlay1 withOverlay:(id<MKOverlay>)overlay2 ``` |
| To | ``` - (void)exchangeOverlay:(id<MKOverlay> _Nonnull)overlay1 withOverlay:(id<MKOverlay> _Nonnull)overlay2 ``` |

Modified [-[MKMapView insertOverlay:aboveOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452427-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertOverlay:(id<MKOverlay>)overlay aboveOverlay:(id<MKOverlay>)sibling ``` |
| To | ``` - (void)insertOverlay:(id<MKOverlay> _Nonnull)overlay aboveOverlay:(id<MKOverlay> _Nonnull)sibling ``` |

Modified [-[MKMapView insertOverlay:atIndex:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452249-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertOverlay:(id<MKOverlay>)overlay atIndex:(NSUInteger)index ``` |
| To | ``` - (void)insertOverlay:(id<MKOverlay> _Nonnull)overlay atIndex:(NSUInteger)index ``` |

Modified [-[MKMapView insertOverlay:atIndex:level:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452723-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertOverlay:(id<MKOverlay>)overlay atIndex:(NSUInteger)index level:(MKOverlayLevel)level ``` |
| To | ``` - (void)insertOverlay:(id<MKOverlay> _Nonnull)overlay atIndex:(NSUInteger)index level:(MKOverlayLevel)level ``` |

Modified [-[MKMapView insertOverlay:belowOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452526-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertOverlay:(id<MKOverlay>)overlay belowOverlay:(id<MKOverlay>)sibling ``` |
| To | ``` - (void)insertOverlay:(id<MKOverlay> _Nonnull)overlay belowOverlay:(id<MKOverlay> _Nonnull)sibling ``` |

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

Modified [-[MKMapView removeAnnotation:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452409-removeannotation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAnnotation:(id<MKAnnotation>)annotation ``` |
| To | ``` - (void)removeAnnotation:(id<MKAnnotation> _Nonnull)annotation ``` |

Modified [-[MKMapView removeAnnotations:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452130-removeannotations)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAnnotations:(NSArray *)annotations ``` |
| To | ``` - (void)removeAnnotations:(NSArray<id<MKAnnotation>> * _Nonnull)annotations ``` |

Modified [-[MKMapView removeOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1451921-removeoverlay)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeOverlay:(id<MKOverlay>)overlay ``` |
| To | ``` - (void)removeOverlay:(id<MKOverlay> _Nonnull)overlay ``` |

Modified [-[MKMapView removeOverlays:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452719-removeoverlays)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeOverlays:(NSArray *)overlays ``` |
| To | ``` - (void)removeOverlays:(NSArray<id<MKOverlay>> * _Nonnull)overlays ``` |

Modified [-[MKMapView rendererForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452464-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (MKOverlayRenderer *)rendererForOverlay:(id<MKOverlay>)overlay ``` |
| To | ``` - (MKOverlayRenderer * _Nullable)rendererForOverlay:(id<MKOverlay> _Nonnull)overlay ``` |

Modified [-[MKMapView selectAnnotation:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1451950-selectannotation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectAnnotation:(id<MKAnnotation>)annotation animated:(BOOL)animated ``` |
| To | ``` - (void)selectAnnotation:(id<MKAnnotation> _Nonnull)annotation animated:(BOOL)animated ``` |

Modified [MKMapView.selectedAnnotations](https://developer.apple.com/documentation/mapkit/mkmapview/1452570-selectedannotations)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *selectedAnnotations ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<id<MKAnnotation>> *selectedAnnotations ``` |

Modified [-[MKMapView setCamera:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452476-setcamera)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setCamera:(MKMapCamera *)camera animated:(BOOL)animated ``` |
| To | ``` - (void)setCamera:(MKMapCamera * _Nonnull)camera animated:(BOOL)animated ``` |

Modified [-[MKMapView showAnnotations:animated:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452309-showannotations)

|  | Declaration |
| --- | --- |
| From | ``` - (void)showAnnotations:(NSArray *)annotations animated:(BOOL)animated ``` |
| To | ``` - (void)showAnnotations:(NSArray<id<MKAnnotation>> * _Nonnull)annotations animated:(BOOL)animated ``` |

Modified [MKMapView.userLocation](https://developer.apple.com/documentation/mapkit/mkmapview/1452459-userlocation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKUserLocation *userLocation ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKUserLocation *userLocation ``` |

Modified [-[MKMapView viewForAnnotation:]](https://developer.apple.com/documentation/mapkit/mkmapview/1452512-viewforannotation)

|  | Declaration |
| --- | --- |
| From | ``` - (MKAnnotationView *)viewForAnnotation:(id<MKAnnotation>)annotation ``` |
| To | ``` - (MKAnnotationView * _Nullable)viewForAnnotation:(id<MKAnnotation> _Nonnull)annotation ``` |

Modified [-[MKMapViewDelegate mapView:annotationView:didChangeDragState:fromOldState:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452229-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView annotationView:(MKAnnotationView *)view didChangeDragState:(MKAnnotationViewDragState)newState fromOldState:(MKAnnotationViewDragState)oldState ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView annotationView:(MKAnnotationView * _Nonnull)view didChangeDragState:(MKAnnotationViewDragState)newState fromOldState:(MKAnnotationViewDragState)oldState ``` |

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

Modified [-[MKMapViewDelegate mapView:didDeselectAnnotationView:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452707-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView didDeselectAnnotationView:(MKAnnotationView *)view ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView didDeselectAnnotationView:(MKAnnotationView * _Nonnull)view ``` |

Modified [-[MKMapViewDelegate mapView:didFailToLocateUserWithError:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452211-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView didFailToLocateUserWithError:(NSError *)error ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView didFailToLocateUserWithError:(NSError * _Nonnull)error ``` |

Modified [-[MKMapViewDelegate mapView:didSelectAnnotationView:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452393-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView didSelectAnnotationView:(MKAnnotationView *)view ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView didSelectAnnotationView:(MKAnnotationView * _Nonnull)view ``` |

Modified [-[MKMapViewDelegate mapView:didUpdateUserLocation:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452086-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView didUpdateUserLocation:(MKUserLocation *)userLocation ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView didUpdateUserLocation:(MKUserLocation * _Nonnull)userLocation ``` |

Modified [-[MKMapViewDelegate mapView:regionDidChangeAnimated:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452345-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView regionDidChangeAnimated:(BOOL)animated ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView regionDidChangeAnimated:(BOOL)animated ``` |

Modified [-[MKMapViewDelegate mapView:regionWillChangeAnimated:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452571-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapView:(MKMapView *)mapView regionWillChangeAnimated:(BOOL)animated ``` |
| To | ``` - (void)mapView:(MKMapView * _Nonnull)mapView regionWillChangeAnimated:(BOOL)animated ``` |

Modified [-[MKMapViewDelegate mapView:rendererForOverlay:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (MKOverlayRenderer *)mapView:(MKMapView *)mapView rendererForOverlay:(id<MKOverlay>)overlay ``` |
| To | ``` - (MKOverlayRenderer * _Nonnull)mapView:(MKMapView * _Nonnull)mapView rendererForOverlay:(id<MKOverlay> _Nonnull)overlay ``` |

Modified [-[MKMapViewDelegate mapView:viewForAnnotation:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview)

|  | Declaration |
| --- | --- |
| From | ``` - (MKAnnotationView *)mapView:(MKMapView *)mapView viewForAnnotation:(id<MKAnnotation>)annotation ``` |
| To | ``` - (MKAnnotationView * _Nullable)mapView:(MKMapView * _Nonnull)mapView viewForAnnotation:(id<MKAnnotation> _Nonnull)annotation ``` |

Modified [-[MKMapViewDelegate mapViewDidFailLoadingMap:withError:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452327-mapviewdidfailloadingmap)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapViewDidFailLoadingMap:(MKMapView *)mapView withError:(NSError *)error ``` |
| To | ``` - (void)mapViewDidFailLoadingMap:(MKMapView * _Nonnull)mapView withError:(NSError * _Nonnull)error ``` |

Modified [-[MKMapViewDelegate mapViewDidFinishLoadingMap:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452291-mapviewdidfinishloadingmap)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapViewDidFinishLoadingMap:(MKMapView *)mapView ``` |
| To | ``` - (void)mapViewDidFinishLoadingMap:(MKMapView * _Nonnull)mapView ``` |

Modified [-[MKMapViewDelegate mapViewDidFinishRenderingMap:fullyRendered:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451897-mapviewdidfinishrenderingmap)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapViewDidFinishRenderingMap:(MKMapView *)mapView fullyRendered:(BOOL)fullyRendered ``` |
| To | ``` - (void)mapViewDidFinishRenderingMap:(MKMapView * _Nonnull)mapView fullyRendered:(BOOL)fullyRendered ``` |

Modified [-[MKMapViewDelegate mapViewDidStopLocatingUser:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452715-mapviewdidstoplocatinguser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapViewDidStopLocatingUser:(MKMapView *)mapView ``` |
| To | ``` - (void)mapViewDidStopLocatingUser:(MKMapView * _Nonnull)mapView ``` |

Modified [-[MKMapViewDelegate mapViewWillStartLoadingMap:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452744-mapviewwillstartloadingmap)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapViewWillStartLoadingMap:(MKMapView *)mapView ``` |
| To | ``` - (void)mapViewWillStartLoadingMap:(MKMapView * _Nonnull)mapView ``` |

Modified [-[MKMapViewDelegate mapViewWillStartLocatingUser:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452171-mapviewwillstartlocatinguser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapViewWillStartLocatingUser:(MKMapView *)mapView ``` |
| To | ``` - (void)mapViewWillStartLocatingUser:(MKMapView * _Nonnull)mapView ``` |

Modified [-[MKMapViewDelegate mapViewWillStartRenderingMap:]](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451970-mapviewwillstartrenderingmap)

|  | Declaration |
| --- | --- |
| From | ``` - (void)mapViewWillStartRenderingMap:(MKMapView *)mapView ``` |
| To | ``` - (void)mapViewWillStartRenderingMap:(MKMapView * _Nonnull)mapView ``` |

#### MKMultiPoint.h

Modified [-[MKMultiPoint getCoordinates:range:]](https://developer.apple.com/documentation/mapkit/mkmultipoint/1451911-getcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` - (void)getCoordinates:(CLLocationCoordinate2D *)coords range:(NSRange)range ``` |
| To | ``` - (void)getCoordinates:(CLLocationCoordinate2D * _Nonnull)coords range:(NSRange)range ``` |

Modified [-[MKMultiPoint points]](https://developer.apple.com/documentation/mapkit/mkmultipoint/1452425-points)

|  | Declaration |
| --- | --- |
| From | ``` - (MKMapPoint *)points ``` |
| To | ``` - (MKMapPoint * _Nonnull)points ``` |

#### MKOverlayPathRenderer.h

Modified [-[MKOverlayPathRenderer applyFillPropertiesToContext:atZoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452281-applyfillproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (void)applyFillPropertiesToContext:(CGContextRef)context atZoomScale:(MKZoomScale)zoomScale ``` |
| To | ``` - (void)applyFillPropertiesToContext:(CGContextRef _Nonnull)context atZoomScale:(MKZoomScale)zoomScale ``` |

Modified [-[MKOverlayPathRenderer applyStrokePropertiesToContext:atZoomScale:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452713-applystrokeproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (void)applyStrokePropertiesToContext:(CGContextRef)context atZoomScale:(MKZoomScale)zoomScale ``` |
| To | ``` - (void)applyStrokePropertiesToContext:(CGContextRef _Nonnull)context atZoomScale:(MKZoomScale)zoomScale ``` |

Modified [MKOverlayPathRenderer.fillColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452668-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSColor *fillColor ``` |
| To | ``` @property(strong, nullable) NSColor *fillColor ``` |

Modified [-[MKOverlayPathRenderer fillPath:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452100-fillpath)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fillPath:(CGPathRef)path inContext:(CGContextRef)context ``` |
| To | ``` - (void)fillPath:(CGPathRef _Nonnull)path inContext:(CGContextRef _Nonnull)context ``` |

Modified [MKOverlayPathRenderer.lineDashPattern](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452493-linedashpattern)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *lineDashPattern ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *lineDashPattern ``` |

Modified [MKOverlayPathRenderer.path](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1451875-path)

|  | Declaration |
| --- | --- |
| From | ``` @property CGPathRef path ``` |
| To | ``` @property CGPathRef _Null_unspecified path ``` |

Modified [MKOverlayPathRenderer.strokeColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452175-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) NSColor *strokeColor ``` |
| To | ``` @property(strong, nullable) NSColor *strokeColor ``` |

Modified [-[MKOverlayPathRenderer strokePath:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452549-strokepath)

|  | Declaration |
| --- | --- |
| From | ``` - (void)strokePath:(CGPathRef)path inContext:(CGContextRef)context ``` |
| To | ``` - (void)strokePath:(CGPathRef _Nonnull)path inContext:(CGContextRef _Nonnull)context ``` |

#### MKOverlayRenderer.h

Modified [-[MKOverlayRenderer drawMapRect:zoomScale:inContext:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452184-draw)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawMapRect:(MKMapRect)mapRect zoomScale:(MKZoomScale)zoomScale inContext:(CGContextRef)context ``` |
| To | ``` - (void)drawMapRect:(MKMapRect)mapRect zoomScale:(MKZoomScale)zoomScale inContext:(CGContextRef _Nonnull)context ``` |

Modified [-[MKOverlayRenderer initWithOverlay:]](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451915-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithOverlay:(id<MKOverlay>)overlay ``` |
| To | ``` - (instancetype _Nonnull)initWithOverlay:(id<MKOverlay> _Nonnull)overlay ``` |

Modified [MKOverlayRenderer.overlay](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452307-overlay)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) id<MKOverlay> overlay ``` |
| To | ``` @property(nonatomic, readonly, nonnull) id<MKOverlay> overlay ``` |

#### MKPinAnnotationView.h

Added [+[MKPinAnnotationView greenPinColor]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452568-greenpincolor)Added [MKPinAnnotationView.pinTintColor](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452042-pintintcolor)Added [+[MKPinAnnotationView purplePinColor]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452110-purplepincolor)Added [+[MKPinAnnotationView redPinColor]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1451990-redpincolor)Modified [MKPinAnnotationView.pinColor](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452530-pincolor)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [MKPinAnnotationColorGreen](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor/green)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [MKPinAnnotationColorPurple](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor/purple)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [MKPinAnnotationColorRed](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor/mkpinannotationcolorred)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### MKPlacemark.h

Modified [MKPlacemark.countryCode](https://developer.apple.com/documentation/mapkit/mkplacemark/1451952-countrycode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *countryCode ``` |
| To | ``` @property(nonatomic, readonly, nullable) NSString *countryCode ``` |

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

Modified [+[MKPolygon polygonWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452497-polygonwithcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |
| To | ``` + (instancetype _Nonnull)polygonWithCoordinates:(CLLocationCoordinate2D * _Nonnull)coords count:(NSUInteger)count ``` |

Modified [+[MKPolygon polygonWithCoordinates:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452532-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |
| To | ``` + (instancetype _Nonnull)polygonWithCoordinates:(CLLocationCoordinate2D * _Nonnull)coords count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> * _Nullable)interiorPolygons ``` |

Modified [+[MKPolygon polygonWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1452247-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count ``` |
| To | ``` + (instancetype _Nonnull)polygonWithPoints:(MKMapPoint * _Nonnull)points count:(NSUInteger)count ``` |

Modified [+[MKPolygon polygonWithPoints:count:interiorPolygons:]](https://developer.apple.com/documentation/mapkit/mkpolygon/1451945-polygonwithpoints)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polygonWithPoints:(MKMapPoint *)points count:(NSUInteger)count interiorPolygons:(NSArray *)interiorPolygons ``` |
| To | ``` + (instancetype _Nonnull)polygonWithPoints:(MKMapPoint * _Nonnull)points count:(NSUInteger)count interiorPolygons:(NSArray<MKPolygon *> * _Nullable)interiorPolygons ``` |

#### MKPolygonRenderer.h

Modified [-[MKPolygonRenderer initWithPolygon:]](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/1448129-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPolygon:(MKPolygon *)polygon ``` |
| To | ``` - (instancetype _Nonnull)initWithPolygon:(MKPolygon * _Nonnull)polygon ``` |

Modified [MKPolygonRenderer.polygon](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/1448132-polygon)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKPolygon *polygon ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKPolygon *polygon ``` |

#### MKPolyline.h

Modified [+[MKPolyline polylineWithCoordinates:count:]](https://developer.apple.com/documentation/mapkit/mkpolyline/1452205-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polylineWithCoordinates:(CLLocationCoordinate2D *)coords count:(NSUInteger)count ``` |
| To | ``` + (instancetype _Nonnull)polylineWithCoordinates:(CLLocationCoordinate2D * _Nonnull)coords count:(NSUInteger)count ``` |

Modified [+[MKPolyline polylineWithPoints:count:]](https://developer.apple.com/documentation/mapkit/mkpolyline/1452773-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)polylineWithPoints:(MKMapPoint *)points count:(NSUInteger)count ``` |
| To | ``` + (instancetype _Nonnull)polylineWithPoints:(MKMapPoint * _Nonnull)points count:(NSUInteger)count ``` |

#### MKPolylineRenderer.h

Modified [-[MKPolylineRenderer initWithPolyline:]](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452074-initwithpolyline)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPolyline:(MKPolyline *)polyline ``` |
| To | ``` - (instancetype _Nonnull)initWithPolyline:(MKPolyline * _Nonnull)polyline ``` |

Modified [MKPolylineRenderer.polyline](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452465-polyline)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) MKPolyline *polyline ``` |
| To | ``` @property(nonatomic, readonly, nonnull) MKPolyline *polyline ``` |

#### MKShape.h

Modified [MKShape.subtitle](https://developer.apple.com/documentation/mapkit/mkshape/1437592-subtitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *subtitle ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *subtitle ``` |

Modified [MKShape.title](https://developer.apple.com/documentation/mapkit/mkshape/1437594-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *title ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *title ``` |

#### MKTileOverlay.h

Modified [-[MKTileOverlay initWithURLTemplate:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452705-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithURLTemplate:(NSString *)URLTemplate ``` |
| To | ``` - (instancetype _Nonnull)initWithURLTemplate:(NSString * _Nullable)URLTemplate ``` |

Modified [-[MKTileOverlay loadTileAtPath:result:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452445-loadtileatpath)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadTileAtPath:(MKTileOverlayPath)path result:(void (^)(NSData *tileData, NSError *error))result ``` |
| To | ``` - (void)loadTileAtPath:(MKTileOverlayPath)path result:(void (^ _Nonnull)(NSData * _Nullable tileData, NSError * _Nullable error))result ``` |

Modified [-[MKTileOverlay URLForTilePath:]](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452606-url)

|  | Declaration |
| --- | --- |
| From | ``` - (NSURL *)URLForTilePath:(MKTileOverlayPath)path ``` |
| To | ``` - (NSURL * _Nonnull)URLForTilePath:(MKTileOverlayPath)path ``` |

Modified [MKTileOverlay.URLTemplate](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452256-urltemplate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *URLTemplate ``` |
| To | ``` @property(readonly, nullable) NSString *URLTemplate ``` |

#### MKTileOverlayRenderer.h

Modified [-[MKTileOverlayRenderer initWithTileOverlay:]](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/1452303-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithTileOverlay:(MKTileOverlay *)overlay ``` |
| To | ``` - (instancetype _Nonnull)initWithTileOverlay:(MKTileOverlay * _Nonnull)overlay ``` |

#### MKTypes.h

Added [MKMapTypeHybridFlyover](https://developer.apple.com/documentation/mapkit/mkmaptype/hybridflyover)Added [MKMapTypeSatelliteFlyover](https://developer.apple.com/documentation/mapkit/mkmaptype/mkmaptypesatelliteflyover)

#### MKUserLocation.h

Modified [MKUserLocation.heading](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452721-heading)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CLHeading *heading ``` |
| To | ``` @property(readonly, nonatomic, nullable) CLHeading *heading ``` |

Modified [MKUserLocation.location](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452415-location)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) CLLocation *location ``` |
| To | ``` @property(readonly, nonatomic, nullable) CLLocation *location ``` |

Modified [MKUserLocation.subtitle](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452562-subtitle)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *subtitle ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *subtitle ``` |

Modified [MKUserLocation.title](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452058-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *title ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *title ``` |

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
