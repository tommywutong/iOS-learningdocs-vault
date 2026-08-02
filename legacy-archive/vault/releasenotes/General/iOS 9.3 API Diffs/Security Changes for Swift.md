---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/Security.html
archived_at: '2026-07-18T02:57:16.562255Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# Security Changes for Swift

### Security

Modified [SecAccessControl](https://developer.apple.com/documentation/security/secaccesscontrolref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecAccessControlRef | ``` typealias SecAccessControlRef = SecAccessControl ``` |
| To | SecAccessControl | ``` class SecAccessControl { } ``` |

Modified [SecCertificate](https://developer.apple.com/documentation/security/seccertificate)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecCertificateRef | ``` typealias SecCertificateRef = SecCertificate ``` |
| To | SecCertificate | ``` class SecCertificate { } ``` |

Modified [SecIdentity](https://developer.apple.com/documentation/security/secidentityref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecIdentityRef | ``` typealias SecIdentityRef = SecIdentity ``` |
| To | SecIdentity | ``` class SecIdentity { } ``` |

Modified [SecKey](https://developer.apple.com/documentation/security/seckeyref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecKeyRef | ``` typealias SecKeyRef = SecKey ``` |
| To | SecKey | ``` class SecKey { } ``` |

Modified [SecPolicy](https://developer.apple.com/documentation/security/secpolicyref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecPolicyRef | ``` typealias SecPolicyRef = SecPolicy ``` |
| To | SecPolicy | ``` class SecPolicy { } ``` |

Modified [SecTrust](https://developer.apple.com/documentation/security/sectrustref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SecTrustRef | ``` typealias SecTrustRef = SecTrust ``` |
| To | SecTrust | ``` class SecTrust { } ``` |

Modified [SecCertificateCopySubjectSummary(_: SecCertificate) -> CFString?](https://developer.apple.com/documentation/security/1396041-seccertificatecopysubjectsummary)

|  | Declaration |
| --- | --- |
| From | ``` func SecCertificateCopySubjectSummary(_ certificate: SecCertificate) -> CFString ``` |
| To | ``` func SecCertificateCopySubjectSummary(_ certificate: SecCertificate) -> CFString? ``` |

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
