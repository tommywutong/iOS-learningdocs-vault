---
title: 'updateUserActivityState(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocument/updateuseractivitystate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/updateuseractivitystate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/updateuseractivitystate%28_%3A%29.json'
content_hash: 'sha256:87bbb32adb60866e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# updateUserActivityState(_:)

<sub>Instance Method</sub>

Updates the state of the given user activity.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func updateUserActivityState(_ userActivity: NSUserActivity)
```

## Parameters

- `userActivity` — The user activity to be updated.

## Discussion

The default implementation of this method puts the document’s [fileURL](fileurl.md) into the [NSUserActivity](../../foundation/nsuseractivity.md) object’s [userInfo](../../foundation/nsuseractivity/userinfo.md) dictionary with the [NSUserActivityDocumentURLKey](useractivityurlkey.md). [UIDocument](../uidocument.md) automatically sets the [needsSave](../../foundation/nsuseractivity/needssave.md) property of the [NSUserActivity](../../foundation/nsuseractivity.md) object to [true](../../swift/true.md) when the [fileURL](fileurl.md) changes.

## See Also

### Supporting user activities

- [userActivity](useractivity.md) — An object encapsulating a user activity supported by this document.
- [- restoreUserActivityState:](<restoreuseractivitystate(__).md>) — Restores the state needed to continue the given user activity.
