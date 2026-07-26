---
title: SecAFPServerSignature
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secafpserversignature
source_url: 'https://developer.apple.com/documentation/security/secafpserversignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secafpserversignature.json'
content_hash: 'sha256:8f3376c882309832'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAFPServerSignature

<sub>Type Alias</sub>

Represents a 16-byte Apple File Protocol server signature block.

> [!warning] Deprecated
> Use internet password items instead of AppleShare password items.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SecAFPServerSignature = (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)
```

## Discussion

> [!important] Important
> This type is deprecated. Use internet password items instead of AppleShare password items.

This type represents a 16-byte Apple File Protocol server signature block. You can use a value of this type with the keychain item attribute constant [kSecSignatureItemAttr](secitemattr/signatureitemattr.md) to specify an Apple File Protocol server signature.
