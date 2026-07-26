---
title: 'addObserver(_:forKeyPath:options:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/addobserver(_:forkeypath:options:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/addobserver(_:forkeypath:options:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/addobserver%28_%3Aforkeypath%3Aoptions%3Acontext%3A%29.json'
content_hash: 'sha256:c4f61b919b964645'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# addObserver(_:forKeyPath:options:context:)

<sub>Instance Method</sub>

Raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The object to register for KVO notifications. The observer must implement the key-value observing method [observeValue(forKeyPath:of:change:context:)](<../../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>).

- `keyPath` — The key path, relative to the array, of the property to observe. This value must not be `nil`.

- `options` — A combination of [NSKeyValueObservingOptions](../nskeyvalueobservingoptions.md) values that specifies what is included in observation notifications.

- `context` — Arbitrary data that is passed to `observer` in [observeValue(forKeyPath:of:change:context:)](<../../objectivec/nsobject-swift.class/observevalue(forkeypath_of_change_context_).md>).

## Discussion

`NSArray` objects are not observable, so this method raises an exception when invoked on an `NSArray` object. Instead of observing an array, observe the to-many relationship for which the array is the collection of related objects.

## See Also

### Key-Value Observing

- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — Raises an exception.
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — Raises an exception.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:context:](<removeobserver(__fromobjectsat_forkeypath_context_).md>) — Raises an exception.
- [- addObserver:toObjectsAtIndexes:forKeyPath:options:context:](<addobserver(__toobjectsat_forkeypath_options_context_).md>) — Registers an observer to receive key value observer notifications for the specified key-path relative to the objects at the indexes.
- [- removeObserver:fromObjectsAtIndexes:forKeyPath:](<removeobserver(__fromobjectsat_forkeypath_).md>) — Removes `anObserver` from all key value observer notifications associated with the specified `keyPath` relative to the array’s objects at `indexes`.
