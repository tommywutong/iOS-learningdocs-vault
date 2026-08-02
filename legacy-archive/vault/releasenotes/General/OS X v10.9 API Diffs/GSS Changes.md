---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/GSS.html
archived_at: '2026-07-18T02:54:13.481773Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# GSS Changes

## GSS

GSS.hgssapi.hAdded [#def kGSSICAppIdentifierACL](https://developer.apple.com/documentation/gss/kgssicappidentifieracl)Added [#def kGSSICKerberosCacheName](https://developer.apple.com/documentation/gss/kgssickerberoscachename)Added [#def kGSSICLKDCHostname](https://developer.apple.com/documentation/gss/kgssiclkdchostname)Modified [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Header | Declaration |
| --- | --- | --- |
| From | GSS/gssapi.h | OM_uint32 gss_aapl_change_password ( const gss_name_t name, gss_const_OID mech, CFDictionaryRef attributes, CFErrorRef \*error); |
| To | GSS/gssapi_apple.h | OM_uint32 gss_aapl_change_password ( const gss_name_t, gss_const_OID, CFDictionaryRef, CFErrorRef \*); |

gssapi_apple.hAdded [GSSCreateCredentialFromUUID()](https://developer.apple.com/documentation/gss/1411915-gsscreatecredentialfromuuid)Added [GSSCreateName()](https://developer.apple.com/documentation/gss/1411907-gsscreatename)Added [GSSCredentialCopyName()](https://developer.apple.com/documentation/gss/1411911-gsscredentialcopyname)Added [GSSCredentialCopyUUID()](https://developer.apple.com/documentation/gss/1411905-gsscredentialcopyuuid)Added [GSSCredentialGetLifetime()](https://developer.apple.com/documentation/gss/1411899-gsscredentialgetlifetime)Added [GSSNameCreateDisplayString()](https://developer.apple.com/documentation/gss/1411901-gssnamecreatedisplaystring)Modified [gss_aapl_change_password()](https://developer.apple.com/documentation/gss/1411903-gss_aapl_change_password)

|  | Header | Declaration |
| --- | --- | --- |
| From | GSS/gssapi.h | OM_uint32 gss_aapl_change_password ( const gss_name_t name, gss_const_OID mech, CFDictionaryRef attributes, CFErrorRef \*error); |
| To | GSS/gssapi_apple.h | OM_uint32 gss_aapl_change_password ( const gss_name_t, gss_const_OID, CFDictionaryRef, CFErrorRef \*); |

gssapi_oid.hAdded #def GSS_C_CRED_HEIMBASEgssapi_protos.hAdded [gss_userok()](https://developer.apple.com/documentation/gss/1438440-gss_userok)

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
