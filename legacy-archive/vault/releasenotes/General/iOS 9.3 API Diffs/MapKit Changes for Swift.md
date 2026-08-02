---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/MapKit.html
archived_at: '2026-07-18T02:57:16.091734Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# MapKit Changes for Swift

### MapKit

Added [MKLocalSearchCompleter](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter)Added [MKLocalSearchCompleter.cancel()](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/1452337-cancel)Added [MKLocalSearchCompleter.delegate](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/1452106-delegate)Added [MKLocalSearchCompleter.filterType](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/1452150-filtertype)Added [MKLocalSearchCompleter.queryFragment](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/1452555-queryfragment)Added [MKLocalSearchCompleter.region](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/1451923-region)Added [MKLocalSearchCompleter.results](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/1452295-results)Added [MKLocalSearchCompleter.searching](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/1452272-searching)Added [MKLocalSearchCompleterDelegate](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate)Added [MKLocalSearchCompleterDelegate.completer(_: MKLocalSearchCompleter, didFailWithError: NSError)](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate/1451885-completer)Added [MKLocalSearchCompleterDelegate.completerDidUpdateResults(_: MKLocalSearchCompleter)](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleterdelegate/1452209-completerdidupdateresults)Added [MKLocalSearchCompletion](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion)Added [MKLocalSearchCompletion.subtitle](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion/1452566-subtitle)Added [MKLocalSearchCompletion.subtitleHighlightRanges](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion/1452489-subtitlehighlightranges)Added [MKLocalSearchCompletion.title](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion/1452455-title)Added [MKLocalSearchCompletion.titleHighlightRanges](https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion/1451935-titlehighlightranges)Added [MKLocalSearchRequest.init(completion: MKLocalSearchCompletion)](https://developer.apple.com/documentation/mapkit/mklocalsearch/request/1452301-init)Added [MKSearchCompletionFilterType [enum]](https://developer.apple.com/documentation/mapkit/mksearchcompletionfiltertype)Added [MKSearchCompletionFilterType.LocationsAndQueries](https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/filtertype/locationsandqueries)Added [MKSearchCompletionFilterType.LocationsOnly](https://developer.apple.com/documentation/mapkit/mksearchcompletionfiltertype/mksearchcompletionfiltertypelocationsonly)Modified [MKLocalSearchRequest](https://developer.apple.com/documentation/mapkit/mklocalsearch/request)

|  | Declaration |
| --- | --- |
| From | ``` class MKLocalSearchRequest : NSObject, NSCopying {     var naturalLanguageQuery: String?     var region: MKCoordinateRegion } ``` |
| To | ``` class MKLocalSearchRequest : NSObject, NSCopying {     var naturalLanguageQuery: String?     var region: MKCoordinateRegion } extension MKLocalSearchRequest {     init(completion completion: MKLocalSearchCompletion) } ``` |

Modified [MKMapView](https://developer.apple.com/documentation/mapkit/mkmapview)

|  | Declaration |
| --- | --- |
| From | ``` class MKMapView : UIView, NSCoding {     weak var delegate: MKMapViewDelegate?     var mapType: MKMapType     var region: MKCoordinateRegion     func setRegion(_ region: MKCoordinateRegion, animated animated: Bool)     var centerCoordinate: CLLocationCoordinate2D     func setCenterCoordinate(_ coordinate: CLLocationCoordinate2D, animated animated: Bool)     func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion     var visibleMapRect: MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect     func _handleSelectionAtPoint(_ locationInView: CGPoint)     func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets) -> MKMapRect     @NSCopying var camera: MKMapCamera     func setCamera(_ camera: MKMapCamera, animated animated: Bool)     func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, toCoordinateFromView view: UIView?) -> CLLocationCoordinate2D     func convertRegion(_ region: MKCoordinateRegion, toRectToView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, toRegionFromView view: UIView?) -> MKCoordinateRegion     var zoomEnabled: Bool     var scrollEnabled: Bool     var rotateEnabled: Bool     var pitchEnabled: Bool     var showsCompass: Bool     var showsScale: Bool     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var showsTraffic: Bool     var showsUserLocation: Bool     var userLocation: MKUserLocation { get }     var userTrackingMode: MKUserTrackingMode     func setUserTrackingMode(_ mode: MKUserTrackingMode, animated animated: Bool)     var userLocationVisible: Bool { get }     func addAnnotation(_ annotation: MKAnnotation)     func addAnnotations(_ annotations: [MKAnnotation])     func removeAnnotation(_ annotation: MKAnnotation)     func removeAnnotations(_ annotations: [MKAnnotation])     var annotations: [MKAnnotation] { get }     func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>     func viewForAnnotation(_ annotation: MKAnnotation) -> MKAnnotationView?     func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String) -> MKAnnotationView?     func selectAnnotation(_ annotation: MKAnnotation, animated animated: Bool)     func deselectAnnotation(_ annotation: MKAnnotation?, animated animated: Bool)     var selectedAnnotations: [MKAnnotation]     var annotationVisibleRect: CGRect { get }     func showAnnotations(_ annotations: [MKAnnotation], animated animated: Bool) } extension MKMapView {     func addOverlay(_ overlay: MKOverlay, level level: MKOverlayLevel)     func addOverlays(_ overlays: [MKOverlay], level level: MKOverlayLevel)     func removeOverlay(_ overlay: MKOverlay)     func removeOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int, level level: MKOverlayLevel)     func insertOverlay(_ overlay: MKOverlay, aboveOverlay sibling: MKOverlay)     func insertOverlay(_ overlay: MKOverlay, belowOverlay sibling: MKOverlay)     func exchangeOverlay(_ overlay1: MKOverlay, withOverlay overlay2: MKOverlay)     var overlays: [MKOverlay] { get }     func overlaysInLevel(_ level: MKOverlayLevel) -> [MKOverlay]     func rendererForOverlay(_ overlay: MKOverlay) -> MKOverlayRenderer?     func viewForOverlay(_ overlay: MKOverlay) -> MKOverlayView     func addOverlay(_ overlay: MKOverlay)     func addOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int)     func exchangeOverlayAtIndex(_ index1: Int, withOverlayAtIndex index2: Int) } ``` |
| To | ``` class MKMapView : UIView, NSCoding {     weak var delegate: MKMapViewDelegate?     var mapType: MKMapType     var region: MKCoordinateRegion     func setRegion(_ region: MKCoordinateRegion, animated animated: Bool)     var centerCoordinate: CLLocationCoordinate2D     func setCenterCoordinate(_ coordinate: CLLocationCoordinate2D, animated animated: Bool)     func regionThatFits(_ region: MKCoordinateRegion) -> MKCoordinateRegion     var visibleMapRect: MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect) -> MKMapRect     func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets, animated animate: Bool)     func mapRectThatFits(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets) -> MKMapRect     @NSCopying var camera: MKMapCamera     func setCamera(_ camera: MKMapCamera, animated animated: Bool)     func convertCoordinate(_ coordinate: CLLocationCoordinate2D, toPointToView view: UIView?) -> CGPoint     func convertPoint(_ point: CGPoint, toCoordinateFromView view: UIView?) -> CLLocationCoordinate2D     func convertRegion(_ region: MKCoordinateRegion, toRectToView view: UIView?) -> CGRect     func convertRect(_ rect: CGRect, toRegionFromView view: UIView?) -> MKCoordinateRegion     var zoomEnabled: Bool     var scrollEnabled: Bool     var rotateEnabled: Bool     var pitchEnabled: Bool     var showsCompass: Bool     var showsScale: Bool     var showsPointsOfInterest: Bool     var showsBuildings: Bool     var showsTraffic: Bool     var showsUserLocation: Bool     var userLocation: MKUserLocation { get }     var userTrackingMode: MKUserTrackingMode     func setUserTrackingMode(_ mode: MKUserTrackingMode, animated animated: Bool)     var userLocationVisible: Bool { get }     func addAnnotation(_ annotation: MKAnnotation)     func addAnnotations(_ annotations: [MKAnnotation])     func removeAnnotation(_ annotation: MKAnnotation)     func removeAnnotations(_ annotations: [MKAnnotation])     var annotations: [MKAnnotation] { get }     func annotationsInMapRect(_ mapRect: MKMapRect) -> Set<NSObject>     func viewForAnnotation(_ annotation: MKAnnotation) -> MKAnnotationView?     func dequeueReusableAnnotationViewWithIdentifier(_ identifier: String) -> MKAnnotationView?     func selectAnnotation(_ annotation: MKAnnotation, animated animated: Bool)     func deselectAnnotation(_ annotation: MKAnnotation?, animated animated: Bool)     var selectedAnnotations: [MKAnnotation]     var annotationVisibleRect: CGRect { get }     func showAnnotations(_ annotations: [MKAnnotation], animated animated: Bool) } extension MKMapView {     func addOverlay(_ overlay: MKOverlay, level level: MKOverlayLevel)     func addOverlays(_ overlays: [MKOverlay], level level: MKOverlayLevel)     func removeOverlay(_ overlay: MKOverlay)     func removeOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int, level level: MKOverlayLevel)     func insertOverlay(_ overlay: MKOverlay, aboveOverlay sibling: MKOverlay)     func insertOverlay(_ overlay: MKOverlay, belowOverlay sibling: MKOverlay)     func exchangeOverlay(_ overlay1: MKOverlay, withOverlay overlay2: MKOverlay)     var overlays: [MKOverlay] { get }     func overlaysInLevel(_ level: MKOverlayLevel) -> [MKOverlay]     func rendererForOverlay(_ overlay: MKOverlay) -> MKOverlayRenderer?     func viewForOverlay(_ overlay: MKOverlay) -> MKOverlayView     func addOverlay(_ overlay: MKOverlay)     func addOverlays(_ overlays: [MKOverlay])     func insertOverlay(_ overlay: MKOverlay, atIndex index: Int)     func exchangeOverlayAtIndex(_ index1: Int, withOverlayAtIndex index2: Int) } ``` |

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
