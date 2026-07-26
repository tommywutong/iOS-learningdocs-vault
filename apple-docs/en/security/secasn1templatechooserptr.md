---
title: SecAsn1TemplateChooserPtr
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/secasn1templatechooserptr
source_url: 'https://developer.apple.com/documentation/security/secasn1templatechooserptr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secasn1templatechooserptr.json'
content_hash: 'sha256:0a93cd2ca9a3b5db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecAsn1TemplateChooserPtr

<sub>Type Alias</sub>

A pointer to the template chooser function.

> [!warning] Deprecated
> SecAsn1 is not supported

<sub>macOS</sub>

```swift
typealias SecAsn1TemplateChooserPtr = (UnsafeMutableRawPointer, DarwinBoolean, UnsafePointer<CChar>, Int, UnsafeMutableRawPointer) -> UnsafePointer<SecAsn1Template>?
```
