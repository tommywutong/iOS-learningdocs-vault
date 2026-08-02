---
title: macOS 10.12.1 API Diffs
apple_id: TP40017565
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12_1/Swift/AudioVideoBridging.html
archived_at: '2026-07-18T02:51:44.617423Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12.1 API Diffs](macOS%2010.12%20to%20macOS%2010.12.1%20API%20Differences.md)


# AudioVideoBridging Changes for Swift

### AudioVideoBridging

Modified AVB17221ACMPInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221ACMPInterface : AVB1722ControlInterface {     @NSCopying var multicastDestinationAddress: AVBMACAddress { get }      init(interface anInterface: AVBInterface)     class func withInterface(_ anInterface: AVBInterface) -> AVB17221ACMPInterface      init(interfaceNamed anInterfaceName: String)     class func withInterfaceNamed(_ anInterfaceName: String) -> AVB17221ACMPInterface     func setHandler(_ handler: AVB17221ACMPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221ACMPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandler(forGUID targetGUID: UInt64)     func removeHandler(forEntityID targetEntityID: UInt64)     func sendACMPResponseMessage(_ message: AVB17221ACMPMessage) throws     func sendACMPCommand(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool } ``` |
| To | ``` class AVB17221ACMPInterface : AVB1722ControlInterface {     @NSCopying var multicastDestinationAddress: AVBMACAddress { get }      init(interface anInterface: AVBInterface)     class func withInterface(_ anInterface: AVBInterface) -> AVB17221ACMPInterface      init(interfaceNamed anInterfaceName: String)     class func withInterfaceNamed(_ anInterfaceName: String) -> AVB17221ACMPInterface     func setHandler(_ handler: AVB17221ACMPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221ACMPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandler(forGUID targetGUID: UInt64)     func removeHandler(forEntityID targetEntityID: UInt64)     func sendACMPResponseMessage(_ message: AVB17221ACMPMessage) throws     func sendACMPCommand(_ message: AVB17221ACMPMessage, completionHandler completionHandler: @escaping AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool } ``` |

Modified AVB17221ACMPInterface.sendACMPCommand(_: AVB17221ACMPMessage, completionHandler: AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendACMPCommand(_ message: AVB17221ACMPMessage, completionHandler completionHandler: AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool ``` |
| To | ``` func sendACMPCommand(_ message: AVB17221ACMPMessage, completionHandler completionHandler: @escaping AudioVideoBridging.AVB17221ACMPInterfaceCompletion) -> Bool ``` |

Modified AVB17221AECPInterface

|  | Declaration |
| --- | --- |
| From | ``` class AVB17221AECPInterface : AVB1722ControlInterface {      init?(interface anInterface: AVBInterface)     class func withInterface(_ anInterface: AVBInterface) -> AVB17221AECPInterface?      init?(interfaceNamed anInterfaceName: String)     class func withInterfaceNamed(_ anInterfaceName: String) -> AVB17221AECPInterface?     func setHandler(_ handler: AVB17221AECPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandler(forGUID targetGUID: UInt64)     func removeHandler(forEntityID targetEntityID: UInt64)     func setCommandHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeCommandHandler(forEntityID targetEntityID: UInt64)     func setResponseHandler(_ handler: AVB17221AECPClient, forControllerEntityID controllerEntityID: UInt64) -> Bool     func removeResponseHandler(forControllerEntityID controllerEntityID: UInt64)     func sendCommand(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress, completionHandler completionHandler: AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool     func sendResponse(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress) throws } ``` |
| To | ``` class AVB17221AECPInterface : AVB1722ControlInterface {      init?(interface anInterface: AVBInterface)     class func withInterface(_ anInterface: AVBInterface) -> AVB17221AECPInterface?      init?(interfaceNamed anInterfaceName: String)     class func withInterfaceNamed(_ anInterfaceName: String) -> AVB17221AECPInterface?     func setHandler(_ handler: AVB17221AECPClient, forGUID targetGUID: UInt64) -> Bool     func setHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeHandler(forGUID targetGUID: UInt64)     func removeHandler(forEntityID targetEntityID: UInt64)     func setCommandHandler(_ handler: AVB17221AECPClient, forEntityID targetEntityID: UInt64) -> Bool     func removeCommandHandler(forEntityID targetEntityID: UInt64)     func setResponseHandler(_ handler: AVB17221AECPClient, forControllerEntityID controllerEntityID: UInt64) -> Bool     func removeResponseHandler(forControllerEntityID controllerEntityID: UInt64)     func sendCommand(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress, completionHandler completionHandler: @escaping AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool     func sendResponse(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress) throws } ``` |

Modified AVB17221AECPInterface.sendCommand(_: AVB17221AECPMessage, to: AVBMACAddress, completionHandler: AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func sendCommand(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress, completionHandler completionHandler: AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool ``` |
| To | ``` func sendCommand(_ message: AVB17221AECPMessage, to destMAC: AVBMACAddress, completionHandler completionHandler: @escaping AudioVideoBridging.AVB17221AECPInterfaceCompletion) -> Bool ``` |

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
