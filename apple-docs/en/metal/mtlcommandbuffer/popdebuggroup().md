---
title: popDebugGroup()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/popdebuggroup()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/popdebuggroup()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/popdebuggroup%28%29.json'
content_hash: 'sha256:da8670d83a8e1411'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# popDebugGroup()

<sub>Instance Method</sub>

Marks the end of a debug group and, if applicable, restores the previous group from a stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func popDebugGroup()
```

## Discussion

Use [- pushDebugGroup:](<pushdebuggroup(__).md>) to group commands within the command buffer, which adds a new group to a stack, effectively nesting a group within any previous group. Call [- popDebugGroup](<popdebuggroup().md>) to mark the end of a group of commands within the command buffer, and restore the previous group, if applicable. You can inspect the group and the commands it contains when viewing the contents of a frame capture with Metal Debugger.

Labels can help you profile and debug your app at runtime with Metal Debugger and other tools. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md) for more information about using labels and other debugging techniques.

## See Also

### Grouping commands within a GPU frame capture

- [- pushDebugGroup:](<pushdebuggroup(__).md>) — Marks the beginning of a debug group and gives it an identifying label, which temporarily replaces the previous group, if applicable.
