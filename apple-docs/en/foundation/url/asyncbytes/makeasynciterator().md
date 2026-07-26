---
title: makeAsyncIterator()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/asyncbytes/makeasynciterator()
source_url: 'https://developer.apple.com/documentation/foundation/url/asyncbytes/makeasynciterator()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/asyncbytes/makeasynciterator%28%29.json'
content_hash: 'sha256:55bdd33992345064'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [AsyncBytes](../asyncbytes.md)

# makeAsyncIterator()

<sub>Instance Method</sub>

Creates the asynchronous iterator that produces elements of this asynchronous sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeAsyncIterator() -> URL.AsyncBytes.AsyncIterator
```

## Return Value

An instance of the `URL.AsyncBytes.AsyncIterator` type used to produce elements of the asynchronous sequence.

## See Also

### Creating an iterator

- [AsyncIterator](asynciterator.md) — The iterator type that produces elements of this asynchronous sequence.
