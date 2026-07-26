---
title: 'init(url:append:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/outputstream/init(url:append:)-5soau'
source_url: 'https://developer.apple.com/documentation/foundation/outputstream/init(url:append:)-5soau'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream/init%28url%3Aappend%3A%29-5soau.json'
content_hash: 'sha256:9b2b02910026d705'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# init(url:append:)

<sub>Initializer</sub>

Returns an initialized output stream for writing to a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(url: URL, append shouldAppend: Bool)
```

## Parameters

- `url` — The URL to the file the output stream will write to.

- `shouldAppend` — [true](../../swift/true.md) if newly written data should be appended to any existing file contents, otherwise [false](../../swift/false.md).

## Return Value

An initialized output stream that can write to `url`.

## Discussion

The stream must be opened before it can be used.

## See Also

### Creating Streams

- [+ outputStreamToMemory](<tomemory().md>) — Creates and returns an initialized output stream that will write stream data to memory.
- [- initToMemory](<init(tomemory_).md>) — Returns an initialized output stream that will write to memory.
- [- initToBuffer:capacity:](<init(tobuffer_capacity_).md>) — Returns an initialized output stream that can write to a provided buffer.
- [- initToFileAtPath:append:](<init(tofileatpath_append_).md>) — Returns an initialized output stream for writing to a specified file.
