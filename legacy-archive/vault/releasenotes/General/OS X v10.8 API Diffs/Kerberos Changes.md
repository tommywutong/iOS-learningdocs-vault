---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/Kerberos.html
archived_at: '2026-07-18T02:54:02.634952Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# Kerberos Changes

## Kerberos

CredentialsCache.hAdded #def cc_deprecatedCredentialsCache2.hModified cred_union

|  | Header |
| --- | --- |
| From | mit-CredentialsCache2.h |
| To | CredentialsCache2.h |

Modified cc_credentials_v5_compat

|  | Header |
| --- | --- |
| From | mit-CredentialsCache2.h |
| To | CredentialsCache2.h |

Modified cc_credentials_v4_compat

|  | Header |
| --- | --- |
| From | mit-CredentialsCache2.h |
| To | CredentialsCache2.h |

mit-krb5.hRemoved mit_krb5_address (no architecture available)Removed mit_krb5_address_compare() (no architecture available)Removed mit_krb5_address_order() (no architecture available)Removed mit_krb5_address_search() (no architecture available)Removed mit_krb5_addrtype (no architecture available)Removed mit_krb5_ap_rep (no architecture available)Removed mit_krb5_ap_rep_enc_part (no architecture available)Removed mit_krb5_ap_req (no architecture available)Removed mit_krb5_auth_context (no architecture available)Removed mit_krb5_authdata (no architecture available)Removed mit_krb5_authdatatype (no architecture available)Removed mit_krb5_authenticator (no architecture available)Removed mit_krb5_boolean (no architecture available)Removed mit_krb5_cc_cursor (no architecture available)Removed mit_krb5_cc_ops (no architecture available)Removed mit_krb5_ccache (no architecture available)Removed mit_krb5_cccol_cursor (no architecture available)Removed mit_krb5_checksum (no architecture available)Removed mit_krb5_checksum_size() (no architecture available)Removed mit_krb5_cksumtype (no architecture available)Removed mit_krb5_cksumtype_to_string() (no architecture available)Removed mit_krb5_const_pointer (no architecture available)Removed mit_krb5_const_principal (no architecture available)Removed mit_krb5_context (no architecture available)Removed mit_krb5_cred (no architecture available)Removed mit_krb5_cred_enc_part (no architecture available)Removed mit_krb5_cred_info (no architecture available)Removed mit_krb5_creds (no architecture available)Removed mit_krb5_data (no architecture available)Removed mit_krb5_deltat (no architecture available)Removed mit_krb5_deltat_to_string() (no architecture available)Removed mit_krb5_enc_data (no architecture available)Removed mit_krb5_enc_kdc_rep_part (no architecture available)Removed mit_krb5_encrypt_block (no architecture available)Removed mit_krb5_enctype (no architecture available)Removed mit_krb5_enctype_to_string() (no architecture available)Removed mit_krb5_error (no architecture available)Removed mit_krb5_error_code() (no architecture available)Removed mit_krb5_error_code (no architecture available)Removed mit_krb5_flags (no architecture available)Removed mit_krb5_get_init_creds_opt (no architecture available)Removed mit_krb5_gic_opt_pa_data (no architecture available)Removed mit_krb5_gic_process_last_req (no architecture available)Removed mit_krb5_int16 (no architecture available)Removed mit_krb5_int32 (no architecture available)Removed mit_krb5_kdc_rep (no architecture available)Removed mit_krb5_kdc_req (no architecture available)Removed mit_krb5_keyblock (no architecture available)Removed mit_krb5_keytab (no architecture available)Removed mit_krb5_keytab_entry (no architecture available)Removed mit_krb5_keyusage (no architecture available)Removed mit_krb5_kt_cursor (no architecture available)Removed mit_krb5_kvno (no architecture available)Removed mit_krb5_last_req_entry (no architecture available)Removed mit_krb5_magic (no architecture available)Removed mit_krb5_msgtype (no architecture available)Removed mit_krb5_octet (no architecture available)Removed mit_krb5_octet_data (no architecture available)Removed mit_krb5_pa_data (no architecture available)Removed mit_krb5_pointer (no architecture available)Removed mit_krb5_preauthtype (no architecture available)Removed mit_krb5_principal (no architecture available)Removed mit_krb5_principal_data (no architecture available)Removed mit_krb5_prompt (no architecture available)Removed mit_krb5_prompt_type (no architecture available)Removed mit_krb5_prompter_fct (no architecture available)Removed mit_krb5_pwd_data (no architecture available)Removed mit_krb5_rcache (no architecture available)Removed mit_krb5_replay_data (no architecture available)Removed mit_krb5_response (no architecture available)Removed mit_krb5_ticket (no architecture available)Removed mit_krb5_ticket_times (no architecture available)Removed mit_krb5_timestamp (no architecture available)Removed mit_krb5_timestamp_to_sfstring() (no architecture available)Removed mit_krb5_timestamp_to_string() (no architecture available)Removed mit_krb5_tkt_authent (no architecture available)Removed mit_krb5_transited (no architecture available)Removed mit_krb5_ui_2 (no architecture available)Removed mit_krb5_ui_4 (no architecture available)Removed mit_krb5_verify_init_creds_opt (no architecture available)Removed mit_passwd_phrase_element (no architecture available)prof_err.hModified #def ERROR_TABLE_BASE_prof

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | prof_err.h |

Modified #def init_prof_err_tbl

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | prof_err.h |

prof_int.hModified #def PROFILE_ITER_SECTIONS_ONLY

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | prof_int.h |

Modified #def PROFILE_ITER_RELATIONS_ONLY

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | prof_int.h |

Modified #def PROFILE_ITER_LIST_SECTION

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | prof_int.h |

profile.hModified #def PROF_NO_PROFILE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_MAGIC_PROFILE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_SECTION_WITH_VALUE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def prof_err_base

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_MAGIC_NODE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_END_OF_SECTIONS

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_SECTION_NOTOP

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_EXISTS

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_NO_SECTION

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_MISSING_OBRACE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_INVALID_SECTION

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_MAGIC_SECTION

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_MAGIC_FILE_DATA

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_TOPSECTION_ITER_NOSUPP

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_BAD_PARENT_PTR

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_BAD_GROUP_LVL

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_ADD_NOT_SECTION

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_NO_RELATION

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_MAGIC_FILE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_READ_ONLY

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_BAD_NAMESET

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_SECTION_SYNTAX

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_BAD_BOOLEAN

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_BAD_INTEGER

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_MAGIC_ITERATOR

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_EINVAL

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_EXTRA_CBRACE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_VERSION

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_BAD_LINK_LIST

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_SET_SECTION_VALUE

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_FAIL_OPEN

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

Modified #def PROF_RELATION_SYNTAX

|  | Header |
| --- | --- |
| From | mit-profile.h |
| To | profile.h |

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
