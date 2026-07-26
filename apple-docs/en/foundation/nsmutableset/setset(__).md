---
title: 'setSet(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/setset(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/setset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/setset%28_%3A%29.json'
content_hash: 'sha256:3caee870c266a95c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# setSet(_:)

<sub>Instance Method</sub>

Empties the receiving set, then adds each object contained in another given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setSet(_ otherSet: Set<AnyHashable>)
```

## Parameters

- `otherSet` — The set whose members replace the receiving set’s content.

## See Also

### Combining and recombining sets

- [- unionSet:](<union(__).md>) — Adds each object in another given set to the receiving set, if not present.
- [- minusSet:](<minus(__).md>) — Removes each object in another given set from the receiving set, if present.
- [- intersectSet:](<intersect(__).md>) — Removes from the receiving set each object that isn’t a member of another given set.
