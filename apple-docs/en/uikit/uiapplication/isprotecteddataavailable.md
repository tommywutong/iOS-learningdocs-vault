---
title: isProtectedDataAvailable
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/isprotecteddataavailable
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/isprotecteddataavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/isprotecteddataavailable.json'
content_hash: 'sha256:18d1023836c71af5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# isProtectedDataAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether content protection is active.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated var isProtectedDataAvailable: Bool { get }
```

## Discussion

The value of this property is [false](../../swift/false.md) if data protection is enabled and the device is currently locked. The value of this property is set to [true](../../swift/true.md) if the device is unlocked or if content protection is not enabled.

When the value of this property is [false](../../swift/false.md), files that were assigned the [complete](../../foundation/fileprotectiontype/complete.md) or [completeUnlessOpen](../../foundation/fileprotectiontype/completeunlessopen.md) protection key cannot be read or written by your app. The user must unlock the device before your app can access them.

## See Also

### Accessing protected content

- [UIApplicationProtectedDataDidBecomeAvailable](protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [UIApplicationProtectedDataWillBecomeUnavailable](protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
