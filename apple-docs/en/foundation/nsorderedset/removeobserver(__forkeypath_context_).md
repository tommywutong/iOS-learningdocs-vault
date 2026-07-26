---
title: 'removeObserver(_:forKeyPath:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/removeobserver(_:forkeypath:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/removeobserver(_:forkeypath:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/removeobserver%28_%3Aforkeypath%3Acontext%3A%29.json'
content_hash: 'sha256:a1a43c091baeb37f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# removeObserver(_:forKeyPath:context:)

<sub>Instance Method</sub>

Raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The object to remove as an observer.

- `keyPath` — A key-path, relative to the set, for which observer is registered to receive KVO change notifications. This value must not be nil.

- `context` — The context passed to the notifications.

## Discussion

`NSOrderedSet` objects are not observable, so this method raises an exception when invoked on an `NSOrderedSet` object. Instead of observing an ordered set, observe the to-many relationship for which the ordered set is the collection of related objects.

## See Also

### Key-Value Observing Support

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Raises an exception.
