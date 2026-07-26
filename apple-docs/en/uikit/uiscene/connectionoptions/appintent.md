---
title: appIntent
framework: AppIntents
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/appintent
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/appintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/appintent.json'
content_hash: 'sha256:5c99c6a1ab52d1bf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# appIntent

<sub>Instance Property</sub>

The `AppIntent` that triggered scene creation `AppIntentSceneDelegate.scene(_:willPerform:)` will always be called after scene connection

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var appIntent: (any UISceneAppIntent)? { get }
```
