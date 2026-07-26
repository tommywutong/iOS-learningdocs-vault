---
title: protectedDataDidBecomeAvailableNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/protecteddatadidbecomeavailablenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/protecteddatadidbecomeavailablenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/protecteddatadidbecomeavailablenotification.json'
content_hash: 'sha256:d9ee574ffe3f6fc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# protectedDataDidBecomeAvailableNotification

<sub>Type Property</sub>

A notification that posts when the protected files become available for your code to access.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let protectedDataDidBecomeAvailableNotification: NSNotification.Name
```

## Discussion

This notification does not contain a `userInfo` dictionary.

## See Also

### Accessing protected content

- [protectedDataAvailable](isprotecteddataavailable.md) — A Boolean value that indicates whether content protection is active.
- [UIApplicationProtectedDataWillBecomeUnavailable](protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
