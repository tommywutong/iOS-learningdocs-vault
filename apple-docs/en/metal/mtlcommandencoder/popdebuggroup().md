---
title: popDebugGroup()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandencoder/popdebuggroup()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandencoder/popdebuggroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandencoder/popdebuggroup%28%29.json'
content_hash: 'sha256:99ac7bd59a8d7ea4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandEncoder](../mtlcommandencoder.md)

# popDebugGroup()

<sub>Instance Method</sub>

Pops the latest string off of a stack of debug group strings for the command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func popDebugGroup()
```

## Discussion

For more information, see [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Annotating the command buffer with debug information

- [- insertDebugSignpost:](<insertdebugsignpost(__).md>) — Inserts a debug string into the captured frame data.
- [- pushDebugGroup:](<pushdebuggroup(__).md>) — Pushes a specific string onto a stack of debug group strings for the command encoder.
