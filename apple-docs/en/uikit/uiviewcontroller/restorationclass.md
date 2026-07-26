---
title: restorationClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/restorationclass
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/restorationclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/restorationclass.json'
content_hash: 'sha256:86e1b48ba349f46e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# restorationClass

<sub>Instance Property</sub>

The class responsible for recreating this view controller when restoring the app’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var restorationClass: (any UIViewControllerRestoration.Type)? { get set }
```

## Discussion

If a view controller has an associated restoration class, the [+ viewControllerWithRestorationIdentifierPath:coder:](<../uiviewcontrollerrestoration/viewcontroller(withrestorationidentifierpath_coder_).md>) method of that class is called during state restoration. That method is responsible for returning the view controller object that matches the indicated view controller. If you do not specify a restoration class for your view controller, the state restoration engine asks your app delegate to provide the view controller object instead.

The restoration class must conform to the [UIViewControllerRestoration](../uiviewcontrollerrestoration.md) protocol.

## See Also

### Managing state restoration

- [Restoring your app’s state](../restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [restorationIdentifier](restorationidentifier.md) — The identifier that determines whether the view controller supports state restoration.
- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the view controller.
- [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) — Decodes and restores state-related information for the view controller.
- [- applicationFinishedRestoringState](<applicationfinishedrestoringstate().md>) — Called on restored view controllers after other object decoding is complete.
