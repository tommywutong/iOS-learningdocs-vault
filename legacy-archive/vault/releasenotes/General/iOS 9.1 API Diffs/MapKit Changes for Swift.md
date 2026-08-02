---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/MapKit.html
archived_at: '2026-07-18T02:57:09.210514Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# MapKit Changes for Swift

### MapKit

Modified [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKAnnotationViewDragState [enum]](https://developer.apple.com/documentation/mapkit/mkannotationviewdragstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MKCircle](https://developer.apple.com/documentation/mapkit/mkcircle)

|  | Protocols |
| --- | --- |
| From | AnyObject, MKAnnotation, MKOverlay, NSObjectProtocol |
| To | MKOverlay |

Modified [MKCircleRenderer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKCircleView](https://developer.apple.com/documentation/mapkit/mkcircleview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKDirections](https://developer.apple.com/documentation/mapkit/mkdirections)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKDirectionsRequest](https://developer.apple.com/documentation/mapkit/mkdirections/request)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKDirectionsResponse](https://developer.apple.com/documentation/mapkit/mkdirections/response)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKDistanceFormatter](https://developer.apple.com/documentation/mapkit/mkdistanceformatter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKDistanceFormatterUnits [enum]](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MKDistanceFormatterUnitStyle [enum]](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MKErrorCode [enum]](https://developer.apple.com/documentation/mapkit/mkerror/code)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MKETAResponse](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKGeodesicPolyline](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKLocalSearch](https://developer.apple.com/documentation/mapkit/mklocalsearch)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKLocalSearchRequest](https://developer.apple.com/documentation/mapkit/mklocalsearch/request)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MKLocalSearchResponse](https://developer.apple.com/documentation/mapkit/mklocalsearchresponse)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKMapCamera](https://developer.apple.com/documentation/mapkit/mkmapcamera)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MKMapCamera : NSObject, NSSecureCoding, NSCoding, NSCopying {     var centerCoordinate: CLLocationCoordinate2D     var heading: CLLocationDirection     var pitch: CGFloat     var altitude: CLLocationDistance     convenience init()     class func camera() -> Self     convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance)     class func cameraLookingAtCenterCoordinate(_ centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) -> Self     convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromDistance distance: CLLocationDistance, pitch pitch: CGFloat, heading heading: CLLocationDirection)     class func cameraLookingAtCenterCoordinate(_ centerCoordinate: CLLocationCoordinate2D, fromDistance distance: CLLocationDistance, pitch pitch: CGFloat, heading heading: CLLocationDirection) -> Self } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class MKMapCamera : NSObject, NSSecureCoding, NSCopying {     var centerCoordinate: CLLocationCoordinate2D     var heading: CLLocationDirection     var pitch: CGFloat     var altitude: CLLocationDistance     convenience init()     class func camera() -> Self     convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance)     class func cameraLookingAtCenterCoordinate(_ centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) -> Self     convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromDistance distance: CLLocationDistance, pitch pitch: CGFloat, heading heading: CLLocationDirection)     class func cameraLookingAtCenterCoordinate(_ centerCoordinate: CLLocationCoordinate2D, fromDistance distance: CLLocationDistance, pitch pitch: CGFloat, heading heading: CLLocationDirection) -> Self } ``` | NSCopying, NSSecureCoding |

Modified [MKMapItem](https://developer.apple.com/documentation/mapkit/mkmapitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKMapSnapshot](https://developer.apple.com/documentation/mapkit/mkmapsnapshot)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKMapSnapshotOptions](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [MKMapSnapshotter](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKMapType [enum]](https://developer.apple.com/documentation/mapkit/mkmaptype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MKMapView : UIView {     weak var delegate: MKMapViewDelegate?     var mapType: MKMapType     var region: MKCoordinateRegion     func setRegion(_ region: MKCoordinateRegion, animated animated: Bool)     var centerCoordinate: CLLocationCoordinate2D     func setCenterCoordinate(_ coordinate: CLLocationCoordinate2D, animated animated: Bool)     func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion     var visibleMapRect: MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect     func _handleSelectionAtPoint(_ locationInView: CGPoint)     func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets) -> MKMapRect     @NSCopying var camera: MKMapCamera     func setCamera(_ camera: MKMapCamera, animated animated: Bool)     func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, toCoordinateFromView view: UIView?) -> CLLocationCoordinate2D     func convertRegion(_ region: MKCoordinateRegion, toRectToView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, toRegionFromView view: UIView?) -> MKCoordinateRegion     var zoomEnabled: Bool     var scrollEnabled: Bool     var rotateEnabled: Bool     var pitchEnabled: Bool     var showsCompass: Bool     var showsScale: Bool     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var showsTraffic: Bool     var showsUserLocation: Bool     var userLocation: MKUserLocation { get }     var userTrackingMode: MKUserTrackingMode     func setUserTrackingMode(_ mode: MKUserTrackingMode, animated animated: Bool)     var userLocationVisible: Bool { get }     func addAnnotation(_ annotation: MKAnnotation)     func addAnnotations(_ annotations: [MKAnnotation])     func removeAnnotation(_ annotation: MKAnnotation)     func removeAnnotations(_ annotations: [MKAnnotation])     var annotations: [MKAnnotation] { get }     func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>     func viewForAnnotation(_ annotation: MKAnnotation) -> MKAnnotationView?     func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String) -> MKAnnotationView?     func selectAnnotation(_ annotation: MKAnnotation, animated animated: Bool)     func deselectAnnotation(_ annotation: MKAnnotation?, animated animated: Bool)     var selectedAnnotations: [MKAnnotation]     var annotationVisibleRect: CGRect { get }     func showAnnotations(_ annotations: [MKAnnotation], animated animated: Bool) } extension MKMapView {     func addOverlay(_ overlay: MKOverlay, level level: MKOverlayLevel)     func addOverlays(_ overlays: [MKOverlay], level level: MKOverlayLevel)     func removeOverlay(_ overlay: MKOverlay)     func removeOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int, level level: MKOverlayLevel)     func insertOverlay(_ overlay: MKOverlay, aboveOverlay sibling: MKOverlay)     func insertOverlay(_ overlay: MKOverlay, belowOverlay sibling: MKOverlay)     func exchangeOverlay(_ overlay1: MKOverlay, withOverlay overlay2: MKOverlay)     var overlays: [MKOverlay] { get }     func overlaysInLevel(_ level: MKOverlayLevel) -> [MKOverlay]     func rendererForOverlay(_ overlay: MKOverlay) -> MKOverlayRenderer?     func viewForOverlay(_ overlay: MKOverlay) -> MKOverlayView     func addOverlay(_ overlay: MKOverlay)     func addOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int)     func exchangeOverlayAtIndex(_ index1: Int, withOverlayAtIndex index2: Int) } ``` | AnyObject, NSCoding |
| To | ``` class MKMapView : UIView, NSCoding {     weak var delegate: MKMapViewDelegate?     var mapType: MKMapType     var region: MKCoordinateRegion     func setRegion(_ region: MKCoordinateRegion, animated animated: Bool)     var centerCoordinate: CLLocationCoordinate2D     func setCenterCoordinate(_ coordinate: CLLocationCoordinate2D, animated animated: Bool)     func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion     var visibleMapRect: MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect     func _handleSelectionAtPoint(_ locationInView: CGPoint)     func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets) -> MKMapRect     @NSCopying var camera: MKMapCamera     func setCamera(_ camera: MKMapCamera, animated animated: Bool)     func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, toCoordinateFromView view: UIView?) -> CLLocationCoordinate2D     func convertRegion(_ region: MKCoordinateRegion, toRectToView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, toRegionFromView view: UIView?) -> MKCoordinateRegion     var zoomEnabled: Bool     var scrollEnabled: Bool     var rotateEnabled: Bool     var pitchEnabled: Bool     var showsCompass: Bool     var showsScale: Bool     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var showsTraffic: Bool     var showsUserLocation: Bool     var userLocation: MKUserLocation { get }     var userTrackingMode: MKUserTrackingMode     func setUserTrackingMode(_ mode: MKUserTrackingMode, animated animated: Bool)     var userLocationVisible: Bool { get }     func addAnnotation(_ annotation: MKAnnotation)     func addAnnotations(_ annotations: [MKAnnotation])     func removeAnnotation(_ annotation: MKAnnotation)     func removeAnnotations(_ annotations: [MKAnnotation])     var annotations: [MKAnnotation] { get }     func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>     func viewForAnnotation(_ annotation: MKAnnotation) -> MKAnnotationView?     func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String) -> MKAnnotationView?     func selectAnnotation(_ annotation: MKAnnotation, animated animated: Bool)     func deselectAnnotation(_ annotation: MKAnnotation?, animated animated: Bool)     var selectedAnnotations: [MKAnnotation]     var annotationVisibleRect: CGRect { get }     func showAnnotations(_ annotations: [MKAnnotation], animated animated: Bool) } extension MKMapView {     func addOverlay(_ overlay: MKOverlay, level level: MKOverlayLevel)     func addOverlays(_ overlays: [MKOverlay], level level: MKOverlayLevel)     func removeOverlay(_ overlay: MKOverlay)     func removeOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int, level level: MKOverlayLevel)     func insertOverlay(_ overlay: MKOverlay, aboveOverlay sibling: MKOverlay)     func insertOverlay(_ overlay: MKOverlay, belowOverlay sibling: MKOverlay)     func exchangeOverlay(_ overlay1: MKOverlay, withOverlay overlay2: MKOverlay)     var overlays: [MKOverlay] { get }     func overlaysInLevel(_ level: MKOverlayLevel) -> [MKOverlay]     func rendererForOverlay(_ overlay: MKOverlay) -> MKOverlayRenderer?     func viewForOverlay(_ overlay: MKOverlay) -> MKOverlayView     func addOverlay(_ overlay: MKOverlay)     func addOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int)     func exchangeOverlayAtIndex(_ index1: Int, withOverlayAtIndex index2: Int) } ``` | NSCoding |

Modified [MKMultiPoint](https://developer.apple.com/documentation/mapkit/mkmultipoint)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKOverlay](https://developer.apple.com/documentation/mapkit/mkoverlay)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MKOverlay : MKAnnotation, NSObjectProtocol {     var coordinate: CLLocationCoordinate2D { get }     var boundingMapRect: MKMapRect { get }     optional func intersectsMapRect(_ mapRect: MKMapRect) -> Bool     optional func canReplaceMapContent() -> Bool } ``` | MKAnnotation, NSObjectProtocol |
| To | ``` protocol MKOverlay : MKAnnotation {     var coordinate: CLLocationCoordinate2D { get }     var boundingMapRect: MKMapRect { get }     optional func intersectsMapRect(_ mapRect: MKMapRect) -> Bool     optional func canReplaceMapContent() -> Bool } ``` | MKAnnotation |

Modified [MKOverlayLevel [enum]](https://developer.apple.com/documentation/mapkit/mkoverlaylevel)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MKOverlayPathRenderer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKOverlayPathView](https://developer.apple.com/documentation/mapkit/mkoverlaypathview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKOverlayView](https://developer.apple.com/documentation/mapkit/mkoverlayview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKPinAnnotationColor [enum]](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MKPinAnnotationView](https://developer.apple.com/documentation/mapkit/mkpinannotationview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKPlacemark](https://developer.apple.com/documentation/mapkit/mkplacemark)

|  | Protocols |
| --- | --- |
| From | AnyObject, MKAnnotation, NSObjectProtocol |
| To | MKAnnotation |

Modified [MKPointAnnotation](https://developer.apple.com/documentation/mapkit/mkpointannotation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKPolygon](https://developer.apple.com/documentation/mapkit/mkpolygon)

|  | Protocols |
| --- | --- |
| From | AnyObject, MKAnnotation, MKOverlay, NSObjectProtocol |
| To | MKOverlay |

Modified [MKPolygonRenderer](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKPolygonView](https://developer.apple.com/documentation/mapkit/mkpolygonview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKPolyline](https://developer.apple.com/documentation/mapkit/mkpolyline)

|  | Protocols |
| --- | --- |
| From | AnyObject, MKAnnotation, MKOverlay, NSObjectProtocol |
| To | MKOverlay |

Modified [MKPolylineRenderer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKPolylineView](https://developer.apple.com/documentation/mapkit/mkpolylineview)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKRoute](https://developer.apple.com/documentation/mapkit/mkroute)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKRouteStep](https://developer.apple.com/documentation/mapkit/mkroutestep)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKShape](https://developer.apple.com/documentation/mapkit/mkshape)

|  | Protocols |
| --- | --- |
| From | AnyObject, MKAnnotation, NSObjectProtocol |
| To | MKAnnotation |

Modified [MKTileOverlay](https://developer.apple.com/documentation/mapkit/mktileoverlay)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MKTileOverlay : NSObject, MKOverlay, MKAnnotation {     init(URLTemplate URLTemplate: String?)     var tileSize: CGSize     var geometryFlipped: Bool     var minimumZ: Int     var maximumZ: Int     var URLTemplate: String? { get }     var canReplaceMapContent: Bool } extension MKTileOverlay {     func URLForTilePath(_ path: MKTileOverlayPath) -> NSURL     func loadTileAtPath(_ path: MKTileOverlayPath, result result: (NSData?, NSError?) -> Void) } ``` | AnyObject, MKAnnotation, MKOverlay, NSObjectProtocol |
| To | ``` class MKTileOverlay : NSObject, MKOverlay {     init(URLTemplate URLTemplate: String?)     var tileSize: CGSize     var geometryFlipped: Bool     var minimumZ: Int     var maximumZ: Int     var URLTemplate: String? { get }     var canReplaceMapContent: Bool } extension MKTileOverlay {     func URLForTilePath(_ path: MKTileOverlayPath) -> NSURL     func loadTileAtPath(_ path: MKTileOverlayPath, result result: (NSData?, NSError?) -> Void) } ``` | MKOverlay |

Modified [MKTileOverlayRenderer](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKUserLocation](https://developer.apple.com/documentation/mapkit/mkuserlocation)

|  | Protocols |
| --- | --- |
| From | AnyObject, MKAnnotation, NSObjectProtocol |
| To | MKAnnotation |

Modified [MKUserTrackingBarButtonItem](https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [MKUserTrackingMode [enum]](https://developer.apple.com/documentation/mapkit/mkusertrackingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
