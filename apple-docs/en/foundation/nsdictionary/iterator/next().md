---
title: next()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdictionary/iterator/next()
source_url: 'https://developer.apple.com/documentation/foundation/nsdictionary/iterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdictionary/iterator/next%28%29.json'
content_hash: 'sha256:8bad6416cbc312c1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSDictionary](../../nsdictionary.md) · [Iterator](../iterator.md)

# next()

<sub>Instance Method</sub>

Returns the next key-value pair of a dictionary object as a tuple.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func next() -> (key: Any, value: Any)?
```

## Discussion

If all key-value pairs have been iterated over, this method returns `nil`.
