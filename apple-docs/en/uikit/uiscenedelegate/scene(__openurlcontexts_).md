---
title: 'scene(_:openURLContexts:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scene(_:openurlcontexts:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:openurlcontexts:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scene%28_%3Aopenurlcontexts%3A%29.json'
content_hash: 'sha256:ff2d85fa933ec4fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# scene(_:openURLContexts:)

<sub>Instance Method</sub>

Asks the delegate to open one or more URLs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>)
```

## Parameters

- `scene` — The scene that UIKit asks to open the URL.

- `URLContexts` — One or more [UIOpenURLContext](../uiopenurlcontext.md) objects. Each object contains one URL to open and any additional information needed to open that URL.
