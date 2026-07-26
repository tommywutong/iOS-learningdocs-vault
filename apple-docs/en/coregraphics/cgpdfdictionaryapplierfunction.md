---
title: CGPDFDictionaryApplierFunction
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdictionaryapplierfunction
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdictionaryapplierfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdictionaryapplierfunction.json'
content_hash: 'sha256:e2a842ea0fa0d90c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDictionaryApplierFunction

<sub>Type Alias</sub>

Performs custom processing on a key-value pair from a PDF dictionary, using optional contextual information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGPDFDictionaryApplierFunction = (UnsafePointer<CChar>, CGPDFObjectRef, UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `key` — The current key in the dictionary.

- `object` — The value in the dictionary associated with the key.

- `info` — The contextual information that your provided in the `info` parameter in [CGPDFDictionaryApplyFunction](<cgpdfdictionaryapplyfunction(______).md>).

## Discussion

[CGPDFDictionaryApplierFunction](cgpdfdictionaryapplierfunction.md) defines the callback for [CGPDFDictionaryApplyFunction](<cgpdfdictionaryapplyfunction(______).md>), that enumerates all of the entries in the dictionary, calling your custom applier function once for each entry. The current key, its associated value, and the contextual information are passed to your applier function using the `key`, `value`, and `info` parameters respectively.
