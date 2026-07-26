---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibrary/label
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/label.json'
content_hash: 'sha256:c1e13dce3cb65901'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# label

<sub>Instance Property</sub>

A string that identifies the library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the library

- [device](device.md) — The Metal device object that created the library.
