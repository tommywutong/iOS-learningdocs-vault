---
title: 'init(url:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inputstream/init(url:)-1lfmj'
source_url: 'https://developer.apple.com/documentation/foundation/inputstream/init(url:)-1lfmj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inputstream/init%28url%3A%29-1lfmj.json'
content_hash: 'sha256:26151dd4a47c4119'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# init(url:)

<sub>Initializer</sub>

Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(url: URL)
```

## Parameters

- `url` — The URL to the file.

## Return Value

An initialized `NSInputStream` object that reads data from the file at `url`.

## Discussion

The stream must be opened before it can be used.

## See Also

### Creating Streams

- [- initWithData:](<init(data_).md>) — Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [- initWithFileAtPath:](<init(fileatpath_).md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
