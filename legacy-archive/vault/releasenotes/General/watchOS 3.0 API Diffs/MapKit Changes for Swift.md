---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/MapKit.html
archived_at: '2026-07-18T02:58:31.607640Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# MapKit Changes for Swift

### MapKit

Added [MKPlacemark.init(coordinate: CLLocationCoordinate2D)](https://developer.apple.com/documentation/mapkit/mkplacemark/2172460-initwithcoordinate)Added [MKPlacemark.init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)](https://developer.apple.com/documentation/mapkit/mkplacemark/2172461-initwithcoordinate)Added [NSUserActivity.mapItem](https://developer.apple.com/documentation/foundation/nsuseractivity/1690596-mapitem)Added [MKLaunchOptionsDirectionsModeDefault](https://developer.apple.com/documentation/mapkit/mklaunchoptionsdirectionsmodedefault)Modified [MKDistanceFormatter](https://developer.apple.com/documentation/mapkit/mkdistanceformatter)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MKDistanceFormatter : NSFormatter {     func stringFromDistance(_ distance: CLLocationDistance) -> String     func distanceFromString(_ distance: String) -> CLLocationDistance     @NSCopying var locale: NSLocale!     var units: MKDistanceFormatterUnits     var unitStyle: MKDistanceFormatterUnitStyle } ``` | -- |
| To | ``` class MKDistanceFormatter : Formatter {     func string(fromDistance distance: CLLocationDistance) -> String     func distance(from distance: String) -> CLLocationDistance     var locale: Locale!     var units: MKDistanceFormatterUnits     var unitStyle: MKDistanceFormatterUnitStyle     enum Context : Int {         case unknown         case dynamic         case standalone         case listItem         case beginningOfSentence         case middleOfSentence     }     enum UnitStyle : Int {         case short         case medium         case long     }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MKDistanceFormatter : CVarArg { } extension MKDistanceFormatter : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MKDistanceFormatter.distance(from: String) -> CLLocationDistance](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452766-distance)

|  | Declaration |
| --- | --- |
| From | ``` func distanceFromString(_ distance: String) -> CLLocationDistance ``` |
| To | ``` func distance(from distance: String) -> CLLocationDistance ``` |

Modified [MKDistanceFormatter.locale](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1452235-locale)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var locale: NSLocale! ``` |
| To | ``` var locale: Locale! ``` |

Modified [MKDistanceFormatter.string(fromDistance: CLLocationDistance) -> String](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/1451994-stringfromdistance)

|  | Declaration |
| --- | --- |
| From | ``` func stringFromDistance(_ distance: CLLocationDistance) -> String ``` |
| To | ``` func string(fromDistance distance: CLLocationDistance) -> String ``` |

Modified [MKDistanceFormatterUnits [enum]](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits)

|  | Declaration |
| --- | --- |
| From | ``` enum MKDistanceFormatterUnits : UInt {     case Default     case Metric     case Imperial     case ImperialWithYards } ``` |
| To | ``` enum MKDistanceFormatterUnits : UInt {     case `default`     case metric     case imperial     case imperialWithYards } ``` |

Modified [MKDistanceFormatterUnits.default](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits/mkdistanceformatterunitsdefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [MKDistanceFormatterUnits.imperial](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/units/imperial)

|  | Declaration |
| --- | --- |
| From | ``` case Imperial ``` |
| To | ``` case imperial ``` |

Modified [MKDistanceFormatterUnits.imperialWithYards](https://developer.apple.com/documentation/mapkit/mkdistanceformatterunits/mkdistanceformatterunitsimperialwithyards)

|  | Declaration |
| --- | --- |
| From | ``` case ImperialWithYards ``` |
| To | ``` case imperialWithYards ``` |

Modified [MKDistanceFormatterUnits.metric](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/units/metric)

|  | Declaration |
| --- | --- |
| From | ``` case Metric ``` |
| To | ``` case metric ``` |

Modified [MKDistanceFormatterUnitStyle [enum]](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum MKDistanceFormatterUnitStyle : UInt {     case Default     case Abbreviated     case Full } ``` |
| To | ``` enum MKDistanceFormatterUnitStyle : UInt {     case `default`     case abbreviated     case full } ``` |

Modified [MKDistanceFormatterUnitStyle.abbreviated](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle/abbreviated)

|  | Declaration |
| --- | --- |
| From | ``` case Abbreviated ``` |
| To | ``` case abbreviated ``` |

Modified [MKDistanceFormatterUnitStyle.default](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [MKDistanceFormatterUnitStyle.full](https://developer.apple.com/documentation/mapkit/mkdistanceformatter/unitstyle/full)

|  | Declaration |
| --- | --- |
| From | ``` case Full ``` |
| To | ``` case full ``` |

Modified [MKMapItem](https://developer.apple.com/documentation/mapkit/mkmapitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class MKMapItem : NSObject {     var placemark: MKPlacemark { get }     var isCurrentLocation: Bool { get }     var name: String?     var phoneNumber: String?     var url: NSURL?     @NSCopying var timeZone: NSTimeZone?     class func mapItemForCurrentLocation() -> MKMapItem     init(placemark placemark: MKPlacemark)     func openInMapsWithLaunchOptions(_ launchOptions: [String : AnyObject]?) -> Bool     class func openMapsWithItems(_ mapItems: [MKMapItem], launchOptions launchOptions: [String : AnyObject]?) -> Bool } ``` | -- |
| To | ``` class MKMapItem : NSObject {     var placemark: MKPlacemark { get }     var isCurrentLocation: Bool { get }     var name: String?     var phoneNumber: String?     var url: URL?     var timeZone: TimeZone?     class func forCurrentLocation() -> MKMapItem     init(placemark placemark: MKPlacemark)     func openInMaps(launchOptions launchOptions: [String : Any]? = nil) -> Bool     class func openMaps(with mapItems: [MKMapItem], launchOptions launchOptions: [String : Any]? = nil) -> Bool     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension MKMapItem : CVarArg { } extension MKMapItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [MKMapItem.forCurrentLocation() -> MKMapItem [class]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452002-mapitemforcurrentlocation)

|  | Declaration |
| --- | --- |
| From | ``` class func mapItemForCurrentLocation() -> MKMapItem ``` |
| To | ``` class func forCurrentLocation() -> MKMapItem ``` |

Modified [MKMapItem.openInMaps(launchOptions: [String : Any]?) -> Bool](https://developer.apple.com/documentation/mapkit/mkmapitem/1452239-openinmapswithlaunchoptions)

|  | Declaration |
| --- | --- |
| From | ``` func openInMapsWithLaunchOptions(_ launchOptions: [String : AnyObject]?) -> Bool ``` |
| To | ``` func openInMaps(launchOptions launchOptions: [String : Any]? = nil) -> Bool ``` |

Modified [MKMapItem.openMaps(with: [MKMapItem], launchOptions: [String : Any]?) -> Bool [class]](https://developer.apple.com/documentation/mapkit/mkmapitem/1452207-openmaps)

|  | Declaration |
| --- | --- |
| From | ``` class func openMapsWithItems(_ mapItems: [MKMapItem], launchOptions launchOptions: [String : AnyObject]?) -> Bool ``` |
| To | ``` class func openMaps(with mapItems: [MKMapItem], launchOptions launchOptions: [String : Any]? = nil) -> Bool ``` |

Modified [MKMapItem.timeZone](https://developer.apple.com/documentation/mapkit/mkmapitem/1452431-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone? ``` |
| To | ``` var timeZone: TimeZone? ``` |

Modified [MKMapItem.url](https://developer.apple.com/documentation/mapkit/mkmapitem/1452746-url)

|  | Declaration |
| --- | --- |
| From | ``` var url: NSURL? ``` |
| To | ``` var url: URL? ``` |

Modified [MKPlacemark](https://developer.apple.com/documentation/mapkit/mkplacemark)

|  | Declaration |
| --- | --- |
| From | ``` class MKPlacemark : CLPlacemark, MKAnnotation {     init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [String : AnyObject]?)     var countryCode: String? { get } } ``` |
| To | ``` class MKPlacemark : CLPlacemark, MKAnnotation {     init(coordinate coordinate: CLLocationCoordinate2D)     init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [String : Any]?)     init(coordinate coordinate: CLLocationCoordinate2D, postalAddress postalAddress: CNPostalAddress)     var countryCode: String? { get } } ``` |

Modified [MKPlacemark.init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)](https://developer.apple.com/documentation/mapkit/mkplacemark/1451895-initwithcoordinate)

|  | Declaration |
| --- | --- |
| From | ``` init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [String : AnyObject]?) ``` |
| To | ``` init(coordinate coordinate: CLLocationCoordinate2D, addressDictionary addressDictionary: [String : Any]?) ``` |

Modified [NSValue.init(mkCoordinate: CLLocationCoordinate2D)](https://developer.apple.com/documentation/foundation/nsvalue/1452193-init)

|  | Declaration |
| --- | --- |
| From | ``` init(MKCoordinate coordinate: CLLocationCoordinate2D) ``` |
| To | ``` init(mkCoordinate coordinate: CLLocationCoordinate2D) ``` |

Modified [NSValue.init(mkCoordinateSpan: MKCoordinateSpan)](https://developer.apple.com/documentation/foundation/nsvalue/1452333-init)

|  | Declaration |
| --- | --- |
| From | ``` init(MKCoordinateSpan span: MKCoordinateSpan) ``` |
| To | ``` init(mkCoordinateSpan span: MKCoordinateSpan) ``` |

Modified [NSValue.mkCoordinateSpanValue](https://developer.apple.com/documentation/foundation/nsvalue/1452516-mkcoordinatespanvalue)

|  | Declaration |
| --- | --- |
| From | ``` var MKCoordinateSpanValue: MKCoordinateSpan { get } ``` |
| To | ``` var mkCoordinateSpanValue: MKCoordinateSpan { get } ``` |

Modified [NSValue.mkCoordinateValue](https://developer.apple.com/documentation/foundation/nsvalue/1452495-mkcoordinatevalue)

|  | Declaration |
| --- | --- |
| From | ``` var MKCoordinateValue: CLLocationCoordinate2D { get } ``` |
| To | ``` var mkCoordinateValue: CLLocationCoordinate2D { get } ``` |

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
