---
title: NSExtensionHostWillResignActive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.2+, iPadOS 8.2+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsextensionhostwillresignactive
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostwillresignactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostwillresignactive.json'
content_hash: 'sha256:856181ce6169f594'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSExtensionHostWillResignActive

<sub>Type Property</sub>

Posted when the extension’s host app moves from the active to the inactive state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let NSExtensionHostWillResignActive: NSNotification.Name
```

## Discussion

Extensions can use this notification to adjust their activity when they become inactive. For example, you might use this notification to save any unsaved data to prevent it from being lost. The `object` parameter contains the `NSExtensionContext` object. This notification does not contain a `userInfo` dictionary.

## See Also

### Working with notifications

- [NSExtensionHostDidBecomeActiveNotification](nsextensionhostdidbecomeactive.md) — Posted when the extension’s host app moves from the inactive to the active state.
- [NSExtensionHostDidEnterBackgroundNotification](nsextensionhostdidenterbackground.md) — Posted when the extension’s host app begins running in the background.
- [NSExtensionHostWillEnterForegroundNotification](nsextensionhostwillenterforeground.md) — Posted when the extension’s host app begins running in the foreground.
