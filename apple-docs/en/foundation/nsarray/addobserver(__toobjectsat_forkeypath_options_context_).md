---
title: 'addObserver(_:toObjectsAt:forKeyPath:options:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/addobserver(_:toobjectsat:forkeypath:options:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/addobserver(_:toobjectsat:forkeypath:options:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/addobserver%28_%3Atoobjectsat%3Aforkeypath%3Aoptions%3Acontext%3A%29.json'
content_hash: 'sha256:701a98cab161d65e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# addObserver(_:toObjectsAt:forKeyPath:options:context:)

<sub>Instance Method</sub>

Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addObserver(_ observer: NSObject, toObjectsAt indexes: IndexSet, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The observer.

- `indexes` — The index set.

- `keyPath` — The key path, relative to the array, to be observed.

- `options` — The options to be included in the notification.

- `context` — The context passed to the notifications.

## Discussion

The `options` determine what is included in the notifications, and the `context` is passed in the notifications.

This is not merely a convenience method; invoking this method is potentially much faster than repeatedly invoking [addObserver(_:forKeyPath:options:context:)](<../../objectivec/nsobject-swift.class/addobserver(__forkeypath_options_context_).md>).

## See Also

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Raises an exception.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:context:](<removeobserver(__fromobjectsat_forkeypath_context_).md>) — Raises an exception.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:](<removeobserver(__fromobjectsat_forkeypath_).md>) — Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.
