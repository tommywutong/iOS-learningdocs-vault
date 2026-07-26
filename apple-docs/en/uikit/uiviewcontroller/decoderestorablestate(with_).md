---
title: 'decodeRestorableState(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/decoderestorablestate(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/decoderestorablestate(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/decoderestorablestate%28with%3A%29.json'
content_hash: 'sha256:375861ffb8678729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# decodeRestorableState(with:)

<sub>Instance Method</sub>

Decodes and restores state-related information for the view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func decodeRestorableState(with coder: NSCoder)
```

## Parameters

- `coder` — The coder object to use to decode the state of the view.

## Discussion

Do not call this method directly. The system calls this method during the state restoration process so that you can restore your view controller to its previous state.

If your app supports state restoration, override this method for any view controllers for which you also overrode the [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) method. Your implementation of this method should use any saved state information to restore the view controller to its previous configuration. If your [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) method called `super`, this method should similarly call `super` at some point in its implementation.

## See Also

### Managing state restoration

- [Restoring your app’s state](../restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [restorationIdentifier](restorationidentifier.md) — The identifier that determines whether the view controller supports state restoration.
- [restorationClass](restorationclass.md) — The class responsible for recreating this view controller when restoring the app’s state.
- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the view controller.
- [- applicationFinishedRestoringState](<applicationfinishedrestoringstate().md>) — Called on restored view controllers after other object decoding is complete.
