---
title: 'pushDebugGroup(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandencoder/pushdebuggroup(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencoder/pushdebuggroup(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencoder/pushdebuggroup%28_%3A%29.json'
content_hash: 'sha256:d15d3f8e51e7320e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandEncoder](../mtlcommandencoder.md)

# pushDebugGroup(_:)

<sub>Instance Method</sub>

Pushes a specific string onto a stack of debug group strings for the command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pushDebugGroup(_ string: String)
```

## Discussion

For more information, see [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Annotating the command buffer with debug information

- [- insertDebugSignpost:](<insertdebugsignpost(__).md>) — Inserts a debug string into the captured frame data.
- [- popDebugGroup](<popdebuggroup().md>) — Pops the latest string off of a stack of debug group strings for the command encoder.
