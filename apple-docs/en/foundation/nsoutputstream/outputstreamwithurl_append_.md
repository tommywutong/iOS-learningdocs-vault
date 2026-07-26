---
title: 'outputStreamWithURL:append:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsoutputstream/outputstreamwithurl:append:'
source_url: 'https://developer.apple.com/documentation/foundation/nsoutputstream/outputstreamwithurl:append:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsoutputstream/outputstreamwithurl%3Aappend%3A.json'
content_hash: 'sha256:bc15f415a762d05a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [OutputStream](../outputstream.md)

# outputStreamWithURL:append:

<sub>Type Method</sub>

Creates and returns an initialized output stream for writing to a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) outputStreamWithURL:(NSURL *) url append:(BOOL) shouldAppend;
```

## Parameters

- `url` — The URL to the file the output stream will write to.

- `shouldAppend` — `YES` if newly written data should be appended to any existing file contents, otherwise `NO`.

## Discussion

The stream must be opened before it can be used.
