---
title: sceneClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneconfiguration/sceneclass
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/sceneclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/sceneclass.json'
content_hash: 'sha256:d4494b31c3096add'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# sceneClass

<sub>Instance Property</sub>

The class of the scene object that you want UIKit to create.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sceneClass: AnyClass? { get set }
```

## Discussion

The class you specify must be [UIScene](../uiscene.md) or one of its subclasses. Typically, you specify the [UIWindowScene](../uiwindowscene.md) class for all windows associated with your app.

UIKit sets this property’s initial value using the [UISceneClassName](../../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uisceneclassname.md) key from the appropriate scene in your app’s `Info.plist` file.

## See Also

### Specifying the scene creation details

- [delegateClass](delegateclass.md) — The class of the custom delegate object that you want UIKit to create.
- [storyboard](storyboard.md) — The storyboard object that contains your scene’s initial view controller.
