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
doc_path: '/documentation/foundation/nsset/removeobserver(_:forkeypath:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/removeobserver(_:forkeypath:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/removeobserver%28_%3Aforkeypath%3Acontext%3A%29.json'
content_hash: 'sha256:65218bff1939a9ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

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

- `context` — Arbitrary data that is passed to `observer` in [observeValue(forKeyPath:of:change:context:)](<../../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>).

## Discussion

`NSSet` objects are not observable, so this method raises an exception when invoked on an `NSSet` object. Instead of observing a set, observe the unordered to-many relationship for which the set is the collection of related objects.

## See Also

### Key-Value Observing

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Raises an exception.
