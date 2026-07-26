---
title: protectedDataWillBecomeUnavailableNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/protecteddatawillbecomeunavailablenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/protecteddatawillbecomeunavailablenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/protecteddatawillbecomeunavailablenotification.json'
content_hash: 'sha256:ba89acc4f3c33ad8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# protectedDataWillBecomeUnavailableNotification

<sub>Type Property</sub>

A notification that posts shortly before protected files are locked down and become inaccessible.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name
```

## Discussion

Upon receiving this notification, clients should release any references to protected files. This notification does not contain a `userInfo` dictionary.

## See Also

### Accessing protected content

- [protectedDataAvailable](isprotecteddataavailable.md) — A Boolean value that indicates whether content protection is active.
- [UIApplicationProtectedDataDidBecomeAvailable](protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
