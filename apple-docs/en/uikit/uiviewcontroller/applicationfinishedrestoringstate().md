---
title: applicationFinishedRestoringState()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/applicationfinishedrestoringstate()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/applicationfinishedrestoringstate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/applicationfinishedrestoringstate%28%29.json'
content_hash: 'sha256:c71a008d79dd477c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# applicationFinishedRestoringState()

<sub>Instance Method</sub>

Called on restored view controllers after other object decoding is complete.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func applicationFinishedRestoringState()
```

## Discussion

After other object decoding has completed, the system calls this method. This allows a view controller to complete setup after other state restoration, relying on the system to ensure that the states of all objects from the restoration archive have been decoded.

## See Also

### Managing state restoration

- [Restoring your app’s state](../restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [restorationIdentifier](restorationidentifier.md) — The identifier that determines whether the view controller supports state restoration.
- [restorationClass](restorationclass.md) — The class responsible for recreating this view controller when restoring the app’s state.
- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the view controller.
- [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) — Decodes and restores state-related information for the view controller.
