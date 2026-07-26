---
title: 'init(applicationURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/init(applicationurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(applicationurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/init%28applicationurl%3A%29.json'
content_hash: 'sha256:c01eedfe0f9b953d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# init(applicationURL:)

<sub>Initializer</sub>

Creates and returns an application address descriptor using the specified application URL.

<sub>macOS</sub>

```swift
init(applicationURL: URL)
```

## Discussion

The result is suitable for use as the `targetDescriptor` parameter of `+appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:`.
