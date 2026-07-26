---
title: 'addSharedObserver(_:forKey:options:context:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyvaluesharedobservers/addsharedobserver(_:forkey:options:context:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluesharedobservers/addsharedobserver(_:forkey:options:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluesharedobservers/addsharedobserver%28_%3Aforkey%3Aoptions%3Acontext%3A%29.json'
content_hash: 'sha256:5f5657da5067403b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueSharedObservers](../nskeyvaluesharedobservers.md)

# addSharedObserver(_:forKey:options:context:)

<sub>Instance Method</sub>

Add a new observer to the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addSharedObserver(_ observer: NSObject, forKey key: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

## Parameters

- `observer` — The observer object to register for KVO notifications. The observer must implement the key-value observing method `observeValue: forKeyPath: of: change: context:`

- `key` — Key of the property being observed. This cannot be a nested key path or a computed property

- `options` — A combination of NSKeyValueObservingOptions values that specify what is included in observation notifications. For possible values see NSKeyValueObservingOptions.

- `context` — Arbitrary data which is passed to the observer object

## Discussion

This method works like `-[NSObject addObserver: forKey: options: context:]`, but observations on nested and computed properties are disallowed. Observers are not registered until `setSharedObservers` is called on the observable.
