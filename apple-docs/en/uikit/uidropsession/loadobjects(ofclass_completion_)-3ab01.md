---
title: 'loadObjects(ofClass:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropsession/loadobjects(ofclass:completion:)-3ab01'
source_url: 'https://developer.apple.com/documentation/uikit/uidropsession/loadobjects(ofclass:completion:)-3ab01'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropsession/loadobjects%28ofclass%3Acompletion%3A%29-3ab01.json'
content_hash: 'sha256:f28e69a0f039d04a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropSession](../uidropsession.md)

# loadObjects(ofClass:completion:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func loadObjects<T>(ofClass: T.Type, completion: @escaping ([T]) -> Void) -> Progress where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```
