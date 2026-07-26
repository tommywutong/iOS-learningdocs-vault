---
title: lock()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/lock()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/lock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/lock%28%29.json'
content_hash: 'sha256:bf6669a1c6e52a45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# lock()

<sub>Type Method</sub>

Attempts to acquire a recursive spin-lock lock, ensuring that returned layer values are valid until unlocked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func lock()
```

## Discussion

Core Animation uses a data model that promises not to corrupt the internal data structures when called from multiple threads concurrently, but not that data returned is still valid if the property was valid on another thread. By locking during a transaction you can ensure data that is read, modified, and set is correctly managed.

## See Also

### Managing Concurrency

- [+ unlock](<unlock().md>) — Relinquishes a previously acquired transaction lock.
