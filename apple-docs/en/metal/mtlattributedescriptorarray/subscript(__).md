---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlattributedescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlattributedescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlattributedescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:cbd694bf98d7f8a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLAttributeDescriptorArray](../mtlattributedescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the state of the specified attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(index: Int) -> MTLAttributeDescriptor! { get set }
```

## Parameters

- `index` — A specified index in the argument table bindings.

## Return Value

The attribute descriptor for data bound at this index.
