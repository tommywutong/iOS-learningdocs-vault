---
title: SecAsn1TemplateChooser
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1templatechooser
source_url: 'https://developer.apple.com/documentation/security/secasn1templatechooser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1templatechooser.json'
content_hash: 'sha256:ebdbccc01794a1b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1TemplateChooser

<sub>Type Alias</sub>

Dynamically provides the sub-template to use during encode or decode.

> [!warning] Deprecated
> SecAsn1 is not supported

<sub>macOS</sub>

```swift
typealias SecAsn1TemplateChooser = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<CChar>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>?
```
