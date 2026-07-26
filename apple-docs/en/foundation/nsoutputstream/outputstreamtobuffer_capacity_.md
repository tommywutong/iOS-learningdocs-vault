---
title: 'outputStreamToBuffer:capacity:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsoutputstream/outputstreamtobuffer:capacity:'
source_url: 'https://developer.apple.com/documentation/foundation/nsoutputstream/outputstreamtobuffer:capacity:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsoutputstream/outputstreamtobuffer%3Acapacity%3A.json'
content_hash: 'sha256:cb2acfe303edcba1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# outputStreamToBuffer:capacity:

<sub>Type Method</sub>

Creates and returns an initialized output stream that can write to a provided buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) outputStreamToBuffer:(uint8_t *) buffer capacity:(NSUInteger) capacity;
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

- [+ outputStreamToMemory](<../outputstream/tomemory().md>) — Creates and returns an initialized output stream that will write stream data to memory.
- [outputStreamToFileAtPath:append:](outputstreamtofileatpath_append_.md) — Creates and returns an initialized output stream for writing to a specified file.
- [- initToMemory](<../outputstream/init(tomemory_).md>) — Returns an initialized output stream that will write to memory.
- [- initToBuffer:capacity:](<../outputstream/init(tobuffer_capacity_).md>) — Returns an initialized output stream that can write to a provided buffer.
- [- initToFileAtPath:append:](<../outputstream/init(tofileatpath_append_).md>) — Returns an initialized output stream for writing to a specified file.
- [- initWithURL:append:](<../outputstream/init(url_append_)-5soau.md>) — Returns an initialized output stream for writing to a specified URL.
