---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/GSS.html
archived_at: '2026-07-18T02:56:50.610223Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# GSS Changes for Swift

### GSS

Added [kGSSICAppleSourceApp](https://developer.apple.com/documentation/gss/kgssicapplesourceapp)Added [kGSSICAppleSourceAppAuditToken](https://developer.apple.com/documentation/gss/kgssicapplesourceappaudittoken)Added [kGSSICAppleSourceAppPID](https://developer.apple.com/documentation/gss/kgssicapplesourceapppid)Added [kGSSICAppleSourceAppSigningIdentity](https://developer.apple.com/documentation/gss/kgssicapplesourceappsigningidentity)Added [kGSSICCreateNewCredential](https://developer.apple.com/documentation/gss/kgssiccreatenewcredential)Added [kGSSICSiteName](https://developer.apple.com/documentation/gss/kgssicsitename)Added [kGSSICVerifyCredentialAcceptorName](https://developer.apple.com/documentation/gss/kgssicverifycredentialacceptorname)Modified [gss_aapl_change_password(_: gss_name_t, _: gss_const_OID, _: CFDictionary, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Declaration |
| --- | --- |
| From | ``` func gss_aapl_change_password(_ name: gss_name_t, _ mech: gss_const_OID, _ attributes: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` |
| To | ``` func gss_aapl_change_password(_ name: gss_name_t, _ mech: gss_const_OID, _ attributes: CFDictionary, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` |

Modified [gss_aapl_initial_cred(_: gss_name_t, _: gss_const_OID, _: CFDictionary?, _: UnsafeMutablePointer<gss_cred_id_t>, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32](https://developer.apple.com/documentation/gss/1411909-gss_aapl_initial_cred)

|  | Declaration |
| --- | --- |
| From | ``` func gss_aapl_initial_cred(_ desired_name: gss_name_t, _ desired_mech: gss_const_OID, _ attributes: CFDictionary!, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` |
| To | ``` func gss_aapl_initial_cred(_ desired_name: gss_name_t, _ desired_mech: gss_const_OID, _ attributes: CFDictionary?, _ output_cred_handle: UnsafeMutablePointer<gss_cred_id_t>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32 ``` |

Modified [gss_iter_creds(_: UnsafeMutablePointer<OM_uint32>, _: OM_uint32, _: gss_const_OID, _: (gss_OID, gss_cred_id_t) -> Void) -> OM_uint32](https://developer.apple.com/documentation/gss/1438515-gss_iter_creds)

|  | Declaration |
| --- | --- |
| From | ``` func gss_iter_creds(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ useriter: ((gss_OID, gss_cred_id_t) -> Void)!) -> OM_uint32 ``` |
| To | ``` func gss_iter_creds(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ useriter: (gss_OID, gss_cred_id_t) -> Void) -> OM_uint32 ``` |

Modified [gss_iter_creds_f(_: UnsafeMutablePointer<OM_uint32>, _: OM_uint32, _: gss_const_OID, _: UnsafeMutablePointer<Void>, _: (UnsafeMutablePointer<Void>, gss_OID, gss_cred_id_t) -> Void) -> OM_uint32](https://developer.apple.com/documentation/gss/1438438-gss_iter_creds_f)

|  | Declaration |
| --- | --- |
| From | ``` func gss_iter_creds_f(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ userctx: UnsafeMutablePointer<Void>, _ useriter: CFunctionPointer<((UnsafeMutablePointer<Void>, gss_OID, gss_cred_id_t) -> Void)>) -> OM_uint32 ``` |
| To | ``` func gss_iter_creds_f(_ min_stat: UnsafeMutablePointer<OM_uint32>, _ flags: OM_uint32, _ mech: gss_const_OID, _ userctx: UnsafeMutablePointer<Void>, _ useriter: (UnsafeMutablePointer<Void>, gss_OID, gss_cred_id_t) -> Void) -> OM_uint32 ``` |

Modified [GSSCreateCredentialFromUUID(_: CFUUID) -> gss_cred_id_t](https://developer.apple.com/documentation/gss/1411915-gsscreatecredentialfromuuid)

|  | Declaration |
| --- | --- |
| From | ``` func GSSCreateCredentialFromUUID(_ uuid: CFUUID!) -> gss_cred_id_t ``` |
| To | ``` func GSSCreateCredentialFromUUID(_ uuid: CFUUID) -> gss_cred_id_t ``` |

Modified [GSSCreateError(_: gss_const_OID, _: OM_uint32, _: OM_uint32) -> Unmanaged<CFError>?](https://developer.apple.com/documentation/gss/1411913-gsscreateerror)

|  | Declaration |
| --- | --- |
| From | ``` func GSSCreateError(_ mech: gss_const_OID, _ major_status: OM_uint32, _ minor_status: OM_uint32) -> Unmanaged<CFError>! ``` |
| To | ``` func GSSCreateError(_ mech: gss_const_OID, _ major_status: OM_uint32, _ minor_status: OM_uint32) -> Unmanaged<CFError>? ``` |

Modified [GSSCreateName(_: AnyObject, _: gss_const_OID, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> gss_name_t](https://developer.apple.com/documentation/gss/1411907-gsscreatename)

|  | Declaration |
| --- | --- |
| From | ``` func GSSCreateName(_ name: AnyObject!, _ name_type: gss_const_OID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> gss_name_t ``` |
| To | ``` func GSSCreateName(_ name: AnyObject, _ name_type: gss_const_OID, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> gss_name_t ``` |

Modified [GSSCredentialCopyUUID(_: gss_cred_id_t) -> Unmanaged<CFUUID>?](https://developer.apple.com/documentation/gss/1411905-gsscredentialcopyuuid)

|  | Declaration |
| --- | --- |
| From | ``` func GSSCredentialCopyUUID(_ credential: gss_cred_id_t) -> Unmanaged<CFUUID>! ``` |
| To | ``` func GSSCredentialCopyUUID(_ credential: gss_cred_id_t) -> Unmanaged<CFUUID>? ``` |

Modified [GSSNameCreateDisplayString(_: gss_name_t) -> Unmanaged<CFString>?](https://developer.apple.com/documentation/gss/1411901-gssnamecreatedisplaystring)

|  | Declaration |
| --- | --- |
| From | ``` func GSSNameCreateDisplayString(_ name: gss_name_t) -> Unmanaged<CFString>! ``` |
| To | ``` func GSSNameCreateDisplayString(_ name: gss_name_t) -> Unmanaged<CFString>? ``` |

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
