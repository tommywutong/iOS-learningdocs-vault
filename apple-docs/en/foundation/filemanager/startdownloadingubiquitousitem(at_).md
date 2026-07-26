---
title: 'startDownloadingUbiquitousItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/startdownloadingubiquitousitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/startdownloadingubiquitousitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/startdownloadingubiquitousitem%28at%3A%29.json'
content_hash: 'sha256:2efbaddcab29824a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# startDownloadingUbiquitousItem(at:)

<sub>Instance Method</sub>

Starts downloading (if necessary) the specified item to the local system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func startDownloadingUbiquitousItem(at url: URL) throws
```

## Parameters

- `url` — The URL for the file or directory in the cloud that you want to download.

## Discussion

If a cloud-based file or directory has not been downloaded yet, calling this method starts the download process. If the item exists locally, calling this method synchronizes the local copy with the version in the cloud.

For a given URL, you can determine if a file is downloaded by getting the value of the [NSMetadataUbiquitousItemDownloadingStatusKey](../nsmetadataubiquitousitemdownloadingstatuskey.md) key. You can also use related keys to determine the current progress in downloading the file.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Managing iCloud-based items

- [ubiquityIdentityToken](ubiquityidentitytoken.md) — An opaque token that represents the current user’s iCloud Drive Documents identity.
- [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) — Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [- isUbiquitousItemAtURL:](<isubiquitousitem(at_).md>) — Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [- setUbiquitous:itemAtURL:destinationURL:error:](<setubiquitous(__itemat_destinationurl_).md>) — Indicates whether the item at the specified URL should be stored in iCloud.
- [- evictUbiquitousItemAtURL:error:](<evictubiquitousitem(at_).md>) — Removes the local copy of the specified item that’s stored in iCloud.
- [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<url(forpublishingubiquitousitemat_expiration_).md>) — Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.
