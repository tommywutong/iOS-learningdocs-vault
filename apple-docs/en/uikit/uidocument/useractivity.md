---
title: userActivity
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/useractivity
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/useractivity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/useractivity.json'
content_hash: 'sha256:28b3f5bf7f571b17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# userActivity

<sub>Instance Property</sub>

An object encapsulating a user activity supported by this document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var userActivity: NSUserActivity? { get set }
```

## Discussion

[UIDocument](../uidocument.md) automatically creates [NSUserActivity](../../foundation/nsuseractivity.md) objects. The system makes user activities eligible for Handoff if the document is iCloud-based and the app’s `Info.plist` property list file includes a [CFBundleDocumentTypes](../../bundleresources/information-property-list/cfbundledocumenttypes.md) key of `NSUbiquitousDocumentUserActivityType`. The value of `NSUbiquitousDocumentUserActivityType` is a string that represents the [NSUserActivity](../../foundation/nsuseractivity.md) object’s activity type. The document’s URL is in the [NSUserActivity](../../foundation/nsuseractivity.md) object’s [userInfo](../../foundation/nsuseractivity/userinfo.md) dictionary with the [NSUserActivityDocumentURLKey](useractivityurlkey.md).

In iOS, to make an  [NSUserActivity](../../foundation/nsuseractivity.md) object that UIKit manages current, you must either call [becomeCurrent()](<../../foundation/nsuseractivity/becomecurrent().md>) explicitly or have the document’s [NSUserActivity](../../foundation/nsuseractivity.md) object also set on a [UIViewController](../uiviewcontroller.md) object that’s in the view hierarchy when the app comes to the foreground.

You can use this property from any thread. It’s KVO-observable in case you share the [userActivity](useractivity.md) object with other objects that need to be kept in sync as the document moves into and out of iCloud.

## See Also

### Supporting user activities

- [- restoreUserActivityState:](<restoreuseractivitystate(__).md>) — Restores the state needed to continue the given user activity.
- [- updateUserActivityState:](<updateuseractivitystate(__).md>) — Updates the state of the given user activity.
