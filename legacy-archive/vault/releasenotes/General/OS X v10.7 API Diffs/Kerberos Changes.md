---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Kerberos.html
archived_at: '2026-07-18T02:54:29.642033Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Kerberos Changes

## Kerberos

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

mit-CredentialsCache2.hModified cred_union

|  | Header |
| --- | --- |
| From | CredentialsCache2.h |
| To | mit-CredentialsCache2.h |

Modified cc_credentials_v5_compat

|  | Header |
| --- | --- |
| From | CredentialsCache2.h |
| To | mit-CredentialsCache2.h |

Modified cc_credentials_v4_compat

|  | Header |
| --- | --- |
| From | CredentialsCache2.h |
| To | mit-CredentialsCache2.h |

mit-krb5.hAdded mit_krb5_address (no architecture available)Added mit_krb5_address_compare() (no architecture available)Added mit_krb5_address_order() (no architecture available)Added mit_krb5_address_search() (no architecture available)Added mit_krb5_addrtype (no architecture available)Added mit_krb5_ap_rep (no architecture available)Added mit_krb5_ap_rep_enc_part (no architecture available)Added mit_krb5_ap_req (no architecture available)Added mit_krb5_auth_context (no architecture available)Added mit_krb5_authdata (no architecture available)Added mit_krb5_authdatatype (no architecture available)Added mit_krb5_authenticator (no architecture available)Added mit_krb5_boolean (no architecture available)Added mit_krb5_cc_cursor (no architecture available)Added mit_krb5_cc_ops (no architecture available)Added mit_krb5_ccache (no architecture available)Added mit_krb5_cccol_cursor (no architecture available)Added mit_krb5_checksum (no architecture available)Added mit_krb5_checksum_size() (no architecture available)Added mit_krb5_cksumtype (no architecture available)Added mit_krb5_cksumtype_to_string() (no architecture available)Added mit_krb5_const_pointer (no architecture available)Added mit_krb5_const_principal (no architecture available)Added mit_krb5_context (no architecture available)Added mit_krb5_cred (no architecture available)Added mit_krb5_cred_enc_part (no architecture available)Added mit_krb5_cred_info (no architecture available)Added mit_krb5_creds (no architecture available)Added mit_krb5_data (no architecture available)Added mit_krb5_deltat (no architecture available)Added mit_krb5_deltat_to_string() (no architecture available)Added mit_krb5_enc_data (no architecture available)Added mit_krb5_enc_kdc_rep_part (no architecture available)Added mit_krb5_encrypt_block (no architecture available)Added mit_krb5_enctype (no architecture available)Added mit_krb5_enctype_to_string() (no architecture available)Added mit_krb5_error (no architecture available)Added mit_krb5_error_code() (no architecture available)Added mit_krb5_error_code (no architecture available)Added mit_krb5_flags (no architecture available)Added mit_krb5_get_init_creds_opt (no architecture available)Added mit_krb5_gic_opt_pa_data (no architecture available)Added mit_krb5_gic_process_last_req (no architecture available)Added mit_krb5_int16 (no architecture available)Added mit_krb5_int32 (no architecture available)Added mit_krb5_kdc_rep (no architecture available)Added mit_krb5_kdc_req (no architecture available)Added mit_krb5_keyblock (no architecture available)Added mit_krb5_keytab (no architecture available)Added mit_krb5_keytab_entry (no architecture available)Added mit_krb5_keyusage (no architecture available)Added mit_krb5_kt_cursor (no architecture available)Added mit_krb5_kvno (no architecture available)Added mit_krb5_last_req_entry (no architecture available)Added mit_krb5_magic (no architecture available)Added mit_krb5_msgtype (no architecture available)Added mit_krb5_octet (no architecture available)Added mit_krb5_octet_data (no architecture available)Added mit_krb5_pa_data (no architecture available)Added mit_krb5_pointer (no architecture available)Added mit_krb5_preauthtype (no architecture available)Added mit_krb5_principal (no architecture available)Added mit_krb5_principal_data (no architecture available)Added mit_krb5_prompt (no architecture available)Added mit_krb5_prompt_type (no architecture available)Added mit_krb5_prompter_fct (no architecture available)Added mit_krb5_pwd_data (no architecture available)Added mit_krb5_rcache (no architecture available)Added mit_krb5_replay_data (no architecture available)Added mit_krb5_response (no architecture available)Added mit_krb5_ticket (no architecture available)Added mit_krb5_ticket_times (no architecture available)Added mit_krb5_timestamp (no architecture available)Added mit_krb5_timestamp_to_sfstring() (no architecture available)Added mit_krb5_timestamp_to_string() (no architecture available)Added mit_krb5_tkt_authent (no architecture available)Added mit_krb5_transited (no architecture available)Added mit_krb5_ui_2 (no architecture available)Added mit_krb5_ui_4 (no architecture available)Added mit_krb5_verify_init_creds_opt (no architecture available)Added mit_passwd_phrase_element (no architecture available)mit-profile.hModified #def PROF_NO_PROFILE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_MAGIC_PROFILE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_SECTION_WITH_VALUE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def prof_err_base

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROFILE_ITER_SECTIONS_ONLY

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_MAGIC_NODE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_END_OF_SECTIONS

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_SECTION_NOTOP

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_EXISTS

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_NO_SECTION

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_MISSING_OBRACE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_INVALID_SECTION

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_MAGIC_SECTION

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_MAGIC_FILE_DATA

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_TOPSECTION_ITER_NOSUPP

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_BAD_PARENT_PTR

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_BAD_GROUP_LVL

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_ADD_NOT_SECTION

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_NO_RELATION

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_MAGIC_FILE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_READ_ONLY

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_BAD_NAMESET

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_SECTION_SYNTAX

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROFILE_ITER_RELATIONS_ONLY

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_BAD_BOOLEAN

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_BAD_INTEGER

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_MAGIC_ITERATOR

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_EINVAL

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_EXTRA_CBRACE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def ERROR_TABLE_BASE_prof

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_VERSION

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROFILE_ITER_LIST_SECTION

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_BAD_LINK_LIST

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_SET_SECTION_VALUE

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_FAIL_OPEN

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def PROF_RELATION_SYNTAX

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

