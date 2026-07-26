---
title: elementTensorReferenceType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarraytype/elementtensorreferencetype()
source_url: 'https://developer.apple.com/documentation/metal/mtlarraytype/elementtensorreferencetype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarraytype/elementtensorreferencetype%28%29.json'
content_hash: 'sha256:b00e64fcb465a74f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArrayType](../mtlarraytype.md)

# elementTensorReferenceType()

<sub>Instance Method</sub>

Provides a description of the underlying tensor type when this array holds tensors as its elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func elementTensorReferenceType() -> MTLTensorReferenceType?
```

## Return Value

A description of the tensor type that this array holds, or `nil` if this struct member doesn’t hold a tensor.
