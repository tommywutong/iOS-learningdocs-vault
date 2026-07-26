---
title: NSUbiquityIdentityDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsubiquityidentitydidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsubiquityidentitydidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsubiquityidentitydidchange.json'
content_hash: 'sha256:854c01fa9f6f7c1d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSUbiquityIdentityDidChange

<sub>Type Property</sub>

Sent after the iCloud (“ubiquity”) identity has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSUbiquityIdentityDidChange: NSNotification.Name
```

## Discussion

The system generates this notification when the user logs into or out of an iCloud account or enables or disables the syncing of documents and data. This notification is your cue to update caches and any interface elements displaying iCloud–related content. For example, hide all references to iCloud files when the user logs out of iCloud.

When your app receives this notification, get the new token from the [ubiquityIdentityToken](../../filemanager/ubiquityidentitytoken.md) instance property. The value of that token is `nil` if the user disabled iCloud or logged out. There is no `userInfo` dictionary.
