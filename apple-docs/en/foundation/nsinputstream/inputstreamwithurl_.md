---
title: 'inputStreamWithURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsinputstream/inputstreamwithurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsinputstream/inputstreamwithurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsinputstream/inputstreamwithurl%3A.json'
content_hash: 'sha256:88e2f3ccc3f79606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [InputStream](../inputstream.md)

# inputStreamWithURL:

<sub>Type Method</sub>

Creates and returns an initialized `NSInputStream` object that reads data from the file at a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) inputStreamWithURL:(NSURL *) url;
```

## Parameters

- `url` — The URL to the file.

## Discussion

The stream must be opened before it can be used.
