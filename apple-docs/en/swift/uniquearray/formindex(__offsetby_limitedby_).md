---
title: 'formIndex(_:offsetBy:limitedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/formindex(_:offsetby:limitedby:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/formindex(_:offsetby:limitedby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/formindex%28_%3Aoffsetby%3Alimitedby%3A%29.json'
content_hash: 'sha256:a201d9052205dbaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# formIndex(_:offsetBy:limitedBy:)

<sub>Instance Method</sub>

Offsets the given index by the specified distance, but no further than the given limiting index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(_ index: inout UniqueArray<Element>.Index, offsetBy n: inout Int, limitedBy limit: UniqueArray<Element>.Index)
```

## Parameters

- `index` — A valid index of the array. On return, `index` is set to the resulting position.

- `n` — The distance to offset `index`. On return, `n` is set to zero if the operation succeeded without hitting the limit; otherwise, `n` reflects the number of steps that couldn’t be taken.

- `limit` — A valid index of the array to use as a limit. If `n > 0`, a limit that is less than `index` has no effect. Likewise, if `n < 0`, a limit that is greater than `index` has no effect.

## Discussion

If the operation was able to offset `index` by exactly the requested number of steps without hitting `limit`, then on return `n` is set to `0`, and `index` is set to the adjusted index.

If the operation hits the limit before it can take the requested number of steps, then on return `index` is set to `limit`, and `n` is set to the number of steps that couldn’t be taken.

The value passed as `n` must not offset `index` beyond the bounds of the container, unless the index passed as `limit` prevents offsetting beyond those bounds.

> [!note] Note
> To improve performance, this method does not validate that the given index is valid before offseting it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> [!abstract] Complexity
> O(1)
