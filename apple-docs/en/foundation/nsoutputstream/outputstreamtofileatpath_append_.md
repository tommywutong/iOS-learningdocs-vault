---
title: 'outputStreamToFileAtPath:append:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsoutputstream/outputstreamtofileatpath:append:'
source_url: 'https://developer.apple.com/documentation/foundation/nsoutputstream/outputstreamtofileatpath:append:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsoutputstream/outputstreamtofileatpath%3Aappend%3A.json'
content_hash: 'sha256:d137f43f3c111680'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# outputStreamToFileAtPath:append:

<sub>Type Method</sub>

Creates and returns an initialized output stream for writing to a specified file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) outputStreamToFileAtPath:(NSString *) path append:(BOOL) shouldAppend;
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

- [+ outputStreamToMemory](<../outputstream/tomemory().md>) — Creates and returns an initialized output stream that will write stream data to memory.
- [outputStreamToBuffer:capacity:](outputstreamtobuffer_capacity_.md) — Creates and returns an initialized output stream that can write to a provided buffer.
- [- initToMemory](<../outputstream/init(tomemory_).md>) — Returns an initialized output stream that will write to memory.
- [- initToBuffer:capacity:](<../outputstream/init(tobuffer_capacity_).md>) — Returns an initialized output stream that can write to a provided buffer.
- [- initToFileAtPath:append:](<../outputstream/init(tofileatpath_append_).md>) — Returns an initialized output stream for writing to a specified file.
- [- initWithURL:append:](<../outputstream/init(url_append_)-5soau.md>) — Returns an initialized output stream for writing to a specified URL.
