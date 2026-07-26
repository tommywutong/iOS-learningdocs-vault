---
title: 'pendingExpiredSessionReports(withAppIdentifier:storageDirectoryAt:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcontentkeysession/pendingexpiredsessionreports(withappidentifier:storagedirectoryat:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession/pendingexpiredsessionreports(withappidentifier:storagedirectoryat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession/pendingexpiredsessionreports%28withappidentifier%3Astoragedirectoryat%3A%29.json'
content_hash: 'sha256:35f0755d11d40b14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContentKeySession](../avcontentkeysession.md)

# pendingExpiredSessionReports(withAppIdentifier:storageDirectoryAt:)

<sub>Type Method</sub>

Returns the expired session reports for content key sessions created with the specified app identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func pendingExpiredSessionReports(withAppIdentifier appIdentifier: Data, storageDirectoryAt storageURL: URL) -> [Data]
```

## Parameters

- `appIdentifier` — The opaque identifier for the app.

- `storageURL` — The URL that points to the directory containing expired session reports.

## Return Value

Returns an array of expired session reports.

## Discussion

The system only returns expired session reports. It doesn’t include reports for active sessions.

## See Also

### Handling expired session reports

- [+ removePendingExpiredSessionReports:withAppIdentifier:storageDirectoryAtURL:](<removependingexpiredsessionreports(__withappidentifier_storagedirectoryat_).md>) — Removes expired session reports from storage.
