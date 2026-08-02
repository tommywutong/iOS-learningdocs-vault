---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/ExternalAccessory.html
archived_at: '2026-07-18T02:57:42.903232Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# ExternalAccessory Changes for Swift

### ExternalAccessory (Added)

Added [EAAccessory](https://developer.apple.com/documentation/externalaccessory/eaaccessory)Added [EAAccessory.connectionID](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613795-connectionid)Added [EAAccessory.delegate](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613850-delegate)Added [EAAccessory.dockType](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613905-docktype)Added [EAAccessory.firmwareRevision](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613897-firmwarerevision)Added [EAAccessory.hardwareRevision](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613883-hardwarerevision)Added [EAAccessory.isConnected](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613803-isconnected)Added [EAAccessory.manufacturer](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613855-manufacturer)Added [EAAccessory.modelNumber](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613848-modelnumber)Added [EAAccessory.name](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613801-name)Added [EAAccessory.protocolStrings](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613877-protocolstrings)Added [EAAccessory.serialNumber](https://developer.apple.com/documentation/externalaccessory/eaaccessory/1613811-serialnumber)Added [EAAccessoryDelegate](https://developer.apple.com/documentation/externalaccessory/eaaccessorydelegate)Added [EAAccessoryDelegate.accessoryDidDisconnect(_: EAAccessory)](https://developer.apple.com/documentation/externalaccessory/eaaccessorydelegate/1613858-accessorydiddisconnect)Added [EAAccessoryManager](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager)Added [EAAccessoryManager.connectedAccessories](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613821-connectedaccessories)Added [EAAccessoryManager.registerForLocalNotifications()](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613873-registerforlocalnotifications)Added [EAAccessoryManager.shared() -> EAAccessoryManager [class]](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613887-shared)Added [EAAccessoryManager.showBluetoothAccessoryPicker(withNameFilter: NSPredicate?, completion: ExternalAccessory.EABluetoothAccessoryPickerCompletion?)](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613913-showbluetoothaccessorypickerwith)Added [EAAccessoryManager.unregisterForLocalNotifications()](https://developer.apple.com/documentation/externalaccessory/eaaccessorymanager/1613903-unregisterforlocalnotifications)Added [EABluetoothAccessoryPickerError [struct]](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror)Added [EABluetoothAccessoryPickerError.alreadyConnected](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335351-alreadyconnected)Added EABluetoothAccessoryPickerError.init(_nsError: NSError)Added [EABluetoothAccessoryPickerError.resultCancelled](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335353-resultcancelled)Added [EABluetoothAccessoryPickerError.resultFailed](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335352-resultfailed)Added [EABluetoothAccessoryPickerError.resultNotFound](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererror/2335354-resultnotfound)Added [EABluetoothAccessoryPickerError.Code [enum]](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode)Added [EABluetoothAccessoryPickerError.Code.alreadyConnected](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickeralreadyconnected)Added [EABluetoothAccessoryPickerError.Code.resultCancelled](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultcancelled)Added [EABluetoothAccessoryPickerError.Code.resultFailed](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultfailed)Added [EABluetoothAccessoryPickerError.Code.resultNotFound](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrorcode/eabluetoothaccessorypickerresultnotfound)Added [EASession](https://developer.apple.com/documentation/externalaccessory/easession)Added [EASession.accessory](https://developer.apple.com/documentation/externalaccessory/easession/1613825-accessory)Added [EASession.init(accessory: EAAccessory, forProtocol: String)](https://developer.apple.com/documentation/externalaccessory/easession/1613849-initwithaccessory)Added [EASession.inputStream](https://developer.apple.com/documentation/externalaccessory/easession/1613867-inputstream)Added [EASession.outputStream](https://developer.apple.com/documentation/externalaccessory/easession/1613823-outputstream)Added [EASession.protocolString](https://developer.apple.com/documentation/externalaccessory/easession/1613799-protocolstring)Added [EAWiFiUnconfiguredAccessory](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory)Added [EAWiFiUnconfiguredAccessory.macAddress](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613860-macaddress)Added [EAWiFiUnconfiguredAccessory.manufacturer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613819-manufacturer)Added [EAWiFiUnconfiguredAccessory.model](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613893-model)Added [EAWiFiUnconfiguredAccessory.name](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613856-name)Added [EAWiFiUnconfiguredAccessory.properties](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613879-properties)Added [EAWiFiUnconfiguredAccessory.ssid](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessory/1613889-ssid)Added [EAWiFiUnconfiguredAccessoryBrowser](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser)Added [EAWiFiUnconfiguredAccessoryBrowser.delegate](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613829-delegate)Added [EAWiFiUnconfiguredAccessoryBrowser.unconfiguredAccessories](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/1613871-unconfiguredaccessories)Added [EAWiFiUnconfiguredAccessoryBrowserDelegate](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserdelegate)Added [EAWiFiUnconfiguredAccessoryBrowserState [enum]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate)Added [EAWiFiUnconfiguredAccessoryBrowserState.configuring](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/configuring)Added [EAWiFiUnconfiguredAccessoryBrowserState.searching](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/searching)Added [EAWiFiUnconfiguredAccessoryBrowserState.stopped](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/stopped)Added [EAWiFiUnconfiguredAccessoryBrowserState.wiFiUnavailable](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowserstate/eawifiunconfiguredaccessorybrowserstatewifiunavailable)Added [EAWiFiUnconfiguredAccessoryConfigurationStatus [enum]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus)Added [EAWiFiUnconfiguredAccessoryConfigurationStatus.failed](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/eawifiunconfiguredaccessoryconfigurationstatusfailed)Added [EAWiFiUnconfiguredAccessoryConfigurationStatus.success](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/success)Added [EAWiFiUnconfiguredAccessoryConfigurationStatus.userCancelledConfiguration](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryconfigurationstatus/usercancelledconfiguration)Added [EAWiFiUnconfiguredAccessoryProperties [struct]](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties)Added [EAWiFiUnconfiguredAccessoryProperties.init(rawValue: UInt)](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/1613809-init)Added [EAWiFiUnconfiguredAccessoryProperties.propertySupportsAirPlay](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/1613793-propertysupportsairplay)Added [EAWiFiUnconfiguredAccessoryProperties.propertySupportsAirPrint](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/eawifiunconfiguredaccessorypropertysupportsairprint)Added [EAWiFiUnconfiguredAccessoryProperties.propertySupportsHomeKit](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessoryproperties/eawifiunconfiguredaccessorypropertysupportshomekit)Added [NSNotification.Name.EAAccessoryDidConnect](https://developer.apple.com/documentation/externalaccessory/eaaccessorydidconnectnotification)Added [NSNotification.Name.EAAccessoryDidDisconnect](https://developer.apple.com/documentation/foundation/nsnotification/name/1613901-eaaccessorydiddisconnect)Added [EAAccessoryKey](https://developer.apple.com/documentation/externalaccessory/eaaccessorykey)Added [EAAccessorySelectedKey](https://developer.apple.com/documentation/externalaccessory/eaaccessoryselectedkey)Added [EABluetoothAccessoryPickerCompletion](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickercompletion)Added [EABluetoothAccessoryPickerErrorDomain](https://developer.apple.com/documentation/externalaccessory/eabluetoothaccessorypickererrordomain)Added [EAConnectionIDNone](https://developer.apple.com/documentation/externalaccessory/1622272-null_connection_id/eaconnectionidnone)

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
