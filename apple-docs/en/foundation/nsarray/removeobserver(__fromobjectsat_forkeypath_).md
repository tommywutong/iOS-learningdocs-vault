---
title: 'removeObserver(_:fromObjectsAt:forKeyPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/removeobserver(_:fromobjectsat:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/removeobserver(_:fromobjectsat:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/removeobserver%28_%3Afromobjectsat%3Aforkeypath%3A%29.json'
content_hash: 'sha256:560456f1c25c2fb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# removeObserver(_:fromObjectsAt:forKeyPath:)

<sub>Instance Method</sub>

Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, fromObjectsAt indexes: IndexSet, forKeyPath keyPath: String)
```

## Parameters

- `observer` — The observer.

- `indexes` — The index set.

- `keyPath` — The key path, relative to the array, to be observed.

## Discussion

This is not merely a convenience method; invoking this method is potentially much faster than repeatedly invoking [removeObserver(_:forKeyPath:)](<../../objectivec/nsobject-swift.class/removeobserver(__forkeypath_).md>).

## See Also

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Raises an exception.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:context:](<removeobserver(__fromobjectsat_forkeypath_context_).md>) — Raises an exception.
- [- addObserver:toObjectsAtIndexes:forKeyPath:options:context:](<addobserver(__toobjectsat_forkeypath_options_context_).md>) — Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
