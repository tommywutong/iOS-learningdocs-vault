---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/MapKit.html
archived_at: '2026-07-18T02:56:14.326673Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# MapKit Changes

## MapKit

Removed MKDirectionsTransportType.valueAdded MKDirectionsTransportType.init(rawValue: UInt)Added NSValue.init(MKCoordinate: CLLocationCoordinate2D)Added NSValue.init(MKCoordinateSpan: MKCoordinateSpan)Added NSValue.MKCoordinateSpanValueAdded NSValue.MKCoordinateValueModified MKAnnotation.setCoordinate(CLLocationCoordinate2D)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKAnnotationView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKAnnotationView.init(annotation: MKAnnotation!, reuseIdentifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(annotation annotation: MKAnnotation!, reuseIdentifier reuseIdentifier: String!) ``` |
| To | ``` init!(annotation annotation: MKAnnotation!, reuseIdentifier reuseIdentifier: String!) ``` |

Modified MKAnnotationView.dragState

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKAnnotationView.draggable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKAnnotationView.setDragState(MKAnnotationViewDragState, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MKAnnotationViewDragState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKCircle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKCircle.init(centerCoordinate: CLLocationCoordinate2D, radius: CLLocationDistance)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(centerCoordinate coord: CLLocationCoordinate2D, radius radius: CLLocationDistance) ``` |
| To | ``` convenience init!(centerCoordinate coord: CLLocationCoordinate2D, radius radius: CLLocationDistance) ``` |

Modified MKCircle.init(mapRect: MKMapRect)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(mapRect mapRect: MKMapRect) ``` |
| To | ``` convenience init!(mapRect mapRect: MKMapRect) ``` |

Modified MKCircleRenderer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKCircleRenderer.init(circle: MKCircle!)

|  | Declaration |
| --- | --- |
| From | ``` init(circle circle: MKCircle!) ``` |
| To | ``` init!(circle circle: MKCircle!) ``` |

Modified MKCircleView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKDirections

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirections.init(request: MKDirectionsRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: MKDirectionsRequest!) ``` |
| To | ``` init!(request request: MKDirectionsRequest!) ``` |

Modified MKDirectionsRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKDirectionsRequest.arrivalDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirectionsRequest.init(contentsOfURL: NSURL!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(contentsOfURL url: NSURL!) ``` | iOS 8.0 |
| To | ``` init!(contentsOfURL url: NSURL!) ``` | iOS 6.0 |

Modified MKDirectionsRequest.departureDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirectionsRequest.destination() -> MKMapItem!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKDirectionsRequest.isDirectionsRequestURL(NSURL!) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKDirectionsRequest.requestsAlternateRoutes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirectionsRequest.setDestination(MKMapItem!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirectionsRequest.setSource(MKMapItem!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirectionsRequest.source() -> MKMapItem!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKDirectionsRequest.transportType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirectionsResponse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDirectionsTransportType [struct]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` struct MKDirectionsTransportType : RawOptionSetType {     init(_ value: UInt)     var value: UInt     static var Automobile: MKDirectionsTransportType { get }     static var Walking: MKDirectionsTransportType { get }     static var Any: MKDirectionsTransportType { get } } ``` | iOS 8.0 |
| To | ``` struct MKDirectionsTransportType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Automobile: MKDirectionsTransportType { get }     static var Walking: MKDirectionsTransportType { get }     static var Any: MKDirectionsTransportType { get } } ``` | iOS 7.0 |

Modified MKDirectionsTransportType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MKDistanceFormatter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDistanceFormatterUnitStyle [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKDistanceFormatterUnits [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKETAResponse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKErrorCode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKGeodesicPolyline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKGeodesicPolyline.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified MKGeodesicPolyline.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified MKLocalSearch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.1 |

Modified MKLocalSearch.init(request: MKLocalSearchRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: MKLocalSearchRequest!) ``` |
| To | ``` init!(request request: MKLocalSearchRequest!) ``` |

Modified MKLocalSearchRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.1 |

Modified MKLocalSearchResponse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.1 |

Modified MKMapCamera

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapCamera.init(lookingAtCenterCoordinate: CLLocationCoordinate2D, fromEyeCoordinate: CLLocationCoordinate2D, eyeAltitude: CLLocationDistance)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) ``` |
| To | ``` convenience init!(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) ``` |

Modified MKMapItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKMapItem.init(placemark: MKPlacemark!)

|  | Declaration |
| --- | --- |
| From | ``` init(placemark placemark: MKPlacemark!) ``` |
| To | ``` init!(placemark placemark: MKPlacemark!) ``` |

Modified MKMapSnapshot

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapSnapshotOptions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapSnapshotter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapSnapshotter.init(options: MKMapSnapshotOptions!)

|  | Declaration |
| --- | --- |
| From | ``` init(options options: MKMapSnapshotOptions!) ``` |
| To | ``` init!(options options: MKMapSnapshotOptions!) ``` |

Modified MKMapType [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKMapView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKMapView.addOverlay(MKOverlay!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.addOverlay(MKOverlay!, level: MKOverlayLevel)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.addOverlays([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.addOverlays([AnyObject]!, level: MKOverlayLevel)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.annotationsInMapRect(MKMapRect) -> NSSet!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified MKMapView.camera

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.exchangeOverlay(MKOverlay!, withOverlay: MKOverlay!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.exchangeOverlayAtIndex(Int, withOverlayAtIndex: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.insertOverlay(MKOverlay!, aboveOverlay: MKOverlay!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.insertOverlay(MKOverlay!, atIndex: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.insertOverlay(MKOverlay!, atIndex: Int, level: MKOverlayLevel)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.insertOverlay(MKOverlay!, belowOverlay: MKOverlay!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.overlays

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.overlaysInLevel(MKOverlayLevel) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.pitchEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.removeOverlay(MKOverlay!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.removeOverlays([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapView.rendererForOverlay(MKOverlay!) -> MKOverlayRenderer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.rotateEnabled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.setCamera(MKMapCamera!, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.setUserTrackingMode(MKUserTrackingMode, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MKMapView.showAnnotations([AnyObject]!, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.showsBuildings

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.showsPointsOfInterest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapView.userTrackingMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, annotationView: MKAnnotationView!, didChangeDragState: MKAnnotationViewDragState, fromOldState: MKAnnotationViewDragState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, didAddOverlayRenderers:[AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, didChangeUserTrackingMode: MKUserTrackingMode, animated: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, didDeselectAnnotationView: MKAnnotationView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, didFailToLocateUserWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, didSelectAnnotationView: MKAnnotationView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, didUpdateUserLocation: MKUserLocation!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapViewDelegate.mapView(MKMapView!, rendererForOverlay: MKOverlay!) -> MKOverlayRenderer!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapViewDelegate.mapViewDidFinishRenderingMap(MKMapView!, fullyRendered: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMapViewDelegate.mapViewDidStopLocatingUser(MKMapView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapViewDelegate.mapViewWillStartLocatingUser(MKMapView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapViewDelegate.mapViewWillStartRenderingMap(MKMapView!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKMultiPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKOverlay.canReplaceMapContent() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKOverlayLevel [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKOverlayPathRenderer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKOverlayPathView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKOverlayRenderer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKOverlayRenderer.init(overlay: MKOverlay!)

|  | Declaration |
| --- | --- |
| From | ``` init(overlay overlay: MKOverlay!) ``` |
| To | ``` init!(overlay overlay: MKOverlay!) ``` |

Modified MKOverlayView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKPinAnnotationColor [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKPinAnnotationView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKPlacemark

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKPlacemark.init(coordinate: CLLocationCoordinate2D, addressDictionary:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` init!(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [NSObject : AnyObject]!) ``` |

Modified MKPointAnnotation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKPolygon

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKPolygon.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified MKPolygon.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int, interiorPolygons:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |

Modified MKPolygon.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified MKPolygon.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int, interiorPolygons:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |

Modified MKPolygonRenderer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKPolygonRenderer.init(polygon: MKPolygon!)

|  | Declaration |
| --- | --- |
| From | ``` init(polygon polygon: MKPolygon!) ``` |
| To | ``` init!(polygon polygon: MKPolygon!) ``` |

Modified MKPolygonView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKPolyline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKPolyline.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified MKPolyline.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified MKPolylineRenderer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKPolylineRenderer.init(polyline: MKPolyline!)

|  | Declaration |
| --- | --- |
| From | ``` init(polyline polyline: MKPolyline!) ``` |
| To | ``` init!(polyline polyline: MKPolyline!) ``` |

Modified MKPolylineView

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKRoute

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKRouteStep

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKShape

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKTileOverlay

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKTileOverlay.init(URLTemplate: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(URLTemplate URLTemplate: String!) ``` |
| To | ``` init!(URLTemplate URLTemplate: String!) ``` |

