---
title: watchOS 3.1 API Diffs
apple_id: TP40017546
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS31APIDiffs/Swift/CoreLocation.html
archived_at: '2026-07-18T02:58:38.070238Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.1 API Diffs](watchOS%203.0%20to%20watchOS%203.1%20API%20Differences.md)


# CoreLocation Changes for Swift

### CoreLocation

Modified [CLGeocoder](https://developer.apple.com/documentation/corelocation/clgeocoder)

|  | Declaration |
| --- | --- |
| From | ``` class CLGeocoder : NSObject {     var isGeocoding: Bool { get }     func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any], completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, in region: CLRegion?, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler)     func cancelGeocode()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLGeocoder : CVarArg { } extension CLGeocoder : Equatable, Hashable {     var hashValue: Int { get } } ``` |
| To | ``` class CLGeocoder : NSObject {     var isGeocoding: Bool { get }     func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any], completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler)     func geocodeAddressString(_ addressString: String, in region: CLRegion?, completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler)     func cancelGeocode()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension CLGeocoder : CVarArg { } extension CLGeocoder : Equatable, Hashable {     var hashValue: Int { get } } ``` |

Modified [CLGeocoder.geocodeAddressDictionary(_: [AnyHashable : Any], completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423693-geocodeaddressdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any], completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |
| To | ``` func geocodeAddressDictionary(_ addressDictionary: [AnyHashable : Any], completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.geocodeAddressString(_: String, completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423509-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressString(_ addressString: String, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |
| To | ``` func geocodeAddressString(_ addressString: String, completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.geocodeAddressString(_: String, in: CLRegion?, completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423591-geocodeaddressstring)

|  | Declaration |
| --- | --- |
| From | ``` func geocodeAddressString(_ addressString: String, in region: CLRegion?, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |
| To | ``` func geocodeAddressString(_ addressString: String, in region: CLRegion?, completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLGeocoder.reverseGeocodeLocation(_: CLLocation, completionHandler: CoreLocation.CLGeocodeCompletionHandler)](https://developer.apple.com/documentation/corelocation/clgeocoder/1423621-reversegeocodelocation)

|  | Declaration |
| --- | --- |
| From | ``` func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: CoreLocation.CLGeocodeCompletionHandler) ``` |
| To | ``` func reverseGeocodeLocation(_ location: CLLocation, completionHandler completionHandler: @escaping CoreLocation.CLGeocodeCompletionHandler) ``` |

Modified [CLLocationCoordinate2D [struct]](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2d)

|  | Declaration |
| --- | --- |
| From | ``` struct CLLocationCoordinate2D {     var latitude: CLLocationDegrees     var longitude: CLLocationDegrees     init()     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) } ``` |
| To | ``` struct CLLocationCoordinate2D {     var latitude: CLLocationDegrees     var longitude: CLLocationDegrees     init()     init(latitude latitude: CLLocationDegrees, longitude longitude: CLLocationDegrees) } extension CLLocationCoordinate2D { } ``` |

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
