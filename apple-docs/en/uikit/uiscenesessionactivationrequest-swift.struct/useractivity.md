---
title: userActivity
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesessionactivationrequest-swift.struct/useractivity
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/useractivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct/useractivity.json'
content_hash: 'sha256:86c580b42c009501'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)

# userActivity

<sub>Instance Property</sub>

A user activity to send to the newly activated scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var userActivity: NSUserActivity? { get set }
```

## Discussion

The system sends the `userActivity` to the session’s scene upon activation, regardless of whether the scene session already exists.

If you don’t provide a scene session to activate, the system uses the [targetContentIdentifier](../../foundation/nsuseractivity/targetcontentidentifier.md) of the user activity to determine which scene session to activate. When the user activity’s [targetContentIdentifier](../../foundation/nsuseractivity/targetcontentidentifier.md) satisfies the [prefersToActivateForTargetContentIdentifierPredicate](../uisceneactivationconditions/preferstoactivatefortargetcontentidentifierpredicate.md), the system activates that scene’s session to handle the user activity.

## See Also

### Managing request details

- [options](options.md) — Activation request options to further customize the request.
- [role](role.md) — The role to request.
- [session](session.md) — The specific scene session to activate.
