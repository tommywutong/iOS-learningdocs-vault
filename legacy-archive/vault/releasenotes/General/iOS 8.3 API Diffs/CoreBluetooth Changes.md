---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreBluetooth.html
archived_at: '2026-07-18T02:56:22.119727Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreBluetooth Changes

## CoreBluetooth

Modified CBATTError.Success

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBCharacteristicProperties.IndicateEncryptionRequired

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBCharacteristicProperties.NotifyEncryptionRequired

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.AlreadyAdvertising

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.ConnectionFailed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.1 |

Modified CBError.ConnectionTimeout

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.InvalidHandle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.InvalidParameters

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.NotConnected

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.OperationCancelled

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.OutOfSpace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.PeripheralDisconnected

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBError.UUIDNotAllowed

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified CBUUID.init(NSUUID: NSUUID!)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 7.0 |

Modified CBATTErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let CBATTErrorDomain: NSString! ``` |
| To | ``` let CBATTErrorDomain: String ``` |

Modified CBAdvertisementDataIsConnectable

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataIsConnectable: NSString! ``` |
| To | ``` let CBAdvertisementDataIsConnectable: String ``` |

Modified CBAdvertisementDataLocalNameKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataLocalNameKey: NSString! ``` |
| To | ``` let CBAdvertisementDataLocalNameKey: String ``` |

Modified CBAdvertisementDataManufacturerDataKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataManufacturerDataKey: NSString! ``` |
| To | ``` let CBAdvertisementDataManufacturerDataKey: String ``` |

Modified CBAdvertisementDataOverflowServiceUUIDsKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataOverflowServiceUUIDsKey: NSString! ``` |
| To | ``` let CBAdvertisementDataOverflowServiceUUIDsKey: String ``` |

Modified CBAdvertisementDataServiceDataKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataServiceDataKey: NSString! ``` |
| To | ``` let CBAdvertisementDataServiceDataKey: String ``` |

Modified CBAdvertisementDataServiceUUIDsKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataServiceUUIDsKey: NSString! ``` |
| To | ``` let CBAdvertisementDataServiceUUIDsKey: String ``` |

Modified CBAdvertisementDataSolicitedServiceUUIDsKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataSolicitedServiceUUIDsKey: NSString! ``` |
| To | ``` let CBAdvertisementDataSolicitedServiceUUIDsKey: String ``` |

Modified CBAdvertisementDataTxPowerLevelKey

|  | Declaration |
| --- | --- |
| From | ``` let CBAdvertisementDataTxPowerLevelKey: NSString! ``` |
| To | ``` let CBAdvertisementDataTxPowerLevelKey: String ``` |

Modified CBCentralManagerOptionRestoreIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerOptionRestoreIdentifierKey: NSString! ``` |
| To | ``` let CBCentralManagerOptionRestoreIdentifierKey: String ``` |

Modified CBCentralManagerOptionShowPowerAlertKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerOptionShowPowerAlertKey: NSString! ``` |
| To | ``` let CBCentralManagerOptionShowPowerAlertKey: String ``` |

Modified CBCentralManagerRestoredStatePeripheralsKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerRestoredStatePeripheralsKey: NSString! ``` |
| To | ``` let CBCentralManagerRestoredStatePeripheralsKey: String ``` |

Modified CBCentralManagerRestoredStateScanOptionsKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerRestoredStateScanOptionsKey: NSString! ``` |
| To | ``` let CBCentralManagerRestoredStateScanOptionsKey: String ``` |

Modified CBCentralManagerRestoredStateScanServicesKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerRestoredStateScanServicesKey: NSString! ``` |
| To | ``` let CBCentralManagerRestoredStateScanServicesKey: String ``` |

Modified CBCentralManagerScanOptionAllowDuplicatesKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerScanOptionAllowDuplicatesKey: NSString! ``` |
| To | ``` let CBCentralManagerScanOptionAllowDuplicatesKey: String ``` |

Modified CBCentralManagerScanOptionSolicitedServiceUUIDsKey

|  | Declaration |
| --- | --- |
| From | ``` let CBCentralManagerScanOptionSolicitedServiceUUIDsKey: NSString! ``` |
| To | ``` let CBCentralManagerScanOptionSolicitedServiceUUIDsKey: String ``` |

Modified CBConnectPeripheralOptionNotifyOnConnectionKey

|  | Declaration |
| --- | --- |
| From | ``` let CBConnectPeripheralOptionNotifyOnConnectionKey: NSString! ``` |
| To | ``` let CBConnectPeripheralOptionNotifyOnConnectionKey: String ``` |

Modified CBConnectPeripheralOptionNotifyOnDisconnectionKey

|  | Declaration |
| --- | --- |
| From | ``` let CBConnectPeripheralOptionNotifyOnDisconnectionKey: NSString! ``` |
| To | ``` let CBConnectPeripheralOptionNotifyOnDisconnectionKey: String ``` |

Modified CBConnectPeripheralOptionNotifyOnNotificationKey

|  | Declaration |
| --- | --- |
| From | ``` let CBConnectPeripheralOptionNotifyOnNotificationKey: NSString! ``` |
| To | ``` let CBConnectPeripheralOptionNotifyOnNotificationKey: String ``` |

Modified CBErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let CBErrorDomain: NSString! ``` |
| To | ``` let CBErrorDomain: String ``` |

Modified CBPeripheralManagerOptionRestoreIdentifierKey

|  | Declaration |
| --- | --- |
| From | ``` let CBPeripheralManagerOptionRestoreIdentifierKey: NSString! ``` |
| To | ``` let CBPeripheralManagerOptionRestoreIdentifierKey: String ``` |

Modified CBPeripheralManagerOptionShowPowerAlertKey

|  | Declaration |
| --- | --- |
| From | ``` let CBPeripheralManagerOptionShowPowerAlertKey: NSString! ``` |
| To | ``` let CBPeripheralManagerOptionShowPowerAlertKey: String ``` |

Modified CBPeripheralManagerRestoredStateAdvertisementDataKey

|  | Declaration |
| --- | --- |
| From | ``` let CBPeripheralManagerRestoredStateAdvertisementDataKey: NSString! ``` |
| To | ``` let CBPeripheralManagerRestoredStateAdvertisementDataKey: String ``` |

Modified CBPeripheralManagerRestoredStateServicesKey

|  | Declaration |
| --- | --- |
| From | ``` let CBPeripheralManagerRestoredStateServicesKey: NSString! ``` |
| To | ``` let CBPeripheralManagerRestoredStateServicesKey: String ``` |

Modified CBUUIDCharacteristicAggregateFormatString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicAggregateFormatString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicAggregateFormatString: String ``` |

Modified CBUUIDCharacteristicExtendedPropertiesString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicExtendedPropertiesString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicExtendedPropertiesString: String ``` |

Modified CBUUIDCharacteristicFormatString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicFormatString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicFormatString: String ``` |

Modified CBUUIDCharacteristicUserDescriptionString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDCharacteristicUserDescriptionString: NSString! ``` |
| To | ``` let CBUUIDCharacteristicUserDescriptionString: String ``` |

Modified CBUUIDClientCharacteristicConfigurationString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDClientCharacteristicConfigurationString: NSString! ``` |
| To | ``` let CBUUIDClientCharacteristicConfigurationString: String ``` |

Modified CBUUIDServerCharacteristicConfigurationString

|  | Declaration |
| --- | --- |
| From | ``` let CBUUIDServerCharacteristicConfigurationString: NSString! ``` |
| To | ``` let CBUUIDServerCharacteristicConfigurationString: String ``` |

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
