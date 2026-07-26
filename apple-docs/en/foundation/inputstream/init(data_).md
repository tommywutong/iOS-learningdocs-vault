---
title: 'init(data:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/inputstream/init(data:)'
source_url: 'https://developer.apple.com/documentation/foundation/inputstream/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/inputstream/init%28data%3A%29.json'
content_hash: 'sha256:4b84461abddaff10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# init(data:)

<sub>Initializer</sub>

Initializes and returns an `NSInputStream` object for reading from a given `NSData` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(data: Data)
```

## Parameters

- `data` — The data object from which to read. The contents of `data` are copied.

## Return Value

An initialized `NSInputStream` object for reading from `data`.

## Discussion

The stream must be opened before it can be used.

## See Also

### Creating Streams

- [- initWithFileAtPath:](<init(fileatpath_).md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given path.
- [- initWithURL:](<init(url_)-1lfmj.md>) — Initializes and returns an `NSInputStream` object that reads data from the file at a given URL.
