---
title: 'insertDebugSignpost(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commandencoder/insertdebugsignpost(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandencoder/insertdebugsignpost(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandencoder/insertdebugsignpost%28_%3A%29.json'
content_hash: 'sha256:6b48a2e034b4abec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandEncoder](../mtl4commandencoder.md)

# insertDebugSignpost(_:)

<sub>Instance Method</sub>

Inserts a debug string into the frame data to aid debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertDebugSignpost(_ string: String)
```

## Parameters

- `string` — The debug string to insert as a signpost.

## Discussion

Calling this method doesn’t change any behaviors, but can be useful for debugging purposes.
