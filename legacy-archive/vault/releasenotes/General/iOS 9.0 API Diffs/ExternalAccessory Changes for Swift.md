---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/ExternalAccessory.html
archived_at: '2026-07-18T02:56:48.960799Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# ExternalAccessory Changes for Swift

### ExternalAccessory

Removed EAWiFiUnconfiguredAccessoryProperties.init(_: UInt)Added [EAAccessory.dockType](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613905-docktype)Modified [EAAccessory](https://developer.apple.com/documentation/externalaccessory/eaaccessory)

|  | Declaration |
| --- | --- |
| From | ``` class EAAccessory : NSObject {     var connected: Bool { get }     var connectionID: Int { get }     var manufacturer: String! { get }     var name: String! { get }     var modelNumber: String! { get }     var serialNumber: String! { get }     var firmwareRevision: String! { get }     var hardwareRevision: String! { get }     var protocolStrings: [AnyObject]! { get }     unowned(unsafe) var delegate: EAAccessoryDelegate! } ``` |
| To | ``` class EAAccessory : NSObject {     var connected: Bool { get }     var connectionID: Int { get }     var manufacturer: String { get }     var name: String { get }     var modelNumber: String { get }     var serialNumber: String { get }     var firmwareRevision: String { get }     var hardwareRevision: String { get }     var dockType: String { get }     var protocolStrings: [String] { get }     unowned(unsafe) var delegate: EAAccessoryDelegate? } ``` |

Modified [EAAccessory.delegate](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613850-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: EAAccessoryDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: EAAccessoryDelegate? ``` |

Modified [EAAccessory.firmwareRevision](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613897-firmwarerevision)

|  | Declaration |
| --- | --- |
| From | ``` var firmwareRevision: String! { get } ``` |
| To | ``` var firmwareRevision: String { get } ``` |

Modified [EAAccessory.hardwareRevision](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613883-hardwarerevision)

|  | Declaration |
| --- | --- |
| From | ``` var hardwareRevision: String! { get } ``` |
| To | ``` var hardwareRevision: String { get } ``` |

Modified [EAAccessory.manufacturer](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613855-manufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var manufacturer: String! { get } ``` |
| To | ``` var manufacturer: String { get } ``` |

Modified [EAAccessory.modelNumber](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613848-modelnumber)

|  | Declaration |
| --- | --- |
| From | ``` var modelNumber: String! { get } ``` |
| To | ``` var modelNumber: String { get } ``` |

Modified [EAAccessory.name](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613801-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [EAAccessory.protocolStrings](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613877-protocolstrings)

|  | Declaration |
| --- | --- |
| From | ``` var protocolStrings: [AnyObject]! { get } ``` |
| To | ``` var protocolStrings: [String] { get } ``` |

Modified [EAAccessory.serialNumber](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613811-serialnumber)

|  | Declaration |
| --- | --- |
| From | ``` var serialNumber: String! { get } ``` |
| To | ``` var serialNumber: String { get } ``` |

Modified [EAAccessoryDelegate](https://developer.apple.com/documentation/externalaccessory/eaaccessorydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol EAAccessoryDelegate : NSObjectProtocol {     optional func accessoryDidDisconnect(_ accessory: EAAccessory!) } ``` |
| To | ``` protocol EAAccessoryDelegate : NSObjectProtocol {     optional func accessoryDidDisconnect(_ accessory: EAAccessory) } ``` |

Modified [EAAccessoryDelegate.accessoryDidDisconnect(_: EAAccessory)](https://developer.apple.com/documentation/externalaccessory/eaaccessorydelegate/1613858-accessorydiddisconnect)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessoryDidDisconnect(_ accessory: EAAccessory!) ``` |
| To | ``` optional func accessoryDidDisconnect(_ accessory: EAAccessory) ``` |

Modified [EAAccessoryManager](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager)

|  | Declaration |
| --- | --- |
| From | ``` class EAAccessoryManager : NSObject {     class func sharedAccessoryManager() -> EAAccessoryManager!     func showBluetoothAccessoryPickerWithNameFilter(_ predicate: NSPredicate!, completion completion: EABluetoothAccessoryPickerCompletion!)     func registerForLocalNotifications()     func unregisterForLocalNotifications()     var connectedAccessories: [AnyObject]! { get } } ``` |
| To | ``` class EAAccessoryManager : NSObject {     class func sharedAccessoryManager() -> EAAccessoryManager     func showBluetoothAccessoryPickerWithNameFilter(_ predicate: NSPredicate?, completion completion: EABluetoothAccessoryPickerCompletion?)     func registerForLocalNotifications()     func unregisterForLocalNotifications()     var connectedAccessories: [EAAccessory] { get } } ``` |

Modified [EAAccessoryManager.connectedAccessories](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613821-connectedaccessories)

|  | Declaration |
| --- | --- |
| From | ``` var connectedAccessories: [AnyObject]! { get } ``` |
| To | ``` var connectedAccessories: [EAAccessory] { get } ``` |

Modified [EAAccessoryManager.sharedAccessoryManager() -> EAAccessoryManager [class]](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613887-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedAccessoryManager() -> EAAccessoryManager! ``` |
| To | ``` class func sharedAccessoryManager() -> EAAccessoryManager ``` |

Modified [EAAccessoryManager.showBluetoothAccessoryPickerWithNameFilter(_: NSPredicate?, completion: EABluetoothAccessoryPickerCompletion?)](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613913-showbluetoothaccessorypickerwith)

|  | Declaration |
| --- | --- |
| From | ``` func showBluetoothAccessoryPickerWithNameFilter(_ predicate: NSPredicate!, completion completion: EABluetoothAccessoryPickerCompletion!) ``` |
| To | ``` func showBluetoothAccessoryPickerWithNameFilter(_ predicate: NSPredicate?, completion completion: EABluetoothAccessoryPickerCompletion?) ``` |

Modified [EABluetoothAccessoryPickerErrorCode [enum]](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [EASession](https://developer.apple.com/documentation/externalaccessory/easession)

|  | Declaration |
| --- | --- |
| From | ``` class EASession : NSObject {     init!(accessory accessory: EAAccessory!, forProtocol protocolString: String!)     var accessory: EAAccessory! { get }     var protocolString: String! { get }     var inputStream: NSInputStream! { get }     var outputStream: NSOutputStream! { get } } ``` |
| To | ``` class EASession : NSObject {     init(accessory accessory: EAAccessory, forProtocol protocolString: String)     var accessory: EAAccessory { get }     var protocolString: String { get }     var inputStream: NSInputStream? { get }     var outputStream: NSOutputStream? { get } } ``` |

Modified [EASession.accessory](https://developer.apple.com/documentation/externalaccessory/easession/1613825-accessory)

|  | Declaration |
| --- | --- |
| From | ``` var accessory: EAAccessory! { get } ``` |
| To | ``` var accessory: EAAccessory { get } ``` |

Modified [EASession.init(accessory: EAAccessory, forProtocol: String)](https://developer.apple.com/documentation/externalaccessory/easession/1613849-initwithaccessory)

|  | Declaration |
| --- | --- |
| From | ``` init!(accessory accessory: EAAccessory!, forProtocol protocolString: String!) ``` |
| To | ``` init(accessory accessory: EAAccessory, forProtocol protocolString: String) ``` |

Modified [EASession.inputStream](https://developer.apple.com/documentation/externalaccessory/easession/1613867-inputstream)

|  | Declaration |
| --- | --- |
| From | ``` var inputStream: NSInputStream! { get } ``` |
| To | ``` var inputStream: NSInputStream? { get } ``` |

Modified [EASession.outputStream](https://developer.apple.com/documentation/externalaccessory/easession/1613823-outputstream)

|  | Declaration |
| --- | --- |
| From | ``` var outputStream: NSOutputStream! { get } ``` |
| To | ``` var outputStream: NSOutputStream? { get } ``` |

Modified [EASession.protocolString](https://developer.apple.com/documentation/externalaccessory/easession/1613799-protocolstring)

|  | Declaration |
| --- | --- |
| From | ``` var protocolString: String! { get } ``` |
| To | ``` var protocolString: String { get } ``` |

Modified [EAWiFiUnconfiguredAccessory](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory)

|  | Declaration |
| --- | --- |
| From | ``` class EAWiFiUnconfiguredAccessory : NSObject {     var name: String! { get }     var manufacturer: String! { get }     var model: String! { get }     var ssid: String! { get }     var macAddress: String! { get }     var properties: EAWiFiUnconfiguredAccessoryProperties { get } } ``` |
| To | ``` class EAWiFiUnconfiguredAccessory : NSObject {     var name: String { get }     var manufacturer: String { get }     var model: String { get }     var ssid: String { get }     var macAddress: String { get }     var properties: EAWiFiUnconfiguredAccessoryProperties { get } } ``` |

Modified [EAWiFiUnconfiguredAccessory.macAddress](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613860-macaddress)

|  | Declaration |
| --- | --- |
| From | ``` var macAddress: String! { get } ``` |
| To | ``` var macAddress: String { get } ``` |

Modified [EAWiFiUnconfiguredAccessory.manufacturer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613819-manufacturer)

|  | Declaration |
| --- | --- |
| From | ``` var manufacturer: String! { get } ``` |
| To | ``` var manufacturer: String { get } ``` |

Modified [EAWiFiUnconfiguredAccessory.model](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613893-model)

|  | Declaration |
| --- | --- |
| From | ``` var model: String! { get } ``` |
| To | ``` var model: String { get } ``` |

Modified [EAWiFiUnconfiguredAccessory.name](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613856-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [EAWiFiUnconfiguredAccessory.ssid](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613889-ssid)

|  | Declaration |
| --- | --- |
| From | ``` var ssid: String! { get } ``` |
| To | ``` var ssid: String { get } ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` class EAWiFiUnconfiguredAccessoryBrowser : NSObject {     weak var delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate!     var unconfiguredAccessories: Set<NSObject>! { get }     init!(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate!, queue queue: dispatch_queue_t!)     func startSearchingForUnconfiguredAccessoriesMatchingPredicate(_ predicate: NSPredicate!)     func stopSearchingForUnconfiguredAccessories()     func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory!, withConfigurationUIOnViewController viewController: UIViewController!) } ``` |
| To | ``` class EAWiFiUnconfiguredAccessoryBrowser : NSObject {     weak var delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?     var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory> { get }     init(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue queue: dispatch_queue_t?)     func startSearchingForUnconfiguredAccessoriesMatchingPredicate(_ predicate: NSPredicate?)     func stopSearchingForUnconfiguredAccessories()     func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory, withConfigurationUIOnViewController viewController: UIViewController) } ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser.configureAccessory(_: EAWiFiUnconfiguredAccessory, withConfigurationUIOnViewController: UIViewController)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613907-configureaccessory)

|  | Declaration |
| --- | --- |
| From | ``` func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory!, withConfigurationUIOnViewController viewController: UIViewController!) ``` |
| To | ``` func configureAccessory(_ accessory: EAWiFiUnconfiguredAccessory, withConfigurationUIOnViewController viewController: UIViewController) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser.delegate](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613829-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate! ``` |
| To | ``` weak var delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate? ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser.init(delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue: dispatch_queue_t?)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613881-initwithdelegate)

|  | Declaration |
| --- | --- |
| From | ``` init!(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate!, queue queue: dispatch_queue_t!) ``` |
| To | ``` init(delegate delegate: EAWiFiUnconfiguredAccessoryBrowserDelegate?, queue queue: dispatch_queue_t?) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser.startSearchingForUnconfiguredAccessoriesMatchingPredicate(_: NSPredicate?)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613869-startsearchingforunconfiguredacc)

|  | Declaration |
| --- | --- |
| From | ``` func startSearchingForUnconfiguredAccessoriesMatchingPredicate(_ predicate: NSPredicate!) ``` |
| To | ``` func startSearchingForUnconfiguredAccessoriesMatchingPredicate(_ predicate: NSPredicate?) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowser.unconfiguredAccessories](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613871-unconfiguredaccessories)

|  | Declaration |
| --- | --- |
| From | ``` var unconfiguredAccessories: Set<NSObject>! { get } ``` |
| To | ``` var unconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory> { get } ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol EAWiFiUnconfiguredAccessoryBrowserDelegate : NSObjectProtocol {     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didUpdateState state: EAWiFiUnconfiguredAccessoryBrowserState)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didFindUnconfiguredAccessories accessories: Set<NSObject>!)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didRemoveUnconfiguredAccessories accessories: Set<NSObject>!)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory!, withStatus status: EAWiFiUnconfiguredAccessoryConfigurationStatus) } ``` |
| To | ``` protocol EAWiFiUnconfiguredAccessoryBrowserDelegate : NSObjectProtocol {     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didUpdateState state: EAWiFiUnconfiguredAccessoryBrowserState)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>)     func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory, withStatus status: EAWiFiUnconfiguredAccessoryConfigurationStatus) } ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(_: EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613861-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didFindUnconfiguredAccessories accessories: Set<NSObject>!) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFindUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(_: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory: EAWiFiUnconfiguredAccessory, withStatus: EAWiFiUnconfiguredAccessoryConfigurationStatus)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613911-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory!, withStatus status: EAWiFiUnconfiguredAccessoryConfigurationStatus) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didFinishConfiguringAccessory accessory: EAWiFiUnconfiguredAccessory, withStatus status: EAWiFiUnconfiguredAccessoryConfigurationStatus) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(_: EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories: Set<EAWiFiUnconfiguredAccessory>)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613862-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didRemoveUnconfiguredAccessories accessories: Set<NSObject>!) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didRemoveUnconfiguredAccessories accessories: Set<EAWiFiUnconfiguredAccessory>) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserDelegate.accessoryBrowser(_: EAWiFiUnconfiguredAccessoryBrowser, didUpdateState: EAWiFiUnconfiguredAccessoryBrowserState)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate/1613845-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser!, didUpdateState state: EAWiFiUnconfiguredAccessoryBrowserState) ``` |
| To | ``` func accessoryBrowser(_ browser: EAWiFiUnconfiguredAccessoryBrowser, didUpdateState state: EAWiFiUnconfiguredAccessoryBrowserState) ``` |

Modified [EAWiFiUnconfiguredAccessoryBrowserState [enum]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [EAWiFiUnconfiguredAccessoryConfigurationStatus [enum]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [EAWiFiUnconfiguredAccessoryProperties [struct]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct EAWiFiUnconfiguredAccessoryProperties : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var PropertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get } } ``` | RawOptionSetType |
| To | ``` struct EAWiFiUnconfiguredAccessoryProperties : OptionSetType {     init(rawValue rawValue: UInt)     static var PropertySupportsAirPlay: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsAirPrint: EAWiFiUnconfiguredAccessoryProperties { get }     static var PropertySupportsHomeKit: EAWiFiUnconfiguredAccessoryProperties { get } } ``` | OptionSetType |

Modified [EABluetoothAccessoryPickerCompletion](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickercompletion)

|  | Declaration |
| --- | --- |
| From | ``` typealias EABluetoothAccessoryPickerCompletion = (NSError!) -> Void ``` |
| To | ``` typealias EABluetoothAccessoryPickerCompletion = (NSError?) -> Void ``` |

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
