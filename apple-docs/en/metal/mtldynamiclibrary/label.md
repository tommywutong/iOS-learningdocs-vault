---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldynamiclibrary/label
source_url: 'https://developer.apple.com/documentation/metal/mtldynamiclibrary/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldynamiclibrary/label.json'
content_hash: 'sha256:fb5f391468415a24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDynamicLibrary](../mtldynamiclibrary.md)

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

- [device](device.md) — The Metal device object that created the dynamic library.
- [installName](installname.md) — A file path for this dynamic library.
