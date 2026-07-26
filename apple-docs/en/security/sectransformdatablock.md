---
title: SecTransformDataBlock
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectransformdatablock
source_url: 'https://developer.apple.com/documentation/security/sectransformdatablock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformdatablock.json'
content_hash: 'sha256:6a4ca0474c061be2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformDataBlock

<sub>Type Alias</sub>

A block used to override the default data handling for a transform.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SecTransformDataBlock = (CFTypeRef) -> Unmanaged<CFTypeRef>?
```

## Parameters

- `data` — The data to be processed. When this block is used to to implement the [kSecTransformActionProcessData](ksectransformactionprocessdata.md) action, the data is the input data that is to be processed into the output data. When this block is used to implement the [kSecTransformActionInternalizeExtraData](ksectransformactioninternalizeextradata.md) action, the data is a [CFDictionary](../corefoundation/cfdictionary.md) that contains the data that needs to be imported.

## Return Value

`NULL` for the [kSecTransformActionInternalizeExtraData](ksectransformactioninternalizeextradata.md) action, the data to be passed to the output attribute for any other action, or a [CFError](../corefoundation/cferror.md) instance on failure.
