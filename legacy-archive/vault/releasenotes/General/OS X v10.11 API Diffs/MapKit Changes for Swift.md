---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/MapKit.html
archived_at: '2026-07-18T02:53:38.639907Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MapKit Changes for Swift

### MapKit

Removed MKDirectionsRequest.destination() -> MKMapItem!Removed MKDirectionsRequest.setDestination(_: MKMapItem!)Removed MKDirectionsRequest.setSource(_: MKMapItem!)Removed MKDirectionsRequest.source() -> MKMapItem!Removed MKDirectionsTransportType.init(_: UInt)Added [MKAnnotationView.detailCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452543-detailcalloutaccessoryview)Added [MKDirectionsRequest.destination](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433146-destination)Added [MKDirectionsRequest.source](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433144-source)Added [MKDirectionsTransportType.Transit](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype/mkdirectionstransporttypetransit)Added [MKETAResponse.distance](https://developer.apple.com/documentation/mapkit/mketaresponse/1452164-distance)Added [MKETAResponse.expectedArrivalDate](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/1451881-expectedarrivaldate)Added [MKETAResponse.expectedDepartureDate](https://developer.apple.com/documentation/mapkit/mketaresponse/1452644-expecteddeparturedate)Added [MKETAResponse.transportType](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/1452616-transporttype)Added [MKMapCamera.init(lookingAtCenterCoordinate: CLLocationCoordinate2D, fromDistance: CLLocationDistance, pitch: CGFloat, heading: CLLocationDirection)](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411079-cameralookingatcentercoordinate)Added [MKMapItem.timeZone](https://developer.apple.com/documentation/mapkit/mkmapitem/1452431-timezone)Added [MKMapType.HybridFlyover](https://developer.apple.com/documentation/mapkit/mkmaptype/hybridflyover)Added [MKMapType.SatelliteFlyover](https://developer.apple.com/documentation/mapkit/mkmaptype/satelliteflyover)Added [MKMapView.showsTraffic](https://developer.apple.com/documentation/mapkit/mkmapview/1452433-showstraffic)Added [MKPinAnnotationView.greenPinColor() -> NSColor [class]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452568-greenpincolor)Added [MKPinAnnotationView.pinTintColor](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452042-pintintcolor)Added [MKPinAnnotationView.purplePinColor() -> NSColor [class]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452110-purplepincolor)Added [MKPinAnnotationView.redPinColor() -> NSColor [class]](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1451990-redpincolor)Added [MKLaunchOptionsDirectionsModeTransit](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodetransit)Modified [MKAnnotation](https://developer.apple.com/documentation/mapkit/mkannotation)

|  | Declaration |
| --- | --- |
| From | ``` protocol MKAnnotation : NSObjectProtocol {     var coordinate: CLLocationCoordinate2D { get }     optional var title: String! { get }     optional var subtitle: String! { get } } ``` |
| To | ``` protocol MKAnnotation : NSObjectProtocol {     var coordinate: CLLocationCoordinate2D { get }     optional var title: String? { get }     optional var subtitle: String? { get } } ``` |

Modified [MKAnnotation.subtitle](https://developer.apple.com/documentation/mapkit/mkannotation/1429520-subtitle)

|  | Declaration |
| --- | --- |
| From | ``` optional var subtitle: String! { get } ``` |
| To | ``` optional var subtitle: String? { get } ``` |

Modified [MKAnnotation.title](https://developer.apple.com/documentation/mapkit/mkannotation/1429522-title)

|  | Declaration |
| --- | --- |
| From | ``` optional var title: String! { get } ``` |
| To | ``` optional var title: String? { get } ``` |

Modified [MKAnnotationView](https://developer.apple.com/documentation/mapkit/mkannotationview)

|  | Declaration |
| --- | --- |
| From | ``` class MKAnnotationView : NSView {     init!(annotation annotation: MKAnnotation!, reuseIdentifier reuseIdentifier: String!)     var reuseIdentifier: String! { get }     func prepareForReuse()     var annotation: MKAnnotation!     var image: NSImage!     var centerOffset: CGPoint     var calloutOffset: CGPoint     var leftCalloutOffset: CGPoint     var rightCalloutOffset: CGPoint     var enabled: Bool     var highlighted: Bool     var selected: Bool     func setSelected(_ selected: Bool, animated animated: Bool)     var canShowCallout: Bool     var leftCalloutAccessoryView: NSView!     var rightCalloutAccessoryView: NSView!     var draggable: Bool     var dragState: MKAnnotationViewDragState     func setDragState(_ newDragState: MKAnnotationViewDragState, animated animated: Bool) } ``` |
| To | ``` class MKAnnotationView : NSView {     init(annotation annotation: MKAnnotation?, reuseIdentifier reuseIdentifier: String?)     var reuseIdentifier: String? { get }     func prepareForReuse()     var annotation: MKAnnotation?     var image: NSImage?     var centerOffset: CGPoint     var calloutOffset: CGPoint     var leftCalloutOffset: CGPoint     var rightCalloutOffset: CGPoint     var enabled: Bool     var highlighted: Bool     var selected: Bool     func setSelected(_ selected: Bool, animated animated: Bool)     var canShowCallout: Bool     var leftCalloutAccessoryView: NSView?     var rightCalloutAccessoryView: NSView?     var detailCalloutAccessoryView: NSView?     var draggable: Bool     var dragState: MKAnnotationViewDragState     func setDragState(_ newDragState: MKAnnotationViewDragState, animated animated: Bool) } ``` |

Modified [MKAnnotationView.annotation](https://developer.apple.com/documentation/mapkit/mkannotationview/1452613-annotation)

|  | Declaration |
| --- | --- |
| From | ``` var annotation: MKAnnotation! ``` |
| To | ``` var annotation: MKAnnotation? ``` |

Modified [MKAnnotationView.image](https://developer.apple.com/documentation/mapkit/mkannotationview/1452094-image)

|  | Declaration |
| --- | --- |
| From | ``` var image: NSImage! ``` |
| To | ``` var image: NSImage? ``` |

Modified [MKAnnotationView.init(annotation: MKAnnotation?, reuseIdentifier: String?)](https://developer.apple.com/documentation/mapkit/mkannotationview/1452779-initwithannotation)

|  | Declaration |
| --- | --- |
| From | ``` init!(annotation annotation: MKAnnotation!, reuseIdentifier reuseIdentifier: String!) ``` |
| To | ``` init(annotation annotation: MKAnnotation?, reuseIdentifier reuseIdentifier: String?) ``` |

Modified [MKAnnotationView.leftCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452423-leftcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` var leftCalloutAccessoryView: NSView! ``` |
| To | ``` var leftCalloutAccessoryView: NSView? ``` |

Modified [MKAnnotationView.reuseIdentifier](https://developer.apple.com/documentation/mapkit/mkannotationview/1452060-reuseidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var reuseIdentifier: String! { get } ``` |
| To | ``` var reuseIdentifier: String? { get } ``` |

Modified [MKAnnotationView.rightCalloutAccessoryView](https://developer.apple.com/documentation/mapkit/mkannotationview/1452233-rightcalloutaccessoryview)

|  | Declaration |
| --- | --- |
| From | ``` var rightCalloutAccessoryView: NSView! ``` |
| To | ``` var rightCalloutAccessoryView: NSView? ``` |

Modified [MKAnnotationViewDragState [enum]](https://developer.apple.com/documentation/mapkit/mkannotationviewdragstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MKCircle](https://developer.apple.com/documentation/mapkit/mkcircle)

|  | Declaration |
| --- | --- |
| From | ``` class MKCircle : MKShape, MKOverlay, MKAnnotation, NSObjectProtocol {     convenience init!(centerCoordinate coord: CLLocationCoordinate2D, radius radius: CLLocationDistance)     class func circleWithCenterCoordinate(_ coord: CLLocationCoordinate2D, radius radius: CLLocationDistance) -> Self!     convenience init!(mapRect mapRect: MKMapRect)     class func circleWithMapRect(_ mapRect: MKMapRect) -> Self!     var coordinate: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var boundingMapRect: MKMapRect { get } } ``` |
| To | ``` class MKCircle : MKShape, MKOverlay {     convenience init(centerCoordinate coord: CLLocationCoordinate2D, radius radius: CLLocationDistance)     class func circleWithCenterCoordinate(_ coord: CLLocationCoordinate2D, radius radius: CLLocationDistance) -> Self     convenience init(mapRect mapRect: MKMapRect)     class func circleWithMapRect(_ mapRect: MKMapRect) -> Self     var coordinate: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var boundingMapRect: MKMapRect { get } } ``` |

Modified [MKCircle.init(centerCoordinate: CLLocationCoordinate2D, radius: CLLocationDistance)](https://developer.apple.com/documentation/mapkit/mkcircle/1411076-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(centerCoordinate coord: CLLocationCoordinate2D, radius radius: CLLocationDistance) ``` |
| To | ``` convenience init(centerCoordinate coord: CLLocationCoordinate2D, radius radius: CLLocationDistance) ``` |

Modified [MKCircle.init(mapRect: MKMapRect)](https://developer.apple.com/documentation/mapkit/mkcircle/1411072-circlewithmaprect)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(mapRect mapRect: MKMapRect) ``` |
| To | ``` convenience init(mapRect mapRect: MKMapRect) ``` |

Modified [MKCircleRenderer](https://developer.apple.com/documentation/mapkit/mkcirclerenderer)

|  | Declaration |
| --- | --- |
| From | ``` class MKCircleRenderer : MKOverlayPathRenderer {     init!(circle circle: MKCircle!)     var circle: MKCircle! { get } } ``` |
| To | ``` class MKCircleRenderer : MKOverlayPathRenderer {     init(circle circle: MKCircle)     var circle: MKCircle { get } } ``` |

Modified [MKCircleRenderer.circle](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/1452413-circle)

|  | Declaration |
| --- | --- |
| From | ``` var circle: MKCircle! { get } ``` |
| To | ``` var circle: MKCircle { get } ``` |

Modified [MKCircleRenderer.init(circle: MKCircle)](https://developer.apple.com/documentation/mapkit/mkcirclerenderer/1452547-initwithcircle)

|  | Declaration |
| --- | --- |
| From | ``` init!(circle circle: MKCircle!) ``` |
| To | ``` init(circle circle: MKCircle) ``` |

Modified [MKDirections](https://developer.apple.com/documentation/mapkit/mkdirections)

|  | Declaration |
| --- | --- |
| From | ``` class MKDirections : NSObject {     init!(request request: MKDirectionsRequest!)     func calculateDirectionsWithCompletionHandler(_ completionHandler: MKDirectionsHandler!)     func calculateETAWithCompletionHandler(_ completionHandler: MKETAHandler!)     func cancel()     var calculating: Bool { get } } ``` |
| To | ``` class MKDirections : NSObject {     init(request request: MKDirectionsRequest)     func calculateDirectionsWithCompletionHandler(_ completionHandler: MKDirectionsHandler)     func calculateETAWithCompletionHandler(_ completionHandler: MKETAHandler)     func cancel()     var calculating: Bool { get } } ``` |

Modified [MKDirections.calculateDirectionsWithCompletionHandler(_: MKDirectionsHandler)](https://developer.apple.com/documentation/mapkit/mkdirections/1452078-calculate)

|  | Declaration |
| --- | --- |
| From | ``` func calculateDirectionsWithCompletionHandler(_ completionHandler: MKDirectionsHandler!) ``` |
| To | ``` func calculateDirectionsWithCompletionHandler(_ completionHandler: MKDirectionsHandler) ``` |

Modified [MKDirections.calculateETAWithCompletionHandler(_: MKETAHandler)](https://developer.apple.com/documentation/mapkit/mkdirections/1452736-calculateetawithcompletionhandle)

|  | Declaration |
| --- | --- |
| From | ``` func calculateETAWithCompletionHandler(_ completionHandler: MKETAHandler!) ``` |
| To | ``` func calculateETAWithCompletionHandler(_ completionHandler: MKETAHandler) ``` |

Modified [MKDirections.init(request: MKDirectionsRequest)](https://developer.apple.com/documentation/mapkit/mkdirections/1452197-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(request request: MKDirectionsRequest!) ``` |
| To | ``` init(request request: MKDirectionsRequest) ``` |

Modified [MKDirectionsRequest](https://developer.apple.com/documentation/mapkit/mkdirections/request)

|  | Declaration |
| --- | --- |
| From | ``` class MKDirectionsRequest : NSObject {     func source() -> MKMapItem!     func setSource(_ source: MKMapItem!)     func destination() -> MKMapItem!     func setDestination(_ destination: MKMapItem!) } extension MKDirectionsRequest {     var transportType: MKDirectionsTransportType     var requestsAlternateRoutes: Bool     @NSCopying var departureDate: NSDate!     @NSCopying var arrivalDate: NSDate! } extension MKDirectionsRequest {     init!(contentsOfURL url: NSURL!)     class func isDirectionsRequestURL(_ url: NSURL!) -> Bool } ``` |
| To | ``` class MKDirectionsRequest : NSObject {     var source: MKMapItem?     var destination: MKMapItem? } extension MKDirectionsRequest {     var transportType: MKDirectionsTransportType     var requestsAlternateRoutes: Bool     @NSCopying var departureDate: NSDate?     @NSCopying var arrivalDate: NSDate? } extension MKDirectionsRequest {     init(contentsOfURL url: NSURL)     class func isDirectionsRequestURL(_ url: NSURL) -> Bool } ``` |

Modified [MKDirectionsRequest.arrivalDate](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433148-arrivaldate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var arrivalDate: NSDate! ``` |
| To | ``` @NSCopying var arrivalDate: NSDate? ``` |

Modified [MKDirectionsRequest.departureDate](https://developer.apple.com/documentation/mapkit/mkdirections/request/1433155-departuredate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var departureDate: NSDate! ``` |
| To | ``` @NSCopying var departureDate: NSDate? ``` |

Modified [MKDirectionsRequest.init(contentsOfURL: NSURL)](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433158-initwithcontentsofurl)

|  | Declaration |
| --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!) ``` |
| To | ``` init(contentsOfURL url: NSURL) ``` |

Modified [MKDirectionsRequest.isDirectionsRequestURL(_: NSURL) -> Bool [class]](https://developer.apple.com/documentation/mapkit/mkdirectionsrequest/1433150-isdirectionsrequesturl)

|  | Declaration |
| --- | --- |
| From | ``` class func isDirectionsRequestURL(_ url: NSURL!) -> Bool ``` |
| To | ``` class func isDirectionsRequestURL(_ url: NSURL) -> Bool ``` |

Modified [MKDirectionsResponse](https://developer.apple.com/documentation/mapkit/mkdirections/response)

|  | Declaration |
| --- | --- |
| From | ``` class MKDirectionsResponse : NSObject {     var source: MKMapItem! { get }     var destination: MKMapItem! { get }     var routes: [AnyObject]! { get } } ``` |
| To | ``` class MKDirectionsResponse : NSObject {     var source: MKMapItem { get }     var destination: MKMapItem { get }     var routes: [MKRoute] { get } } ``` |

Modified [MKDirectionsResponse.destination](https://developer.apple.com/documentation/mapkit/mkdirectionsresponse/1451981-destination)

|  | Declaration |
| --- | --- |
| From | ``` var destination: MKMapItem! { get } ``` |
| To | ``` var destination: MKMapItem { get } ``` |

Modified [MKDirectionsResponse.routes](https://developer.apple.com/documentation/mapkit/mkdirections/response/1452071-routes)

|  | Declaration |
| --- | --- |
| From | ``` var routes: [AnyObject]! { get } ``` |
| To | ``` var routes: [MKRoute] { get } ``` |

Modified [MKDirectionsResponse.source](https://developer.apple.com/documentation/mapkit/mkdirections/response/1452261-source)

|  | Declaration |
| --- | --- |
| From | ``` var source: MKMapItem! { get } ``` |
| To | ``` var source: MKMapItem { get } ``` |

Modified [MKDirectionsTransportType [struct]](https://developer.apple.com/documentation/mapkit/mkdirectionstransporttype)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MKDirectionsTransportType : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var Automobile: MKDirectionsTransportType { get }     static var Walking: MKDirectionsTransportType { get }     static var Any: MKDirectionsTransportType { get } } ``` | RawOptionSetType |
| To | ``` struct MKDirectionsTransportType : OptionSetType {     init(rawValue rawValue: UInt)     static var Automobile: MKDirectionsTransportType { get }     static var Walking: MKDirectionsTransportType { get }     static var Transit: MKDirectionsTransportType { get }     static var Any: MKDirectionsTransportType { get } } ``` | OptionSetType |

Modified [MKDistanceFormatter](https://developer.apple.com/documentation/mapkit/mkdistanceformatter)

|  | Declaration |
| --- | --- |
| From | ``` class MKDistanceFormatter : NSFormatter {     func stringFromDistance(_ distance: CLLocationDistance) -> String!     func distanceFromString(_ distance: String!) -> CLLocationDistance     @NSCopying var locale: NSLocale!     var units: MKDistanceFormatterUnits     var unitStyle: MKDistanceFormatterUnitStyle } ``` |
| To | ``` class MKDistanceFormatter : NSFormatter {     func stringFromDistance(_ distance: CLLocationDistance) -> String     func distanceFromString(_ distance: String) -> CLLocationDistance     @NSCopying var locale: NSLocale!     var units: MKDistanceFormatterUnits     var unitStyle: MKDistanceFormatterUnitStyle } ``` |

Modified [MKDistanceFormatter.distanceFromString(_: String) -> CLLocationDistance](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452766-distance)

|  | Declaration |
| --- | --- |
| From | ``` func distanceFromString(_ distance: String!) -> CLLocationDistance ``` |
| To | ``` func distanceFromString(_ distance: String) -> CLLocationDistance ``` |

Modified [MKDistanceFormatter.stringFromDistance(_: CLLocationDistance) -> String](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1451994-stringfromdistance)

|  | Declaration |
| --- | --- |
| From | ``` func stringFromDistance(_ distance: CLLocationDistance) -> String! ``` |
| To | ``` func stringFromDistance(_ distance: CLLocationDistance) -> String ``` |

Modified [MKDistanceFormatterUnits [enum]](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MKDistanceFormatterUnitStyle [enum]](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MKErrorCode [enum]](https://developer.apple.com/documentation/mapkit/mkerror/code)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [MKETAResponse](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse)

|  | Declaration |
| --- | --- |
| From | ``` class MKETAResponse : NSObject {     var source: MKMapItem! { get }     var destination: MKMapItem! { get }     var expectedTravelTime: NSTimeInterval { get } } ``` |
| To | ``` class MKETAResponse : NSObject {     var source: MKMapItem { get }     var destination: MKMapItem { get }     var expectedTravelTime: NSTimeInterval { get }     var distance: CLLocationDistance { get }     var expectedArrivalDate: NSDate { get }     var expectedDepartureDate: NSDate { get }     var transportType: MKDirectionsTransportType { get } } ``` |

Modified [MKETAResponse.destination](https://developer.apple.com/documentation/mapkit/mketaresponse/1452611-destination)

|  | Declaration |
| --- | --- |
| From | ``` var destination: MKMapItem! { get } ``` |
| To | ``` var destination: MKMapItem { get } ``` |

Modified [MKETAResponse.source](https://developer.apple.com/documentation/mapkit/mkdirections/etaresponse/1451947-source)

|  | Declaration |
| --- | --- |
| From | ``` var source: MKMapItem! { get } ``` |
| To | ``` var source: MKMapItem { get } ``` |

Modified [MKGeodesicPolyline](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline)

|  | Declaration |
| --- | --- |
| From | ``` class MKGeodesicPolyline : MKPolyline {     convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int)     class func polylineWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int) -> Self!     convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int)     class func polylineWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) -> Self! } ``` |
| To | ``` class MKGeodesicPolyline : MKPolyline {     convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int)     class func polylineWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int) -> Self     convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int)     class func polylineWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) -> Self } ``` |

Modified [MKGeodesicPolyline.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/1452314-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified [MKGeodesicPolyline.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)](https://developer.apple.com/documentation/mapkit/mkgeodesicpolyline/1452053-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified [MKLocalSearch](https://developer.apple.com/documentation/mapkit/mklocalsearch)

|  | Declaration |
| --- | --- |
| From | ``` class MKLocalSearch : NSObject {     init!(request request: MKLocalSearchRequest!)     func startWithCompletionHandler(_ completionHandler: MKLocalSearchCompletionHandler!)     func cancel()     var searching: Bool { get } } ``` |
| To | ``` class MKLocalSearch : NSObject {     init(request request: MKLocalSearchRequest)     func startWithCompletionHandler(_ completionHandler: MKLocalSearchCompletionHandler)     func cancel()     var searching: Bool { get } } ``` |

Modified [MKLocalSearch.init(request: MKLocalSearchRequest)](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452759-initwithrequest)

|  | Declaration |
| --- | --- |
| From | ``` init!(request request: MKLocalSearchRequest!) ``` |
| To | ``` init(request request: MKLocalSearchRequest) ``` |

Modified [MKLocalSearch.startWithCompletionHandler(_: MKLocalSearchCompletionHandler)](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452652-start)

|  | Declaration |
| --- | --- |
| From | ``` func startWithCompletionHandler(_ completionHandler: MKLocalSearchCompletionHandler!) ``` |
| To | ``` func startWithCompletionHandler(_ completionHandler: MKLocalSearchCompletionHandler) ``` |

Modified [MKLocalSearchRequest](https://developer.apple.com/documentation/mapkit/mklocalsearch/request)

|  | Declaration |
| --- | --- |
| From | ``` class MKLocalSearchRequest : NSObject, NSCopying {     var naturalLanguageQuery: String!     var region: MKCoordinateRegion } ``` |
| To | ``` class MKLocalSearchRequest : NSObject, NSCopying {     var naturalLanguageQuery: String?     var region: MKCoordinateRegion } ``` |

Modified [MKLocalSearchRequest.naturalLanguageQuery](https://developer.apple.com/documentation/mapkit/mklocalsearchrequest/1452353-naturallanguagequery)

|  | Declaration |
| --- | --- |
| From | ``` var naturalLanguageQuery: String! ``` |
| To | ``` var naturalLanguageQuery: String? ``` |

Modified [MKLocalSearchResponse](https://developer.apple.com/documentation/mapkit/mklocalsearchresponse)

|  | Declaration |
| --- | --- |
| From | ``` class MKLocalSearchResponse : NSObject {     var mapItems: [AnyObject]! { get }     var boundingRegion: MKCoordinateRegion { get } } ``` |
| To | ``` class MKLocalSearchResponse : NSObject {     var mapItems: [MKMapItem] { get }     var boundingRegion: MKCoordinateRegion { get } } ``` |

Modified [MKLocalSearchResponse.mapItems](https://developer.apple.com/documentation/mapkit/mklocalsearchresponse/1451939-mapitems)

|  | Declaration |
| --- | --- |
| From | ``` var mapItems: [AnyObject]! { get } ``` |
| To | ``` var mapItems: [MKMapItem] { get } ``` |

Modified [MKMapCamera](https://developer.apple.com/documentation/mapkit/mkmapcamera)

|  | Declaration |
| --- | --- |
| From | ``` class MKMapCamera : NSObject, NSSecureCoding, NSCoding, NSCopying {     var centerCoordinate: CLLocationCoordinate2D     var heading: CLLocationDirection     var pitch: CGFloat     var altitude: CLLocationDistance     convenience init!()     class func camera() -> Self!     convenience init!(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance)     class func cameraLookingAtCenterCoordinate(_ centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) -> Self! } ``` |
| To | ``` class MKMapCamera : NSObject, NSSecureCoding, NSCoding, NSCopying {     var centerCoordinate: CLLocationCoordinate2D     var heading: CLLocationDirection     var pitch: CGFloat     var altitude: CLLocationDistance     convenience init()     class func camera() -> Self     convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance)     class func cameraLookingAtCenterCoordinate(_ centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) -> Self     convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromDistance distance: CLLocationDistance, pitch pitch: CGFloat, heading heading: CLLocationDirection)     class func cameraLookingAtCenterCoordinate(_ centerCoordinate: CLLocationCoordinate2D, fromDistance distance: CLLocationDistance, pitch pitch: CGFloat, heading heading: CLLocationDirection) -> Self } ``` |

Modified [MKMapCamera.init(lookingAtCenterCoordinate: CLLocationCoordinate2D, fromEyeCoordinate: CLLocationCoordinate2D, eyeAltitude: CLLocationDistance)](https://developer.apple.com/documentation/mapkit/mkmapcamera/1411092-cameralookingatcentercoordinate)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) ``` |
| To | ``` convenience init(lookingAtCenterCoordinate centerCoordinate: CLLocationCoordinate2D, fromEyeCoordinate eyeCoordinate: CLLocationCoordinate2D, eyeAltitude eyeAltitude: CLLocationDistance) ``` |

Modified [MKMapItem](https://developer.apple.com/documentation/mapkit/mkmapitem)

|  | Declaration |
| --- | --- |
| From | ``` class MKMapItem : NSObject {     var placemark: MKPlacemark! { get }     var isCurrentLocation: Bool { get }     var name: String!     var phoneNumber: String!     var url: NSURL!     class func mapItemForCurrentLocation() -> MKMapItem!     init!(placemark placemark: MKPlacemark!)     func openInMapsWithLaunchOptions(_ launchOptions: [NSObject : AnyObject]!) -> Bool     class func openMapsWithItems(_ mapItems: [AnyObject]!, launchOptions launchOptions: [NSObject : AnyObject]!) -> Bool } ``` |
| To | ``` class MKMapItem : NSObject {     var placemark: MKPlacemark { get }     var isCurrentLocation: Bool { get }     var name: String?     var phoneNumber: String?     var url: NSURL?     @NSCopying var timeZone: NSTimeZone?     class func mapItemForCurrentLocation() -> MKMapItem     init(placemark placemark: MKPlacemark)     func openInMapsWithLaunchOptions(_ launchOptions: [String : AnyObject]?) -> Bool     class func openMapsWithItems(_ mapItems: [MKMapItem], launchOptions launchOptions: [String : AnyObject]?) -> Bool } ``` |

Modified [MKMapItem.init(placemark: MKPlacemark)](https://developer.apple.com/documentation/mapkit/mkmapitem/1452285-initwithplacemark)

|  | Declaration |
| --- | --- |
| From | ``` init!(placemark placemark: MKPlacemark!) ``` |
| To | ``` init(placemark placemark: MKPlacemark) ``` |

Modified [MKMapItem.mapItemForCurrentLocation() -> MKMapItem [class]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452002-mapitemforcurrentlocation)

|  | Declaration |
| --- | --- |
| From | ``` class func mapItemForCurrentLocation() -> MKMapItem! ``` |
| To | ``` class func mapItemForCurrentLocation() -> MKMapItem ``` |

Modified [MKMapItem.name](https://developer.apple.com/documentation/mapkit/mkmapitem/1452339-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified [MKMapItem.openInMapsWithLaunchOptions(_: [String : AnyObject]?) -> Bool](https://developer.apple.com/documentation/mapkit/mkmapitem/1452239-openinmapswithlaunchoptions)

|  | Declaration |
| --- | --- |
| From | ``` func openInMapsWithLaunchOptions(_ launchOptions: [NSObject : AnyObject]!) -> Bool ``` |
| To | ``` func openInMapsWithLaunchOptions(_ launchOptions: [String : AnyObject]?) -> Bool ``` |

Modified [MKMapItem.openMapsWithItems(_: [MKMapItem], launchOptions: [String : AnyObject]?) -> Bool [class]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452207-openmaps)

|  | Declaration |
| --- | --- |
| From | ``` class func openMapsWithItems(_ mapItems: [AnyObject]!, launchOptions launchOptions: [NSObject : AnyObject]!) -> Bool ``` |
| To | ``` class func openMapsWithItems(_ mapItems: [MKMapItem], launchOptions launchOptions: [String : AnyObject]?) -> Bool ``` |

Modified [MKMapItem.phoneNumber](https://developer.apple.com/documentation/mapkit/mkmapitem/1452088-phonenumber)

|  | Declaration |
| --- | --- |
| From | ``` var phoneNumber: String! ``` |
| To | ``` var phoneNumber: String? ``` |

Modified [MKMapItem.placemark](https://developer.apple.com/documentation/mapkit/mkmapitem/1452134-placemark)

|  | Declaration |
| --- | --- |
| From | ``` var placemark: MKPlacemark! { get } ``` |
| To | ``` var placemark: MKPlacemark { get } ``` |

Modified [MKMapItem.url](https://developer.apple.com/documentation/mapkit/mkmapitem/1452746-url)

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL! ``` |
| To | ``` var url: NSURL? ``` |

Modified [MKMapSnapshot](https://developer.apple.com/documentation/mapkit/mkmapsnapshot)

|  | Declaration |
| --- | --- |
| From | ``` class MKMapSnapshot : NSObject {     var image: NSImage! { get }     func pointForCoordinate(_ coordinate: CLLocationCoordinate2D) -> NSPoint } ``` |
| To | ``` class MKMapSnapshot : NSObject {     var image: NSImage { get }     func pointForCoordinate(_ coordinate: CLLocationCoordinate2D) -> NSPoint } ``` |

Modified [MKMapSnapshot.image](https://developer.apple.com/documentation/mapkit/mkmapsnapshot/1452701-image)

|  | Declaration |
| --- | --- |
| From | ``` var image: NSImage! { get } ``` |
| To | ``` var image: NSImage { get } ``` |

Modified [MKMapSnapshotOptions](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options)

|  | Declaration |
| --- | --- |
| From | ``` class MKMapSnapshotOptions : NSObject, NSCopying {     @NSCopying var camera: MKMapCamera!     var mapRect: MKMapRect     var region: MKCoordinateRegion     var mapType: MKMapType     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var size: NSSize } ``` |
| To | ``` class MKMapSnapshotOptions : NSObject, NSCopying {     @NSCopying var camera: MKMapCamera     var mapRect: MKMapRect     var region: MKCoordinateRegion     var mapType: MKMapType     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var size: NSSize } ``` |

Modified [MKMapSnapshotOptions.camera](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/options/1452082-camera)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var camera: MKMapCamera! ``` |
| To | ``` @NSCopying var camera: MKMapCamera ``` |

Modified [MKMapSnapshotter](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter)

|  | Declaration |
| --- | --- |
| From | ``` class MKMapSnapshotter : NSObject {     init!(options options: MKMapSnapshotOptions!)     func startWithCompletionHandler(_ completionHandler: MKMapSnapshotCompletionHandler!)     func startWithQueue(_ queue: dispatch_queue_t!, completionHandler completionHandler: MKMapSnapshotCompletionHandler!)     func cancel()     var loading: Bool { get } } ``` |
| To | ``` class MKMapSnapshotter : NSObject {     init(options options: MKMapSnapshotOptions)     func startWithCompletionHandler(_ completionHandler: MKMapSnapshotCompletionHandler)     func startWithQueue(_ queue: dispatch_queue_t, completionHandler completionHandler: MKMapSnapshotCompletionHandler)     func cancel()     var loading: Bool { get } } ``` |

Modified [MKMapSnapshotter.init(options: MKMapSnapshotOptions)](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452090-initwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` init!(options options: MKMapSnapshotOptions!) ``` |
| To | ``` init(options options: MKMapSnapshotOptions) ``` |

Modified [MKMapSnapshotter.startWithCompletionHandler(_: MKMapSnapshotCompletionHandler)](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452479-startwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func startWithCompletionHandler(_ completionHandler: MKMapSnapshotCompletionHandler!) ``` |
| To | ``` func startWithCompletionHandler(_ completionHandler: MKMapSnapshotCompletionHandler) ``` |

Modified [MKMapSnapshotter.startWithQueue(_: dispatch_queue_t, completionHandler: MKMapSnapshotCompletionHandler)](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/1452419-start)

|  | Declaration |
| --- | --- |
| From | ``` func startWithQueue(_ queue: dispatch_queue_t!, completionHandler completionHandler: MKMapSnapshotCompletionHandler!) ``` |
| To | ``` func startWithQueue(_ queue: dispatch_queue_t, completionHandler completionHandler: MKMapSnapshotCompletionHandler) ``` |

Modified [MKMapType [enum]](https://developer.apple.com/documentation/mapkit/mkmaptype)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum MKMapType : UInt {     case Standard     case Satellite     case Hybrid } ``` | -- |
| To | ``` enum MKMapType : UInt {     case Standard     case Satellite     case Hybrid     case SatelliteFlyover     case HybridFlyover } ``` | UInt |

Modified [MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview)

|  | Declaration |
| --- | --- |
| From | ``` class MKMapView : NSView, NSCoding {     weak var delegate: MKMapViewDelegate!     var mapType: MKMapType     var region: MKCoordinateRegion     func setRegion(_ region: MKCoordinateRegion, animated animated: Bool)     var centerCoordinate: CLLocationCoordinate2D     func setCenterCoordinate(_ coordinate: CLLocationCoordinate2D, animated animated: Bool)     func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion     var visibleMapRect: MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: NSEdgeInsets, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: NSEdgeInsets) -> MKMapRect     @NSCopying var camera: MKMapCamera!     func setCamera(_ camera: MKMapCamera!, animated animated: Bool)     func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: NSView!) -> CGPoint     func convertPoint(_ point: CGPoint, toCoordinateFromView view: NSView!) -> CLLocationCoordinate2D     func convertRegion(_ region: MKCoordinateRegion, toRectToView view: NSView!) -> CGRect     func convertRect(_ rect: CGRect, toRegionFromView view: NSView!) -> MKCoordinateRegion     var zoomEnabled: Bool     var scrollEnabled: Bool     var rotateEnabled: Bool     var pitchEnabled: Bool     var showsCompass: Bool     var showsZoomControls: Bool     var showsScale: Bool     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var showsUserLocation: Bool     var userLocation: MKUserLocation! { get }     var userLocationVisible: Bool { get }     func addAnnotation(_ annotation: MKAnnotation!)     func addAnnotations(_ annotations: [AnyObject]!)     func removeAnnotation(_ annotation: MKAnnotation!)     func removeAnnotations(_ annotations: [AnyObject]!)     var annotations: [AnyObject]! { get }     func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>!     func viewForAnnotation(_ annotation: MKAnnotation!) -> MKAnnotationView!     func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String!) -> MKAnnotationView!     func selectAnnotation(_ annotation: MKAnnotation!, animated animated: Bool)     func deselectAnnotation(_ annotation: MKAnnotation!, animated animated: Bool)     var selectedAnnotations: [AnyObject]!     var annotationVisibleRect: CGRect { get }     func showAnnotations(_ annotations: [AnyObject]!, animated animated: Bool) } extension MKMapView {     func addOverlay(_ overlay: MKOverlay!, level level: MKOverlayLevel)     func addOverlays(_ overlays: [AnyObject]!, level level: MKOverlayLevel)     func removeOverlay(_ overlay: MKOverlay!)     func removeOverlays(_ overlays: [AnyObject]!)     func insertOverlay(_ overlay: MKOverlay!, atIndex index: Int, level level: MKOverlayLevel)     func insertOverlay(_ overlay: MKOverlay!, aboveOverlay sibling: MKOverlay!)     func insertOverlay(_ overlay: MKOverlay!, belowOverlay sibling: MKOverlay!)     func exchangeOverlay(_ overlay1: MKOverlay!, withOverlay overlay2: MKOverlay!)     var overlays: [AnyObject]! { get }     func overlaysInLevel(_ level: MKOverlayLevel) -> [AnyObject]!     func rendererForOverlay(_ overlay: MKOverlay!) -> MKOverlayRenderer!     func addOverlay(_ overlay: MKOverlay!)     func addOverlays(_ overlays: [AnyObject]!)     func insertOverlay(_ overlay: MKOverlay!, atIndex index: Int)     func exchangeOverlayAtIndex(_ index1: Int, withOverlayAtIndex index2: Int) } ``` |
| To | ``` class MKMapView : NSView {     weak var delegate: MKMapViewDelegate?     var mapType: MKMapType     var region: MKCoordinateRegion     func setRegion(_ region: MKCoordinateRegion, animated animated: Bool)     var centerCoordinate: CLLocationCoordinate2D     func setCenterCoordinate(_ coordinate: CLLocationCoordinate2D, animated animated: Bool)     func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion     var visibleMapRect: MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect     func _handleSelectionAtPoint(_ locationInView: CGPoint)     func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: NSEdgeInsets, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: NSEdgeInsets) -> MKMapRect     @NSCopying var camera: MKMapCamera     func setCamera(_ camera: MKMapCamera, animated animated: Bool)     func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: NSView?) -> CGPoint     func convertPoint(_ point: CGPoint, toCoordinateFromView view: NSView?) -> CLLocationCoordinate2D     func convertRegion(_ region: MKCoordinateRegion, toRectToView view: NSView?) -> CGRect     func convertRect(_ rect: CGRect, toRegionFromView view: NSView?) -> MKCoordinateRegion     var zoomEnabled: Bool     var scrollEnabled: Bool     var rotateEnabled: Bool     var pitchEnabled: Bool     var showsZoomControls: Bool     var showsCompass: Bool     var showsScale: Bool     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var showsTraffic: Bool     var showsUserLocation: Bool     var userLocation: MKUserLocation { get }     var userLocationVisible: Bool { get }     func addAnnotation(_ annotation: MKAnnotation)     func addAnnotations(_ annotations: [MKAnnotation])     func removeAnnotation(_ annotation: MKAnnotation)     func removeAnnotations(_ annotations: [MKAnnotation])     var annotations: [MKAnnotation] { get }     func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>     func viewForAnnotation(_ annotation: MKAnnotation) -> MKAnnotationView?     func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String) -> MKAnnotationView?     func selectAnnotation(_ annotation: MKAnnotation, animated animated: Bool)     func deselectAnnotation(_ annotation: MKAnnotation?, animated animated: Bool)     var selectedAnnotations: [MKAnnotation]     var annotationVisibleRect: CGRect { get }     func showAnnotations(_ annotations: [MKAnnotation], animated animated: Bool) } extension MKMapView {     func addOverlay(_ overlay: MKOverlay, level level: MKOverlayLevel)     func addOverlays(_ overlays: [MKOverlay], level level: MKOverlayLevel)     func removeOverlay(_ overlay: MKOverlay)     func removeOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int, level level: MKOverlayLevel)     func insertOverlay(_ overlay: MKOverlay, aboveOverlay sibling: MKOverlay)     func insertOverlay(_ overlay: MKOverlay, belowOverlay sibling: MKOverlay)     func exchangeOverlay(_ overlay1: MKOverlay, withOverlay overlay2: MKOverlay)     var overlays: [MKOverlay] { get }     func overlaysInLevel(_ level: MKOverlayLevel) -> [MKOverlay]     func rendererForOverlay(_ overlay: MKOverlay) -> MKOverlayRenderer?     func addOverlay(_ overlay: MKOverlay)     func addOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int)     func exchangeOverlayAtIndex(_ index1: Int, withOverlayAtIndex index2: Int) } ``` |

Modified [MKMapView.addAnnotation(_: MKAnnotation)](https://developer.apple.com/documentation/mapkit/mkmapview/1452069-addannotation)

|  | Declaration |
| --- | --- |
| From | ``` func addAnnotation(_ annotation: MKAnnotation!) ``` |
| To | ``` func addAnnotation(_ annotation: MKAnnotation) ``` |

Modified [MKMapView.addAnnotations(_: [MKAnnotation])](https://developer.apple.com/documentation/mapkit/mkmapview/1451889-addannotations)

|  | Declaration |
| --- | --- |
| From | ``` func addAnnotations(_ annotations: [AnyObject]!) ``` |
| To | ``` func addAnnotations(_ annotations: [MKAnnotation]) ``` |

Modified [MKMapView.addOverlay(_: MKOverlay)](https://developer.apple.com/documentation/mapkit/mkmapview/1451964-addoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func addOverlay(_ overlay: MKOverlay!) ``` |
| To | ``` func addOverlay(_ overlay: MKOverlay) ``` |

Modified [MKMapView.addOverlay(_: MKOverlay, level: MKOverlayLevel)](https://developer.apple.com/documentation/mapkit/mkmapview/1452635-addoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func addOverlay(_ overlay: MKOverlay!, level level: MKOverlayLevel) ``` |
| To | ``` func addOverlay(_ overlay: MKOverlay, level level: MKOverlayLevel) ``` |

Modified [MKMapView.addOverlays(_: [MKOverlay])](https://developer.apple.com/documentation/mapkit/mkmapview/1452335-addoverlays)

|  | Declaration |
| --- | --- |
| From | ``` func addOverlays(_ overlays: [AnyObject]!) ``` |
| To | ``` func addOverlays(_ overlays: [MKOverlay]) ``` |

Modified [MKMapView.addOverlays(_: [MKOverlay], level: MKOverlayLevel)](https://developer.apple.com/documentation/mapkit/mkmapview/1452518-addoverlays)

|  | Declaration |
| --- | --- |
| From | ``` func addOverlays(_ overlays: [AnyObject]!, level level: MKOverlayLevel) ``` |
| To | ``` func addOverlays(_ overlays: [MKOverlay], level level: MKOverlayLevel) ``` |

Modified [MKMapView.annotations](https://developer.apple.com/documentation/mapkit/mkmapview/1452593-annotations)

|  | Declaration |
| --- | --- |
| From | ``` var annotations: [AnyObject]! { get } ``` |
| To | ``` var annotations: [MKAnnotation] { get } ``` |

Modified [MKMapView.annotationsInMapRect(_: MKMapRect) -> Set<NSObject>](https://developer.apple.com/documentation/mapkit/mkmapview/1452279-annotations)

|  | Declaration |
| --- | --- |
| From | ``` func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>! ``` |
| To | ``` func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject> ``` |

Modified [MKMapView.camera](https://developer.apple.com/documentation/mapkit/mkmapview/1452277-camera)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var camera: MKMapCamera! ``` |
| To | ``` @NSCopying var camera: MKMapCamera ``` |

Modified [MKMapView.convertCoordinate(_: CLLocationCoordinate2D, toPointToView: NSView?) -> CGPoint](https://developer.apple.com/documentation/mapkit/mkmapview/1452694-convertcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: NSView!) -> CGPoint ``` |
| To | ``` func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: NSView?) -> CGPoint ``` |

Modified [MKMapView.convertPoint(_: CGPoint, toCoordinateFromView: NSView?) -> CLLocationCoordinate2D](https://developer.apple.com/documentation/mapkit/mkmapview/1452503-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ point: CGPoint, toCoordinateFromView view: NSView!) -> CLLocationCoordinate2D ``` |
| To | ``` func convertPoint(_ point: CGPoint, toCoordinateFromView view: NSView?) -> CLLocationCoordinate2D ``` |

Modified [MKMapView.convertRect(_: CGRect, toRegionFromView: NSView?) -> MKCoordinateRegion](https://developer.apple.com/documentation/mapkit/mkmapview/1452305-convertrect)

|  | Declaration |
| --- | --- |
| From | ``` func convertRect(_ rect: CGRect, toRegionFromView view: NSView!) -> MKCoordinateRegion ``` |
| To | ``` func convertRect(_ rect: CGRect, toRegionFromView view: NSView?) -> MKCoordinateRegion ``` |

Modified [MKMapView.convertRegion(_: MKCoordinateRegion, toRectToView: NSView?) -> CGRect](https://developer.apple.com/documentation/mapkit/mkmapview/1452055-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertRegion(_ region: MKCoordinateRegion, toRectToView view: NSView!) -> CGRect ``` |
| To | ``` func convertRegion(_ region: MKCoordinateRegion, toRectToView view: NSView?) -> CGRect ``` |

Modified [MKMapView.delegate](https://developer.apple.com/documentation/mapkit/mkmapview/1452115-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: MKMapViewDelegate! ``` |
| To | ``` weak var delegate: MKMapViewDelegate? ``` |

Modified [MKMapView.dequeueReusableAnnotationViewWithIdentifier(_: String) -> MKAnnotationView?](https://developer.apple.com/documentation/mapkit/mkmapview/1452672-dequeuereusableannotationview)

|  | Declaration |
| --- | --- |
| From | ``` func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String!) -> MKAnnotationView! ``` |
| To | ``` func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String) -> MKAnnotationView? ``` |

Modified [MKMapView.deselectAnnotation(_: MKAnnotation?, animated: Bool)](https://developer.apple.com/documentation/mapkit/mkmapview/1451988-deselectannotation)

|  | Declaration |
| --- | --- |
| From | ``` func deselectAnnotation(_ annotation: MKAnnotation!, animated animated: Bool) ``` |
| To | ``` func deselectAnnotation(_ annotation: MKAnnotation?, animated animated: Bool) ``` |

Modified [MKMapView.exchangeOverlay(_: MKOverlay, withOverlay: MKOverlay)](https://developer.apple.com/documentation/mapkit/mkmapview/1452491-exchangeoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func exchangeOverlay(_ overlay1: MKOverlay!, withOverlay overlay2: MKOverlay!) ``` |
| To | ``` func exchangeOverlay(_ overlay1: MKOverlay, withOverlay overlay2: MKOverlay) ``` |

Modified [MKMapView.insertOverlay(_: MKOverlay, aboveOverlay: MKOverlay)](https://developer.apple.com/documentation/mapkit/mkmapview/1452427-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func insertOverlay(_ overlay: MKOverlay!, aboveOverlay sibling: MKOverlay!) ``` |
| To | ``` func insertOverlay(_ overlay: MKOverlay, aboveOverlay sibling: MKOverlay) ``` |

Modified [MKMapView.insertOverlay(_: MKOverlay, atIndex: Int)](https://developer.apple.com/documentation/mapkit/mkmapview/1452249-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func insertOverlay(_ overlay: MKOverlay!, atIndex index: Int) ``` |
| To | ``` func insertOverlay(_ overlay: MKOverlay, atIndex index: Int) ``` |

Modified [MKMapView.insertOverlay(_: MKOverlay, atIndex: Int, level: MKOverlayLevel)](https://developer.apple.com/documentation/mapkit/mkmapview/1452723-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func insertOverlay(_ overlay: MKOverlay!, atIndex index: Int, level level: MKOverlayLevel) ``` |
| To | ``` func insertOverlay(_ overlay: MKOverlay, atIndex index: Int, level level: MKOverlayLevel) ``` |

Modified [MKMapView.insertOverlay(_: MKOverlay, belowOverlay: MKOverlay)](https://developer.apple.com/documentation/mapkit/mkmapview/1452526-insertoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func insertOverlay(_ overlay: MKOverlay!, belowOverlay sibling: MKOverlay!) ``` |
| To | ``` func insertOverlay(_ overlay: MKOverlay, belowOverlay sibling: MKOverlay) ``` |

Modified [MKMapView.overlays](https://developer.apple.com/documentation/mapkit/mkmapview/1452784-overlays)

|  | Declaration |
| --- | --- |
| From | ``` var overlays: [AnyObject]! { get } ``` |
| To | ``` var overlays: [MKOverlay] { get } ``` |

Modified [MKMapView.overlaysInLevel(_: MKOverlayLevel) -> [MKOverlay]](https://developer.apple.com/documentation/mapkit/mkmapview/1452757-overlaysinlevel)

|  | Declaration |
| --- | --- |
| From | ``` func overlaysInLevel(_ level: MKOverlayLevel) -> [AnyObject]! ``` |
| To | ``` func overlaysInLevel(_ level: MKOverlayLevel) -> [MKOverlay] ``` |

Modified [MKMapView.removeAnnotation(_: MKAnnotation)](https://developer.apple.com/documentation/mapkit/mkmapview/1452409-removeannotation)

|  | Declaration |
| --- | --- |
| From | ``` func removeAnnotation(_ annotation: MKAnnotation!) ``` |
| To | ``` func removeAnnotation(_ annotation: MKAnnotation) ``` |

Modified [MKMapView.removeAnnotations(_: [MKAnnotation])](https://developer.apple.com/documentation/mapkit/mkmapview/1452130-removeannotations)

|  | Declaration |
| --- | --- |
| From | ``` func removeAnnotations(_ annotations: [AnyObject]!) ``` |
| To | ``` func removeAnnotations(_ annotations: [MKAnnotation]) ``` |

Modified [MKMapView.removeOverlay(_: MKOverlay)](https://developer.apple.com/documentation/mapkit/mkmapview/1451921-removeoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func removeOverlay(_ overlay: MKOverlay!) ``` |
| To | ``` func removeOverlay(_ overlay: MKOverlay) ``` |

Modified [MKMapView.removeOverlays(_: [MKOverlay])](https://developer.apple.com/documentation/mapkit/mkmapview/1452719-removeoverlays)

|  | Declaration |
| --- | --- |
| From | ``` func removeOverlays(_ overlays: [AnyObject]!) ``` |
| To | ``` func removeOverlays(_ overlays: [MKOverlay]) ``` |

Modified [MKMapView.rendererForOverlay(_: MKOverlay) -> MKOverlayRenderer?](https://developer.apple.com/documentation/mapkit/mkmapview/1452464-rendererforoverlay)

|  | Declaration |
| --- | --- |
| From | ``` func rendererForOverlay(_ overlay: MKOverlay!) -> MKOverlayRenderer! ``` |
| To | ``` func rendererForOverlay(_ overlay: MKOverlay) -> MKOverlayRenderer? ``` |

Modified [MKMapView.selectAnnotation(_: MKAnnotation, animated: Bool)](https://developer.apple.com/documentation/mapkit/mkmapview/1451950-selectannotation)

|  | Declaration |
| --- | --- |
| From | ``` func selectAnnotation(_ annotation: MKAnnotation!, animated animated: Bool) ``` |
| To | ``` func selectAnnotation(_ annotation: MKAnnotation, animated animated: Bool) ``` |

Modified [MKMapView.selectedAnnotations](https://developer.apple.com/documentation/mapkit/mkmapview/1452570-selectedannotations)

|  | Declaration |
| --- | --- |
| From | ``` var selectedAnnotations: [AnyObject]! ``` |
| To | ``` var selectedAnnotations: [MKAnnotation] ``` |

Modified [MKMapView.setCamera(_: MKMapCamera, animated: Bool)](https://developer.apple.com/documentation/mapkit/mkmapview/1452476-setcamera)

|  | Declaration |
| --- | --- |
| From | ``` func setCamera(_ camera: MKMapCamera!, animated animated: Bool) ``` |
| To | ``` func setCamera(_ camera: MKMapCamera, animated animated: Bool) ``` |

Modified [MKMapView.showAnnotations(_: [MKAnnotation], animated: Bool)](https://developer.apple.com/documentation/mapkit/mkmapview/1452309-showannotations)

|  | Declaration |
| --- | --- |
| From | ``` func showAnnotations(_ annotations: [AnyObject]!, animated animated: Bool) ``` |
| To | ``` func showAnnotations(_ annotations: [MKAnnotation], animated animated: Bool) ``` |

Modified [MKMapView.userLocation](https://developer.apple.com/documentation/mapkit/mkmapview/1452459-userlocation)

|  | Declaration |
| --- | --- |
| From | ``` var userLocation: MKUserLocation! { get } ``` |
| To | ``` var userLocation: MKUserLocation { get } ``` |

Modified [MKMapView.viewForAnnotation(_: MKAnnotation) -> MKAnnotationView?](https://developer.apple.com/documentation/mapkit/mkmapview/1452512-view)

|  | Declaration |
| --- | --- |
| From | ``` func viewForAnnotation(_ annotation: MKAnnotation!) -> MKAnnotationView! ``` |
| To | ``` func viewForAnnotation(_ annotation: MKAnnotation) -> MKAnnotationView? ``` |

Modified [MKMapViewDelegate](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol MKMapViewDelegate : NSObjectProtocol {     optional func mapView(_ mapView: MKMapView!, regionWillChangeAnimated animated: Bool)     optional func mapView(_ mapView: MKMapView!, regionDidChangeAnimated animated: Bool)     optional func mapViewWillStartLoadingMap(_ mapView: MKMapView!)     optional func mapViewDidFinishLoadingMap(_ mapView: MKMapView!)     optional func mapViewDidFailLoadingMap(_ mapView: MKMapView!, withError error: NSError!)     optional func mapViewWillStartRenderingMap(_ mapView: MKMapView!)     optional func mapViewDidFinishRenderingMap(_ mapView: MKMapView!, fullyRendered fullyRendered: Bool)     optional func mapView(_ mapView: MKMapView!, viewForAnnotation annotation: MKAnnotation!) -> MKAnnotationView!     optional func mapView(_ mapView: MKMapView!, didAddAnnotationViews views: [AnyObject]!)     optional func mapView(_ mapView: MKMapView!, didSelectAnnotationView view: MKAnnotationView!)     optional func mapView(_ mapView: MKMapView!, didDeselectAnnotationView view: MKAnnotationView!)     optional func mapViewWillStartLocatingUser(_ mapView: MKMapView!)     optional func mapViewDidStopLocatingUser(_ mapView: MKMapView!)     optional func mapView(_ mapView: MKMapView!, didUpdateUserLocation userLocation: MKUserLocation!)     optional func mapView(_ mapView: MKMapView!, didFailToLocateUserWithError error: NSError!)     optional func mapView(_ mapView: MKMapView!, annotationView view: MKAnnotationView!, didChangeDragState newState: MKAnnotationViewDragState, fromOldState oldState: MKAnnotationViewDragState)     optional func mapView(_ mapView: MKMapView!, rendererForOverlay overlay: MKOverlay!) -> MKOverlayRenderer!     optional func mapView(_ mapView: MKMapView!, didAddOverlayRenderers renderers: [AnyObject]!) } ``` |
| To | ``` protocol MKMapViewDelegate : NSObjectProtocol {     optional func mapView(_ mapView: MKMapView, regionWillChangeAnimated animated: Bool)     optional func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool)     optional func mapViewWillStartLoadingMap(_ mapView: MKMapView)     optional func mapViewDidFinishLoadingMap(_ mapView: MKMapView)     optional func mapViewDidFailLoadingMap(_ mapView: MKMapView, withError error: NSError)     optional func mapViewWillStartRenderingMap(_ mapView: MKMapView)     optional func mapViewDidFinishRenderingMap(_ mapView: MKMapView, fullyRendered fullyRendered: Bool)     optional func mapView(_ mapView: MKMapView, viewForAnnotation annotation: MKAnnotation) -> MKAnnotationView?     optional func mapView(_ mapView: MKMapView, didAddAnnotationViews views: [MKAnnotationView])     optional func mapView(_ mapView: MKMapView, didSelectAnnotationView view: MKAnnotationView)     optional func mapView(_ mapView: MKMapView, didDeselectAnnotationView view: MKAnnotationView)     optional func mapViewWillStartLocatingUser(_ mapView: MKMapView)     optional func mapViewDidStopLocatingUser(_ mapView: MKMapView)     optional func mapView(_ mapView: MKMapView, didUpdateUserLocation userLocation: MKUserLocation)     optional func mapView(_ mapView: MKMapView, didFailToLocateUserWithError error: NSError)     optional func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, didChangeDragState newState: MKAnnotationViewDragState, fromOldState oldState: MKAnnotationViewDragState)     optional func mapView(_ mapView: MKMapView, rendererForOverlay overlay: MKOverlay) -> MKOverlayRenderer     optional func mapView(_ mapView: MKMapView, didAddOverlayRenderers renderers: [MKOverlayRenderer]) } ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, annotationView: MKAnnotationView, didChangeDragState: MKAnnotationViewDragState, fromOldState: MKAnnotationViewDragState)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452229-mapview)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, annotationView view: MKAnnotationView!, didChangeDragState newState: MKAnnotationViewDragState, fromOldState oldState: MKAnnotationViewDragState) ``` |
| To | ``` optional func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, didChangeDragState newState: MKAnnotationViewDragState, fromOldState oldState: MKAnnotationViewDragState) ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, didAddAnnotationViews: [MKAnnotationView])](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452311-mapview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, didAddAnnotationViews views: [AnyObject]!) ``` | OS X 10.10 |
| To | ``` optional func mapView(_ mapView: MKMapView, didAddAnnotationViews views: [MKAnnotationView]) ``` | OS X 10.9 |

Modified [MKMapViewDelegate.mapView(_: MKMapView, didAddOverlayRenderers: [MKOverlayRenderer])](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452609-mapview)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, didAddOverlayRenderers renderers: [AnyObject]!) ``` |
| To | ``` optional func mapView(_ mapView: MKMapView, didAddOverlayRenderers renderers: [MKOverlayRenderer]) ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, didDeselectAnnotationView: MKAnnotationView)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452707-mapview)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, didDeselectAnnotationView view: MKAnnotationView!) ``` |
| To | ``` optional func mapView(_ mapView: MKMapView, didDeselectAnnotationView view: MKAnnotationView) ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, didFailToLocateUserWithError: NSError)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452211-mapview)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, didFailToLocateUserWithError error: NSError!) ``` |
| To | ``` optional func mapView(_ mapView: MKMapView, didFailToLocateUserWithError error: NSError) ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, didSelectAnnotationView: MKAnnotationView)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452393-mapview)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, didSelectAnnotationView view: MKAnnotationView!) ``` |
| To | ``` optional func mapView(_ mapView: MKMapView, didSelectAnnotationView view: MKAnnotationView) ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, didUpdateUserLocation: MKUserLocation)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452086-mapview)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, didUpdateUserLocation userLocation: MKUserLocation!) ``` |
| To | ``` optional func mapView(_ mapView: MKMapView, didUpdateUserLocation userLocation: MKUserLocation) ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, regionDidChangeAnimated: Bool)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452345-mapview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, regionDidChangeAnimated animated: Bool) ``` | OS X 10.10 |
| To | ``` optional func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool) ``` | OS X 10.9 |

Modified [MKMapViewDelegate.mapView(_: MKMapView, regionWillChangeAnimated: Bool)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452571-mapview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, regionWillChangeAnimated animated: Bool) ``` | OS X 10.10 |
| To | ``` optional func mapView(_ mapView: MKMapView, regionWillChangeAnimated animated: Bool) ``` | OS X 10.9 |

Modified [MKMapViewDelegate.mapView(_: MKMapView, rendererForOverlay: MKOverlay) -> MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452203-mapview)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, rendererForOverlay overlay: MKOverlay!) -> MKOverlayRenderer! ``` |
| To | ``` optional func mapView(_ mapView: MKMapView, rendererForOverlay overlay: MKOverlay) -> MKOverlayRenderer ``` |

Modified [MKMapViewDelegate.mapView(_: MKMapView, viewForAnnotation: MKAnnotation) -> MKAnnotationView?](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452045-mapview)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mapView(_ mapView: MKMapView!, viewForAnnotation annotation: MKAnnotation!) -> MKAnnotationView! ``` | OS X 10.10 |
| To | ``` optional func mapView(_ mapView: MKMapView, viewForAnnotation annotation: MKAnnotation) -> MKAnnotationView? ``` | OS X 10.9 |

Modified [MKMapViewDelegate.mapViewDidFailLoadingMap(_: MKMapView, withError: NSError)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452327-mapviewdidfailloadingmap)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mapViewDidFailLoadingMap(_ mapView: MKMapView!, withError error: NSError!) ``` | OS X 10.10 |
| To | ``` optional func mapViewDidFailLoadingMap(_ mapView: MKMapView, withError error: NSError) ``` | OS X 10.9 |

Modified [MKMapViewDelegate.mapViewDidFinishLoadingMap(_: MKMapView)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452291-mapviewdidfinishloadingmap)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mapViewDidFinishLoadingMap(_ mapView: MKMapView!) ``` | OS X 10.10 |
| To | ``` optional func mapViewDidFinishLoadingMap(_ mapView: MKMapView) ``` | OS X 10.9 |

Modified [MKMapViewDelegate.mapViewDidFinishRenderingMap(_: MKMapView, fullyRendered: Bool)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451897-mapviewdidfinishrenderingmap)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapViewDidFinishRenderingMap(_ mapView: MKMapView!, fullyRendered fullyRendered: Bool) ``` |
| To | ``` optional func mapViewDidFinishRenderingMap(_ mapView: MKMapView, fullyRendered fullyRendered: Bool) ``` |

Modified [MKMapViewDelegate.mapViewDidStopLocatingUser(_: MKMapView)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452715-mapviewdidstoplocatinguser)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapViewDidStopLocatingUser(_ mapView: MKMapView!) ``` |
| To | ``` optional func mapViewDidStopLocatingUser(_ mapView: MKMapView) ``` |

Modified [MKMapViewDelegate.mapViewWillStartLoadingMap(_: MKMapView)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452744-mapviewwillstartloadingmap)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func mapViewWillStartLoadingMap(_ mapView: MKMapView!) ``` | OS X 10.10 |
| To | ``` optional func mapViewWillStartLoadingMap(_ mapView: MKMapView) ``` | OS X 10.9 |

Modified [MKMapViewDelegate.mapViewWillStartLocatingUser(_: MKMapView)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1452171-mapviewwillstartlocatinguser)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapViewWillStartLocatingUser(_ mapView: MKMapView!) ``` |
| To | ``` optional func mapViewWillStartLocatingUser(_ mapView: MKMapView) ``` |

Modified [MKMapViewDelegate.mapViewWillStartRenderingMap(_: MKMapView)](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/1451970-mapviewwillstartrenderingmap)

|  | Declaration |
| --- | --- |
| From | ``` optional func mapViewWillStartRenderingMap(_ mapView: MKMapView!) ``` |
| To | ``` optional func mapViewWillStartRenderingMap(_ mapView: MKMapView) ``` |

Modified [MKOverlayLevel [enum]](https://developer.apple.com/documentation/mapkit/mkoverlaylevel)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [MKOverlayPathRenderer](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer)

|  | Declaration |
| --- | --- |
| From | ``` class MKOverlayPathRenderer : MKOverlayRenderer {     var fillColor: NSColor!     var strokeColor: NSColor!     var lineWidth: CGFloat     var lineJoin: CGLineJoin     var lineCap: CGLineCap     var miterLimit: CGFloat     var lineDashPhase: CGFloat     var lineDashPattern: [AnyObject]!     func createPath()     var path: CGPath!     func invalidatePath()     func applyStrokePropertiesToContext(_ context: CGContext!, atZoomScale zoomScale: MKZoomScale)     func applyFillPropertiesToContext(_ context: CGContext!, atZoomScale zoomScale: MKZoomScale)     func strokePath(_ path: CGPath!, inContext context: CGContext!)     func fillPath(_ path: CGPath!, inContext context: CGContext!) } ``` |
| To | ``` class MKOverlayPathRenderer : MKOverlayRenderer {     var fillColor: NSColor?     var strokeColor: NSColor?     var lineWidth: CGFloat     var lineJoin: CGLineJoin     var lineCap: CGLineCap     var miterLimit: CGFloat     var lineDashPhase: CGFloat     var lineDashPattern: [NSNumber]?     func createPath()     var path: CGPath!     func invalidatePath()     func applyStrokePropertiesToContext(_ context: CGContext, atZoomScale zoomScale: MKZoomScale)     func applyFillPropertiesToContext(_ context: CGContext, atZoomScale zoomScale: MKZoomScale)     func strokePath(_ path: CGPath, inContext context: CGContext)     func fillPath(_ path: CGPath, inContext context: CGContext) } ``` |

Modified [MKOverlayPathRenderer.applyFillPropertiesToContext(_: CGContext, atZoomScale: MKZoomScale)](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452281-applyfillpropertiestocontext)

|  | Declaration |
| --- | --- |
| From | ``` func applyFillPropertiesToContext(_ context: CGContext!, atZoomScale zoomScale: MKZoomScale) ``` |
| To | ``` func applyFillPropertiesToContext(_ context: CGContext, atZoomScale zoomScale: MKZoomScale) ``` |

Modified [MKOverlayPathRenderer.applyStrokePropertiesToContext(_: CGContext, atZoomScale: MKZoomScale)](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452713-applystrokepropertiestocontext)

|  | Declaration |
| --- | --- |
| From | ``` func applyStrokePropertiesToContext(_ context: CGContext!, atZoomScale zoomScale: MKZoomScale) ``` |
| To | ``` func applyStrokePropertiesToContext(_ context: CGContext, atZoomScale zoomScale: MKZoomScale) ``` |

Modified [MKOverlayPathRenderer.fillColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452668-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` var fillColor: NSColor! ``` |
| To | ``` var fillColor: NSColor? ``` |

Modified [MKOverlayPathRenderer.fillPath(_: CGPath, inContext: CGContext)](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452100-fillpath)

|  | Declaration |
| --- | --- |
| From | ``` func fillPath(_ path: CGPath!, inContext context: CGContext!) ``` |
| To | ``` func fillPath(_ path: CGPath, inContext context: CGContext) ``` |

Modified [MKOverlayPathRenderer.lineDashPattern](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452493-linedashpattern)

|  | Declaration |
| --- | --- |
| From | ``` var lineDashPattern: [AnyObject]! ``` |
| To | ``` var lineDashPattern: [NSNumber]? ``` |

Modified [MKOverlayPathRenderer.strokeColor](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452175-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` var strokeColor: NSColor! ``` |
| To | ``` var strokeColor: NSColor? ``` |

Modified [MKOverlayPathRenderer.strokePath(_: CGPath, inContext: CGContext)](https://developer.apple.com/documentation/mapkit/mkoverlaypathrenderer/1452549-strokepath)

|  | Declaration |
| --- | --- |
| From | ``` func strokePath(_ path: CGPath!, inContext context: CGContext!) ``` |
| To | ``` func strokePath(_ path: CGPath, inContext context: CGContext) ``` |

Modified [MKOverlayRenderer](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer)

|  | Declaration |
| --- | --- |
| From | ``` class MKOverlayRenderer : NSObject {     init!(overlay overlay: MKOverlay!)     var overlay: MKOverlay! { get }     func pointForMapPoint(_ mapPoint: MKMapPoint) -> CGPoint     func mapPointForPoint(_ point: CGPoint) -> MKMapPoint     func rectForMapRect(_ mapRect: MKMapRect) -> CGRect     func mapRectForRect(_ rect: CGRect) -> MKMapRect     func canDrawMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale) -> Bool     func drawMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale, inContext context: CGContext!)     func setNeedsDisplay()     func setNeedsDisplayInMapRect(_ mapRect: MKMapRect)     func setNeedsDisplayInMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale)     var alpha: CGFloat     var contentScaleFactor: CGFloat { get } } ``` |
| To | ``` class MKOverlayRenderer : NSObject {     init(overlay overlay: MKOverlay)     var overlay: MKOverlay { get }     func pointForMapPoint(_ mapPoint: MKMapPoint) -> CGPoint     func mapPointForPoint(_ point: CGPoint) -> MKMapPoint     func rectForMapRect(_ mapRect: MKMapRect) -> CGRect     func mapRectForRect(_ rect: CGRect) -> MKMapRect     func canDrawMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale) -> Bool     func drawMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale, inContext context: CGContext)     func setNeedsDisplay()     func setNeedsDisplayInMapRect(_ mapRect: MKMapRect)     func setNeedsDisplayInMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale)     var alpha: CGFloat     var contentScaleFactor: CGFloat { get } } ``` |

Modified [MKOverlayRenderer.drawMapRect(_: MKMapRect, zoomScale: MKZoomScale, inContext: CGContext)](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452184-draw)

|  | Declaration |
| --- | --- |
| From | ``` func drawMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale, inContext context: CGContext!) ``` |
| To | ``` func drawMapRect(_ mapRect: MKMapRect, zoomScale zoomScale: MKZoomScale, inContext context: CGContext) ``` |

Modified [MKOverlayRenderer.init(overlay: MKOverlay)](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1451915-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(overlay overlay: MKOverlay!) ``` |
| To | ``` init(overlay overlay: MKOverlay) ``` |

Modified [MKOverlayRenderer.overlay](https://developer.apple.com/documentation/mapkit/mkoverlayrenderer/1452307-overlay)

|  | Declaration |
| --- | --- |
| From | ``` var overlay: MKOverlay! { get } ``` |
| To | ``` var overlay: MKOverlay { get } ``` |

Modified [MKPinAnnotationColor [enum]](https://developer.apple.com/documentation/mapkit/mkpinannotationcolor)

|  | Deprecation | Raw Value Type |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.11 | UInt |

Modified [MKPinAnnotationView](https://developer.apple.com/documentation/mapkit/mkpinannotationview)

|  | Declaration |
| --- | --- |
| From | ``` class MKPinAnnotationView : MKAnnotationView {     var pinColor: MKPinAnnotationColor     var animatesDrop: Bool } ``` |
| To | ``` class MKPinAnnotationView : MKAnnotationView {     class func redPinColor() -> NSColor     class func greenPinColor() -> NSColor     class func purplePinColor() -> NSColor     var pinTintColor: NSColor!     var animatesDrop: Bool     var pinColor: MKPinAnnotationColor } ``` |

Modified [MKPinAnnotationView.pinColor](https://developer.apple.com/documentation/mapkit/mkpinannotationview/1452530-pincolor)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.11 |

Modified [MKPlacemark](https://developer.apple.com/documentation/mapkit/mkplacemark)

|  | Declaration |
| --- | --- |
| From | ``` class MKPlacemark : CLPlacemark, MKAnnotation, NSObjectProtocol {     init!(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [NSObject : AnyObject]!)     var countryCode: String! { get } } ``` |
| To | ``` class MKPlacemark : CLPlacemark, MKAnnotation {     init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [String : AnyObject]?)     var countryCode: String? { get } } ``` |

Modified [MKPlacemark.countryCode](https://developer.apple.com/documentation/mapkit/mkplacemark/1451952-countrycode)

|  | Declaration |
| --- | --- |
| From | ``` var countryCode: String! { get } ``` |
| To | ``` var countryCode: String? { get } ``` |

Modified [MKPlacemark.init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : AnyObject]?)](https://developer.apple.com/documentation/mapkit/mkplacemark/1451895-initwithcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` init!(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [NSObject : AnyObject]!) ``` |
| To | ``` init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [String : AnyObject]?) ``` |

Modified [MKPolygon](https://developer.apple.com/documentation/mapkit/mkpolygon)

|  | Declaration |
| --- | --- |
| From | ``` class MKPolygon : MKMultiPoint, MKOverlay, MKAnnotation, NSObjectProtocol {     convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int)     class func polygonWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int) -> Self!     convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!)     class func polygonWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) -> Self!     convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int)     class func polygonWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) -> Self!     convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!)     class func polygonWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) -> Self!     var interiorPolygons: [AnyObject]! { get } } ``` |
| To | ``` class MKPolygon : MKMultiPoint, MKOverlay {     convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int)     class func polygonWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int) -> Self     convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [MKPolygon]?)     class func polygonWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [MKPolygon]?) -> Self     convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int)     class func polygonWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) -> Self     convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [MKPolygon]?)     class func polygonWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [MKPolygon]?) -> Self     var interiorPolygons: [MKPolygon]? { get } } ``` |

Modified [MKPolygon.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)](https://developer.apple.com/documentation/mapkit/mkpolygon/1452497-polygonwithcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified [MKPolygon.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int, interiorPolygons: [MKPolygon]?)](https://developer.apple.com/documentation/mapkit/mkpolygon/1452532-polygonwithcoordinates)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |
| To | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int, interiorPolygons interiorPolygons: [MKPolygon]?) ``` |

Modified [MKPolygon.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)](https://developer.apple.com/documentation/mapkit/mkpolygon/1452247-polygonwithpoints)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified [MKPolygon.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int, interiorPolygons: [MKPolygon]?)](https://developer.apple.com/documentation/mapkit/mkpolygon/1451945-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [AnyObject]!) ``` |
| To | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int, interiorPolygons interiorPolygons: [MKPolygon]?) ``` |

Modified [MKPolygon.interiorPolygons](https://developer.apple.com/documentation/mapkit/mkpolygon/1452521-interiorpolygons)

|  | Declaration |
| --- | --- |
| From | ``` var interiorPolygons: [AnyObject]! { get } ``` |
| To | ``` var interiorPolygons: [MKPolygon]? { get } ``` |

Modified [MKPolygonRenderer](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer)

|  | Declaration |
| --- | --- |
| From | ``` class MKPolygonRenderer : MKOverlayPathRenderer {     init!(polygon polygon: MKPolygon!)     var polygon: MKPolygon! { get } } ``` |
| To | ``` class MKPolygonRenderer : MKOverlayPathRenderer {     init(polygon polygon: MKPolygon)     var polygon: MKPolygon { get } } ``` |

Modified [MKPolygonRenderer.init(polygon: MKPolygon)](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/1448129-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(polygon polygon: MKPolygon!) ``` |
| To | ``` init(polygon polygon: MKPolygon) ``` |

Modified [MKPolygonRenderer.polygon](https://developer.apple.com/documentation/mapkit/mkpolygonrenderer/1448132-polygon)

|  | Declaration |
| --- | --- |
| From | ``` var polygon: MKPolygon! { get } ``` |
| To | ``` var polygon: MKPolygon { get } ``` |

Modified [MKPolyline](https://developer.apple.com/documentation/mapkit/mkpolyline)

|  | Declaration |
| --- | --- |
| From | ``` class MKPolyline : MKMultiPoint, MKOverlay, MKAnnotation, NSObjectProtocol {     convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int)     class func polylineWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int) -> Self!     convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int)     class func polylineWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) -> Self! } ``` |
| To | ``` class MKPolyline : MKMultiPoint, MKOverlay {     convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int)     class func polylineWithPoints(_ points: UnsafeMutablePointer<MKMapPoint>, count count: Int) -> Self     convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int)     class func polylineWithCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) -> Self } ``` |

Modified [MKPolyline.init(coordinates: UnsafeMutablePointer<CLLocationCoordinate2D>, count: Int)](https://developer.apple.com/documentation/mapkit/mkpolyline/1452205-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |
| To | ``` convenience init(coordinates coords: UnsafeMutablePointer<CLLocationCoordinate2D>, count count: Int) ``` |

Modified [MKPolyline.init(points: UnsafeMutablePointer<MKMapPoint>, count: Int)](https://developer.apple.com/documentation/mapkit/mkpolyline/1452773-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |
| To | ``` convenience init(points points: UnsafeMutablePointer<MKMapPoint>, count count: Int) ``` |

Modified [MKPolylineRenderer](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer)

|  | Declaration |
| --- | --- |
| From | ``` class MKPolylineRenderer : MKOverlayPathRenderer {     init!(polyline polyline: MKPolyline!)     var polyline: MKPolyline! { get } } ``` |
| To | ``` class MKPolylineRenderer : MKOverlayPathRenderer {     init(polyline polyline: MKPolyline)     var polyline: MKPolyline { get } } ``` |

Modified [MKPolylineRenderer.init(polyline: MKPolyline)](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452074-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(polyline polyline: MKPolyline!) ``` |
| To | ``` init(polyline polyline: MKPolyline) ``` |

Modified [MKPolylineRenderer.polyline](https://developer.apple.com/documentation/mapkit/mkpolylinerenderer/1452465-polyline)

|  | Declaration |
| --- | --- |
| From | ``` var polyline: MKPolyline! { get } ``` |
| To | ``` var polyline: MKPolyline { get } ``` |

Modified [MKRoute](https://developer.apple.com/documentation/mapkit/mkroute)

|  | Declaration |
| --- | --- |
| From | ``` class MKRoute : NSObject {     var name: String! { get }     var advisoryNotices: [AnyObject]! { get }     var distance: CLLocationDistance { get }     var expectedTravelTime: NSTimeInterval { get }     var transportType: MKDirectionsTransportType { get }     var polyline: MKPolyline! { get }     var steps: [AnyObject]! { get } } ``` |
| To | ``` class MKRoute : NSObject {     var name: String { get }     var advisoryNotices: [String] { get }     var distance: CLLocationDistance { get }     var expectedTravelTime: NSTimeInterval { get }     var transportType: MKDirectionsTransportType { get }     var polyline: MKPolyline { get }     var steps: [MKRouteStep] { get } } ``` |

Modified [MKRoute.advisoryNotices](https://developer.apple.com/documentation/mapkit/mkroute/1452359-advisorynotices)

|  | Declaration |
| --- | --- |
| From | ``` var advisoryNotices: [AnyObject]! { get } ``` |
| To | ``` var advisoryNotices: [String] { get } ``` |

Modified [MKRoute.name](https://developer.apple.com/documentation/mapkit/mkroute/1452684-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [MKRoute.polyline](https://developer.apple.com/documentation/mapkit/mkroute/1451943-polyline)

|  | Declaration |
| --- | --- |
| From | ``` var polyline: MKPolyline! { get } ``` |
| To | ``` var polyline: MKPolyline { get } ``` |

Modified [MKRoute.steps](https://developer.apple.com/documentation/mapkit/mkroute/1452173-steps)

|  | Declaration |
| --- | --- |
| From | ``` var steps: [AnyObject]! { get } ``` |
| To | ``` var steps: [MKRouteStep] { get } ``` |

Modified [MKRouteStep](https://developer.apple.com/documentation/mapkit/mkroutestep)

|  | Declaration |
| --- | --- |
| From | ``` class MKRouteStep : NSObject {     var instructions: String! { get }     var notice: String! { get }     var polyline: MKPolyline! { get }     var distance: CLLocationDistance { get }     var transportType: MKDirectionsTransportType { get } } ``` |
| To | ``` class MKRouteStep : NSObject {     var instructions: String { get }     var notice: String? { get }     var polyline: MKPolyline { get }     var distance: CLLocationDistance { get }     var transportType: MKDirectionsTransportType { get } } ``` |

Modified [MKRouteStep.instructions](https://developer.apple.com/documentation/mapkit/mkroutestep/1452447-instructions)

|  | Declaration |
| --- | --- |
| From | ``` var instructions: String! { get } ``` |
| To | ``` var instructions: String { get } ``` |

Modified [MKRouteStep.notice](https://developer.apple.com/documentation/mapkit/mkroutestep/1452347-notice)

|  | Declaration |
| --- | --- |
| From | ``` var notice: String! { get } ``` |
| To | ``` var notice: String? { get } ``` |

Modified [MKRouteStep.polyline](https://developer.apple.com/documentation/mapkit/mkroutestep/1452223-polyline)

|  | Declaration |
| --- | --- |
| From | ``` var polyline: MKPolyline! { get } ``` |
| To | ``` var polyline: MKPolyline { get } ``` |

Modified [MKShape](https://developer.apple.com/documentation/mapkit/mkshape)

|  | Declaration |
| --- | --- |
| From | ``` class MKShape : NSObject, MKAnnotation, NSObjectProtocol {     var title: String!     var subtitle: String! } ``` |
| To | ``` class MKShape : NSObject, MKAnnotation {     var title: String?     var subtitle: String? } ``` |

Modified [MKShape.subtitle](https://developer.apple.com/documentation/mapkit/mkshape/1437592-subtitle)

|  | Declaration |
| --- | --- |
| From | ``` var subtitle: String! ``` |
| To | ``` var subtitle: String? ``` |

Modified [MKShape.title](https://developer.apple.com/documentation/mapkit/mkshape/1437594-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String? ``` |

Modified [MKTileOverlay](https://developer.apple.com/documentation/mapkit/mktileoverlay)

|  | Declaration |
| --- | --- |
| From | ``` class MKTileOverlay : NSObject, MKOverlay, MKAnnotation, NSObjectProtocol {     init!(URLTemplate URLTemplate: String!)     var tileSize: CGSize     var geometryFlipped: Bool     var minimumZ: Int     var maximumZ: Int     var URLTemplate: String! { get }     var canReplaceMapContent: Bool } extension MKTileOverlay {     func URLForTilePath(_ path: MKTileOverlayPath) -> NSURL!     func loadTileAtPath(_ path: MKTileOverlayPath, result result: ((NSData!, NSError!) -> Void)!) } ``` |
| To | ``` class MKTileOverlay : NSObject, MKOverlay, MKAnnotation {     init(URLTemplate URLTemplate: String?)     var tileSize: CGSize     var geometryFlipped: Bool     var minimumZ: Int     var maximumZ: Int     var URLTemplate: String? { get }     var canReplaceMapContent: Bool } extension MKTileOverlay {     func URLForTilePath(_ path: MKTileOverlayPath) -> NSURL     func loadTileAtPath(_ path: MKTileOverlayPath, result result: (NSData?, NSError?) -> Void) } ``` |

Modified [MKTileOverlay.init(URLTemplate: String?)](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452705-initwithurltemplate)

|  | Declaration |
| --- | --- |
| From | ``` init!(URLTemplate URLTemplate: String!) ``` |
| To | ``` init(URLTemplate URLTemplate: String?) ``` |

Modified [MKTileOverlay.loadTileAtPath(_: MKTileOverlayPath, result: (NSData?, NSError?) -> Void)](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452445-loadtile)

|  | Declaration |
| --- | --- |
| From | ``` func loadTileAtPath(_ path: MKTileOverlayPath, result result: ((NSData!, NSError!) -> Void)!) ``` |
| To | ``` func loadTileAtPath(_ path: MKTileOverlayPath, result result: (NSData?, NSError?) -> Void) ``` |

Modified [MKTileOverlay.URLForTilePath(_: MKTileOverlayPath) -> NSURL](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452606-url)

|  | Declaration |
| --- | --- |
| From | ``` func URLForTilePath(_ path: MKTileOverlayPath) -> NSURL! ``` |
| To | ``` func URLForTilePath(_ path: MKTileOverlayPath) -> NSURL ``` |

Modified [MKTileOverlay.URLTemplate](https://developer.apple.com/documentation/mapkit/mktileoverlay/1452256-urltemplate)

|  | Declaration |
| --- | --- |
| From | ``` var URLTemplate: String! { get } ``` |
| To | ``` var URLTemplate: String? { get } ``` |

Modified [MKTileOverlayRenderer](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer)

|  | Declaration |
| --- | --- |
| From | ``` class MKTileOverlayRenderer : MKOverlayRenderer {     init!(tileOverlay overlay: MKTileOverlay!)     func reloadData() } ``` |
| To | ``` class MKTileOverlayRenderer : MKOverlayRenderer {     init(tileOverlay overlay: MKTileOverlay)     func reloadData() } ``` |

Modified [MKTileOverlayRenderer.init(tileOverlay: MKTileOverlay)](https://developer.apple.com/documentation/mapkit/mktileoverlayrenderer/1452303-initwithtileoverlay)

|  | Declaration |
| --- | --- |
| From | ``` init!(tileOverlay overlay: MKTileOverlay!) ``` |
| To | ``` init(tileOverlay overlay: MKTileOverlay) ``` |

Modified [MKUserLocation](https://developer.apple.com/documentation/mapkit/mkuserlocation)

|  | Declaration |
| --- | --- |
| From | ``` class MKUserLocation : NSObject, MKAnnotation, NSObjectProtocol {     var updating: Bool { get }     var location: CLLocation! { get }     var heading: CLHeading! { get }     var title: String!     var subtitle: String! } ``` |
| To | ``` class MKUserLocation : NSObject, MKAnnotation {     var updating: Bool { get }     var location: CLLocation? { get }     var heading: CLHeading? { get }     var title: String?     var subtitle: String? } ``` |

Modified [MKUserLocation.heading](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452721-heading)

|  | Declaration |
| --- | --- |
| From | ``` var heading: CLHeading! { get } ``` |
| To | ``` var heading: CLHeading? { get } ``` |

Modified [MKUserLocation.location](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452415-location)

|  | Declaration |
| --- | --- |
| From | ``` var location: CLLocation! { get } ``` |
| To | ``` var location: CLLocation? { get } ``` |

Modified [MKUserLocation.subtitle](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452562-subtitle)

|  | Declaration |
| --- | --- |
| From | ``` var subtitle: String! ``` |
| To | ``` var subtitle: String? ``` |

Modified [MKUserLocation.title](https://developer.apple.com/documentation/mapkit/mkuserlocation/1452058-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! ``` |
| To | ``` var title: String? ``` |

Modified [NSValue.init(MKCoordinate: CLLocationCoordinate2D)](https://developer.apple.com/documentation/foundation/nsvalue/1452193-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(MKCoordinate coordinate: CLLocationCoordinate2D) -> NSValue ``` |
| To | ``` init(MKCoordinate coordinate: CLLocationCoordinate2D) ``` |

Modified [NSValue.init(MKCoordinateSpan: MKCoordinateSpan)](https://developer.apple.com/documentation/foundation/nsvalue/1452333-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(MKCoordinateSpan span: MKCoordinateSpan) -> NSValue ``` |
| To | ``` init(MKCoordinateSpan span: MKCoordinateSpan) ``` |

Modified [MKDirectionsHandler](https://developer.apple.com/documentation/mapkit/mkdirections/directionshandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MKDirectionsHandler = (MKDirectionsResponse!, NSError!) -> Void ``` |
| To | ``` typealias MKDirectionsHandler = (MKDirectionsResponse?, NSError?) -> Void ``` |

Modified [MKETAHandler](https://developer.apple.com/documentation/mapkit/mkdirections/etahandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MKETAHandler = (MKETAResponse!, NSError!) -> Void ``` |
| To | ``` typealias MKETAHandler = (MKETAResponse?, NSError?) -> Void ``` |

Modified [MKLocalSearchCompletionHandler](https://developer.apple.com/documentation/mapkit/mklocalsearch/completionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MKLocalSearchCompletionHandler = (MKLocalSearchResponse!, NSError!) -> Void ``` |
| To | ``` typealias MKLocalSearchCompletionHandler = (MKLocalSearchResponse?, NSError?) -> Void ``` |

Modified [MKMapSnapshotCompletionHandler](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/completionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias MKMapSnapshotCompletionHandler = (MKMapSnapshot!, NSError!) -> Void ``` |
| To | ``` typealias MKMapSnapshotCompletionHandler = (MKMapSnapshot?, NSError?) -> Void ``` |

Modified [MKStringFromMapPoint(_: MKMapPoint) -> String](https://developer.apple.com/documentation/mapkit/1451962-mkstringfrommappoint)

|  | Declaration |
| --- | --- |
| From | ``` func MKStringFromMapPoint(_ point: MKMapPoint) -> String! ``` |
| To | ``` func MKStringFromMapPoint(_ point: MKMapPoint) -> String ``` |

Modified [MKStringFromMapRect(_: MKMapRect) -> String](https://developer.apple.com/documentation/mapkit/1451996-mkstringfrommaprect)

|  | Declaration |
| --- | --- |
| From | ``` func MKStringFromMapRect(_ rect: MKMapRect) -> String! ``` |
| To | ``` func MKStringFromMapRect(_ rect: MKMapRect) -> String ``` |

Modified [MKStringFromMapSize(_: MKMapSize) -> String](https://developer.apple.com/documentation/mapkit/1452351-mkstringfrommapsize)

|  | Declaration |
| --- | --- |
| From | ``` func MKStringFromMapSize(_ size: MKMapSize) -> String! ``` |
| To | ``` func MKStringFromMapSize(_ size: MKMapSize) -> String ``` |

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
