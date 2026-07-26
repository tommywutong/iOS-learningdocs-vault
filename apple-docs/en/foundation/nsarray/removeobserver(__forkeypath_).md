---
title: 'removeObserver(_:forKeyPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/removeobserver(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/removeobserver(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/removeobserver%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:5c327513e30cccda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# removeObserver(_:forKeyPath:)

<sub>Instance Method</sub>

Raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

## Parameters

- `observer` — The object to remove as an observer.

- `keyPath` — A key-path, relative to the array, for which `observer` is registered to receive KVO change notifications. This value must not be `nil`.

## Discussion

`NSArray` objects are not observable, so this method raises an exception when invoked on an `NSArray` object. Instead of observing an array, observe the to-many relationship for which the array is the collection of related objects.

## See Also

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Raises an exception.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:context:](<removeobserver(__fromobjectsat_forkeypath_context_).md>) — Raises an exception.
- [- addObserver:toObjectsAtIndexes:forKeyPath:options:context:](<addobserver(__toobjectsat_forkeypath_options_context_).md>) — Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:](<removeobserver(__fromobjectsat_forkeypath_).md>) — Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.
