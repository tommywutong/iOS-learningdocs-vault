---
title: GKPlayerAuthenticationDidChangeNotificationName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/gkplayerauthenticationdidchangenotificationname
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/gkplayerauthenticationdidchangenotificationname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/gkplayerauthenticationdidchangenotificationname.json'
content_hash: 'sha256:2073c20209ee4024'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# GKPlayerAuthenticationDidChangeNotificationName

<sub>Type Property</sub>

A notification that posts after GameKit authenticates the local player.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let GKPlayerAuthenticationDidChangeNotificationName: NSNotification.Name
```

## Discussion

The object property for this notification is a `GKLocalPlayer` object. Passing `nil` provides standard Notification Center behavior, which is to receive the notification for any object.

## See Also

### GameKit

- [GKPlayerDidChangeNotificationName](gkplayerdidchangenotificationname.md) — A notification that posts when a player object’s data changes.
