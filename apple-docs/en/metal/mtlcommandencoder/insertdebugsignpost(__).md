---
title: 'insertDebugSignpost(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandencoder/insertdebugsignpost(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencoder/insertdebugsignpost(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencoder/insertdebugsignpost%28_%3A%29.json'
content_hash: 'sha256:31cb2372989a6b51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandEncoder](../mtlcommandencoder.md)

# insertDebugSignpost(_:)

<sub>Instance Method</sub>

Inserts a debug string into the captured frame data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertDebugSignpost(_ string: String)
```

## Discussion

For more information, see [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Annotating the command buffer with debug information

- [- pushDebugGroup:](<pushdebuggroup(__).md>) — Pushes a specific string onto a stack of debug group strings for the command encoder.
- [- popDebugGroup](<popdebuggroup().md>) — Pops the latest string off of a stack of debug group strings for the command encoder.
