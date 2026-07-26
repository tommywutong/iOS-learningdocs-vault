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
doc_path: /documentation/metal/mtlbinaryarchive/label
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchive/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchive/label.json'
content_hash: 'sha256:990870a4fc034dfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBinaryArchive](../mtlbinaryarchive.md)

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

### Identifying the archive

- [device](device.md) — The Metal device object that created the binary archive.
