---
title: 'removeObserver(_:forKeyPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/removeobserver(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/removeobserver(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/removeobserver%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:a80c71bae309aa8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# removeObserver(_:forKeyPath:)

<sub>Instance Method</sub>

Raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

## Parameters

- `observer` — The object to remove as an observer.

- `keyPath` — A key-path, relative to the set, for which observer is registered to receive KVO change notifications. This value must not be nil.

## Discussion

`NSOrderedSet` objects are not observable, so this method raises an exception when invoked on an `NSOrderedSet` object. Instead of observing an ordered set, observe the to-many relationship for which the ordered set is the collection of related objects.

## See Also

### Key-Value Observing Support

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Raises an exception.
