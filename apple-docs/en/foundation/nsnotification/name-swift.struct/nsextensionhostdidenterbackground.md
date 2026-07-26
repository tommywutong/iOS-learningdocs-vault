---
title: NSExtensionHostDidEnterBackground
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.2+, iPadOS 8.2+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsextensionhostdidenterbackground
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostdidenterbackground'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsextensionhostdidenterbackground.json'
content_hash: 'sha256:7332e1d85c4141c5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSExtensionHostDidEnterBackground

<sub>Type Property</sub>

Posted when the extension’s host app begins running in the background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let NSExtensionHostDidEnterBackground: NSNotification.Name
```

## Discussion

Extensions can use this notification to stop tasks and prepare the extension to be suspended. The `object` parameter contains the `NSExtensionContext` object. This notification does not contain a `userInfo` dictionary.

Extensions receive only a short amount of time to perform any background work. If you need more time to complete critical tasks, use the methods of the [ProcessInfo](../../processinfo.md) class to request that time.

## See Also

### Working with notifications

- [NSExtensionHostDidBecomeActiveNotification](nsextensionhostdidbecomeactive.md) — Posted when the extension’s host app moves from the inactive to the active state.
- [NSExtensionHostWillResignActiveNotification](nsextensionhostwillresignactive.md) — Posted when the extension’s host app moves from the active to the inactive state.
- [NSExtensionHostWillEnterForegroundNotification](nsextensionhostwillenterforeground.md) — Posted when the extension’s host app begins running in the foreground.
