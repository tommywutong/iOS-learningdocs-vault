---
title: NSExtensionHostDidBecomeActive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.2+, iPadOS 8.2+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsextensionhostdidbecomeactive
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostdidbecomeactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostdidbecomeactive.json'
content_hash: 'sha256:47d819331df218ca'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSExtensionHostDidBecomeActive

<sub>Type Property</sub>

Posted when the extension’s host app moves from the inactive to the active state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let NSExtensionHostDidBecomeActive: NSNotification.Name
```

## Discussion

Extensions can use this notification to adjust their activity when they become active. The `object` parameter contains the `NSExtensionContext` object. This notification does not contain a `userInfo` dictionary.

## See Also

### Working with notifications

- [NSExtensionHostWillResignActiveNotification](nsextensionhostwillresignactive.md) — Posted when the extension’s host app moves from the active to the inactive state.
- [NSExtensionHostDidEnterBackgroundNotification](nsextensionhostdidenterbackground.md) — Posted when the extension’s host app begins running in the background.
- [NSExtensionHostWillEnterForegroundNotification](nsextensionhostwillenterforeground.md) — Posted when the extension’s host app begins running in the foreground.
