---
title: 'dataWithContentsOfURL:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/datawithcontentsofurl:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/datawithcontentsofurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/datawithcontentsofurl%3A.json'
content_hash: 'sha256:620f838030ed1af6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# dataWithContentsOfURL:

<sub>Type Method</sub>

Creates a data object from the data at the specified file URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithContentsOfURL:(NSURL *) url;
```

## Parameters

- `url` — The location on disk of the data to read.

## Return Value

A data object that contains the file’s data, or `nil` if the system can’t create one.

## Discussion

> [!important] Important
> As this method runs synchronously and blocks the calling thread until it finishes, don’t invoke it from the main thread. Use file coordination or one of the nonblocking file-related APIs instead.

If you specify a malformed URL or the referenced location doesn’t exist on disk, the initializer fails and returns `nil`. To handle such errors, use `NSData/init(contentsOfURL:options:)-95rht` instead.
