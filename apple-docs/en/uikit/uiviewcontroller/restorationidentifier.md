---
title: restorationIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/restorationidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/restorationidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/restorationidentifier.json'
content_hash: 'sha256:c1cab0f4984ba3cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# restorationIdentifier

<sub>Instance Property</sub>

The identifier that determines whether the view controller supports state restoration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var restorationIdentifier: String? { get set }
```

## Discussion

This property indicates whether the view controller and its contents should be preserved and is used to identify the view controller during the restoration process. The value of this property is `nil` by default, which indicates that the view controller should not be saved. Assigning a string object to the property lets the system know that the view controller should be saved. In addition, the contents of the string are your way to identify the purpose of the view controller.

During subsequent launches, UIKit asks your app for help in recreating the view controllers that were installed the last time your app ran. When it asks for a specific view controller, UIKit provides your app with this restoration identifier and the restoration identifiers of any parent view controllers in the view controller hierarchy. Your app must use this information to create or locate the appropriate view controller object.

> [!important] Important
> Simply setting the value of this property is not enough to ensure that the view controller is preserved and restored. All parent view controllers must also have a restoration identifier. For more information about the preservation and restoration process, see [View Controller Programming Guide for iOS](https://developer.apple.com/library/archive/featuredarticles/ViewControllerPGforiPhoneOS/index.html#//apple_ref/doc/uid/TP40007457).

## See Also

### Managing state restoration

- [Restoring your app’s state](../restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [restorationClass](restorationclass.md) — The class responsible for recreating this view controller when restoring the app’s state.
- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the view controller.
- [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) — Decodes and restores state-related information for the view controller.
- [- applicationFinishedRestoringState](<applicationfinishedrestoringstate().md>) — Called on restored view controllers after other object decoding is complete.
