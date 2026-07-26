---
title: 'init(bundleIdentifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/init(bundleidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(bundleidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/init%28bundleidentifier%3A%29.json'
content_hash: 'sha256:5acf1022c8068643'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# init(bundleIdentifier:)

<sub>Initializer</sub>

Creates and returns an application address descriptor using the specified bundle identifier.

<sub>macOS</sub>

```swift
init(bundleIdentifier: String)
```

## Discussion

The result is suitable for use as the `targetDescriptor` parameter of `+appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:`.
