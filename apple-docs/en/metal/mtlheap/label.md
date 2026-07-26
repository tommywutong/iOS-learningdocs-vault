---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlheap/label
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/label.json'
content_hash: 'sha256:24bef07dd1e3bac3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# label

<sub>Instance Property</sub>

A string that identifies the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).
