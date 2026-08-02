---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Objective-C/Security.html
archived_at: '2026-07-18T02:53:49.468782Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# Security Changes for Objective-C

### Security

#### CMSEncoder.h

Added [kCMSAttrAppleCodesigningHashAgility](https://developer.apple.com/documentation/security/cmssignedattributes/kcmsattrapplecodesigninghashagility)

#### CSCommon.h

Added [errSecCSBadDiskImageFormat](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsbaddiskimageformat)Added [errSecCSNotAppLike](https://developer.apple.com/documentation/security/errseccsnotapplike)Added [errSecCSUnsupportedDigestAlgorithm](https://developer.apple.com/documentation/security/errseccsunsupporteddigestalgorithm)Added [kSecCodeSignatureHashSHA1](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha1)Added [kSecCodeSignatureHashSHA256](https://developer.apple.com/documentation/security/seccsdigestalgorithm/codesignaturehashsha256)Added [kSecCodeSignatureHashSHA256Truncated](https://developer.apple.com/documentation/security/seccsdigestalgorithm/codesignaturehashsha256truncated)Added [kSecCodeSignatureHashSHA384](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturehashsha384)Added [kSecCodeSignatureNoHash](https://developer.apple.com/documentation/security/seccsdigestalgorithm/kseccodesignaturenohash)Added [SecCSDigestAlgorithm](https://developer.apple.com/documentation/security/seccsdigestalgorithm)

#### cssmapple.h

Added [CSSM_ACL_AUTHORIZATION_INTEGRITY](https://developer.apple.com/documentation/security/cssm_acl_authorization_integrity)Added [CSSM_ACL_AUTHORIZATION_PARTITION_ID](https://developer.apple.com/documentation/security/1434848-anonymous/cssm_acl_authorization_partition_id)Added [CSSM_ACL_SUBJECT_TYPE_PARTITION](https://developer.apple.com/documentation/security/cssm_acl_subject_type_partition)Added [#def CSSM_APPLE_ACL_TAG_INTEGRITY](https://developer.apple.com/documentation/security/cssm_apple_acl_tag_integrity)Added [#def CSSM_APPLE_ACL_TAG_PARTITION_ID](https://developer.apple.com/documentation/security/cssm_apple_acl_tag_partition_id)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_19](https://developer.apple.com/documentation/security/1434766-anonymous/cssm_apple_private_cspdl_code_19)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_20](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_20)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_21](https://developer.apple.com/documentation/security/1434766-anonymous/cssm_apple_private_cspdl_code_21)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_22](https://developer.apple.com/documentation/security/cssm_apple_private_cspdl_code_22)Added [CSSM_APPLE_PRIVATE_CSPDL_CODE_23](https://developer.apple.com/documentation/security/1434766-anonymous/cssm_apple_private_cspdl_code_23)Added [CSSM_APPLEFILEDL_MAKE_BACKUP](https://developer.apple.com/documentation/security/1434707-anonymous/cssm_applefiledl_make_backup)Added [CSSM_APPLEFILEDL_TAKE_FILE_LOCK](https://developer.apple.com/documentation/security/1434707-anonymous/cssm_applefiledl_take_file_lock)Added [CSSM_WORDID_PARTITION](https://developer.apple.com/documentation/security/cssm_wordid_partition)

#### SecAccess.h

Added [kSecACLAuthorizationIntegrity](https://developer.apple.com/documentation/security/ksecaclauthorizationintegrity)Added [kSecACLAuthorizationPartitionID](https://developer.apple.com/documentation/security/ksecaclauthorizationpartitionid)

#### SecCode.h

Added [kSecCodeInfoCdHashes](https://developer.apple.com/documentation/security/kseccodeinfocdhashes)Added [kSecCodeInfoDigestAlgorithms](https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithms)

#### SecStaticCode.h

Added [kSecCSRestrictToAppLike](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsrestricttoapplike)

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
