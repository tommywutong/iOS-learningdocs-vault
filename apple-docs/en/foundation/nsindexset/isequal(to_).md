---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsindexset/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsindexset/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexset/isequal%28to%3A%29.json'
content_hash: 'sha256:7799e6e5c15b46f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSIndexSet](../nsindexset.md)

# isEqual(to:)

<sub>Instance Method</sub>

Indicates whether the indexes in the receiving index set are the same indexes contained in another index set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to indexSet: IndexSet) -> Bool
```

## Parameters

- `indexSet` — Index set being inquired about.

## Return Value

[true](../../swift/true.md) when the indexes in the receiving index set are the same indexes `indexSet` contains, [false](../../swift/false.md) otherwise.
