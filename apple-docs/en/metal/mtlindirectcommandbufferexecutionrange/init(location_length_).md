---
title: 'init(location:length:)'
framework: Metal
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlindirectcommandbufferexecutionrange/init(location:length:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlindirectcommandbufferexecutionrange/init(location:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlindirectcommandbufferexecutionrange/init%28location%3Alength%3A%29.json'
content_hash: 'sha256:a92a393c188788c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIndirectCommandBufferExecutionRange](../mtlindirectcommandbufferexecutionrange.md)

# init(location:length:)

<sub>Initializer</sub>

Initializes an command execution range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(location: UInt32, length: UInt32)
```

## Parameters

- `location` — The start index of the range.

- `length` — The number of items in the range.

## See Also

### Creating a command execution range

- [init()](<init().md>) — Initializes an empty command execution range.
- [MTLIndirectCommandBufferExecutionRangeMake](<../mtlindirectcommandbufferexecutionrangemake(____).md>) — Creates a command execution range.
