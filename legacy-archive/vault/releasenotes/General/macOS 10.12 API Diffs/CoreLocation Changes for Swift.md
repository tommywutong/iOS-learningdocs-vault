---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/CoreLocation.html
archived_at: '2026-07-18T02:51:09.564141Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# CoreLocation Changes for Swift

### CoreLocation

Removed CLHeading.descriptionRemoved CLLocation.descriptionAdded [CLAuthorizationStatus.authorizedAlways](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusauthorizedalways)Added [CLError [struct]](https://developer.apple.com/documentation/corelocation/clerror)Added [CLError.deferredAccuracyTooLow](https://developer.apple.com/documentation/corelocation/clerror/2320662-deferredaccuracytoolow)Added [CLError.deferredCanceled](https://developer.apple.com/documentation/corelocation/clerror/2320675-deferredcanceled)Added [CLError.deferredDistanceFiltered](https://developer.apple.com/documentation/corelocation/clerror/2320668-deferreddistancefiltered)Added [CLError.deferredFailed](https://developer.apple.com/documentation/corelocation/clerror/2320665-deferredfailed)Added [CLError.deferredNotUpdatingLocation](https://developer.apple.com/documentation/corelocation/clerror/2320663-deferrednotupdatinglocation)Added [CLError.denied](https://developer.apple.com/documentation/corelocation/clerror/2320672-denied)Added [CLError.geocodeCanceled](https://developer.apple.com/documentation/corelocation/clerror/2320667-geocodecanceled)Added [CLError.geocodeFoundNoResult](https://developer.apple.com/documentation/corelocation/clerror/2320666-geocodefoundnoresult)Added [CLError.geocodeFoundPartialResult](https://developer.apple.com/documentation/corelocation/clerror/2320664-geocodefoundpartialresult)Added [CLError.headingFailure](https://developer.apple.com/documentation/corelocation/clerror/2320676-headingfailure)Added CLError.init(_nsError: NSError)Added [CLError.locationUnknown](https://developer.apple.com/documentation/corelocation/clerror/2320673-locationunknown)Added [CLError.network](https://developer.apple.com/documentation/corelocation/clerror/2320660-network)Added [CLError.rangingFailure](https://developer.apple.com/documentation/corelocation/clerror/2320669-rangingfailure)Added [CLError.rangingUnavailable](https://developer.apple.com/documentation/corelocation/clerror/2320671-rangingunavailable)Added [CLError.regionMonitoringDenied](https://developer.apple.com/documentation/corelocation/clerror/2320670-regionmonitoringdenied)Added [CLError.regionMonitoringFailure](https://developer.apple.com/documentation/corelocation/clerror/2320674-regionmonitoringfailure)Added [CLError.regionMonitoringResponseDelayed](https://developer.apple.com/documentation/corelocation/clerror/2320677-regionmonitoringresponsedelayed)Added [CLError.regionMonitoringSetupDelayed](https://developer.apple.com/documentation/corelocation/clerror/2320661-regionmonitoringsetupdelayed)Modified [CLActivityType [enum]](https://developer.apple.com/documentation/corelocation/clactivitytype)

|  | Declaration |
| --- | --- |
| From | ``` enum CLActivityType : Int {     case Other     case AutomotiveNavigation     case Fitness     case OtherNavigation } ``` |
| To | ``` enum CLActivityType : Int {     case other     case automotiveNavigation     case fitness     case otherNavigation } ``` |

Modified [CLActivityType.automotiveNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/automotivenavigation)

|  | Declaration |
| --- | --- |
| From | ``` case AutomotiveNavigation ``` |
| To | ``` case automotiveNavigation ``` |

Modified [CLActivityType.fitness](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypefitness)

|  | Declaration |
| --- | --- |
| From | ``` case Fitness ``` |
| To | ``` case fitness ``` |

Modified [CLActivityType.other](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypeother)

|  | Declaration |
| --- | --- |
| From | ``` case Other ``` |
| To | ``` case other ``` |

Modified [CLActivityType.otherNavigation](https://developer.apple.com/documentation/corelocation/clactivitytype/clactivitytypeothernavigation)

|  | Declaration |
| --- | --- |
| From | ``` case OtherNavigation ``` |
| To | ``` case otherNavigation ``` |

Modified [CLAuthorizationStatus [enum]](https://developer.apple.com/documentation/corelocation/clauthorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum CLAuthorizationStatus : Int32 {     case NotDetermined     case Restricted     case Denied     case Authorized } ``` |
| To | ``` enum CLAuthorizationStatus : Int32 {     case notDetermined     case restricted     case denied     case authorizedAlways     case authorizedWhenInUse     static var authorized: CLAuthorizationStatus { get } } ``` |

Modified [CLAuthorizationStatus.authorized](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusauthorized)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | Authorized | ``` case Authorized ``` | OS X 10.10 |
| To | authorized | ``` static var authorized: CLAuthorizationStatus { get } ``` | OS X 10.6 |

Modified [CLAuthorizationStatus.denied](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/denied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [CLAuthorizationStatus.notDetermined](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/notdetermined)

|  | Declaration |
| --- | --- |
| From | ``` case NotDetermined ``` |
| To | ``` case notDetermined ``` |

Modified [CLAuthorizationStatus.restricted](https://developer.apple.com/documentation/corelocation/clauthorizationstatus/kclauthorizationstatusrestricted)

|  | Declaration |
| --- | --- |
| From | ``` case Restricted ``` |
| To | ``` case restricted ``` |

Modified [CLCircularRegion](https://developer.apple.com/documentation/corelocation/clcircularregion)

|  | Declaration |
| --- | --- |
| From | ``` class CLCircularRegion : CLRegion {     init(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` |
| To | ``` class CLCircularRegion : CLRegion {     init(center center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     func contains(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` |

Modified [CLCircularRegion.contains(_: CLLocationCoordinate2D) -> Bool](https://developer.apple.com/documentation/corelocation/clcircularregion/1423697-contains)

|  | Declaration |
| --- | --- |
| From | ``` func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool ``` |
| To | ``` func contains(_ coordinate: CLLocationCoordinate2D) -> Bool ``` |

Modified [CLDeviceOrientation [enum]](https://developer.apple.com/documentation/corelocation/cldeviceorientation)

|  | Declaration |
| --- | --- |
| From | ``` enum CLDeviceOrientation : Int32 {     case Unknown     case Portrait     case PortraitUpsideDown     case LandscapeLeft     case LandscapeRight     case FaceUp     case FaceDown } ``` |
| To | ``` enum CLDeviceOrientation : Int32 {     case unknown     case portrait     case portraitUpsideDown     case landscapeLeft     case landscapeRight     case faceUp     case faceDown } ``` |

Modified [CLDeviceOrientation.faceDown](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationfacedown)

|  | Declaration |
| --- | --- |
| From | ``` case FaceDown ``` |
| To | ``` case faceDown ``` |

Modified [CLDeviceOrientation.faceUp](https://developer.apple.com/documentation/corelocation/cldeviceorientation/faceup)

|  | Declaration |
| --- | --- |
| From | ``` case FaceUp ``` |
| To | ``` case faceUp ``` |

Modified [CLDeviceOrientation.landscapeLeft](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationlandscapeleft)

|  | Declaration |
| --- | --- |
| From | ``` case LandscapeLeft ``` |
| To | ``` case landscapeLeft ``` |

Modified [CLDeviceOrientation.landscapeRight](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationlandscaperight)

|  | Declaration |
| --- | --- |
| From | ``` case LandscapeRight ``` |
| To | ``` case landscapeRight ``` |

Modified [CLDeviceOrientation.portrait](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationportrait)

|  | Declaration |
| --- | --- |
| From | ``` case Portrait ``` |
| To | ``` case portrait ``` |

Modified [CLDeviceOrientation.portraitUpsideDown](https://developer.apple.com/documentation/corelocation/cldeviceorientation/portraitupsidedown)

|  | Declaration |
| --- | --- |
| From | ``` case PortraitUpsideDown ``` |
| To | ``` case portraitUpsideDown ``` |

Modified [CLDeviceOrientation.unknown](https://developer.apple.com/documentation/corelocation/cldeviceorientation/cldeviceorientationunknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CLError.Code [enum]](https://developer.apple.com/documentation/corelocation/clerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum CLError : Int {     case LocationUnknown     case Denied     case Network     case HeadingFailure     case RegionMonitoringDenied     case RegionMonitoringFailure     case RegionMonitoringSetupDelayed     case RegionMonitoringResponseDelayed     case GeocodeFoundNoResult     case GeocodeFoundPartialResult     case GeocodeCanceled     case DeferredFailed     case DeferredNotUpdatingLocation     case DeferredAccuracyTooLow     case DeferredDistanceFiltered     case DeferredCanceled     case RangingUnavailable     case RangingFailure } extension CLError : _BridgedNSError { } extension CLError : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = CLError         case locationUnknown         case denied         case network         case headingFailure         case regionMonitoringDenied         case regionMonitoringFailure         case regionMonitoringSetupDelayed         case regionMonitoringResponseDelayed         case geocodeFoundNoResult         case geocodeFoundPartialResult         case geocodeCanceled         case deferredFailed         case deferredNotUpdatingLocation         case deferredAccuracyTooLow         case deferredDistanceFiltered         case deferredCanceled         case rangingUnavailable         case rangingFailure     } ``` |

Modified [CLError.Code.deferredAccuracyTooLow](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferredaccuracytoolow)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case DeferredAccuracyTooLow ``` | OS X 10.10 |
| To | ``` case deferredAccuracyTooLow ``` | OS X 10.12 |

Modified [CLError.Code.deferredCanceled](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferredcanceled)

|  | Declaration |
| --- | --- |
| From | ``` case DeferredCanceled ``` |
| To | ``` case deferredCanceled ``` |

Modified [CLError.Code.deferredDistanceFiltered](https://developer.apple.com/documentation/corelocation/clerror/code/deferreddistancefiltered)

|  | Declaration |
| --- | --- |
| From | ``` case DeferredDistanceFiltered ``` |
| To | ``` case deferredDistanceFiltered ``` |

Modified [CLError.Code.deferredFailed](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferredfailed)

|  | Declaration |
| --- | --- |
| From | ``` case DeferredFailed ``` |
| To | ``` case deferredFailed ``` |

Modified [CLError.Code.deferredNotUpdatingLocation](https://developer.apple.com/documentation/corelocation/clerror/kclerrordeferrednotupdatinglocation)

|  | Declaration |
| --- | --- |
| From | ``` case DeferredNotUpdatingLocation ``` |
| To | ``` case deferredNotUpdatingLocation ``` |

Modified [CLError.Code.denied](https://developer.apple.com/documentation/corelocation/clerror/code/denied)

|  | Declaration |
| --- | --- |
| From | ``` case Denied ``` |
| To | ``` case denied ``` |

Modified [CLError.Code.geocodeCanceled](https://developer.apple.com/documentation/corelocation/clerror/code/geocodecanceled)

|  | Declaration |
| --- | --- |
| From | ``` case GeocodeCanceled ``` |
| To | ``` case geocodeCanceled ``` |

Modified [CLError.Code.geocodeFoundNoResult](https://developer.apple.com/documentation/corelocation/clerror/kclerrorgeocodefoundnoresult)

|  | Declaration |
| --- | --- |
| From | ``` case GeocodeFoundNoResult ``` |
| To | ``` case geocodeFoundNoResult ``` |

Modified [CLError.Code.geocodeFoundPartialResult](https://developer.apple.com/documentation/corelocation/clerror/kclerrorgeocodefoundpartialresult)

|  | Declaration |
| --- | --- |
| From | ``` case GeocodeFoundPartialResult ``` |
| To | ``` case geocodeFoundPartialResult ``` |

Modified [CLError.Code.headingFailure](https://developer.apple.com/documentation/corelocation/clerror/code/headingfailure)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case HeadingFailure ``` | OS X 10.10 |
| To | ``` case headingFailure ``` | OS X 10.12 |

Modified [CLError.Code.locationUnknown](https://developer.apple.com/documentation/corelocation/clerror/kclerrorlocationunknown)

|  | Declaration |
| --- | --- |
| From | ``` case LocationUnknown ``` |
| To | ``` case locationUnknown ``` |

Modified [CLError.Code.network](https://developer.apple.com/documentation/corelocation/clerror/code/network)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Network ``` | OS X 10.10 |
| To | ``` case network ``` | OS X 10.12 |

Modified [CLError.Code.rangingFailure](https://developer.apple.com/documentation/corelocation/clerror/code/rangingfailure)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case RangingFailure ``` | OS X 10.10 |
| To | ``` case rangingFailure ``` | OS X 10.12 |

Modified [CLError.Code.rangingUnavailable](https://developer.apple.com/documentation/corelocation/clerror/code/rangingunavailable)

|  | Declaration |
| --- | --- |
| From | ``` case RangingUnavailable ``` |
| To | ``` case rangingUnavailable ``` |

Modified [CLError.Code.regionMonitoringDenied](https://developer.apple.com/documentation/corelocation/clerror/kclerrorregionmonitoringdenied)

|  | Declaration |
| --- | --- |
| From | ``` case RegionMonitoringDenied ``` |
| To | ``` case regionMonitoringDenied ``` |

Modified [CLError.Code.regionMonitoringFailure](https://developer.apple.com/documentation/corelocation/clerror/kclerrorregionmonitoringfailure)

|  | Declaration |
| --- | --- |
| From | ``` case RegionMonitoringFailure ``` |
| To | ``` case regionMonitoringFailure ``` |

Modified [CLError.Code.regionMonitoringResponseDelayed](https://developer.apple.com/documentation/corelocation/clerror/code/regionmonitoringresponsedelayed)

|  | Declaration |
| --- | --- |
| From | ``` case RegionMonitoringResponseDelayed ``` |
| To | ``` case regionMonitoringResponseDelayed ``` |

Modified [CLError.Code.regionMonitoringSetupDelayed](https://developer.apple.com/documentation/corelocation/clerror/code/regionmonitoringsetupdelayed)

|  | Declaration |
| --- | --- |
| From | ``` case RegionMonitoringSetupDelayed ``` |
| To | ``` case regionMonitoringSetupDelayed ``` |

Modified [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLGeocoder : NSObject {     var geocoding: Bool { get }     func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CLGeocodeCompletionHandler)     func geocodeAddressDictionary(_ addressDictionary: [NSObject : AnyObject], completionHandler completionHandler: CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, inRegion region: CLRegion?, completionHandler completionHandler: CLGeocodeCompletionHandler)     func cancelGeocode() } ``` | -- |
| To | ``` class CLGeocoder : NSObject {     var isGeocoding: Bool { get }     func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any], completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, in region: CLRegion?, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func cancelGeocode()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLGeocoder : CVarArg { } extension CLGeocoder : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [CLGeocoder.geocodeAddressDictionary(_: [AnyHashable : Any], completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423693-geocodeaddressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressDictionary(_ addressDictionary: [NSObject : AnyObject], completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |
| To | ``` func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any], completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.geocodeAddressString(_: String, completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423509-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |
| To | ``` func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.geocodeAddressString(_: String, in: CLRegion?, completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423591-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressString(_ addressString: String, inRegion region: CLRegion?, completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |
| To | ``` func geocodeAddressString(_ addressString: String, in region: CLRegion?, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.isGeocoding](https://developer.apple.com/documentation/corelocation/clgeocoder/1423765-geocoding)

|  | Declaration |
| --- | --- |
| From | ``` var geocoding: Bool { get } ``` |
| To | ``` var isGeocoding: Bool { get } ``` |

Modified [CLGeocoder.reverseGeocodeLocation(_: CLLocation, completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423621-reversegeocodelocation)

|  | Declaration |
| --- | --- |
| From | ``` func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CLGeocodeCompletionHandler) ``` |
| To | ``` func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLHeading](https://developer.apple.com/documentation/corelocation/clheading)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLHeading : NSObject, NSCopying, NSSecureCoding {     var magneticHeading: CLLocationDirection { get }     var trueHeading: CLLocationDirection { get }     var headingAccuracy: CLLocationDirection { get }     var x: CLHeadingComponentValue { get }     var y: CLHeadingComponentValue { get }     var z: CLHeadingComponentValue { get }     @NSCopying var timestamp: NSDate { get }     var description: String { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CLHeading : NSObject, NSCopying, NSSecureCoding {     var magneticHeading: CLLocationDirection { get }     var trueHeading: CLLocationDirection { get }     var headingAccuracy: CLLocationDirection { get }     var x: CLHeadingComponentValue { get }     var y: CLHeadingComponentValue { get }     var z: CLHeadingComponentValue { get }     var timestamp: Date { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLHeading : CVarArg { } extension CLHeading : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CLHeading.timestamp](https://developer.apple.com/documentation/corelocation/clheading/1423525-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timestamp: NSDate { get } ``` |
| To | ``` var timestamp: Date { get } ``` |

Modified [CLLocation](https://developer.apple.com/documentation/corelocation/cllocation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLLocation : NSObject, NSCopying, NSSecureCoding {     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate)     var coordinate: CLLocationCoordinate2D { get }     var altitude: CLLocationDistance { get }     var horizontalAccuracy: CLLocationAccuracy { get }     var verticalAccuracy: CLLocationAccuracy { get }     var course: CLLocationDirection { get }     var speed: CLLocationSpeed { get }     @NSCopying var timestamp: NSDate { get }     var description: String { get }     func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance     func distanceFromLocation(_ location: CLLocation) -> CLLocationDistance } extension CLLocation : CKRecordValue { } ``` | CKRecordValue, NSCopying, NSSecureCoding |
| To | ``` class CLLocation : NSObject, NSCopying, NSSecureCoding {     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: Date)     init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: Date)     var coordinate: CLLocationCoordinate2D { get }     var altitude: CLLocationDistance { get }     var horizontalAccuracy: CLLocationAccuracy { get }     var verticalAccuracy: CLLocationAccuracy { get }     var course: CLLocationDirection { get }     var speed: CLLocationSpeed { get }     var timestamp: Date { get }     @NSCopying var floor: CLFloor? { get }     func getDistanceFrom(_ location: CLLocation) -> CLLocationDistance     func distance(from location: CLLocation) -> CLLocationDistance     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLLocation : CKRecordValue { } extension CLLocation : CVarArg { } extension CLLocation : Equatable, Hashable {     var hashValue: Int { get } } ``` | CKRecordValue, CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CLLocation.distance(from: CLLocation) -> CLLocationDistance](https://developer.apple.com/documentation/corelocation/cllocation/1423689-distance)

|  | Declaration |
| --- | --- |
| From | ``` func distanceFromLocation(_ location: CLLocation) -> CLLocationDistance ``` |
| To | ``` func distance(from location: CLLocation) -> CLLocationDistance ``` |

Modified [CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, course: CLLocationDirection, speed: CLLocationSpeed, timestamp: Date)](https://developer.apple.com/documentation/corelocation/cllocation/1423718-init)

|  | Declaration |
| --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: NSDate) ``` |
| To | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, course course: CLLocationDirection, speed speed: CLLocationSpeed, timestamp timestamp: Date) ``` |

Modified [CLLocation.init(coordinate: CLLocationCoordinate2D, altitude: CLLocationDistance, horizontalAccuracy: CLLocationAccuracy, verticalAccuracy: CLLocationAccuracy, timestamp: Date)](https://developer.apple.com/documentation/corelocation/cllocation/1423666-initwithcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: NSDate) ``` |
| To | ``` init(coordinate coordinate: CLLocationCoordinate2D, altitude altitude: CLLocationDistance, horizontalAccuracy hAccuracy: CLLocationAccuracy, verticalAccuracy vAccuracy: CLLocationAccuracy, timestamp timestamp: Date) ``` |

Modified [CLLocation.timestamp](https://developer.apple.com/documentation/corelocation/cllocation/1423589-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timestamp: NSDate { get } ``` |
| To | ``` var timestamp: Date { get } ``` |

Modified [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLLocationManager : NSObject {     class func locationServicesEnabled() -> Bool     class func headingAvailable() -> Bool     class func significantLocationChangeMonitoringAvailable() -> Bool     class func isMonitoringAvailableForClass(_ regionClass: AnyClass) -> Bool     class func regionMonitoringAvailable() -> Bool     class func regionMonitoringEnabled() -> Bool     class func isRangingAvailable() -> Bool     class func authorizationStatus() -> CLAuthorizationStatus     unowned(unsafe) var delegate: CLLocationManagerDelegate?     var locationServicesEnabled: Bool { get }     var purpose: String?     var activityType: CLActivityType     var distanceFilter: CLLocationDistance     var desiredAccuracy: CLLocationAccuracy     var pausesLocationUpdatesAutomatically: Bool     @NSCopying var location: CLLocation? { get }     var headingAvailable: Bool { get }     var headingFilter: CLLocationDegrees     var headingOrientation: CLDeviceOrientation     @NSCopying var heading: CLHeading? { get }     var maximumRegionMonitoringDistance: CLLocationDistance { get }     var monitoredRegions: Set<CLRegion> { get }     var rangedRegions: Set<CLRegion> { get }     func startUpdatingLocation()     func stopUpdatingLocation()     func startUpdatingHeading()     func stopUpdatingHeading()     func dismissHeadingCalibrationDisplay()     func startMonitoringSignificantLocationChanges()     func stopMonitoringSignificantLocationChanges()     func startMonitoringForRegion(_ region: CLRegion, desiredAccuracy accuracy: CLLocationAccuracy)     func stopMonitoringForRegion(_ region: CLRegion)     func startMonitoringForRegion(_ region: CLRegion)     func requestStateForRegion(_ region: CLRegion)     func allowDeferredLocationUpdatesUntilTraveled(_ distance: CLLocationDistance, timeout timeout: NSTimeInterval)     func disallowDeferredLocationUpdates()     class func deferredLocationUpdatesAvailable() -> Bool } ``` | -- |
| To | ``` class CLLocationManager : NSObject {     class func locationServicesEnabled() -> Bool     class func headingAvailable() -> Bool     class func significantLocationChangeMonitoringAvailable() -> Bool     class func isMonitoringAvailable(for regionClass: Swift.AnyClass) -> Bool     class func regionMonitoringAvailable() -> Bool     class func regionMonitoringEnabled() -> Bool     class func isRangingAvailable() -> Bool     class func authorizationStatus() -> CLAuthorizationStatus     unowned(unsafe) var delegate: CLLocationManagerDelegate?     var locationServicesEnabled: Bool { get }     var purpose: String?     var activityType: CLActivityType     var distanceFilter: CLLocationDistance     var desiredAccuracy: CLLocationAccuracy     var pausesLocationUpdatesAutomatically: Bool     var allowsBackgroundLocationUpdates: Bool     @NSCopying var location: CLLocation? { get }     var headingAvailable: Bool { get }     var headingFilter: CLLocationDegrees     var headingOrientation: CLDeviceOrientation     @NSCopying var heading: CLHeading? { get }     var maximumRegionMonitoringDistance: CLLocationDistance { get }     var monitoredRegions: Set<CLRegion> { get }     var rangedRegions: Set<CLRegion> { get }     func requestWhenInUseAuthorization()     func requestAlwaysAuthorization()     func startUpdatingLocation()     func stopUpdatingLocation()     func requestLocation()     func startUpdatingHeading()     func stopUpdatingHeading()     func dismissHeadingCalibrationDisplay()     func startMonitoringSignificantLocationChanges()     func stopMonitoringSignificantLocationChanges()     func startMonitoring(for region: CLRegion, desiredAccuracy accuracy: CLLocationAccuracy)     func stopMonitoring(for region: CLRegion)     func startMonitoring(for region: CLRegion)     func requestState(for region: CLRegion)     func startRangingBeacons(in region: CLBeaconRegion)     func stopRangingBeacons(in region: CLBeaconRegion)     func allowDeferredLocationUpdates(untilTraveled distance: CLLocationDistance, timeout timeout: TimeInterval)     func disallowDeferredLocationUpdates()     class func deferredLocationUpdatesAvailable() -> Bool     func startMonitoringVisits()     func stopMonitoringVisits()     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLLocationManager : CVarArg { } extension CLLocationManager : Equatable, Hashable {     var hashValue: Int { get } } extension CLLocationManager {     func startMonitoringVisits()     func stopMonitoringVisits() } ``` | CVarArg, Equatable, Hashable |

Modified [CLLocationManager.isMonitoringAvailable(for: Swift.AnyClass) -> Bool [class]](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423654-ismonitoringavailableforclass)

|  | Declaration |
| --- | --- |
| From | ``` class func isMonitoringAvailableForClass(_ regionClass: AnyClass) -> Bool ``` |
| To | ``` class func isMonitoringAvailable(for regionClass: Swift.AnyClass) -> Bool ``` |

Modified [CLLocationManager.requestState(for: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423804-requeststate)

|  | Declaration |
| --- | --- |
| From | ``` func requestStateForRegion(_ region: CLRegion) ``` |
| To | ``` func requestState(for region: CLRegion) ``` |

Modified [CLLocationManager.startMonitoring(for: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423656-startmonitoringforregion)

|  | Declaration |
| --- | --- |
| From | ``` func startMonitoringForRegion(_ region: CLRegion) ``` |
| To | ``` func startMonitoring(for region: CLRegion) ``` |

Modified [CLLocationManager.stopMonitoring(for: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanager/1423840-stopmonitoring)

|  | Declaration |
| --- | --- |
| From | ``` func stopMonitoringForRegion(_ region: CLRegion) ``` |
| To | ``` func stopMonitoring(for region: CLRegion) ``` |

Modified [CLLocationManagerDelegate](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol CLLocationManagerDelegate : NSObjectProtocol {     optional func locationManager(_ manager: CLLocationManager, didUpdateToLocation newLocation: CLLocation, fromLocation oldLocation: CLLocation)     optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [AnyObject])     optional func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading)     optional func locationManagerShouldDisplayHeadingCalibration(_ manager: CLLocationManager) -> Bool     optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, forRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didFailWithError error: NSError)     optional func locationManager(_ manager: CLLocationManager, monitoringDidFailForRegion region: CLRegion?, withError error: NSError)     optional func locationManager(_ manager: CLLocationManager, didChangeAuthorizationStatus status: CLAuthorizationStatus)     optional func locationManager(_ manager: CLLocationManager, didStartMonitoringForRegion region: CLRegion)     optional func locationManagerDidPauseLocationUpdates(_ manager: CLLocationManager)     optional func locationManagerDidResumeLocationUpdates(_ manager: CLLocationManager)     optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: NSError?) } ``` |
| To | ``` protocol CLLocationManagerDelegate : NSObjectProtocol {     optional func locationManager(_ manager: CLLocationManager, didUpdateTo newLocation: CLLocation, from oldLocation: CLLocation)     optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation])     optional func locationManager(_ manager: CLLocationManager, didUpdateHeading newHeading: CLHeading)     optional func locationManagerShouldDisplayHeadingCalibration(_ manager: CLLocationManager) -> Bool     optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, for region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didRangeBeacons beacons: [CLBeacon], in region: CLBeaconRegion)     optional func locationManager(_ manager: CLLocationManager, rangingBeaconsDidFailFor region: CLBeaconRegion, withError error: Error)     optional func locationManager(_ manager: CLLocationManager, didEnterRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didExitRegion region: CLRegion)     optional func locationManager(_ manager: CLLocationManager, didFailWithError error: Error)     optional func locationManager(_ manager: CLLocationManager, monitoringDidFailFor region: CLRegion?, withError error: Error)     optional func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus)     optional func locationManager(_ manager: CLLocationManager, didStartMonitoringFor region: CLRegion)     optional func locationManagerDidPauseLocationUpdates(_ manager: CLLocationManager)     optional func locationManagerDidResumeLocationUpdates(_ manager: CLLocationManager)     optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: Error?)     optional func locationManager(_ manager: CLLocationManager, didVisit visit: CLVisit) } ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didChangeAuthorization: CLAuthorizationStatus)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423701-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, didChangeAuthorizationStatus status: CLAuthorizationStatus) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didChangeAuthorization status: CLAuthorizationStatus) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didDetermineState: CLRegionState, for: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423570-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, forRegion region: CLRegion) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didDetermineState state: CLRegionState, for region: CLRegion) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didFailWithError: Error)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423786-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, didFailWithError error: NSError) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didFinishDeferredUpdatesWithError: Error?)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423537-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: NSError?) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didFinishDeferredUpdatesWithError error: Error?) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didStartMonitoringFor: CLRegion)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423842-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, didStartMonitoringForRegion region: CLRegion) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didStartMonitoringFor region: CLRegion) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didUpdateLocations: [CLLocation])](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423615-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [AnyObject]) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, didUpdateTo: CLLocation, from: CLLocation)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423716-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, didUpdateToLocation newLocation: CLLocation, fromLocation oldLocation: CLLocation) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, didUpdateTo newLocation: CLLocation, from oldLocation: CLLocation) ``` |

Modified [CLLocationManagerDelegate.locationManager(_: CLLocationManager, monitoringDidFailFor: CLRegion?, withError: Error)](https://developer.apple.com/documentation/corelocation/cllocationmanagerdelegate/1423720-locationmanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func locationManager(_ manager: CLLocationManager, monitoringDidFailForRegion region: CLRegion?, withError error: NSError) ``` |
| To | ``` optional func locationManager(_ manager: CLLocationManager, monitoringDidFailFor region: CLRegion?, withError error: Error) ``` |

Modified [CLPlacemark](https://developer.apple.com/documentation/corelocation/clplacemark)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLPlacemark : NSObject, NSCopying, NSSecureCoding {     init(placemark placemark: CLPlacemark)     @NSCopying var location: CLLocation? { get }     @NSCopying var region: CLRegion? { get }     @NSCopying var timeZone: NSTimeZone? { get }     var addressDictionary: [NSObject : AnyObject]? { get }     var name: String? { get }     var thoroughfare: String? { get }     var subThoroughfare: String? { get }     var locality: String? { get }     var subLocality: String? { get }     var administrativeArea: String? { get }     var subAdministrativeArea: String? { get }     var postalCode: String? { get }     var ISOcountryCode: String? { get }     var country: String? { get }     var inlandWater: String? { get }     var ocean: String? { get }     var areasOfInterest: [String]? { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class CLPlacemark : NSObject, NSCopying, NSSecureCoding {     init(placemark placemark: CLPlacemark)     @NSCopying var location: CLLocation? { get }     @NSCopying var region: CLRegion? { get }     var timeZone: TimeZone? { get }     var addressDictionary: [AnyHashable : Any]? { get }     var name: String? { get }     var thoroughfare: String? { get }     var subThoroughfare: String? { get }     var locality: String? { get }     var subLocality: String? { get }     var administrativeArea: String? { get }     var subAdministrativeArea: String? { get }     var postalCode: String? { get }     var isoCountryCode: String? { get }     var country: String? { get }     var inlandWater: String? { get }     var ocean: String? { get }     var areasOfInterest: [String]? { get }     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLPlacemark : CVarArg { } extension CLPlacemark : Equatable, Hashable {     var hashValue: Int { get } } extension CLPlacemark {     convenience init(location location: CLLocation, name name: String?, postalAddress postalAddress: CNPostalAddress?)     class func withLocation(_ location: CLLocation, name name: String?, postalAddress postalAddress: CNPostalAddress?) -> Self } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CLPlacemark.addressDictionary](https://developer.apple.com/documentation/corelocation/clplacemark/1423605-addressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` var addressDictionary: [NSObject : AnyObject]? { get } ``` |
| To | ``` var addressDictionary: [AnyHashable : Any]? { get } ``` |

Modified [CLPlacemark.isoCountryCode](https://developer.apple.com/documentation/corelocation/clplacemark/1423796-isocountrycode)

|  | Declaration |
| --- | --- |
| From | ``` var ISOcountryCode: String? { get } ``` |
| To | ``` var isoCountryCode: String? { get } ``` |

Modified [CLPlacemark.timeZone](https://developer.apple.com/documentation/corelocation/clplacemark/1423707-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone? { get } ``` |
| To | ``` var timeZone: TimeZone? { get } ``` |

Modified [CLRegion](https://developer.apple.com/documentation/corelocation/clregion)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CLRegion : NSObject, NSCopying, NSSecureCoding {     init(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var identifier: String { get }     var notifyOnEntry: Bool     var notifyOnExit: Bool     func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool } ``` | NSCopying, NSSecureCoding |
| To | ``` class CLRegion : NSObject, NSCopying, NSSecureCoding {     init(circularRegionWithCenter center: CLLocationCoordinate2D, radius radius: CLLocationDistance, identifier identifier: String)     var center: CLLocationCoordinate2D { get }     var radius: CLLocationDistance { get }     var identifier: String { get }     var notifyOnEntry: Bool     var notifyOnExit: Bool     func contains(_ coordinate: CLLocationCoordinate2D) -> Bool     func scriptingIsEqual(to object: Any) -> Bool     func scriptingIsLessThanOrEqual(to object: Any) -> Bool     func scriptingIsLessThan(_ object: Any) -> Bool     func scriptingIsGreaterThanOrEqual(to object: Any) -> Bool     func scriptingIsGreaterThan(_ object: Any) -> Bool     func scriptingBegins(with object: Any) -> Bool     func scriptingEnds(with object: Any) -> Bool     func scriptingContains(_ object: Any) -> Bool     func isEqual(to object: Any?) -> Bool     func isLessThanOrEqual(to object: Any?) -> Bool     func isLessThan(_ object: Any?) -> Bool     func isGreaterThanOrEqual(to object: Any?) -> Bool     func isGreaterThan(_ object: Any?) -> Bool     func isNotEqual(to object: Any?) -> Bool     func doesContain(_ object: Any) -> Bool     func isLike(_ object: String) -> Bool     func isCaseInsensitiveLike(_ object: String) -> Bool     var objectSpecifier: NSScriptObjectSpecifier? { get }     func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?     func value(at index: Int, inPropertyWithKey key: String) -> Any?     func value(withName name: String, inPropertyWithKey key: String) -> Any?     func value(withUniqueID uniqueID: Any, inPropertyWithKey key: String) -> Any?     func insertValue(_ value: Any, at index: Int, inPropertyWithKey key: String)     func removeValue(at index: Int, fromPropertyWithKey key: String)     func replaceValue(at index: Int, inPropertyWithKey key: String, withValue value: Any)     func insertValue(_ value: Any, inPropertyWithKey key: String)     func coerceValue(_ value: Any?, forKey key: String) -> Any?     var classCode: FourCharCode { get }     var className: String { get }     func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?     var scriptingProperties: [String : Any]?     func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?     func newScriptingObject(of objectClass: AnyClass, forValueForKey key: String, withContentsValue contentsValue: Any?, properties properties: [String : Any]) -> Any?     @NSCopying var classDescription: NSClassDescription { get }     var attributeKeys: [String] { get }     var toOneRelationshipKeys: [String] { get }     var toManyRelationshipKeys: [String] { get }     func inverse(forRelationshipKey relationshipKey: String) -> String?     var classForPortCoder: AnyClass { get }     func replacementObject(for coder: NSPortCoder) -> Any?     var classForArchiver: AnyClass? { get }     func replacementObject(for archiver: NSArchiver) -> Any?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func setKeys(_ keys: [Any], triggerChangeNotificationsForDependentKey dependentKey: String)     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class func useStoredAccessor() -> Bool     func storedValue(forKey key: String) -> Any?     func takeStoredValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKey key: String)     func takeValue(_ value: Any?, forKeyPath keyPath: String)     func handleQuery(withUnboundKey key: String) -> Any?     func handleTakeValue(_ value: Any?, forUnboundKey key: String)     func unableToSetNil(forKey key: String)     func values(forKeys keys: [Any]) -> [AnyHashable : Any]     func takeValues(from properties: [AnyHashable : Any])     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func pose(as aClass: AnyClass)     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func replacementObject(for aCoder: NSCoder) -> Any?     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLRegion : CVarArg { } extension CLRegion : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [CLRegion.contains(_: CLLocationCoordinate2D) -> Bool](https://developer.apple.com/documentation/corelocation/clregion/1423828-containscoordinate)

|  | Declaration |
| --- | --- |
| From | ``` func containsCoordinate(_ coordinate: CLLocationCoordinate2D) -> Bool ``` |
| To | ``` func contains(_ coordinate: CLLocationCoordinate2D) -> Bool ``` |

Modified [CLRegionState [enum]](https://developer.apple.com/documentation/corelocation/clregionstate)

|  | Declaration |
| --- | --- |
| From | ``` enum CLRegionState : Int {     case Unknown     case Inside     case Outside } ``` |
| To | ``` enum CLRegionState : Int {     case unknown     case inside     case outside } ``` |

Modified [CLRegionState.inside](https://developer.apple.com/documentation/corelocation/clregionstate/clregionstateinside)

|  | Declaration |
| --- | --- |
| From | ``` case Inside ``` |
| To | ``` case inside ``` |

Modified [CLRegionState.outside](https://developer.apple.com/documentation/corelocation/clregionstate/clregionstateoutside)

|  | Declaration |
| --- | --- |
| From | ``` case Outside ``` |
| To | ``` case outside ``` |

Modified [CLRegionState.unknown](https://developer.apple.com/documentation/corelocation/clregionstate/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CLGeocodeCompletionHandler](https://developer.apple.com/documentation/corelocation/clgeocodecompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CLGeocodeCompletionHandler = ([CLPlacemark]?, NSError?) -> Void ``` |
| To | ``` typealias CLGeocodeCompletionHandler = ([CLPlacemark]?, Error?) -> Swift.Void ``` |

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
