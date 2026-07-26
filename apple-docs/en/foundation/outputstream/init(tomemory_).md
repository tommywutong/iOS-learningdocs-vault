---
title: 'init(toMemory:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/outputstream/init(tomemory:)'
source_url: 'https://developer.apple.com/documentation/foundation/outputstream/init(tomemory:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream/init%28tomemory%3A%29.json'
content_hash: 'sha256:35071474fb6f4afc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# init(toMemory:)

<sub>Initializer</sub>

Returns an initialized output stream that will write to memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(toMemory: ())
```

## Return Value

An initialized output stream that will write stream data to memory.

## Discussion

The stream must be opened before it can be used.

The contents of the memory stream are retrieved by passing the constant `NSStreamDataWrittenToMemoryStreamKey` to [- propertyForKey:](<../stream/property(forkey_).md>).

## See Also

### Creating Streams

- [+ outputStreamToMemory](<tomemory().md>) — Creates and returns an initialized output stream that will write stream data to memory.
- [- initToBuffer:capacity:](<init(tobuffer_capacity_).md>) — Returns an initialized output stream that can write to a provided buffer.
- [- initToFileAtPath:append:](<init(tofileatpath_append_).md>) — Returns an initialized output stream for writing to a specified file.
- [- initWithURL:append:](<init(url_append_)-5soau.md>) — Returns an initialized output stream for writing to a specified URL.
