---
title: NSURLCredentialStorageChanged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.14 起废弃）, tvOS 9.0+（12.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（5.0 起废弃）]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsurlcredentialstoragechanged
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsurlcredentialstoragechanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsurlcredentialstoragechanged.json'
content_hash: 'sha256:a5f6c003311fd2a8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSURLCredentialStorageChanged

<sub>Type Property</sub>

A notification posted when the set of stored credentials changes.

> [!warning] Deprecated
> Notification is never posted

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSURLCredentialStorageChanged: NSNotification.Name
```

## Discussion

The notification’s [object](../../notification/object.md) is the [URLCredentialStorage](../../urlcredentialstorage.md) instance that changed. This notification does not contain a [userInfo](../../notification/userinfo.md) dictionary.
