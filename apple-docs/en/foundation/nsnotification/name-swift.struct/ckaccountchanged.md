---
title: CKAccountChanged
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/ckaccountchanged
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/ckaccountchanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/ckaccountchanged.json'
content_hash: 'sha256:0262769a865ea59c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# CKAccountChanged

<sub>Type Property</sub>

A notification that a container posts when the status of an iCloud account changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let CKAccountChanged: NSNotification.Name
```

## Discussion

Create an instance of [CKContainer](../../../cloudkit/ckcontainer.md) to receive this notification. The container posts the notification using an arbitrary queue. Use the [accountStatus(completionHandler:)](<../../../cloudkit/ckcontainer/accountstatus(completionhandler_).md>) method to obtain the account’s status.
