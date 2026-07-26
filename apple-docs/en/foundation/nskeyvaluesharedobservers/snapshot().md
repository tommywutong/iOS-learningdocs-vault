---
title: snapshot()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nskeyvaluesharedobservers/snapshot()
source_url: 'https://developer.apple.com/documentation/foundation/nskeyvaluesharedobservers/snapshot()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyvaluesharedobservers/snapshot%28%29.json'
content_hash: 'sha256:9952cdd9d31dc9e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyValueSharedObservers](../nskeyvaluesharedobservers.md)

# snapshot()

<sub>Instance Method</sub>

A momentary snapshot of all observers added to the collection thus far, that can be assigned to an observable using `-[NSObject setSharedObservers:]`

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func snapshot() -> NSKeyValueSharedObserversSnapshot
```
