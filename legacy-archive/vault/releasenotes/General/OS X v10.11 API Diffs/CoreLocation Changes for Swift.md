---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreLocation.html
archived_at: '2026-07-18T02:53:27.461126Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreLocation Changes for Swift

### CoreLocation

Added [CLPlacemark.timeZone](https://developer.apple.com/documentation/corelocation/clplacemark/1423707-timezone)Modified [CLActivityType [enum]](https://developer.apple.com/documentation/corelocation/clactivitytype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CLAuthorizationStatus [enum]](https://developer.apple.com/documentation/corelocation/clauthorizationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CLCircularRegion](https://developer.apple.com/documentation/corelocation/clcircularregion)

|  | Declaration |
| --- | --- |
| From | ``` class CLCircularRegion : CLRegion {     init!(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` |
| To | ``` class CLCircularRegion : CLRegion {     init(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` |

Modified [CLCircularRegion.init(center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](https://developer.apple.com/documentation/corelocation/clcircularregion/1423761-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` |
| To | ``` init(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String) ``` |

Modified [CLDeviceOrientation [enum]](https://developer.apple.com/documentation/corelocation/cldeviceorientation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CLError [enum]](https://developer.apple.com/documentation/corelocation/clerror/code)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum CLError : Int {     case LocationUnknown     case Denied     case Network     case HeadingFailure     case RegionMonitoringDenied     case RegionMonitoringFailure     case RegionMonitoringSetupDelayed     case RegionMonitoringResponseDelayed     case GeocodeFoundNoResult     case GeocodeFoundPartialResult     case GeocodeCanceled     case DeferredFailed     case DeferredNotUpdatingLocation     case DeferredAccuracyTooLow     case DeferredDistanceFiltered     case DeferredCanceled     case RangingUnavailable     case RangingFailure } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum CLError : Int {     case LocationUnknown     case Denied     case Network     case HeadingFailure     case RegionMonitoringDenied     case RegionMonitoringFailure     case RegionMonitoringSetupDelayed     case RegionMonitoringResponseDelayed     case GeocodeFoundNoResult     case GeocodeFoundPartialResult     case GeocodeCanceled     case DeferredFailed     case DeferredNotUpdatingLocation     case DeferredAccuracyTooLow     case DeferredDistanceFiltered     case DeferredCanceled     case RangingUnavailable     case RangingFailure } extension CLError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension CLError : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder)

|  | Declaration |
| --- | --- |
| From | ``` class CLGeocoder : NSObject {     var geocoding: Bool { get }     func reverseGeocodeLocation(_ location: CLLocation!, completionHandler completionHandler: CLGeocodeCompletionHandler!)     func geocodeAddressDictionary(_ addressDictionary: [NSObject : AnyObject]!, completionHandler completionHandler: CLGeocodeCompletionHandler!)     func geocodeAddressString(_ addressString: String!, completionHandler completionHandler: CLGeocodeCompletionHandler!)     func geocodeAddressString(_ addressString: String!, inRegion region: CLRegion!, completionHandler completionHandler: CLGeocodeCompletionHandler!)     func cancelGeocode() } ``` |
| To | ``` class CLGeocoder : NSObject {     var geocoding: Bool { get }     func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CLGeocodeCompletionHandler)     func geocodeAddressDictionary(_ addressDictionary: [NSObject : AnyObject], completionHandler completionHandler: CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, inRegion region: CLRegion?, completionHandler completionHandler: CLGeocodeCompletionHandler)     func cancelGeocode() } ``` |

Modified [CLGeocoder.geocodeAddressDictionary(_: [NSObject : AnyObject], completionHandler: CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423693-geocodeaddressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressDictionary(_ addressDictionary: [NSObject : AnyObject]!, completionHandler completionHandler: CLGeocodeCompletionHandler!) ``` |
| To | ``` func geocodeAddressDictionary(_ addressDictionary: [NSObject : AnyObject], completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.geocodeAddressString(_: String, completionHandler: CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423509-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressString(_ addressString: String!, completionHandler completionHandler: CLGeocodeCompletionHandler!) ``` |
| To | ``` func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.geocodeAddressString(_: String, inRegion: CLRegion?, completionHandler: CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423591-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressString(_ addressString: String!, inRegion region: CLRegion!, completionHandler completionHandler: CLGeocodeCompletionHandler!) ``` |
| To | ``` func geocodeAddressString(_ addressString: String, inRegion region: CLRegion?, completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.reverseGeocodeLocation(_: CLLocation, completionHandler: CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423621-reversegeocodelocation)

|  | Declaration |
| --- | --- |
| From | ``` func reverseGeocodeLocation(_ location: CLLocation!, completionHandler completionHandler: CLGeocodeCompletionHandler!) ``` |
| To | ``` func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |

Modified [CLHeading](https://developer.apple.com/documentation/corelocation/clheading)

|  | Declaration |
| --- | --- |
| From | ``` class CLHeading : NSObject, NSCopying, NSSecureCoding, NSCoding {     var magneticHeading: CLLocationDirection { get }     var trueHeading: CLLocationDirection { get }     var headingAccuracy: CLLocationDirection { get }     var x: CLHeadingComponentValue { get }     var y: CLHeadingComponentValue { get }     var z: CLHeadingComponentValue { get }     @NSCopying var timestamp: NSDate! { get }     var description: String! { get } } ``` |
| To | ``` class CLHeading : NSObject, NSCopying, NSSecureCoding, NSCoding {     var magneticHeading: CLLocationDirection { get }     var trueHeading: CLLocationDirection { get }     var headingAccuracy: CLLocationDirection { get }     var x: CLHeadingComponentValue { get }     var y: CLHeadingComponentValue { get }     var z: CLHeadingComponentValue { get }     @NSCopying var timestamp: NSDate { get }     var description: String { get } } ``` |

Modified CLHeading.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified [CLHeading.timestamp](https://developer.apple.com/documentation/corelocation/clheading/1423525-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timestamp: NSDate! { get } ``` |
| To | ``` @NSCopying var timestamp: NSDate { get } ``` |

Modified [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation)

|  | Declaration |
| --- | --- |
| From | ``` class CLLocation : NSObject, NSCopying, NSSecureCoding, NSCoding {     init!(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees)     init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate!)     init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate!)     var coordinate: CLLocationCoordinate2D { get }     var altitude: CLLocationDistance { get }     var horizontalAccuracy: CLLocationAccuracy { get }     var verticalAccuracy: CLLocationAccuracy { get }     var course: CLLocationDirection { get }     var speed: CLLocationSpeed { get }     @NSCopying var timestamp: NSDate! { get }     var description: String! { get }     func getDistanceFrom(_ location: CLLocation!) -> CLLocationDistance     func distanceFromLocation(_ location: CLLocation!) -> CLLocationDistance } extension CLLocation : CKRecordValue, NSObjectProtocol { } ``` |
| To | ``` class CLLocation : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate)     var coordinate: CLLocationCoordinate2D { get }     var altitude: CLLocationDistance { get }     var horizontalAccuracy: CLLocationAccuracy { get }     var verticalAccuracy: CLLocationAccuracy { get }     var course: CLLocationDirection { get }     var speed: CLLocationSpeed { get }     @NSCopying var timestamp: NSDate { get }     var description: String { get }     func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance     func distanceFromLocation(_ location: CLLocation) -> CLLocationDistance } extension CLLocation : CKRecordValue { } ``` |

Modified CLLocation.description

|  | Declaration |
| --- | --- |
| From | ``` var description: String! { get } ``` |
| To | ``` var description: String { get } ``` |

Modified [CLLocation.distanceFromLocation(_: CLLocation) -> CLLocationDistance](https://developer.apple.com/documentation/corelocation/cllocation/1423689-distance)

|  | Declaration |
| --- | --- |
| From | ``` func distanceFromLocation(_ location: CLLocation!) -> CLLocationDistance ``` |
| To | ``` func distanceFromLocation(_ location: CLLocation) -> CLLocationDistance ``` |

Modified [CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: NSDate)](https://developer.apple.com/documentation/corelocation/cllocation/1423718-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate!) ``` |
| To | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate) ``` |

Modified [CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: NSDate)](https://developer.apple.com/documentation/corelocation/cllocation/1423666-initwithcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` init!(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate!) ``` |
| To | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate) ``` |

Modified [CLLocation.init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](https://developer.apple.com/documentation/corelocation/cllocation/1423660-initwithlatitude)

|  | Declaration |
| --- | --- |
| From | ``` init!(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) ``` |
| To | ``` init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) ``` |

Modified [CLLocation.timestamp](https://developer.apple.com/documentation/corelocation/cllocation/1423589-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timestamp: NSDate! { get } ``` |
| To | ``` @NSCopying var timestamp: NSDate { get } ``` |

Modified [CLLocationCoordinate2D [struct]](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.11 |

Modified [CLLocationCoordinate2D.latitude](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d/1423513-latitude)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.11 |

Modified [CLLocationCoordinate2D.longitude](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d/1423552-longitude)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.11 |

Modified [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager)

|  | Declaration |
| --- | --- |
| From | ``` class CLLocationManager : NSObject {     class func locationServicesEnabled() -> Bool     class func headingAvailable() -> Bool     class func significantLocationChangeMonitoringAvailable() -> Bool     class func isMonitoringAvailableForClass(_ regionClass: AnyClass!) -> Bool     class func regionMonitoringAvailable() -> Bool     class func regionMonitoringEnabled() -> Bool     class func isRangingAvailable() -> Bool     class func authorizationStatus() -> CLAuthorizationStatus     unowned(unsafe) var delegate: CLLocationManagerDelegate!     var locationServicesEnabled: Bool { get }     var purpose: String!     var activityType: CLActivityType     var distanceFilter: CLLocationDistance     var desiredAccuracy: CLLocationAccuracy     var pausesLocationUpdatesAutomatically: Bool     @NSCopying var location: CLLocation! { get }     var headingAvailable: Bool { get }     var headingFilter: CLLocationDegrees     var headingOrientation: CLDeviceOrientation     @NSCopying var heading: CLHeading! { get }     var maximumRegionMonitoringDistance: CLLocationDistance { get }     var monitoredRegions: Set<NSObject>! { get }     var rangedRegions: Set<NSObject>! { get }     func startUpdatingLocation()     func stopUpdatingLocation()     func startUpdatingHeading()     func stopUpdatingHeading()     func dismissHeadingCalibrationDisplay()     func startMonitoringSignificantLocationChanges()     func stopMonitoringSignificantLocationChanges()     func startMonitoringForRegion(_ region: CLRegion!, desiredAccuracy accuracy: CLLocationAccuracy)     func stopMonitoringForRegion(_ region: CLRegion!)     func startMonitoringForRegion(_ region: CLRegion!)     func requestStateForRegion(_ region: CLRegion!)     func allowDeferredLocationUpdatesUntilTraveled(_ distance: CLLocationDistance, timeout timeout: NSTimeInterval)     func disallowDeferredLocationUpdates()     class func deferredLocationUpdatesAvailable() -> Bool } ``` |
| To | ``` class CLLocationManager : NSObject {     class func locationServicesEnabled() -> Bool     class func headingAvailable() -> Bool     class func significantLocationChangeMonitoringAvailable() -> Bool     class func isMonitoringAvailableForClass(_ regionClass: AnyClass) -> Bool     class func regionMonitoringAvailable() -> Bool     class func regionMonitoringEnabled() -> Bool     class func isRangingAvailable() -> Bool     class func authorizationStatus() -> CLAuthorizationStatus     unowned(unsafe) var delegate: CLLocationManagerDelegate?     var locationServicesEnabled: Bool { get }     var purpose: String?     var activityType: CLActivityType     var distanceFilter: CLLocationDistance     var desiredAccuracy: CLLocationAccuracy     var pausesLocationUpdatesAutomatically: Bool     @NSCopying var location: CLLocation? { get }     var headingAvailable: Bool { get }     var headingFilter: CLLocationDegrees     var headingOrientation: CLDeviceOrientation     @NSCopying var heading: CLHeading? { get }     var maximumRegionMonitoringDistance: CLLocationDistance { get }     var monitoredRegions: Set<CLRegion> { get }     var rangedRegions: Set<CLRegion> { get }     func startUpdatingLocation()     func stopUpdatingLocation()     func startUpdatingHeading()     func stopUpdatingHeading()     func dismissHeadingCalibrationDisplay()     func startMonitoringSignificantLocationChanges()     func stopMonitoringSignificantLocationChanges()     func startMonitoringForRegion(_ region: CLRegion, desiredAccuracy accuracy: CLLocationAccuracy)     func stopMonitoringForRegion(_ region: CLRegion)     func startMonitoringForRegion(_ region: CLRegion)     func requestStateForRegion(_ region: CLRegion)     func allowDeferredLocationUpdatesUntilTraveled(_ distance: CLLocationDistance, timeout timeout: NSTimeInterval)     func disallowDeferredLocationUpdates()     class func deferredLocationUpdatesAvailable() -> Bool } ``` |

Modified [CLLocationManager.delegate](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423792-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: CLLocationManagerDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: CLLocationManagerDelegate? ``` |

Modified [CLLocationManager.isMonitoringAvailableForClass(_: AnyClass) -> Bool [class]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423654-ismonitoringavailableforclass)

|  | Declaration |
| --- | --- |
| From | ``` class func isMonitoringAvailableForClass(_ regionClass: AnyClass!) -> Bool ``` |
| To | ``` class func isMonitoringAvailableForClass(_ regionClass: AnyClass) -> Bool ``` |

Modified [CLLocationManager.location](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423687-location)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var location: CLLocation! { get } ``` |
| To | ``` @NSCopying var location: CLLocation? { get } ``` |

Modified [CLLocationManager.monitoredRegions](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423790-monitoredregions)

|  | Declaration |
| --- | --- |
| From | ``` var monitoredRegions: Set<NSObject>! { get } ``` |
| To | ``` var monitoredRegions: Set<CLRegion> { get } ``` |

Modified [CLLocationManager.purpose](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423742-purpose)

|  | Declaration |
| --- | --- |
| From | ``` var purpose: String! ``` |
| To | ``` var purpose: String? ``` |

Modified [CLLocationManager.requestStateForRegion(_: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423804-requeststate)

|  | Declaration |
| --- | --- |
| From | ``` func requestStateForRegion(_ region: CLRegion!) ``` |
| To | ``` func requestStateForRegion(_ region: CLRegion) ``` |

Modified [CLLocationManager.startMonitoringForRegion(_: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoringforregion)

|  | Declaration |
| --- | --- |
| From | ``` func startMonitoringForRegion(_ region: CLRegion!) ``` |
| To | ``` func startMonitoringForRegion(_ region: CLRegion) ``` |

Modified [CLLocationManager.stopMonitoringForRegion(_: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423840-stopmonitoring)

|  | Declaration |
| --- | --- |
| From | ``` func stopMonitoringForRegion(_ region: CLRegion!) ``` |
| To | ``` func stopMonitoringForRegion(_ region: CLRegion) ``` |

Modified [CLLocationManagerDelegate](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CLLocationManagerDelegate : NSObjectProtocol {     optional func locationManager(_ manager: CLLocationManager!, didUpdateToLocation newLocation: CLLocation!, fromLocation oldLocation: CLLocation!)     optional func locationManager(_ manager: CLLocationManager!, didUpdateLocations locations: [AnyObject]!)     optional func locationManager(_ manager: CLLocationManager!, didUpdateHeading newHeading: CLHeading!)     optional func locationManagerShouldDisplayHeadingCalibration(_ manager: CLLocationManager!) -> Bool     optional func locationManager(_ manager: CLLocationManager!, didDetermineState state: CLRegionState, forRegion region: CLRegion!)     optional func locationManager(_ manager: CLLocationManager!, didEnterRegion region: CLRegion!)     optional func locationManager(_ manager: CLLocationManager!, didExitRegion region: CLRegion!)     optional func locationManager(_ manager: CLLocationManager!, didFailWithError error: NSError!)     optional func locationManager(_ manager: CLLocationManager!, monitoringDidFailForRegion region: CLRegion!, withError error: NSError!)     optional func locationManager(_ manager: CLLocationManager!, didChangeAuthorizationStatus status: CLAuthorizationStatus)     optional func locationManager(_ manager: CLLocationManager!, didStartMonitoringForRegion region: CLRegion!)     optional func locationManagerDidPauseLocationUpdates(_ manager: CLLocationManager!)     optional func locationManagerDidResumeLocationUpdates(_ manager: CLLocationManager!)     optional func locationManager(_ manager: CLLocationManager!, didFinishDeferredUpdatesWithError error: NSError!) } ``` |
| To | ``` protocol CLLocationManagerDelegate : NSObjectProtocol {     optional func locationManager(_ manager: CLLocationManager, didUpdateToLocation newLocation: CLLocation, fromLocation oldLocation: CLLocation)     optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [AnyObject])     optional func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading)     optional func locationManagerShouldDisplayHeadingCalibration(_ manager: CLLocationManager) -> Bool     optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, forRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didFailWithError error: NSError)     optional func locationManager(_ manager: CLLocationManager, monitoringDidFailForRegion region: CLRegion?, withError error: NSError)     optional func locationManager(_ manager: CLLocationManager, didChangeAuthorizationStatus status: CLAuthorizationStatus)     optional func locationManager(_ manager: CLLocationManager, didStartMonitoringForRegion region: CLRegion)     optional func locationManagerDidPauseLocationUpdates(_ manager: CLLocationManager)     optional func locationManagerDidResumeLocationUpdates(_ manager: CLLocationManager)     optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: NSError?) } ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didChangeAuthorizationStatus: CLAuthorizationStatus)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423701-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didChangeAuthorizationStatus status: CLAuthorizationStatus) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didChangeAuthorizationStatus status: CLAuthorizationStatus) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didDetermineState: CLRegionState, forRegion: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423570-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didDetermineState state: CLRegionState, forRegion region: CLRegion!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, forRegion region: CLRegion) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didEnterRegion: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423560-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didEnterRegion region: CLRegion!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didExitRegion: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423630-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didExitRegion region: CLRegion!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didFailWithError: NSError)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423786-locationmanager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didFailWithError error: NSError!) ``` | OS X 10.10 |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didFailWithError error: NSError) ``` | OS X 10.6 |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didFinishDeferredUpdatesWithError: NSError?)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423537-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didFinishDeferredUpdatesWithError error: NSError!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: NSError?) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didStartMonitoringForRegion: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423842-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didStartMonitoringForRegion region: CLRegion!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didStartMonitoringForRegion region: CLRegion) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didUpdateLocations: [AnyObject])](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didUpdateLocations locations: [AnyObject]!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [AnyObject]) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didUpdateToLocation: CLLocation, fromLocation: CLLocation)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423716-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, didUpdateToLocation newLocation: CLLocation!, fromLocation oldLocation: CLLocation!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didUpdateToLocation newLocation: CLLocation, fromLocation oldLocation: CLLocation) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, monitoringDidFailForRegion: CLRegion?, withError: NSError)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423720-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager!, monitoringDidFailForRegion region: CLRegion!, withError error: NSError!) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, monitoringDidFailForRegion region: CLRegion?, withError error: NSError) ``` |

Modified [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark)

|  | Declaration |
| --- | --- |
| From | ``` class CLPlacemark : NSObject, NSCopying, NSSecureCoding, NSCoding {     init!(placemark placemark: CLPlacemark!)     @NSCopying var location: CLLocation! { get }     @NSCopying var region: CLRegion! { get }     var addressDictionary: [NSObject : AnyObject]! { get }     var name: String! { get }     var thoroughfare: String! { get }     var subThoroughfare: String! { get }     var locality: String! { get }     var subLocality: String! { get }     var administrativeArea: String! { get }     var subAdministrativeArea: String! { get }     var postalCode: String! { get }     var ISOcountryCode: String! { get }     var country: String! { get }     var inlandWater: String! { get }     var ocean: String! { get }     var areasOfInterest: [AnyObject]! { get } } ``` |
| To | ``` class CLPlacemark : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(placemark placemark: CLPlacemark)     @NSCopying var location: CLLocation? { get }     @NSCopying var region: CLRegion? { get }     @NSCopying var timeZone: NSTimeZone? { get }     var addressDictionary: [NSObject : AnyObject]? { get }     var name: String? { get }     var thoroughfare: String? { get }     var subThoroughfare: String? { get }     var locality: String? { get }     var subLocality: String? { get }     var administrativeArea: String? { get }     var subAdministrativeArea: String? { get }     var postalCode: String? { get }     var ISOcountryCode: String? { get }     var country: String? { get }     var inlandWater: String? { get }     var ocean: String? { get }     var areasOfInterest: [String]? { get } } ``` |

Modified [CLPlacemark.addressDictionary](https://developer.apple.com/documentation/corelocation/clplacemark/1423605-addressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` var addressDictionary: [NSObject : AnyObject]! { get } ``` |
| To | ``` var addressDictionary: [NSObject : AnyObject]? { get } ``` |

Modified [CLPlacemark.administrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423628-administrativearea)

|  | Declaration |
| --- | --- |
| From | ``` var administrativeArea: String! { get } ``` |
| To | ``` var administrativeArea: String? { get } ``` |

Modified [CLPlacemark.areasOfInterest](https://developer.apple.com/documentation/corelocation/clplacemark/1423673-areasofinterest)

|  | Declaration |
| --- | --- |
| From | ``` var areasOfInterest: [AnyObject]! { get } ``` |
| To | ``` var areasOfInterest: [String]? { get } ``` |

Modified [CLPlacemark.country](https://developer.apple.com/documentation/corelocation/clplacemark/1423800-country)

|  | Declaration |
| --- | --- |
| From | ``` var country: String! { get } ``` |
| To | ``` var country: String? { get } ``` |

Modified [CLPlacemark.init(placemark: CLPlacemark)](https://developer.apple.com/documentation/corelocation/clplacemark/1423818-initwithplacemark)

|  | Declaration |
| --- | --- |
| From | ``` init!(placemark placemark: CLPlacemark!) ``` |
| To | ``` init(placemark placemark: CLPlacemark) ``` |

Modified [CLPlacemark.inlandWater](https://developer.apple.com/documentation/corelocation/clplacemark/1423738-inlandwater)

|  | Declaration |
| --- | --- |
| From | ``` var inlandWater: String! { get } ``` |
| To | ``` var inlandWater: String? { get } ``` |

Modified [CLPlacemark.ISOcountryCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423796-isocountrycode)

|  | Declaration |
| --- | --- |
| From | ``` var ISOcountryCode: String! { get } ``` |
| To | ``` var ISOcountryCode: String? { get } ``` |

Modified [CLPlacemark.locality](https://developer.apple.com/documentation/corelocation/clplacemark/1423507-locality)

|  | Declaration |
| --- | --- |
| From | ``` var locality: String! { get } ``` |
| To | ``` var locality: String? { get } ``` |

Modified [CLPlacemark.location](https://developer.apple.com/documentation/corelocation/clplacemark/1423603-location)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var location: CLLocation! { get } ``` |
| To | ``` @NSCopying var location: CLLocation? { get } ``` |

