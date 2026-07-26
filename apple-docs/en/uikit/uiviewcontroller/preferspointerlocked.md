---
title: prefersPointerLocked
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/preferspointerlocked
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferspointerlocked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferspointerlocked.json'
content_hash: 'sha256:f92f1065501ad957'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# prefersPointerLocked

<sub>Instance Property</sub>

A Boolean value that indicates whether the view controller prefers to lock the pointer to a specific scene.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var prefersPointerLocked: Bool { get }
```

## Discussion

The default is [false](../../swift/false.md). Setting this property to [true](../../swift/true.md) indicates the view controller’s preference to lock the pointer, although the system may not honor the request. Use [locked](../uipointerlockstate/islocked.md) to determine the current pointer lock state. For the system to consider locking the pointer:

- The scene must be full screen, not in Split View or Slide Over, with no other apps in Slide Over.
- The scene must be in the [UISceneActivationStateForegroundActive](../uiscene/activationstate-swift.enum/foregroundactive.md) state.
- For an app built with Mac Catalyst, the app must be in the foreground, and the window that contains the scene ordered to the front.

> [!note] Note
> Bringing an app built with Mac Catalyst to the foreground doesn’t immediately enable pointer lock. To enable pointer lock, the user must click in the window. To exit pointer lock, users can use Command-tab to switch to another app, or using Command-tilde.

The system continuously monitors the state and when the app no longer satisfies the requirements, it disables the pointer lock. When the lock state changes, the system posts [UIPointerLockStateDidChangeNotification](../uipointerlockstate/didchangenotification.md).

If you change the value of [prefersPointerLocked](preferspointerlocked.md), call [- setNeedsUpdateOfPrefersPointerLocked](<setneedsupdateofpreferspointerlocked().md>).

## See Also

### Managing pointer lock state

- [- setNeedsUpdateOfPrefersPointerLocked](<setneedsupdateofpreferspointerlocked().md>) — Indicates that the view controller changed the pointer lock preference.
- [childViewControllerForPointerLock](childviewcontrollerforpointerlock.md) — A child view controller to query for the pointer lock preference.
