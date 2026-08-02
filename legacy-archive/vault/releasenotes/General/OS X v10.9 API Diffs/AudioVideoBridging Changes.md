---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/AudioVideoBridging.html
archived_at: '2026-07-18T02:54:10.902787Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# AudioVideoBridging Changes

## AudioVideoBridging

AVB17221ACMPInterface.hAdded -[AVB17221ACMPInterface removeHandlerForEntityID:]Added -[AVB17221ACMPInterface setHandler:forEntityID:]Modified -[AVB17221ACMPInterface removeHandlerForGUID:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified -[AVB17221ACMPInterface setHandler:forGUID:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVB17221ACMPMessage.hAdded AVB17221ACMPMessage.controllerEntityIDAdded AVB17221ACMPMessage.listenerEntityIDAdded AVB17221ACMPMessage.talkerEntityIDModified AVB17221ACMPMessage.controllerGUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221ACMPMessage.listenerGUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221ACMPMessage.talkerGUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVB17221AECPInterface.hAdded -[AVB17221AECPInterface removeHandlerForEntityID:]Added -[AVB17221AECPInterface setHandler:forEntityID:]Modified -[AVB17221AECPInterface removeHandlerForGUID:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified -[AVB17221AECPInterface setHandler:forGUID:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVB17221AECPMessage.hAdded AVB17221AECPAEMMessage.controllerRequestAdded AVB17221AECPMessage.controllerEntityIDAdded AVB17221AECPMessage.targetEntityIDModified AVB17221AECPAddressAccessTLV.mode

|  | Declaration |
| --- | --- |
| From | @property(assign) uint8_t mode |
| To | @property(assign) AVB17221AECPAddressAccessTLVMode mode |

Modified AVB17221AECPMessage.controllerGUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221AECPMessage.targetGUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVB17221Entity.hAdded AVB17221Entity.entityIDAdded AVB17221Entity.entityModelIDAdded AVB17221Entity.gPTPDomainNumberAdded AVB17221Entity.gPTPGrandmasterIDAdded AVB17221Entity.identifyControlIndexAdded AVB17221Entity.interfaceIndexModified AVB17221Entity.asGrandmasterID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221Entity.guid

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221Entity.modelID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221Entity.vendorID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVB17221EntityDiscovery.hAdded -[AVB17221EntityDiscovery changeEntityWithEntityID:toNewGPTPGrandmasterID:error:]Modified -[AVB17221EntityDiscovery changeEntityWithGUID:toNewASGrandmasterID:error:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified -[AVB17221EntityDiscovery discoverEntity:]

|  | Declaration |
| --- | --- |
| From | - (BOOL)discoverEntity:(uint64_t)entityGUID |
| To | - (BOOL)discoverEntity:(uint64_t)entityID |

AVB17221EntityDiscoveryDelegate.hAdded AVB17221EntityPropertyChangedEntityIDAdded AVB17221EntityPropertyChangedGPTPDomainNumberAdded AVB17221EntityPropertyChangedGPTPGrandmasterIDAdded AVB17221EntityPropertyChangedIdentifyControlIndexAdded AVB17221EntityPropertyChangedInterfaceIndexModified AVB17221EntityPropertyChangedASGrandmasterID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221EntityPropertyChangedGUID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVB1722ControlInterface.hAdded -[AVB1722ControlInterface initWithInterfaceName:]Modified -[AVB1722ControlInterface initWithService:onInterface:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified -[AVB1722ControlInterface initWithService:onInterfaceNamed:]

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVBConstants.hRemoved AVB17221AECPStatusAddressAccessAddressToHighRemoved AVB17221AECPStatusAddressAccessAddressToLowAdded AVB17221ADPEntityCapabilitiesAEMAuthenticationRequiredAdded AVB17221ADPEntityCapabilitiesAEMAuthenticationSupportedAdded AVB17221ADPEntityCapabilitiesAEMIdenitifyControlIndexValidAdded AVB17221ADPEntityCapabilitiesAEMInterfaceIndexValidAdded AVB17221ADPEntityCapabilitiesAEMPersistentAcquireSupportedAdded AVB17221ADPEntityCapabilitiesEFUModeAdded AVB17221ADPEntityCapabilitiesEntityNotReadyAdded AVB17221ADPEntityCapabilitiesGPTPSupportedAdded AVB17221ADPEntityCapabilitiesGeneralControllerIgnoreAdded AVB17221AECPAddressAccessTLVModeAdded AVB17221AECPAddressAccessTLVModeExecuteAdded AVB17221AECPAddressAccessTLVModeReadAdded AVB17221AECPAddressAccessTLVModeWriteAdded AVB17221AECPStatusAddressAccessAddressTooHighAdded AVB17221AECPStatusAddressAccessAddressTooLowModified AVB17221ADPEntityCapabilitiesASSupported

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified AVB17221ADPEntityCapabilitiesDFUMode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

AVBInterface.hAdded +[AVBInterface myEntityID]

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
