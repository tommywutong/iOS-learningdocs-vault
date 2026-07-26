---
title: targetContentIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/targetcontentidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/targetcontentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/targetcontentidentifier.json'
content_hash: 'sha256:474378a7dee44033'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# targetContentIdentifier

<sub>Instance Property</sub>

A string that identifies the user activity’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var targetContentIdentifier: String? { get set }
```

## Discussion

A target content identifier is a string you define within your app. This string provides a unique identifier for specific content in your app, like a particular document or the location of a piece of data in a database. This string isn’t visible to the user.

If you set this property, when the system delivers an [NSUserActivity](../nsuseractivity.md) object to an app with multiple scenes, it chooses the [UIScene](../../uikit/uiscene.md) whose [UISceneActivationConditions](../../uikit/uisceneactivationconditions.md) have the best match with the target content identifier. For more information, see [UISceneActivationConditions](../../uikit/uisceneactivationconditions.md).

This property is optional but is highly recommended to create a great multitasking experience for apps that run on iPad. Setting this property doesn’t automatically set [needsSave](needssave.md) to [true](../../swift/true.md).

## See Also

### Specifying app identifiers

- [appEntityIdentifier](appentityidentifier.md) — The identifier of an app entity that you associate with the user activity.
- [externalMediaContentIdentifier](externalmediacontentidentifier.md) — A unique identifier from the app’s media content catalog for the currently displayed media item.
