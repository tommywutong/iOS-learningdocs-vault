---
title: SecItemAttr
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemattr
source_url: 'https://developer.apple.com/documentation/security/secitemattr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemattr.json'
content_hash: 'sha256:08039429bf1de4a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecItemAttr

<sub>Enumeration</sub>

Specifies a keychain item’s attributes.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecItemAttr
```

## Overview

Not all of these attributes are used for all types of items. Which set of attributes exist for each type of item is documented in the “Data Storage Library Services” chapter of _Common Security: CDSA and CSSM, version 2 (with corrigenda)_ from The Open Group ([http://www.opengroup.org/security/cdsa.htm](http://www.opengroup.org/security/cdsa.htm)) for standard items and in the DL section of the _Security Release Notes_ for Apple-defined item types (if any).

To obtain information about a certificate, use the CDSA Certificate Library (CL) API. To obtain information about a key, use the `SecKeyGetCSSMKey` function and the CDSA Cryptographic Service Provider (CSP) API.

For attributes for keys, see [Keychain Item Attribute Constants For Keys](keychain-item-attribute-constants-for-keys.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecCreationDateItemAttr](secitemattr/creationdateitemattr.md) — Identifies the creation date attribute.
- [kSecModDateItemAttr](secitemattr/moddateitemattr.md) — Identifies the modification date attribute.
- [kSecDescriptionItemAttr](secitemattr/descriptionitemattr.md) — Identifies the description attribute.
- [kSecCommentItemAttr](secitemattr/commentitemattr.md) — Identifies the comment attribute.
- [kSecCreatorItemAttr](secitemattr/creatoritemattr.md) — Identifies the creator attribute.
- [kSecTypeItemAttr](secitemattr/typeitemattr.md) — Identifies the type attribute.
- [kSecScriptCodeItemAttr](secitemattr/scriptcodeitemattr.md) — Identifies the script code attribute.
- [kSecLabelItemAttr](secitemattr/labelitemattr.md) — Identifies the label attribute.
- [kSecInvisibleItemAttr](secitemattr/invisibleitemattr.md) — Identifies the invisible attribute.
- [kSecNegativeItemAttr](secitemattr/negativeitemattr.md) — Identifies the negative attribute.
- [kSecCustomIconItemAttr](secitemattr/customiconitemattr.md) — Identifies the custom icon attribute.
- [kSecAccountItemAttr](secitemattr/accountitemattr.md) — Identifies the account attribute.
- [kSecServiceItemAttr](secitemattr/serviceitemattr.md) — Identifies the service attribute.
- [kSecGenericItemAttr](secitemattr/genericitemattr.md) — Identifies the generic attribute.
- [kSecSecurityDomainItemAttr](secitemattr/securitydomainitemattr.md) — Identifies the security domain attribute.
- [kSecServerItemAttr](secitemattr/serveritemattr.md) — Identifies the server attribute.
- [kSecAuthenticationTypeItemAttr](secitemattr/authenticationtypeitemattr.md) — Identifies the authentication type attribute.
- [kSecPortItemAttr](secitemattr/portitemattr.md) — Identifies the port attribute.
- [kSecPathItemAttr](secitemattr/pathitemattr.md) — Identifies the path attribute.
- [kSecVolumeItemAttr](secitemattr/volumeitemattr.md) — Identifies the volume attribute.
- [kSecAddressItemAttr](secitemattr/addressitemattr.md) — Identifies the address attribute.
- [kSecSignatureItemAttr](secitemattr/signatureitemattr.md) — Identifies the server signature attribute.
- [kSecProtocolItemAttr](secitemattr/protocolitemattr.md) — Identifies the protocol attribute.
- [kSecCertificateType](secitemattr/certificatetype.md) — Indicates a `CSSM_CERT_TYPE` type.
- [kSecCertificateEncoding](secitemattr/certificateencoding.md) — Indicates a `CSSM_CERT_ENCODING` type.
- [kSecCrlType](secitemattr/crltype.md) — Indicates a `CSSM_CRL_TYPE` type.
- [kSecCrlEncoding](secitemattr/crlencoding.md) — Indicates a `CSSM_CRL_ENCODING` type.
- [kSecAlias](secitemattr/alias.md) — Indicates an alias.

### Initializers

- [init(rawValue:)](<secitemattr/init(rawvalue_).md>)
