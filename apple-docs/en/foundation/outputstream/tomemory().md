---
title: toMemory()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/outputstream/tomemory()
source_url: 'https://developer.apple.com/documentation/foundation/outputstream/tomemory()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/outputstream/tomemory%28%29.json'
content_hash: 'sha256:7cce5df8988ad7c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# toMemory()

<sub>Type Method</sub>

Creates and returns an initialized output stream that will write stream data to memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func toMemory() -> Self
```

## Return Value

An initialized output stream that will write stream data to memory.

## Discussion

The stream must be opened before it can be used.

You retrieve the contents of the memory stream by sending the message [- propertyForKey:](<../stream/property(forkey_).md>) to the receiver with an argument of `NSStreamDataWrittenToMemoryStreamKey`.

## See Also

### Related Documentation

- [Stream Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)

### Creating Streams

- [- initToMemory](<init(tomemory_).md>) — Returns an initialized output stream that will write to memory.
- [- initToBuffer:capacity:](<init(tobuffer_capacity_).md>) — Returns an initialized output stream that can write to a provided buffer.
- [- initToFileAtPath:append:](<init(tofileatpath_append_).md>) — Returns an initialized output stream for writing to a specified file.
- [- initWithURL:append:](<init(url_append_)-5soau.md>) — Returns an initialized output stream for writing to a specified URL.
