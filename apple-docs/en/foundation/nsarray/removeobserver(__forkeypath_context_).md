---
title: 'removeObserver(_:forKeyPath:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/removeobserver(_:forkeypath:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/removeobserver(_:forkeypath:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/removeobserver%28_%3Aforkeypath%3Acontext%3A%29.json'
content_hash: 'sha256:f28b93e602495ddc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# removeObserver(_:forKeyPath:context:)

<sub>Instance Method</sub>

Raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The object to remove as an observer.

- `keyPath` — A key-path, relative to the set, for which `observer` is registered to receive KVO change notifications. This value must not be `nil`.

- `context` — The context passed to the notifications.

## Discussion

`NSArray` objects are not observable, so this method raises an exception when invoked on an `NSArray` object. Instead of observing a array, observe the ordered to-many relationship for which the array is the collection of related objects.

## See Also

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Raises an exception.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:context:](<removeobserver(__fromobjectsat_forkeypath_context_).md>) — Raises an exception.
- [- addObserver:toObjectsAtIndexes:forKeyPath:options:context:](<addobserver(__toobjectsat_forkeypath_options_context_).md>) — Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:](<removeobserver(__fromobjectsat_forkeypath_).md>) — Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.
