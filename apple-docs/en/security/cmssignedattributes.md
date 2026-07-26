---
title: CMSSignedAttributes
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/cmssignedattributes
source_url: 'https://developer.apple.com/documentation/security/cmssignedattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmssignedattributes.json'
content_hash: 'sha256:b6145ccaf979ed8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSSignedAttributes

<sub>Structure</sub>

Optional attributes you can add to a signed message.

<sub>Mac Catalyst, macOS</sub>

```swift
struct CMSSignedAttributes
```

## Overview

Use these flags with the [CMSEncoderAddSignedAttributes](<cmsencoderaddsignedattributes(____).md>) method to cause the encoder to add attributes to a signed message that can be interpreted by the recipient. These attributes are not used for unsigned messages.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Attributes

- [kCMSAttrSmimeCapabilities](cmssignedattributes/attrsmimecapabilities.md) — Identify signature, encryption, and digest algorithms supported by the encoder.
- [kCMSAttrSmimeEncryptionKeyPrefs](cmssignedattributes/attrsmimeencryptionkeyprefs.md) — Indicate that the signing certificate included with the message is the preferred one for S/MIME encryption.
- [kCMSAttrSmimeMSEncryptionKeyPrefs](cmssignedattributes/attrsmimemsencryptionkeyprefs.md) — Indicate that the signing certificate included with the message is the preferred one for S/MIME encryption, but using an attribute object identifier (OID) preferred by Microsoft.
- [kCMSAttrSigningTime](cmssignedattributes/attrsigningtime.md) — Include the signing time.
- [kCMSAttrAppleCodesigningHashAgility](cmssignedattributes/attrapplecodesigninghashagility.md) — Include Apple codesigning hash agility.
- [kCMSAttrAppleCodesigningHashAgilityV2](cmssignedattributes/attrapplecodesigninghashagilityv2.md) — Include Apple codesigning hash agility, version 2.
- [kCMSAttrAppleExpirationTime](cmssignedattributes/attrappleexpirationtime.md) — Include the expiration time.

### Initializers

- [init(rawValue:)](<cmssignedattributes/init(rawvalue_).md>) — Initializes a new attributes structure.
