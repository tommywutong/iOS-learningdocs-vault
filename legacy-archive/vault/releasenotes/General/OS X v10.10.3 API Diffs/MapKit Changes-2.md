---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/MapKit.html
archived_at: '2026-07-18T02:52:33.464801Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# MapKit Changes

## MapKit

Removed MKAnnotation.setCoordinate(CLLocationCoordinate2D)Removed MKDirectionsTransportType.valueAdded MKCoordinateRegion.init()Added MKCoordinateRegion.init(center: CLLocationCoordinate2D, span: MKCoordinateSpan)Added MKCoordinateSpan.init()Added MKCoordinateSpan.init(latitudeDelta: CLLocationDegrees, longitudeDelta: CLLocationDegrees)Added MKDirectionsTransportType.init(rawValue: UInt)Added MKMapPoint.init()Added MKMapPoint.init(x: Double, y: Double)Added MKMapRect.init()Added MKMapRect.init(origin: MKMapPoint, size: MKMapSize)Added MKMapSize.init()Added MKMapSize.init(width: Double, height: Double)Added MKTileOverlayPath.init()Added MKTileOverlayPath.init(x: Int, y: Int, z: Int, contentScaleFactor: CGFloat)Added NSValue.init(MKCoordinate: CLLocationCoordinate2D)Added NSValue.init(MKCoordinateSpan: MKCoordinateSpan)Added NSValue.MKCoordinateSpanValueAdded NSValue.MKCoordinateValueModified MKAnnotation.subtitle

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKAnnotation.title

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKAnnotationView

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKAnnotationView.init(annotation: MKAnnotation!, reuseIdentifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(annotation annotation: MKAnnotation!, reuseIdentifier reuseIdentifier: String!) ``` |
| To | ``` init!(annotation annotation: MKAnnotation!, reuseIdentifier reuseIdentifier: String!) ``` |

Modified MKAnnotationView.dragState

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKAnnotationView.draggable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKAnnotationView.setDragState(MKAnnotationViewDragState, animated: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKAnnotationViewDragState [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKCircle

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

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
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKCircleRenderer.init(circle: MKCircle!)

|  | Declaration |
| --- | --- |
| From | ``` init(circle circle: MKCircle!) ``` |
| To | ``` init!(circle circle: MKCircle!) ``` |

Modified MKCoordinateRegion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKCoordinateRegion {     var center: CLLocationCoordinate2D     var span: MKCoordinateSpan } ``` |
| To | ``` struct MKCoordinateRegion {     var center: CLLocationCoordinate2D     var span: MKCoordinateSpan     init()     init(center center: CLLocationCoordinate2D, span span: MKCoordinateSpan) } ``` |

Modified MKCoordinateSpan [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKCoordinateSpan {     var latitudeDelta: CLLocationDegrees     var longitudeDelta: CLLocationDegrees } ``` |
| To | ``` struct MKCoordinateSpan {     var latitudeDelta: CLLocationDegrees     var longitudeDelta: CLLocationDegrees     init()     init(latitudeDelta latitudeDelta: CLLocationDegrees, longitudeDelta longitudeDelta: CLLocationDegrees) } ``` |

Modified MKDirections

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirections.init(request: MKDirectionsRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: MKDirectionsRequest!) ``` |
| To | ``` init!(request request: MKDirectionsRequest!) ``` |

Modified MKDirectionsRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsRequest.arrivalDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var arrivalDate: NSDate! ``` | OS X 10.10 |
| To | ``` @NSCopying var arrivalDate: NSDate! ``` | OS X 10.9 |

Modified MKDirectionsRequest.init(contentsOfURL: NSURL!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(contentsOfURL url: NSURL!) ``` | OS X 10.10 |
| To | ``` init!(contentsOfURL url: NSURL!) ``` | OS X 10.9 |

Modified MKDirectionsRequest.departureDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var departureDate: NSDate! ``` | OS X 10.10 |
| To | ``` @NSCopying var departureDate: NSDate! ``` | OS X 10.9 |

Modified MKDirectionsRequest.destination() -> MKMapItem!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsRequest.isDirectionsRequestURL(NSURL!) -> Bool [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsRequest.requestsAlternateRoutes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsRequest.setDestination(MKMapItem!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsRequest.setSource(MKMapItem!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsRequest.source() -> MKMapItem!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsRequest.transportType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsResponse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDirectionsTransportType [struct]

|  | Declaration | Protocols | Introduction |
| --- | --- | --- | --- |
| From | ``` struct MKDirectionsTransportType : RawOptionSet {     init(_ value: UInt)     var value: UInt     static var Automobile: MKDirectionsTransportType { get }     static var Walking: MKDirectionsTransportType { get }     static var Any: MKDirectionsTransportType { get } } ``` | RawOptionSet | OS X 10.10 |
| To | ``` struct MKDirectionsTransportType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Automobile: MKDirectionsTransportType { get }     static var Walking: MKDirectionsTransportType { get }     static var Any: MKDirectionsTransportType { get } } ``` | RawOptionSetType | OS X 10.9 |

Modified MKDirectionsTransportType.init(_: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt) ``` |
| To | ``` init(_ rawValue: UInt) ``` |

Modified MKDistanceFormatter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDistanceFormatter.locale

|  | Declaration |
| --- | --- |
| From | ``` var locale: NSLocale! ``` |
| To | ``` @NSCopying var locale: NSLocale! ``` |

Modified MKDistanceFormatterUnitStyle [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKDistanceFormatterUnits [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKETAResponse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKErrorCode [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKErrorCode.DirectionsNotFound

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKGeodesicPolyline

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKGeodesicPolyline.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified MKGeodesicPolyline.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified MKLocalSearch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKLocalSearch.init(request: MKLocalSearchRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(request request: MKLocalSearchRequest!) ``` |
| To | ``` init!(request request: MKLocalSearchRequest!) ``` |

Modified MKLocalSearchRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKLocalSearchResponse

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapCamera

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapCamera.init(lookingAtCenterCoordinate: CLLocationCoordinate2D, fromEyeCoordinate: CLLocationCoordinate2D, eyeAltitude: CLLocationDistance)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) ``` |
| To | ``` convenience init!(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) ``` |

Modified MKMapItem

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapItem.init(placemark: MKPlacemark!)

|  | Declaration |
| --- | --- |
| From | ``` init(placemark placemark: MKPlacemark!) ``` |
| To | ``` init!(placemark placemark: MKPlacemark!) ``` |

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

Modified MKMapSnapshot

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapSnapshotOptions

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapSnapshotOptions.camera

|  | Declaration |
| --- | --- |
| From | ``` var camera: MKMapCamera! ``` |
| To | ``` @NSCopying var camera: MKMapCamera! ``` |

Modified MKMapSnapshotter

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapSnapshotter.init(options: MKMapSnapshotOptions!)

|  | Declaration |
| --- | --- |
| From | ``` init(options options: MKMapSnapshotOptions!) ``` |
| To | ``` init!(options options: MKMapSnapshotOptions!) ``` |

Modified MKMapType [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.addOverlay(MKOverlay!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.addOverlay(MKOverlay!, level: MKOverlayLevel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.addOverlays([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.addOverlays([AnyObject]!, level: MKOverlayLevel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.annotationsInMapRect(MKMapRect) -> Set<NSObject>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func annotationsInMapRect(_ mapRect: MKMapRect) -> NSSet! ``` | OS X 10.10 |
| To | ``` func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>! ``` | OS X 10.9 |

Modified MKMapView.camera

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var camera: MKMapCamera! ``` | OS X 10.10 |
| To | ``` @NSCopying var camera: MKMapCamera! ``` | OS X 10.9 |

Modified MKMapView.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: MKMapViewDelegate! ``` |
| To | ``` weak var delegate: MKMapViewDelegate! ``` |

Modified MKMapView.exchangeOverlay(MKOverlay!, withOverlay: MKOverlay!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.exchangeOverlayAtIndex(Int, withOverlayAtIndex: Int)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.insertOverlay(MKOverlay!, aboveOverlay: MKOverlay!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.insertOverlay(MKOverlay!, atIndex: Int)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.insertOverlay(MKOverlay!, atIndex: Int, level: MKOverlayLevel)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.insertOverlay(MKOverlay!, belowOverlay: MKOverlay!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.overlays

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.overlaysInLevel(MKOverlayLevel) -> [AnyObject]!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.pitchEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.removeOverlay(MKOverlay!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.removeOverlays([AnyObject]!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.rendererForOverlay(MKOverlay!) -> MKOverlayRenderer!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.rotateEnabled

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.setCamera(MKMapCamera!, animated: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.showAnnotations([AnyObject]!, animated: Bool)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.showsBuildings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.showsCompass

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.showsPointsOfInterest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapView.showsZoomControls

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapViewDelegate.mapView(MKMapView!, annotationView: MKAnnotationView!, didChangeDragState: MKAnnotationViewDragState, fromOldState: MKAnnotationViewDragState)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, didAddAnnotationViews:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, didAddOverlayRenderers:[AnyObject]!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, didDeselectAnnotationView: MKAnnotationView!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, didFailToLocateUserWithError: NSError!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, didSelectAnnotationView: MKAnnotationView!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, didUpdateUserLocation: MKUserLocation!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, regionDidChangeAnimated: Bool)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, regionWillChangeAnimated: Bool)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, rendererForOverlay: MKOverlay!) -> MKOverlayRenderer!

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapView(MKMapView!, viewForAnnotation: MKAnnotation!) -> MKAnnotationView!

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKMapViewDelegate.mapViewDidFailLoadingMap(MKMapView!, withError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKMapViewDelegate.mapViewDidFinishLoadingMap(MKMapView!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKMapViewDelegate.mapViewDidFinishRenderingMap(MKMapView!, fullyRendered: Bool)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapViewDidStopLocatingUser(MKMapView!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapViewWillStartLoadingMap(MKMapView!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKMapViewDelegate.mapViewWillStartLocatingUser(MKMapView!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMapViewDelegate.mapViewWillStartRenderingMap(MKMapView!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKMultiPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMultiPoint.getCoordinates(UnsafeMutablePointer<CLLocationCoordinate2D>, range: NSRange)

|  | Declaration |
| --- | --- |
| From | ``` func getCoordinates(_ coords: UnsafePointer<CLLocationCoordinate2D>, range range: NSRange) ``` |
| To | ``` func getCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, range range: NSRange) ``` |

Modified MKMultiPoint.points() -> UnsafeMutablePointer<MKMapPoint>

|  | Declaration |
| --- | --- |
| From | ``` func points() -> UnsafePointer<MKMapPoint> ``` |
| To | ``` func points() -> UnsafeMutablePointer<MKMapPoint> ``` |

Modified MKOverlay.canReplaceMapContent() -> Bool

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | yes |

Modified MKOverlay.intersectsMapRect(MKMapRect) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MKOverlayLevel [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKOverlayPathRenderer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKOverlayRenderer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKOverlayRenderer.init(overlay: MKOverlay!)

|  | Declaration |
| --- | --- |
| From | ``` init(overlay overlay: MKOverlay!) ``` |
| To | ``` init!(overlay overlay: MKOverlay!) ``` |

Modified MKPinAnnotationColor [enum]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPinAnnotationView

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPlacemark

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPlacemark.init(coordinate: CLLocationCoordinate2D, addressDictionary:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` init!(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [NSObject : AnyObject]!) ``` |

Modified MKPointAnnotation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPolygon

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPolygon.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified MKPolygon.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int, interiorPolygons:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |

Modified MKPolygon.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified MKPolygon.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int, interiorPolygons:[AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |

Modified MKPolygonRenderer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPolygonRenderer.init(polygon: MKPolygon!)

|  | Declaration |
| --- | --- |
| From | ``` init(polygon polygon: MKPolygon!) ``` |
| To | ``` init!(polygon polygon: MKPolygon!) ``` |

Modified MKPolyline

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPolyline.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(coordinates coords: UnsafePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified MKPolyline.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(points points: UnsafePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified MKPolylineRenderer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKPolylineRenderer.init(polyline: MKPolyline!)

|  | Declaration |
| --- | --- |
| From | ``` init(polyline polyline: MKPolyline!) ``` |
| To | ``` init!(polyline polyline: MKPolyline!) ``` |

Modified MKRoute

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKRouteStep

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKShape

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKTileOverlay

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKTileOverlay.init(URLTemplate: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(URLTemplate URLTemplate: String!) ``` |
| To | ``` init!(URLTemplate URLTemplate: String!) ``` |

Modified MKTileOverlayPath [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MKTileOverlayPath {     var x: Int     var y: Int     var z: Int     var contentScaleFactor: CGFloat } ``` |
| To | ``` struct MKTileOverlayPath {     var x: Int     var y: Int     var z: Int     var contentScaleFactor: CGFloat     init()     init(x x: Int, y y: Int, z z: Int, contentScaleFactor contentScaleFactor: CGFloat) } ``` |

Modified MKTileOverlayRenderer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKTileOverlayRenderer.init(tileOverlay: MKTileOverlay!)

|  | Declaration |
| --- | --- |
| From | ``` init(tileOverlay overlay: MKTileOverlay!) ``` |
| To | ``` init!(tileOverlay overlay: MKTileOverlay!) ``` |

Modified MKUserLocation

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKUserLocation.heading

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKAnnotationCalloutInfoDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let MKAnnotationCalloutInfoDidChangeNotification: NSString! ``` |
| To | ``` let MKAnnotationCalloutInfoDidChangeNotification: String ``` |

Modified MKCoordinateForMapPoint(MKMapPoint) -> CLLocationCoordinate2D

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKCoordinateRegionForMapRect(MKMapRect) -> MKCoordinateRegion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

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

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let MKLaunchOptionsDirectionsModeDriving: NSString! ``` | OS X 10.10 |
| To | ``` let MKLaunchOptionsDirectionsModeDriving: String ``` | OS X 10.9 |

Modified MKLaunchOptionsDirectionsModeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let MKLaunchOptionsDirectionsModeKey: NSString! ``` | OS X 10.10 |
| To | ``` let MKLaunchOptionsDirectionsModeKey: String ``` | OS X 10.9 |

Modified MKLaunchOptionsDirectionsModeWalking

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let MKLaunchOptionsDirectionsModeWalking: NSString! ``` | OS X 10.10 |
| To | ``` let MKLaunchOptionsDirectionsModeWalking: String ``` | OS X 10.9 |

Modified MKLaunchOptionsMapCenterKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let MKLaunchOptionsMapCenterKey: NSString! ``` | OS X 10.10 |
| To | ``` let MKLaunchOptionsMapCenterKey: String ``` | OS X 10.9 |

Modified MKLaunchOptionsMapSpanKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let MKLaunchOptionsMapSpanKey: NSString! ``` | OS X 10.10 |
| To | ``` let MKLaunchOptionsMapSpanKey: String ``` | OS X 10.9 |

Modified MKLaunchOptionsMapTypeKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let MKLaunchOptionsMapTypeKey: NSString! ``` | OS X 10.10 |
| To | ``` let MKLaunchOptionsMapTypeKey: String ``` | OS X 10.9 |

Modified MKLaunchOptionsShowsTrafficKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let MKLaunchOptionsShowsTrafficKey: NSString! ``` | OS X 10.10 |
| To | ``` let MKLaunchOptionsShowsTrafficKey: String ``` | OS X 10.9 |

Modified MKMapPointForCoordinate(CLLocationCoordinate2D) -> MKMapPoint

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapPointsPerMeterAtLatitude(CLLocationDegrees) -> Double

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectContainsPoint(MKMapRect, MKMapPoint) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectContainsRect(MKMapRect, MKMapRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectDivide(MKMapRect, UnsafeMutablePointer<MKMapRect>, UnsafeMutablePointer<MKMapRect>, Double, CGRectEdge)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func MKMapRectDivide(_ rect: MKMapRect, _ slice: UnsafePointer<MKMapRect>, _ remainder: UnsafePointer<MKMapRect>, _ amount: Double, _ edge: CGRectEdge) ``` | OS X 10.10 |
| To | ``` func MKMapRectDivide(_ rect: MKMapRect, _ slice: UnsafeMutablePointer<MKMapRect>, _ remainder: UnsafeMutablePointer<MKMapRect>, _ amount: Double, _ edge: CGRectEdge) ``` | OS X 10.9 |

Modified MKMapRectInset(MKMapRect, Double, Double) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectIntersection(MKMapRect, MKMapRect) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectIntersectsRect(MKMapRect, MKMapRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectNull

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectOffset(MKMapRect, Double, Double) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectRemainder(MKMapRect) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectSpans180thMeridian(MKMapRect) -> Bool

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectUnion(MKMapRect, MKMapRect) -> MKMapRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapRectWorld

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMapSizeWorld

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMetersBetweenMapPoints(MKMapPoint, MKMapPoint) -> CLLocationDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKMetersPerMapPointAtLatitude(CLLocationDegrees) -> CLLocationDistance

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified MKRoadWidthAtZoomScale(MKZoomScale) -> CGFloat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

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
