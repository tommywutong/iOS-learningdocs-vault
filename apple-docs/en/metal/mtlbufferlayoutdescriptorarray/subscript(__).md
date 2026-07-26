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
doc_path: '/documentation/metal/mtlbufferlayoutdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbufferlayoutdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbufferlayoutdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:ed042633c9691a5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBufferLayoutDescriptorArray](../mtlbufferlayoutdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the state of the specified buffer layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(index: Int) -> MTLBufferLayoutDescriptor! { get set }
```

## Parameters

- `index` — A specified index in the array of buffer layouts.

## Return Value

The buffer layout descriptor for the buffer bound to the given attribute table index.
