---
title: NSBundleResourceRequestLowDiskSpace
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsbundleresourcerequestlowdiskspace.json'
content_hash: 'sha256:09b4c3a64e42e5b5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSBundleResourceRequestLowDiskSpace

<sub>Type Property</sub>

Posted after the system detects that the amount of available disk space is getting low. The notification is posted to the default notification center.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let NSBundleResourceRequestLowDiskSpace: NSNotification.Name
```

## Discussion

After receiving this notification, the app should release any on-demand resources that are not required. Call [- endAccessingResources](<../../nsbundleresourcerequest/endaccessingresources().md>) to release the managed resources. If the app is in the background and the app does not free up enough space, it may be terminated.

> [!note] Note
> This notification is generated independently of any other iOS notifications for low disk space.
