---
title: 'restoreUserActivityState(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiuseractivityrestoring/restoreuseractivitystate(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiuseractivityrestoring/restoreuseractivitystate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiuseractivityrestoring/restoreuseractivitystate%28_%3A%29.json'
content_hash: 'sha256:2427281cbbb198bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserActivityRestoring](../uiuseractivityrestoring.md)

# restoreUserActivityState(_:)

<sub>Instance Method</sub>

Restores the state necessary to continue the specified user activity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

## Parameters

- `userActivity` — The user activity to continue.

## Discussion

Implement this method to restore an object’s state using the specified user activity. The system calls this method on any objects passed to the restoration handler in [application(_:continue:restorationHandler:)](<../../appkit/nsapplicationdelegate/application(__continue_restorationhandler_).md>). Your implementation should use the state data contained in the specified user activity’s [userInfo](../../foundation/nsuseractivity/userinfo.md) dictionary to restore the object.
