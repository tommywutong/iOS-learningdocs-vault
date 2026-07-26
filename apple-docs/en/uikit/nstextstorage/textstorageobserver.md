---
title: textStorageObserver
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/textstorageobserver
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/textstorageobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/textstorageobserver.json'
content_hash: 'sha256:c44114e471a8dc0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# textStorageObserver

<sub>Instance Property</sub>

The observer for the text storage object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var textStorageObserver: (any NSTextStorageObserving)? { get set }
```

## See Also

### Accessing the storage controller

- [NSTextStorageObserving](../nstextstorageobserving.md) — Optional methods that delegates implement to handle editing and transaction processing.
