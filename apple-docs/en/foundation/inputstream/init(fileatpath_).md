---
title: 'init(fileAtPath:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inputstream/init(fileatpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/inputstream/init(fileatpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inputstream/init%28fileatpath%3A%29.json'
content_hash: 'sha256:f1b39a3bfb6a3eda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# init(fileAtPath:)

<sub>Initializer</sub>

Initializes and returns an `NSInputStream` object that reads data from the file at a given path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(fileAtPath path: String)
```

## Parameters

- `path` — The path to the file.

## Return Value

An initialized `NSInputStream` object that reads data from the file at `path`.

## Discussion

The stream must be opened before it can be used.

## See Also

### Creating Streams

- [- initWithData:](<init(data_).md>) — Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.
- [- initWithURL:](<init(url_)-1lfmj.md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.
