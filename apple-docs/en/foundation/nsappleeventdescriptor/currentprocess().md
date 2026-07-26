---
title: currentProcess()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/currentprocess()
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/currentprocess()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/currentprocess%28%29.json'
content_hash: 'sha256:f8ffe6de2db5ebde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# currentProcess()

<sub>Type Method</sub>

Creates and returns an application address descriptor using the current process.

<sub>macOS</sub>

```swift
class func currentProcess() -> NSAppleEventDescriptor
```

## Discussion

The result is suitable for use as the `targetDescriptor` parameter of `+appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:`.
