---
title: objectIDNotification()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorytransaction/objectidnotification()
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorytransaction/objectidnotification()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorytransaction/objectidnotification%28%29.json'
content_hash: 'sha256:2d74429f308a446f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryTransaction](../nspersistenthistorytransaction.md)

# objectIDNotification()

<sub>Instance Method</sub>

Obtains a notification for use in merging the transaction’s changes into a managed object context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectIDNotification() -> Notification
```

## Return Value

An `NSManagedObjectContextDidSaveObjectIDsNotification` notification.

## Discussion

To merge the relevant changes into your view context, first obtain a notification by calling `objectIDNotification()` on the transaction. Then, pass the notification to [- mergeChangesFromContextDidSaveNotification:](<../nsmanagedobjectcontext/mergechanges(fromcontextdidsave_).md>).
