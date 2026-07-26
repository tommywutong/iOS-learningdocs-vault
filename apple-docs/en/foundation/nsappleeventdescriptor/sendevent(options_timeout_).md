---
title: 'sendEvent(options:timeout:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/sendevent(options:timeout:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/sendevent(options:timeout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/sendevent%28options%3Atimeout%3A%29.json'
content_hash: 'sha256:70126b3eb58a1f52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# sendEvent(options:timeout:)

<sub>Instance Method</sub>

Sends an Apple event.

<sub>macOS</sub>

```swift
func sendEvent(options sendOptions: NSAppleEventDescriptor.SendOptions = [], timeout timeoutInSeconds: TimeInterval) throws -> NSAppleEventDescriptor
```
