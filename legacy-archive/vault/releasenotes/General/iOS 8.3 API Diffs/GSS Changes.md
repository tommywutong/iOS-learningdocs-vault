---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/GSS.html
archived_at: '2026-07-18T02:56:25.615095Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# GSS Changes

## GSS

Added gss_OID_desc_struct.init()Added gss_OID_desc_struct.init(length: OM_uint32, elements: UnsafeMutablePointer<Void>)Added gss_OID_set_desc_struct.init()Added gss_OID_set_desc_struct.init(count: Int, elements: gss_OID)Added gss_buffer_desc_struct.init()Added gss_buffer_desc_struct.init(length: Int, value: UnsafeMutablePointer<Void>)Added gss_buffer_set_desc_struct.init()Added gss_buffer_set_desc_struct.init(count: Int, elements: UnsafeMutablePointer<gss_buffer_desc>)Added gss_channel_bindings_struct.init()Added gss_channel_bindings_struct.init(initiator_addrtype: OM_uint32, initiator_address: gss_buffer_desc, acceptor_addrtype: OM_uint32, acceptor_address: gss_buffer_desc, application_data: gss_buffer_desc)Added gss_iov_buffer_desc_struct.init()Added gss_iov_buffer_desc_struct.init(type: OM_uint32, buffer: gss_buffer_desc)Added kGSSChangePasswordNewPasswordAdded kGSSChangePasswordOldPasswordAdded kGSSCredentialUsageAdded kGSSICAppIdentifierACLAdded kGSSICCertificateAdded kGSSICKerberosCacheNameAdded kGSSICLKDCHostnameAdded kGSSICPasswordAdded kGSSICVerifyCredentialAdded kGSS_C_ACCEPTAdded kGSS_C_BOTHAdded kGSS_C_INITIATEModified gss_OID_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_OID_desc_struct {     var length: OM_uint32     var elements: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct gss_OID_desc_struct {     var length: OM_uint32     var elements: UnsafeMutablePointer<Void>     init()     init(length length: OM_uint32, elements elements: UnsafeMutablePointer<Void>) } ``` |

Modified gss_OID_set_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_OID_set_desc_struct {     var count: UInt     var elements: gss_OID } ``` |
| To | ``` struct gss_OID_set_desc_struct {     var count: Int     var elements: gss_OID     init()     init(count count: Int, elements elements: gss_OID) } ``` |

Modified gss_OID_set_desc_struct.count

|  | Declaration |
| --- | --- |
| From | ``` var count: UInt ``` |
| To | ``` var count: Int ``` |

Modified gss_buffer_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_buffer_desc_struct {     var length: UInt     var value: UnsafeMutablePointer<Void> } ``` |
| To | ``` struct gss_buffer_desc_struct {     var length: Int     var value: UnsafeMutablePointer<Void>     init()     init(length length: Int, value value: UnsafeMutablePointer<Void>) } ``` |

Modified gss_buffer_desc_struct.length

|  | Declaration |
| --- | --- |
| From | ``` var length: UInt ``` |
| To | ``` var length: Int ``` |

Modified gss_buffer_set_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_buffer_set_desc_struct {     var count: UInt     var elements: UnsafeMutablePointer<gss_buffer_desc> } ``` |
| To | ``` struct gss_buffer_set_desc_struct {     var count: Int     var elements: UnsafeMutablePointer<gss_buffer_desc>     init()     init(count count: Int, elements elements: UnsafeMutablePointer<gss_buffer_desc>) } ``` |

Modified gss_buffer_set_desc_struct.count

|  | Declaration |
| --- | --- |
| From | ``` var count: UInt ``` |
| To | ``` var count: Int ``` |

Modified gss_channel_bindings_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_channel_bindings_struct {     var initiator_addrtype: OM_uint32     var initiator_address: gss_buffer_desc     var acceptor_addrtype: OM_uint32     var acceptor_address: gss_buffer_desc     var application_data: gss_buffer_desc } ``` |
| To | ``` struct gss_channel_bindings_struct {     var initiator_addrtype: OM_uint32     var initiator_address: gss_buffer_desc     var acceptor_addrtype: OM_uint32     var acceptor_address: gss_buffer_desc     var application_data: gss_buffer_desc     init()     init(initiator_addrtype initiator_addrtype: OM_uint32, initiator_address initiator_address: gss_buffer_desc, acceptor_addrtype acceptor_addrtype: OM_uint32, acceptor_address acceptor_address: gss_buffer_desc, application_data application_data: gss_buffer_desc) } ``` |

Modified gss_iov_buffer_desc_struct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct gss_iov_buffer_desc_struct {     var type: OM_uint32     var buffer: gss_buffer_desc } ``` |
| To | ``` struct gss_iov_buffer_desc_struct {     var type: OM_uint32     var buffer: gss_buffer_desc     init()     init(type type: OM_uint32, buffer buffer: gss_buffer_desc) } ``` |

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
