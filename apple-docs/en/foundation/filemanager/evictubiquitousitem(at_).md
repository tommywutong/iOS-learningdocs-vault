---
title: 'evictUbiquitousItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/evictubiquitousitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/evictubiquitousitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/evictubiquitousitem%28at%3A%29.json'
content_hash: 'sha256:6b836542b5a7e789'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# evictUbiquitousItem(at:)

<sub>Instance Method</sub>

Removes the local copy of the specified item that’s stored in iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func evictUbiquitousItem(at url: URL) throws
```

## Parameters

- `url` — The URL to a file or directory in iCloud storage.

## Discussion

Don’t use a coordinated write to perform this operation. In macOS 10.7 or earlier, the framework takes a coordinated write in its implementation of this method, so taking one in your app causes a deadlock. In macOS 10.8 and later, the framework detects coordination done by your app on the same thread as the call to this method, to avoid deadlocking.

This method doesn’t remove the item from iCloud. It removes only the local version. You can then use [- startDownloadingUbiquitousItemAtURL:error:](<startdownloadingubiquitousitem(at_).md>) to force iCloud to download a new version of the file or directory from the server.

To delete a file permanently from the user’s iCloud storage, use the regular [FileManager](../filemanager.md) routines for deleting files and directories. Remember that deleting items from iCloud can’t be undone. Once deleted, the item is gone forever.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- removeItemAtURL:error:](<removeitem(at_).md>) — Removes the file or directory at the specified URL.

### Managing iCloud-based items

- [ubiquityIdentityToken](ubiquityidentitytoken.md) — An opaque token that represents the current user’s iCloud Drive Documents identity.
- [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) — Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [- isUbiquitousItemAtURL:](<isubiquitousitem(at_).md>) — Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [- setUbiquitous:itemAtURL:destinationURL:error:](<setubiquitous(__itemat_destinationurl_).md>) — Indicates whether the item at the specified URL should be stored in iCloud.
- [- startDownloadingUbiquitousItemAtURL:error:](<startdownloadingubiquitousitem(at_).md>) — Starts downloading (if necessary) the specified item to the local system.
- [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<url(forpublishingubiquitousitemat_expiration_).md>) — Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.
