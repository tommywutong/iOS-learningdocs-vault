---
title: Keychain Item Attribute Constants For Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/keychain-item-attribute-constants-for-keys
source_url: 'https://developer.apple.com/documentation/security/keychain-item-attribute-constants-for-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/keychain-item-attribute-constants-for-keys.json'
content_hash: 'sha256:8b3343b4b27a4955'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Keychain items](keychain-items.md)

# Keychain Item Attribute Constants For Keys

<sub>API Collection</sub>

Specifies the attributes for a key item in a keychain.

## Overview

For attributes for items other than keys, see [SecItemAttr](secitemattr.md).

## Topics

### Constants

- [kSecKeyKeyClass](kseckeykeyclass.md) — Type uint32 (`CSSM_KEYCLASS`); value is one of `CSSM_KEYCLASS_PUBLIC_KEY`, `CSSM_KEYCLASS_PRIVATE_KEY` or `CSSM_KEYCLASS_SESSION_KEY`.
- [kSecKeyPrintName](kseckeyprintname.md) — Type blob; human readable name of the key. Same as `kSecLabelItemAttr` for typical keychain items.
- [kSecKeyAlias](kseckeyalias.md) — Type blob; currently unused.
- [kSecKeyPermanent](kseckeypermanent.md) — Type uint32; value is nonzero. This key is permanent (stored in some keychain) and is always `1`.
- [kSecKeyPrivate](kseckeyprivate.md) — Type uint32; value is nonzero. This key is protected by a user login, a password, or both.
- [kSecKeyModifiable](kseckeymodifiable.md) — Type uint32; value is nonzero. Attributes of this key can be modified.
- [kSecKeyLabel](kseckeylabel.md)
- [kSecKeyApplicationTag](kseckeyapplicationtag.md) — Type blob; currently unused.
- [kSecKeyKeyCreator](kseckeykeycreator.md) — Type data. The data points to a `CSSM_GUID` structure representing the module ID of the CSP owning this key.
- [kSecKeyKeyType](kseckeykeytype.md) — Type uint32; value is a CSSM algorithm (`CSSM_ALGORITHMS`) representing the algorithm associated with this key.
- [kSecKeyKeySizeInBits](kseckeykeysizeinbits.md) — Type uint32; value is the number of bits in this key.
- [kSecKeyEffectiveKeySize](kseckeyeffectivekeysize.md) — Type uint32; value is the effective number of bits in this key.  For example, a DES key has a key size in bits (`kSecKeyKeySizeInBits`) of 64 but a value for `kSecKeyEffectiveKeySize` of 56.
- [kSecKeyStartDate](kseckeystartdate.md) — Type `CSSM_DATE`.  Earliest date at which this key may be used.  If the value is all zeros or not present, no restriction applies.
- [kSecKeyEndDate](kseckeyenddate.md) — Type `CSSM_DATE`.  Latest date at which this key may be used.  If the value is all zeros or not present, no restriction applies.
- [kSecKeySensitive](kseckeysensitive.md) — Type uint32; value is nonzero. This key cannot be wrapped with `CSSM_ALGID_NONE`.
- [kSecKeyAlwaysSensitive](kseckeyalwayssensitive.md) — Type uint32; value is nonzero. This key has always been marked sensitive.
- [kSecKeyExtractable](kseckeyextractable.md) — Type uint32; value is nonzero. This key can be wrapped.
- [kSecKeyNeverExtractable](kseckeyneverextractable.md) — Type uint32; value is nonzero. This key was never marked extractable.
- [kSecKeyEncrypt](kseckeyencrypt.md) — Type uint32; value is nonzero. This key can be used in an encrypt operation.
- [kSecKeyDecrypt](kseckeydecrypt.md) — Type uint32; value is nonzero. This key can be used in a decrypt operation.
- [kSecKeyDerive](kseckeyderive.md) — Type uint32; value is nonzero. This key can be used in a key derivation operation.
- [kSecKeySign](kseckeysign.md) — Type uint32, value is nonzero. This key can be used in a sign operation.
- [kSecKeyVerify](kseckeyverify.md) — Type uint32, value is nonzero. This key can be used in a verify operation.
- [kSecKeySignRecover](kseckeysignrecover.md) — Type uint32.
- [kSecKeyVerifyRecover](kseckeyverifyrecover.md) — Type uint32. This key can unwrap other keys.
- [kSecKeyWrap](kseckeywrap.md) — Type uint32; value is nonzero. This key can wrap other keys.
- [kSecKeyUnwrap](kseckeyunwrap.md) — Type uint32; value is nonzero. This key can unwrap other keys.
