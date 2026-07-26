---
title: 'readingIntent(with:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfileaccessintent/readingintent(with:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfileaccessintent/readingintent(with:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileaccessintent/readingintent%28with%3Aoptions%3A%29.json'
content_hash: 'sha256:3d4ae6ec7ad2c59c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileAccessIntent](../nsfileaccessintent.md)

# readingIntent(with:options:)

<sub>Type Method</sub>

Returns a file access intent object for reading the given URL with the provided options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func readingIntent(with url: URL, options: NSFileCoordinator.ReadingOptions = []) -> Self
```

## Parameters

- `url` — The URL of the document you intend to read from.

- `options` — The coordinated reading options. For a list of valid values, see [ReadingOptions](../nsfilecoordinator/readingoptions.md) in the [NSFileCoordinator](../nsfilecoordinator.md).

## Return Value

A newly instantiated and configured file access intent object.

## Discussion

When calling a file coordinator’s [- coordinateAccessWithIntents:queue:byAccessor:](<../nsfilecoordinator/coordinate(with_queue_byaccessor_).md>) method, you pass an array of file access intent objects. Each intent object represents a specific read or write operation on a single document or directory. Use `readingIntentWithURL:options:` to create an intent object suitable for reading.

## See Also

### Related Documentation

- [- coordinateAccessWithIntents:queue:byAccessor:](<../nsfilecoordinator/coordinate(with_queue_byaccessor_).md>) — Performs a number of coordinated-read or -write operations asynchronously.

### Creating a File Access Intent

- [+ writingIntentWithURL:options:](<writingintent(with_options_).md>) — Returns a file access intent object for writing to the given URL with the provided options.
