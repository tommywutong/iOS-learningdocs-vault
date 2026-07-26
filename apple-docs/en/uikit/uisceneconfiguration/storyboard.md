---
title: storyboard
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneconfiguration/storyboard
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/storyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/storyboard.json'
content_hash: 'sha256:2c36ddd1ade463a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# storyboard

<sub>Instance Property</sub>

The storyboard object that contains your scene’s initial view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var storyboard: UIStoryboard? { get set }
```

## Discussion

UIKit loads the initial view controller from the specified scene and displays it appropriately.

UIKit sets this property’s initial value using the [UISceneStoryboardFile](../../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) key from the appropriate scene in your app’s `Info.plist` file.

## See Also

### Specifying the scene creation details

- [sceneClass](sceneclass.md) — The class of the scene object that you want UIKit to create.
- [delegateClass](delegateclass.md) — The class of the custom delegate object that you want UIKit to create.
