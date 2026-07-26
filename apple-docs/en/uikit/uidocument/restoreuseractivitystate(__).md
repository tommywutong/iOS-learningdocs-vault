---
title: 'restoreUserActivityState(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/restoreuseractivitystate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/restoreuseractivitystate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/restoreuseractivitystate%28_%3A%29.json'
content_hash: 'sha256:12800391afb33e69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# restoreUserActivityState(_:)

<sub>Instance Method</sub>

Restores the state needed to continue the given user activity.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

## Parameters

- `userActivity` — The user activity to be continued.

## Discussion

Subclasses override this method to restore the responder’s state with the given user activity. The override should use the state data contained in the `userInfo` dictionary of the given user activity to restore the object.

The system can restore user activities that [UIDocument](../uidocument.md) manages automatically, if you return [false](../../swift/false.md) from [- application:continueUserActivity:restorationHandler:](<../uiapplicationdelegate/application(__continue_restorationhandler_).md>) or if you don’t implement the method. In this situation, the [UIDocumentViewController](../uidocumentviewcontroller.md) method [- openDocumentWithCompletionHandler:](<../uidocumentviewcontroller/opendocument(completionhandler_).md>) opens the document, and calls [- restoreUserActivityState:](<restoreuseractivitystate(__).md>).

## See Also

### Supporting user activities

- [userActivity](useractivity.md) — An object encapsulating a user activity supported by this document.
- [- updateUserActivityState:](<updateuseractivitystate(__).md>) — Updates the state of the given user activity.
