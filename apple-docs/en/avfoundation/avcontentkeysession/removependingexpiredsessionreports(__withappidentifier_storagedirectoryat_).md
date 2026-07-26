---
title: 'removePendingExpiredSessionReports(_:withAppIdentifier:storageDirectoryAt:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/removependingexpiredsessionreports(_:withappidentifier:storagedirectoryat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/removependingexpiredsessionreports(_:withappidentifier:storagedirectoryat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/removependingexpiredsessionreports%28_%3Awithappidentifier%3Astoragedirectoryat%3A%29.json'
content_hash: 'sha256:4dc855759898ca15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# removePendingExpiredSessionReports(_:withAppIdentifier:storageDirectoryAt:)

<sub>Type Method</sub>

Removes expired session reports from storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func removePendingExpiredSessionReports(_ expiredSessionReports: [Data], withAppIdentifier appIdentifier: Data, storageDirectoryAt storageURL: URL)
```

## Parameters

- `expiredSessionReports` — An array of expired session reports to delete.

- `appIdentifier` — The opaque identifier for the app.

- `storageURL` — The URL that points to the directory containing expired session reports.

## See Also

### Handling expired session reports

- [+ pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:](<pendingexpiredsessionreports(withappidentifier_storagedirectoryat_).md>) — Returns the expired session reports for content key sessions created with the specified app identifier.
