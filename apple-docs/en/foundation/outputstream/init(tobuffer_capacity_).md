---
title: 'init(toBuffer:capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/outputstream/init(tobuffer:capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/outputstream/init(tobuffer:capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream/init%28tobuffer%3Acapacity%3A%29.json'
content_hash: 'sha256:8837bfa66812cec0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# init(toBuffer:capacity:)

<sub>Initializer</sub>

Returns an initialized output stream that can write to a provided buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(toBuffer buffer: UnsafeMutablePointer<UInt8>, capacity: Int)
```

## Parameters

- `buffer` — The buffer the output stream will write to.

- `capacity` — The size of the buffer in bytes.

## Return Value

An initialized output stream that can write to `buffer`.

## Discussion

The stream must be opened before it can be used.

When the number of bytes written to `buffer` has reached `capacity`, the stream’s [streamStatus](../stream/streamstatus.md) will return `NSStreamStatusAtEnd`.

## See Also

### Creating Streams

- [+ outputStreamToMemory](<tomemory().md>) — Creates and returns an initialized output stream that will write stream data to memory.
- [- initToMemory](<init(tomemory_).md>) — Returns an initialized output stream that will write to memory.
- [- initToFileAtPath:append:](<init(tofileatpath_append_).md>) — Returns an initialized output stream for writing to a specified file.
- [- initWithURL:append:](<init(url_append_)-5soau.md>) — Returns an initialized output stream for writing to a specified URL.
