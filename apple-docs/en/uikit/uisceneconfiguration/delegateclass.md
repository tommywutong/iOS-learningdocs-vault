---
title: delegateClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneconfiguration/delegateclass
source_url: 'https://developer.apple.com/documentation/uikit/uisceneconfiguration/delegateclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneconfiguration/delegateclass.json'
content_hash: 'sha256:068f3aceb1d75deb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneConfiguration](../uisceneconfiguration.md)

# delegateClass

<sub>Instance Property</sub>

The class of the custom delegate object that you want UIKit to create.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var delegateClass: AnyClass? { get set }
```

## Discussion

If you specified [UIWindowScene](../uiwindowscene.md) in the [sceneClass](sceneclass.md) property, your delegate class must conform to the [UIWindowSceneDelegate](../uiwindowscenedelegate.md) protocol. Otherwise, you must specify a class that conforms to the [UISceneDelegate](../uiscenedelegate.md) protocol.

UIKit sets this property’s initial value using the [UISceneDelegateClassName](../../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenedelegateclassname.md) key from the appropriate scene in your app’s `Info.plist` file.

## See Also

### Specifying the scene creation details

- [sceneClass](sceneclass.md) — The class of the scene object that you want UIKit to create.
- [storyboard](storyboard.md) — The storyboard object that contains your scene’s initial view controller.
