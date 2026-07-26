---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlargumentencoder/label
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/label.json'
content_hash: 'sha256:7324db9ec4084a47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# label

<sub>Instance Property</sub>

A string that identifies the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the argument encoder

- [device](device.md) — The device object that created the argument encoder.
