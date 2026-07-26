---
title: 'init(session:connectionOptions:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscene/init(session:connectionoptions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/init(session:connectionoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/init%28session%3Aconnectionoptions%3A%29.json'
content_hash: 'sha256:cb87abe7b84d3d1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# init(session:connectionOptions:)

<sub>Initializer</sub>

Creates a scene object using the specified session and connection information.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(session: UISceneSession, connectionOptions: UIScene.ConnectionOptions)
```

## Parameters

- `session` — A session object containing the configuration details for the scene. The system creates the session object and passes it to this initialization method.

- `connectionOptions` — An object containing additional options for connecting the scene to your app.

## Return Value

An initialized scene object.

## Discussion

Subclasses call this method to initialize the scene details.