Modified #def init_prof_err_tbl

|  | Header |
| --- | --- |
| From | profile.h |
| To | mit-profile.h |

prof_err.hAdded #def COM_ERR_BINDDOMAIN_profAdded PROF_ADD_NOT_SECTION (no architecture available)Added PROF_BAD_BOOLEAN (no architecture available)Added PROF_BAD_GROUP_LVL (no architecture available)Added PROF_BAD_INTEGER (no architecture available)Added PROF_BAD_LINK_LIST (no architecture available)Added PROF_BAD_NAMESET (no architecture available)Added PROF_BAD_PARENT_PTR (no architecture available)Added PROF_EINVAL (no architecture available)Added PROF_END_OF_SECTIONS (no architecture available)Added PROF_EXISTS (no architecture available)Added PROF_EXTRA_CBRACE (no architecture available)Added PROF_FAIL_OPEN (no architecture available)Added PROF_INVALID_SECTION (no architecture available)Added PROF_MAGIC_FILE (no architecture available)Added PROF_MAGIC_FILE_DATA (no architecture available)Added PROF_MAGIC_ITERATOR (no architecture available)Added PROF_MAGIC_NODE (no architecture available)Added PROF_MAGIC_PROFILE (no architecture available)Added PROF_MAGIC_SECTION (no architecture available)Added PROF_MISSING_OBRACE (no architecture available)Added PROF_NO_PROFILE (no architecture available)Added PROF_NO_RELATION (no architecture available)Added PROF_NO_SECTION (no architecture available)Added PROF_READ_ONLY (no architecture available)Added PROF_RELATION_SYNTAX (no architecture available)Added PROF_SECTION_NOTOP (no architecture available)Added PROF_SECTION_SYNTAX (no architecture available)Added PROF_SECTION_WITH_VALUE (no architecture available)Added PROF_SET_SECTION_VALUE (no architecture available)Added PROF_TOPSECTION_ITER_NOSUPP (no architecture available)Added PROF_VERSION (no architecture available)Added initialize_prof_error_table_r()Added prof_error_numberModified initialize_prof_error_table()

|  | Header |
| --- | --- |
| From | profile.h |
| To | prof_err.h |

prof_int.hAdded #def PROFILE_FILE_DEPRECATED_RWAdded #def PROFILE_FILE_DIRTYAdded #def PROFILE_FILE_HAVE_DATAAdded #def PROFILE_FILE_INVALIDAdded #def PROFILE_FILE_SHAREDAdded #def PROFILE_ITER_FINAL_SEENAdded #def PROFILE_LAST_FILESPECAdded #def PROFILE_SUPPORTS_FOREIGN_NEWLINESAdded prf_data_tAdded prf_file_tAdded prf_magic_tAdded profile_add_node()Added profile_close_file()Added profile_copy()Added profile_create_node()Added profile_delete_node_relation()Added profile_dereference_data()Added profile_dereference_data_locked()Added profile_file_is_writable()Added profile_find_node()Added profile_find_node_name()Added profile_find_node_relation()Added profile_find_node_subsection()Added #def profile_flush_fileAdded profile_flush_file_data()Added profile_flush_file_data_to_buffer()Added profile_flush_file_data_to_file()Added #def profile_flush_file_to_fileAdded profile_free_file()Added profile_free_node()Added profile_get_node_name()Added profile_get_node_parent()Added profile_get_node_value()Added profile_get_value()Added profile_is_node_final()Added profile_lock_global()Added profile_make_node_final()Added profile_make_prf_data()Added profile_node_iterator()Added profile_node_iterator_create()Added profile_node_iterator_free()Added profile_open_file()Added profile_parse_file()Added profile_remove_node()Added profile_rename_node()Added profile_ser_externalize()Added profile_ser_internalize()Added profile_ser_size()Added profile_set_relation_value()Added profile_unlock_global()Added profile_update_file_data()Added profile_verify_node()Added profile_write_tree_file()Added profile_write_tree_to_buffer()

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
