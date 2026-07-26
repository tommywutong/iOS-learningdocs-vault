---
title: 'add(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableindexset/add(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableindexset/add(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableindexset/add%28in%3A%29.json'
content_hash: 'sha256:df4069306913b7fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableIndexSet](../nsmutableindexset.md)

# add(in:)

<sub>Instance Method</sub>

Adds the indexes in an index range to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(in range: NSRange)
```

## Parameters

- `range` — Index range to add. Must be in the range `0 .. NSNotFound - 1`.

## Discussion

This method raises an [NSRangeException](../nsexceptionname/rangeexception.md) when `range` would add an index that exceeds the maximum allowed value for unsigned integers.

## See Also

### Adding Indexes

- [- addIndex:](<add(__)-6dtkj.md>) — Adds an index  to the receiver.
- [- addIndexes:](<add(__)-6zmti.md>) — Adds the indexes in an index set to the receiver.
