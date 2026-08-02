---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/GSS.html
archived_at: '2026-07-18T02:56:13.247098Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# GSS Changes

## GSS

Modified GSSCreateCredentialFromUUID(CFUUID!) -> gss_cred_id_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GSSCreateName(AnyObject!, gss_const_OID, UnsafeMutablePointer<Unmanaged<CFError>?>) -> gss_name_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GSSCredentialCopyName(gss_cred_id_t) -> gss_name_t

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GSSCredentialCopyUUID(gss_cred_id_t) -> Unmanaged<CFUUID>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GSSCredentialGetLifetime(gss_cred_id_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GSSNameCreateDisplayString(gss_name_t) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified gss_aapl_change_password(gss_name_t, gss_const_OID, CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified gss_aapl_initial_cred(gss_name_t, gss_const_OID, CFDictionary!, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<Unmanaged<CFError>?>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_accept_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_cred_id_t, gss_buffer_t, gss_channel_bindings_t, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<gss_OID>, gss_buffer_t, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_acquire_cred(UnsafeMutablePointer<OM_uint32>, gss_name_t, OM_uint32, gss_OID_set, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_acquire_cred_with_password(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, OM_uint32, gss_OID_set, gss_cred_usage_t, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_add_buffer_set_member(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_add_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_name_t, gss_OID, gss_cred_usage_t, OM_uint32, OM_uint32, UnsafeMutablePointer<gss_cred_id_t>, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_add_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_canonicalize_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_OID, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_compare_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_name_t, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_context_time(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_create_empty_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_create_empty_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_decapsulate_token(gss_const_buffer_t, gss_const_OID, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_delete_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_destroy_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_display_mech_attr(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_buffer_t, gss_buffer_t, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_display_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t, UnsafeMutablePointer<gss_OID>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_display_status(UnsafeMutablePointer<OM_uint32>, OM_uint32, Int32, gss_OID, UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_duplicate_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_encapsulate_token(gss_const_buffer_t, gss_const_OID, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_export_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_export_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_export_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_get_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_qop_t, gss_buffer_t, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_import_cred(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_import_name(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, gss_const_OID, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_import_sec_context(UnsafeMutablePointer<OM_uint32>, gss_buffer_t, UnsafeMutablePointer<gss_ctx_id_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_indicate_mechs(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_init_sec_context(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, UnsafeMutablePointer<gss_ctx_id_t>, gss_name_t, gss_OID, OM_uint32, OM_uint32, gss_channel_bindings_t, gss_buffer_t, UnsafeMutablePointer<gss_OID>, gss_buffer_t, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_attrs_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_cred(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_usage_t>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_cred_by_mech(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_OID, UnsafeMutablePointer<gss_name_t>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_usage_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_cred_by_oid(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_mechs_for_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_name(UnsafeMutablePointer<OM_uint32>, gss_name_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<gss_OID>, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_names_for_mech(UnsafeMutablePointer<OM_uint32>, gss_const_OID, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_inquire_sec_context_by_oid(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_OID, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_iter_creds(UnsafeMutablePointer<OM_uint32>, OM_uint32, gss_const_OID,((gss_OID, gss_cred_id_t) -> Void)!) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_iter_creds_f(UnsafeMutablePointer<OM_uint32>, OM_uint32, gss_const_OID, UnsafeMutablePointer<Void>, CFunctionPointer<((UnsafeMutablePointer<Void>, gss_OID, gss_cred_id_t) -> Void)>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_krb5_ccache_name(UnsafeMutablePointer<OM_uint32>, UnsafePointer<Int8>, UnsafeMutablePointer<UnsafePointer<Int8>>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_krb5_export_lucid_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, OM_uint32, UnsafeMutablePointer<UnsafeMutablePointer<Void>>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_krb5_free_lucid_sec_context(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<Void>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_krb5_set_allowable_enctypes(UnsafeMutablePointer<OM_uint32>, gss_cred_id_t, OM_uint32, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_oid_equal(gss_const_OID, gss_const_OID) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_oid_to_str(UnsafeMutablePointer<OM_uint32>, gss_OID, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_process_context_token(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_pseudo_random(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t, Int, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_release_buffer(UnsafeMutablePointer<OM_uint32>, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_release_buffer_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_buffer_set_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_release_cred(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_release_name(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_name_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_release_oid_set(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_OID_set>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_set_cred_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_cred_id_t>, gss_OID, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_set_sec_context_option(UnsafeMutablePointer<OM_uint32>, UnsafeMutablePointer<gss_ctx_id_t>, gss_OID, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_test_oid_set_member(UnsafeMutablePointer<OM_uint32>, gss_const_OID, gss_OID_set, UnsafeMutablePointer<Int32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_unwrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<gss_qop_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_userok(gss_name_t, UnsafePointer<Int8>) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified gss_verify_mic(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, gss_buffer_t, gss_buffer_t, UnsafeMutablePointer<gss_qop_t>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_wrap(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, gss_buffer_t, UnsafeMutablePointer<Int32>, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gss_wrap_size_limit(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_qop_t, OM_uint32, UnsafeMutablePointer<OM_uint32>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gsskrb5_extract_authz_data_from_sec_context(UnsafeMutablePointer<OM_uint32>, gss_ctx_id_t, Int32, gss_buffer_t) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified gsskrb5_register_acceptor_identity(UnsafePointer<Int8>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified krb5_gss_register_acceptor_identity(UnsafePointer<Int8>) -> OM_uint32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

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
