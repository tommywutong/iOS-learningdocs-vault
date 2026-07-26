---
title: 'init(processIdentifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/init(processidentifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(processidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/init%28processidentifier%3A%29.json'
content_hash: 'sha256:19ca422c367bcac8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# init(processIdentifier:)

<sub>Initializer</sub>

Creates and returns an application address descriptor using the specified process identifier.

<sub>macOS</sub>

```swift
init(processIdentifier: pid_t)
```

## Discussion

The result is suitable for use as the `targetDescriptor` parameter of `+appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:`.
