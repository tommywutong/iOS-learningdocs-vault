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
doc_path: '/documentation/foundation/nsset/removeobserver(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/removeobserver(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/removeobserver%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:fe5999e63705a892'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# removeObserver(_:forKeyPath:)

<sub>Instance Method</sub>

Raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

## Parameters

- `observer` — The object to remove as an observer.

- `keyPath` — A key-path, relative to the set, for which `observer` is registered to receive KVO change notifications. This value must not be `nil`.

## Discussion

`NSSet` objects are not observable, so this method raises an exception when invoked on an `NSSet` object. Instead of observing a set, observe the unordered to-many relationship for which the set is the collection of related objects.

## See Also

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Raises an exception.
