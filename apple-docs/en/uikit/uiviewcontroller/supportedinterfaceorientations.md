---
title: supportedInterfaceOrientations
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/supportedinterfaceorientations
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/supportedinterfaceorientations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/supportedinterfaceorientations.json'
content_hash: 'sha256:5e9d858e32721200'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# supportedInterfaceOrientations

<sub>Instance Property</sub>

The interface orientations that the view controller supports.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var supportedInterfaceOrientations: UIInterfaceOrientationMask { get }
```

## Discussion

This property returns a bit mask that specifies which orientations the view controller supports. For more information, see [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md).

When the device orientation changes, the system calls this method on the root view controller or the topmost modal view controller that fills the window. If the view controller supports the new orientation, the system rotates the window and the view controller. The system only calls this method if the view controller’s [shouldAutorotate](shouldautorotate.md) method returns [true](../../swift/true.md).

Override this method to declare which orientations the view controller supports. The default value is [UIInterfaceOrientationMaskAll](../uiinterfaceorientationmask/all.md) for the iPad idiom and [UIInterfaceOrientationMaskAllButUpsideDown](../uiinterfaceorientationmask/allbutupsidedown.md) for the iPhone idiom. The value you return must not be 0.

To determine whether to rotate, the system compares the view controller’s supported orientations with the app’s supported orientations — as determined by the `Info.plist` file or the app delegate’s [- application:supportedInterfaceOrientationsForWindow:](<../uiapplicationdelegate/application(__supportedinterfaceorientationsfor_).md>) method — and the device’s supported orientations.

> [!note] Note
> All iPadOS devices support the [UIInterfaceOrientationMaskPortraitUpsideDown](../uiinterfaceorientationmask/portraitupsidedown.md) orientation. It’s best practice to enable it for the iPad idiom. iOS devices without a Home button, such as iPhone 12, don’t support this orientation. You should disable it entirely for the iPhone idiom.

If your app supports multitasking, the system doesn’t call this method on your view controller because multitasking apps must support all orientations. You can opt out of multitasking by enabling _Requires full screen_ on your iOS target or by not declaring support for all possible orientations within the `Info.plist` file.

For design guidance, see [Adaptivity and Layout](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/adaptivity-and-layout/) in the iOS Human Interface Guidelines.

## See Also

### Configuring the view rotation settings

- [preferredInterfaceOrientationForPresentation](preferredinterfaceorientationforpresentation.md) — The interface orientation to use when presenting the view controller.
- [- setNeedsUpdateOfSupportedInterfaceOrientations](<setneedsupdateofsupportedinterfaceorientations().md>) — Notifies the view controller about a change in supported interface orientations or preferred interface orientation for presentation.
- [prefersInterfaceOrientationLocked](prefersinterfaceorientationlocked.md) — A Boolean value that indicates whether the view controller prefers to lock the scene’s interface orientation when the scene is visible.
- [- setNeedsUpdateOfPrefersInterfaceOrientationLocked](<setneedsupdateofprefersinterfaceorientationlocked().md>) — Indicates that the view controller changed the interface orientation lock preference.
- [childViewControllerForInterfaceOrientationLock](childforinterfaceorientationlock.md) — A child view controller to query for the interface orientation lock preference.
