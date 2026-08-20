---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/NetworkExtension.html
archived_at: '2026-07-18T02:56:27.020478Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# NetworkExtension Changes

## NetworkExtension

Removed NEOnDemandRuleInterfaceType.EthernetAdded NEVPNIKEv2CertificateType [enum]Added NEVPNIKEv2CertificateType.ECDSA256Added NEVPNIKEv2CertificateType.ECDSA384Added NEVPNIKEv2CertificateType.ECDSA521Added NEVPNIKEv2CertificateType.RSAAdded NEVPNIKEv2DiffieHellmanGroup.Group19Added NEVPNIKEv2DiffieHellmanGroup.Group20Added NEVPNIKEv2DiffieHellmanGroup.Group21Added NEVPNIKEv2EncryptionAlgorithm.AlgorithmAES128GCMAdded NEVPNIKEv2EncryptionAlgorithm.AlgorithmAES256GCMAdded NEVPNProtocolIKEv2.certificateTypeModified NEVPNIKEv2DiffieHellmanGroup [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNIKEv2DiffieHellmanGroup : Int {     case Group0     case Group1     case Group2     case Group5     case Group14     case Group15     case Group16     case Group17     case Group18 } ``` |
| To | ``` enum NEVPNIKEv2DiffieHellmanGroup : Int {     case Group0     case Group1     case Group2     case Group5     case Group14     case Group15     case Group16     case Group17     case Group18     case Group19     case Group20     case Group21 } ``` |

Modified NEVPNIKEv2EncryptionAlgorithm [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum NEVPNIKEv2EncryptionAlgorithm : Int {     case AlgorithmDES     case Algorithm3DES     case AlgorithmAES128     case AlgorithmAES256 } ``` |
| To | ``` enum NEVPNIKEv2EncryptionAlgorithm : Int {     case AlgorithmDES     case Algorithm3DES     case AlgorithmAES128     case AlgorithmAES256     case AlgorithmAES128GCM     case AlgorithmAES256GCM } ``` |

Modified NEVPNConfigurationChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NEVPNConfigurationChangeNotification: NSString! ``` |
| To | ``` let NEVPNConfigurationChangeNotification: String ``` |

Modified NEVPNErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let NEVPNErrorDomain: NSString! ``` |
| To | ``` let NEVPNErrorDomain: String ``` |

Modified NEVPNStatusDidChangeNotification

|  | Declaration |
| --- | --- |
| From | ``` let NEVPNStatusDidChangeNotification: NSString! ``` |
| To | ``` let NEVPNStatusDidChangeNotification: String ``` |

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
