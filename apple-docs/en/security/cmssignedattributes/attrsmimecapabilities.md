---
title: attrSmimeCapabilities
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/cmssignedattributes/attrsmimecapabilities
source_url: 'https://developer.apple.com/documentation/security/cmssignedattributes/attrsmimecapabilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmssignedattributes/attrsmimecapabilities.json'
content_hash: 'sha256:b72f7b64e389aa67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [CMSSignedAttributes](../cmssignedattributes.md)

# attrSmimeCapabilities

<sub>Type Property</sub>

Identify signature, encryption, and digest algorithms supported by the encoder.

<sub>Mac Catalyst, macOS</sub>

```swift
static var attrSmimeCapabilities: CMSSignedAttributes { get }
```

## Discussion

Using this attribute doesn’t change the encoding. See [RFC 2311: S/MIME Version 2 Message Specification](https://tools.ietf.org/html/rfc2311) section 2.5.2 for more information about the capabilities attribute.
