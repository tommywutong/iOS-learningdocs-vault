---
title: ACL Authorization Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/acl-authorization-keys
source_url: 'https://developer.apple.com/documentation/security/acl-authorization-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/acl-authorization-keys.json'
content_hash: 'sha256:ec85ac5b5914e77f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Access Control Lists](access-control-lists.md)

# ACL Authorization Keys

<sub>API Collection</sub>

The operations an access control list entry applies to.

## Topics

### Constants

- [kSecACLAuthorizationAny](ksecaclauthorizationany.md) — No restrictions. This ACL entry applies to all operations available to the caller.
- [kSecACLAuthorizationLogin](ksecaclauthorizationlogin.md) — Use for a CSP (smart card) login.
- [kSecACLAuthorizationGenKey](ksecaclauthorizationgenkey.md) — Generate a key.
- [kSecACLAuthorizationDelete](ksecaclauthorizationdelete.md) — Delete this item.
- [kSecACLAuthorizationExportWrapped](ksecaclauthorizationexportwrapped.md) — Export a wrapped (that is, encrypted) key. This tag is checked on the key being exported; in addition, the `CSSM_ACL_AUTHORIZATION_ENCRYPT` tag is checked for any key used in the wrapping operation.
- [kSecACLAuthorizationExportClear](ksecaclauthorizationexportclear.md) — Export an unencrypted key.
- [kSecACLAuthorizationImportWrapped](ksecaclauthorizationimportwrapped.md) — Import an encrypted key. This tag is checked on the key being imported; in addition, the `CSSM_ACL_AUTHORIZATION_DECRYPT` tag is checked for any key used in the unwrapping operation.
- [kSecACLAuthorizationImportClear](ksecaclauthorizationimportclear.md) — Import an unencrypted key.
- [kSecACLAuthorizationSign](ksecaclauthorizationsign.md) — Digitally sign data.
- [kSecACLAuthorizationEncrypt](ksecaclauthorizationencrypt.md) — Encrypt data.
- [kSecACLAuthorizationDecrypt](ksecaclauthorizationdecrypt.md) — Decrypt data.
- [kSecACLAuthorizationMAC](ksecaclauthorizationmac.md) — Create or verify a message authentication code.
- [kSecACLAuthorizationDerive](ksecaclauthorizationderive.md) — Derive a new key from another key.
- [kSecACLAuthorizationKeychainCreate](ksecaclauthorizationkeychaincreate.md) — Create a new keychain.
- [kSecACLAuthorizationKeychainDelete](ksecaclauthorizationkeychaindelete.md) — Delete a keychain.
- [kSecACLAuthorizationKeychainItemRead](ksecaclauthorizationkeychainitemread.md) — Read an item from a keychain.
- [kSecACLAuthorizationKeychainItemInsert](ksecaclauthorizationkeychainiteminsert.md) — Insert an item into a keychain.
- [kSecACLAuthorizationKeychainItemModify](ksecaclauthorizationkeychainitemmodify.md) — Modify an item in a keychain.
- [kSecACLAuthorizationKeychainItemDelete](ksecaclauthorizationkeychainitemdelete.md) — Delete an item from a keychain.
- [kSecACLAuthorizationChangeACL](ksecaclauthorizationchangeacl.md) — Change an access control list entry.
- [kSecACLAuthorizationChangeOwner](ksecaclauthorizationchangeowner.md) — For internal system use only. Use the `CSSM_ACL_AUTHORIZATION_CHANGE_ACL` tag for changes to owner ACL entries.
- [kSecACLAuthorizationIntegrity](ksecaclauthorizationintegrity.md)
- [kSecACLAuthorizationPartitionID](ksecaclauthorizationpartitionid.md)
