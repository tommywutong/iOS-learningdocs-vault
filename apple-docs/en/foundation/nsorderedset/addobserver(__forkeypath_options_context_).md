---
title: 'addObserver(_:forKeyPath:options:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/addobserver(_:forkeypath:options:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/addobserver(_:forkeypath:options:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/addobserver%28_%3Aforkeypath%3Aoptions%3Acontext%3A%29.json'
content_hash: 'sha256:4afd121dfa0f2353'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# addObserver(_:forKeyPath:options:context:)

<sub>Instance Method</sub>

Raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The object to register for KVO notifications.

- `keyPath` — The key path, relative to the array, of the property to observe. This value must not be nil.

- `options` — A combination of [NSKeyValueObservingOptions](../nskeyvalueobservingoptions.md) values that specifies what is included in observation notifications.

- `context` — Arbitrary data that is passed to observer in [observeValue(forKeyPath:of:change:context:)](<../../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>).

## Discussion

`NSOrderedSet` objects are not observable, so this method raises an exception when invoked on an `NSOrderedSet` object. Instead of observing an ordered set, observe the to-many relationship for which the ordered set is the collection of related objects.

## See Also

### Key-Value Observing Support

- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Raises an exception.