Modified MKTileOverlayRenderer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MKTileOverlayRenderer.init(tileOverlay: MKTileOverlay!)

|  | Declaration |
| --- | --- |
| From | ``` init(tileOverlay overlay: MKTileOverlay!) ``` |
| To | ``` init!(tileOverlay overlay: MKTileOverlay!) ``` |

Modified MKUserLocation

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified MKUserLocation.heading

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MKUserTrackingBarButtonItem

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MKUserTrackingBarButtonItem.init(mapView: MKMapView!)

|  | Declaration |
| --- | --- |
| From | ``` init(mapView mapView: MKMapView!) ``` |
| To | ``` init!(mapView mapView: MKMapView!) ``` |

Modified MKUserTrackingMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified MKCoordinateForMapPoint(MKMapPoint) -> CLLocationCoordinate2D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKCoordinateRegionForMapRect(MKMapRect) -> MKCoordinateRegion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKLaunchOptionsCameraKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified MKLaunchOptionsDirectionsModeDriving

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKLaunchOptionsDirectionsModeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKLaunchOptionsDirectionsModeWalking

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKLaunchOptionsMapCenterKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKLaunchOptionsMapSpanKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKLaunchOptionsMapTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKLaunchOptionsShowsTrafficKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified MKMapPointForCoordinate(CLLocationCoordinate2D) -> MKMapPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapPointsPerMeterAtLatitude(CLLocationDegrees) -> Double

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectContainsPoint(MKMapRect, MKMapPoint) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectContainsRect(MKMapRect, MKMapRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectInset(MKMapRect, Double, Double) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectIntersection(MKMapRect, MKMapRect) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectIntersectsRect(MKMapRect, MKMapRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectNull

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectOffset(MKMapRect, Double, Double) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectRemainder(MKMapRect) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectSpans180thMeridian(MKMapRect) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectUnion(MKMapRect, MKMapRect) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapRectWorld

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMapSizeWorld

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMetersBetweenMapPoints(MKMapPoint, MKMapPoint) -> CLLocationDistance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKMetersPerMapPointAtLatitude(CLLocationDegrees) -> CLLocationDistance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified MKRoadWidthAtZoomScale(MKZoomScale) -> CGFloat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
