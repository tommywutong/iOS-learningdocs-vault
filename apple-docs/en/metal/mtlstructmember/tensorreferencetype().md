---
title: tensorReferenceType()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructmember/tensorreferencetype()
source_url: 'https://developer.apple.com/documentation/metal/mtlstructmember/tensorreferencetype()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructmember/tensorreferencetype%28%29.json'
content_hash: 'sha256:b744dae668214a7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructMember](../mtlstructmember.md)

# tensorReferenceType()

<sub>Instance Method</sub>

Provides a description of the underlying tensor type when this struct member holds a tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func tensorReferenceType() -> MTLTensorReferenceType?
```

## Return Value

A description of the tensor type that this struct member holds, or `nil` if this struct member doesn’t hold a tensor.
