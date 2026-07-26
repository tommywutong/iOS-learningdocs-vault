---
title: NSUbiquitousFileUnavailableError
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsubiquitousfileunavailableerror-swift.var
source_url: 'https://developer.apple.com/documentation/foundation/nsubiquitousfileunavailableerror-swift.var'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsubiquitousfileunavailableerror-swift.var.json'
content_hash: 'sha256:d0e4e0abdb8f4dc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUbiquitousFileUnavailableError

<sub>Global Variable</sub>

The item has not been uploaded to iCloud by another device yet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSUbiquitousFileUnavailableError: Int { get }
```

## Discussion

When this error occurs, you do not need to ask the system to start downloading the item. The system will download the item as soon as it can. If you want to know when the item becomes available, use an [NSMetadataQuery](nsmetadataquery.md) object to monitor changes to the file’s URL.

## See Also

### General iCloud File Errors

- [NSUbiquitousFileErrorMinimum](nsubiquitousfileerrorminimum-swift.var.md) — The minimum error code value that represents an iCloud error.
- [NSUbiquitousFileNotUploadedDueToQuotaError](nsubiquitousfilenotuploadedduetoquotaerror-swift.var.md) — The item could not be uploaded to iCloud because it would make the account go over its quota.
- [NSUbiquitousFileUbiquityServerNotAvailable](nsubiquitousfileubiquityservernotavailable-swift.var.md) — A failure to connect to the iCloud servers.
- [NSUbiquitousFileErrorMaximum](nsubiquitousfileerrormaximum-swift.var.md) — The maximum error code value that represents an iCloud error.
