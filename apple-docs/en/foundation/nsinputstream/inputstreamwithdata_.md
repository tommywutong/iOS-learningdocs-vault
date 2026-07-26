---
title: 'inputStreamWithData:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinputstream/inputstreamwithdata:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinputstream/inputstreamwithdata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinputstream/inputstreamwithdata%3A.json'
content_hash: 'sha256:33bd8d9ce6c60559'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# inputStreamWithData:

<sub>Type Method</sub>

Creates and returns an initialized `NSInputStream` object for reading from a given `NSData` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) inputStreamWithData:(NSData *) data;
```

## Parameters

- `data` — The data object from which to read. The contents of `data` are copied.

## Return Value

An initialized `NSInputStream` object for reading from `data`. If `data` is not an NSData object, this method returns `nil`.

## Discussion

The stream must be opened before it can be used.

## See Also

### Related Documentation

- [Stream Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Streams/Streams.html#//apple_ref/doc/uid/10000188i)

### Creating Streams

- [inputStreamWithFileAtPath:](inputstreamwithfileatpath_.md) — Creates and returns an initialized `NSInputStream` object that reads data from the file at a given path.
- [- initWithData:](<../inputstream/init(data_).md>) — Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [- initWithFileAtPath:](<../inputstream/init(fileatpath_).md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [- initWithURL:](<../inputstream/init(url_)-1lfmj.md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.
