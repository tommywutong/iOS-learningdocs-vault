---
title: 'canLoadObjects(ofClass:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragdropsession/canloadobjects(ofclass:)-6x43t'
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession/canloadobjects(ofclass:)-6x43t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession/canloadobjects%28ofclass%3A%29-6x43t.json'
content_hash: 'sha256:90e6e1f758c27a5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragDropSession](../uidragdropsession.md)

# canLoadObjects(ofClass:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func canLoadObjects<T>(ofClass: T.Type) -> Bool where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```
