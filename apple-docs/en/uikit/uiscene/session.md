---
title: session
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/session
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/session'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/session.json'
content_hash: 'sha256:92415cead754d73b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# session

<sub>Instance Property</sub>

The session associated with the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var session: UISceneSession { get }
```

## Discussion

UIKit maintains a session object for each scene. The session object contains a unique identifier for the scene and other information about its configuration.

## See Also

### Getting the scene’s session

- [UISceneSession](../uiscenesession.md) — An object that contains information about one of your app’s scenes.
