---
title: 'init(toFileAtPath:append:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/outputstream/init(tofileatpath:append:)'
source_url: 'https://developer.apple.com/documentation/foundation/outputstream/init(tofileatpath:append:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream/init%28tofileatpath%3Aappend%3A%29.json'
content_hash: 'sha256:5ea1a7df52d4864c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# init(toFileAtPath:append:)

<sub>Initializer</sub>

Returns an initialized output stream for writing to a specified file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(toFileAtPath path: String, append shouldAppend: Bool)
```

## Parameters

- `path` — The path to the file the output stream will write to.

- `shouldAppend` — [true](../../swift/true.md) if newly written data should be appended to any existing file contents, otherwise [false](../../swift/false.md).

## Return Value

An initialized output stream that can write to `path`.

## Discussion

The stream must be opened before it can be used.

## See Also

### Creating Streams

- [+ outputStreamToMemory](<tomemory().md>) — Creates and returns an initialized output stream that will write stream data to memory.
- [- initToMemory](<init(tomemory_).md>) — Returns an initialized output stream that will write to memory.
- [- initToBuffer:capacity:](<init(tobuffer_capacity_).md>) — Returns an initialized output stream that can write to a provided buffer.
- [- initWithURL:append:](<init(url_append_)-5soau.md>) — Returns an initialized output stream for writing to a specified URL.
