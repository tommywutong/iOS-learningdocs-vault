---
title: 'remove(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nscountedset/remove(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nscountedset/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscountedset/remove%28_%3A%29.json'
content_hash: 'sha256:53ce5cd205f5cbdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCountedSet](../nscountedset.md)

# remove(_:)

<sub>Instance Method</sub>

Removes a given object from the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ object: Any)
```

## Parameters

- `object` — The object to remove from the set.

## Discussion

If `object` is present in the set, decrements the count associated with it. If the count is decremented to `0`, `object` is removed from the set. [- removeObject:](<remove(__).md>) does nothing if `object` is not present in the set.

## See Also

### Related Documentation

- [- countForObject:](<count(for_).md>) — Returns the count associated with a given object in the set.

### Adding and Removing Entries

- [- addObject:](<add(__).md>) — Adds a given object to the set.
