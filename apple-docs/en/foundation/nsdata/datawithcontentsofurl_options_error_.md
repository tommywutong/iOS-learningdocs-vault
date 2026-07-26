---
title: 'dataWithContentsOfURL:options:error:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/datawithcontentsofurl:options:error:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsofurl:options:error:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/datawithcontentsofurl%3Aoptions%3Aerror%3A.json'
content_hash: 'sha256:ae38af34fb5f6e46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# dataWithContentsOfURL:options:error:

<sub>Type Method</sub>

Creates a data object from the data at the provided file URL using specific reading options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithContentsOfURL:(NSURL *) url options:(NSDataReadingOptions) readOptionsMask error:(NSError **) errorPtr;
```

## Parameters

- `url` — The location on disk of the data to read.

- `readOptionsMask` — The mask specifying the options to use when reading the data. For more information, see [ReadingOptions](readingoptions.md).

- `errorPtr` — `nil` if the data is read; otherwise, an error object describing the failure.

## Return Value

A data object that contains the file’s data, or `nil` if the system can’t create one.

## Discussion

> [!important] Important
> As this method runs synchronously and blocks the calling thread until it finishes, don’t invoke it from the main thread. Use file coordination or one of the nonblocking file-related APIs instead.
