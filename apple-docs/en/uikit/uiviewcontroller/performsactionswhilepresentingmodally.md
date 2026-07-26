---
title: performsActionsWhilePresentingModally
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/performsactionswhilepresentingmodally
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/performsactionswhilepresentingmodally'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/performsactionswhilepresentingmodally.json'
content_hash: 'sha256:fca6aef4b763a009'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# performsActionsWhilePresentingModally

<sub>Instance Property</sub>

A Boolean value indicating whether the view controller performs menu-related actions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var performsActionsWhilePresentingModally: Bool { get }
```

## Discussion

The default value of this property is [true](../../swift/true.md), which causes the view controller to handle actions passed along the responder chain by modally presented view controllers. If the app includes the `UIViewControllerPerformsActionsWhilePresentingModally` key in its `Info.plist` file, the default value matches the value of that key instead.

A presenting view controller might not want to handle actions in one of its modally presented child view controllers. Overriding this property and returning [false](../../swift/false.md) causes UIKit to ignore this view controller when searching for a target to handle actions.

## See Also

### Accessing the available key commands

- [- addKeyCommand:](<addkeycommand(__).md>) — Associates the specified keyboard shortcut with the view controller.
- [- removeKeyCommand:](<removekeycommand(__).md>) — Removes the key command from the view controller.
