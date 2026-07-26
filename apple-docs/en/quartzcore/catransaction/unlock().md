---
title: unlock()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/unlock()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/unlock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/unlock%28%29.json'
content_hash: 'sha256:0cb401685497a00d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# unlock()

<sub>Type Method</sub>

Relinquishes a previously acquired transaction lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func unlock()
```

## See Also

### Managing Concurrency

- [+ lock](<lock().md>) — Attempts to acquire a recursive spin-lock lock, ensuring that returned layer values are valid until unlocked.
