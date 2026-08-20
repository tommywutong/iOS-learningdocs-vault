---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/AudioVideoBridging.html
archived_at: '2026-07-15T07:34:44.832754Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# AudioVideoBridging Changes

## AudioVideoBridging

AVB17221ACMPMessage.hAdded AVB17221ACMPMessage.vlanIDAVB17221EntityDiscovery.hModified -[AVB17221EntityDiscovery initWithInterfaceName:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithInterfaceName:(NSString *)anInterfaceName ``` |
| To | ``` - (instancetype)initWithInterfaceName:(NSString *)anInterfaceName ``` |

AVB1722ControlInterface.hModified -[AVB1722ControlInterface initWithInterfaceName:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithInterfaceName:(NSString *)anInterfaceName ``` |
| To | ``` - (instancetype)initWithInterfaceName:(NSString *)anInterfaceName ``` |

AVBCentralManager.h (Added)Added AVBCentralManagerAdded -[AVBCentralManager didAddInterface:]Added -[AVBCentralManager didRemoveInterface:]Added +[AVBCentralManager nextAvailableDynamicEntityID]Added +[AVBCentralManager nextAvailableDynamicEntityModelID]Added +[AVBCentralManager releaseDynamicEntityID:]Added +[AVBCentralManager releaseDynamicEntityModelID:]Added -[AVBCentralManager startControllerMatching]Added -[AVBCentralManager streamingEnabledInterfacesOnly]Added AVBNullEUI64AVBConstants.hRemoved AVB17221AEMCommandTypeAuthenticateGetKeyCountAdded AVB17221ACMPFlagsEncryptedPDUAdded AVB17221ACMPFlagsStreamingTalkerFailedAdded AVB17221ACMPFlagsSupportsEncryptedAdded AVB17221AEMCommandTypeAuthenticateAddKeyToChainAdded AVB17221AEMCommandTypeAuthenticateAddTokenAdded AVB17221AEMCommandTypeAuthenticateDeleteKeyFromChainAdded AVB17221AEMCommandTypeAuthenticateDeleteTokenAdded AVB17221AEMCommandTypeAuthenticateGetIdentityAdded AVB17221AEMCommandTypeAuthenticateGetKeyListAdded AVB17221AEMCommandTypeAuthenticateGetKeychainListAdded AVB17221AEMCommandTypeDisableStreamEncryptionAdded AVB17221AEMCommandTypeDisableTransportSecurityAdded AVB17221AEMCommandTypeEnableStreamEncryptionAdded AVB17221AEMCommandTypeEnableTransportSecurityAdded AVB17221AEMCommandTypeGetMemoryObjectLengthAdded AVB17221AEMCommandTypeGetStreamBackupAdded AVB17221AEMCommandTypeSetMemoryObjectLengthAdded AVB17221AEMCommandTypeSetStreamBackupModified AVB17221AECPStatusAddressAccessAddressTooHigh

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified AVB17221AECPStatusAddressAccessAddressTooLow

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

AVBInterface.hModified -[AVBInterface initWithInterfaceName:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithInterfaceName:(NSString *)anInterfaceName ``` |
| To | ``` - (instancetype)initWithInterfaceName:(NSString *)anInterfaceName ``` |

AVBMACAddress.hModified -[AVBMACAddress initWithBytes:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithBytes:(uint8_t *)bytes ``` |
| To | ``` - (instancetype)initWithBytes:(uint8_t *)bytes ``` |

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
