---
title: 'inputStreamWithFileAtPath:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinputstream/inputstreamwithfileatpath:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinputstream/inputstreamwithfileatpath:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinputstream/inputstreamwithfileatpath%3A.json'
content_hash: 'sha256:4ad0d7ef4de03eb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# inputStreamWithFileAtPath:

<sub>Type Method</sub>

Creates and returns an initialized `NSInputStream` object that reads data from the file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) inputStreamWithFileAtPath:(NSString *) path;
```

## Parameters

- `path` — The path to the file.

## Return Value

An initialized `NSInputStream` object that reads data from the file at `path`.

## Discussion

The stream must be opened before it can be used.

## See Also

### Creating Streams

- [inputStreamWithData:](inputstreamwithdata_.md) — Creates and returns an initialized `NSInputStream` object for reading from a given `NSData` object.
- [- initWithData:](<../inputstream/init(data_).md>) — Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [- initWithFileAtPath:](<../inputstream/init(fileatpath_).md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [- initWithURL:](<../inputstream/init(url_)-1lfmj.md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.