Modified [CLPlacemark.name](https://developer.apple.com/documentation/corelocation/clplacemark/1423634-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [CLPlacemark.ocean](https://developer.apple.com/documentation/corelocation/clplacemark/1423619-ocean)

|  | Declaration |
| --- | --- |
| From | ``` var ocean: String! { get } ``` |
| To | ``` var ocean: String? { get } ``` |

Modified [CLPlacemark.postalCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423851-postalcode)

|  | Declaration |
| --- | --- |
| From | ``` var postalCode: String! { get } ``` |
| To | ``` var postalCode: String? { get } ``` |

Modified [CLPlacemark.region](https://developer.apple.com/documentation/corelocation/clplacemark/1423808-region)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var region: CLRegion! { get } ``` |
| To | ``` @NSCopying var region: CLRegion? { get } ``` |

Modified [CLPlacemark.subAdministrativeArea](https://developer.apple.com/documentation/corelocation/clplacemark/1423776-subadministrativearea)

|  | Declaration |
| --- | --- |
| From | ``` var subAdministrativeArea: String! { get } ``` |
| To | ``` var subAdministrativeArea: String? { get } ``` |

Modified [CLPlacemark.subLocality](https://developer.apple.com/documentation/corelocation/clplacemark/1423794-sublocality)

|  | Declaration |
| --- | --- |
| From | ``` var subLocality: String! { get } ``` |
| To | ``` var subLocality: String? { get } ``` |

Modified [CLPlacemark.subThoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423782-subthoroughfare)

|  | Declaration |
| --- | --- |
| From | ``` var subThoroughfare: String! { get } ``` |
| To | ``` var subThoroughfare: String? { get } ``` |

Modified [CLPlacemark.thoroughfare](https://developer.apple.com/documentation/corelocation/clplacemark/1423814-thoroughfare)

|  | Declaration |
| --- | --- |
| From | ``` var thoroughfare: String! { get } ``` |
| To | ``` var thoroughfare: String? { get } ``` |

Modified [CLRegion](https://developer.apple.com/documentation/corelocation/clregion)

|  | Declaration |
| --- | --- |
| From | ``` class CLRegion : NSObject, NSCopying, NSSecureCoding, NSCoding {     init!(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var identifier: String! { get }     var notifyOnEntry: Bool     var notifyOnExit: Bool     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` |
| To | ``` class CLRegion : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var identifier: String { get }     var notifyOnEntry: Bool     var notifyOnExit: Bool     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` |

Modified [CLRegion.identifier](https://developer.apple.com/documentation/corelocation/clregion/1423583-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified [CLRegion.init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](https://developer.apple.com/documentation/corelocation/clregion/1423681-initcircularregionwithcenter)

|  | Declaration |
| --- | --- |
| From | ``` init!(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String!) ``` |
| To | ``` init(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String) ``` |

Modified [CLRegionState [enum]](https://developer.apple.com/documentation/corelocation/clregionstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CLGeocodeCompletionHandler](https://developer.apple.com/documentation/corelocation/clgeocodecompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CLGeocodeCompletionHandler = ([AnyObject]!, NSError!) -> Void ``` |
| To | ``` typealias CLGeocodeCompletionHandler = ([CLPlacemark]?, NSError?) -> Void ``` |

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
