---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlsharedtexturehandle/label
source_url: 'https://developer.apple.com/documentation/metal/mtlsharedtexturehandle/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlsharedtexturehandle/label.json'
content_hash: 'sha256:4410d21399f92ace'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLSharedTextureHandle](../mtlsharedtexturehandle.md)

# label

<sub>Instance Property</sub>

A string that identifies the texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying the shared texture handle

- [device](device.md) — The device object that created the texture.
