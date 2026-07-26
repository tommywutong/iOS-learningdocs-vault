---
title: kSecEncodeLineLengthAttribute
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksecencodelinelengthattribute
source_url: 'https://developer.apple.com/documentation/security/ksecencodelinelengthattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecencodelinelengthattribute.json'
content_hash: 'sha256:f2a933191c311480'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecEncodeLineLengthAttribute

<sub>Global Variable</sub>

The length of encoded Base32 or Base64 lines.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecEncodeLineLengthAttribute: CFString
```

## Discussion

Some systems can’t handle excessively long lines, or may be defined to limit lines to specific lengths (for example RFC1421 - 64, and RFC2045 - 76).

The corresponding value may be set to any positive value using a [CFNumber](../corefoundation/cfnumber.md) to limit to a specific length (values smaller then X for Base32 or Y for Base64 are assume to be X or Y), or to zero for no specific limit. Either of the string constants [kSecLineLength64](kseclinelength64.md) (RFC1421), or [kSecLineLength76](kseclinelength76.md) (RFC2045) may be used to set line lengths of 64 or 76 bytes.
