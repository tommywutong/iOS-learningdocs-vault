---
title: 'url(forPublishingUbiquitousItemAt:expiration:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/url(forpublishingubiquitousitemat:expiration:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/url(forpublishingubiquitousitemat:expiration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/url%28forpublishingubiquitousitemat%3Aexpiration%3A%29.json'
content_hash: 'sha256:f1b5eba603bc4767'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# url(forPublishingUbiquitousItemAt:expiration:)

<sub>Instance Method</sub>

Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func url(forPublishingUbiquitousItemAt url: URL, expiration outDate: AutoreleasingUnsafeMutablePointer<NSDate?>?) throws -> URL
```

## Parameters

- `url` — The URL of the item in the cloud that you want to share. The URL must be prefixed with the base URL returned from the [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) method that corresponds to the item’s location. The file must be a flat file, not a bundle. The file at the specified URL must already be uploaded to iCloud when you call this method.

- `outDate` — On input, a pointer to a variable for a date object. On output, this parameter contains the date after which the item is no longer available at the returned URL. You may specify `nil` for this parameter if you are not interested in the date.

## Return Value

A URL with which users can download a copy of the item at `url`. In Objective-C, returns `nil` if the URL could not be created for any reason.

## Discussion

This method creates a snapshot of the specified flat file and places that copy in a temporary iCloud location where it can be accessed by other users using the returned URL. The snapshot reflects the contents of the file at the time the URL was generated and is not updated when subsequent changes are made to the original file in the user’s iCloud storage. The snapshot file remains available at the specified URL until the date specified in the `outDate` parameter, after which it is automatically deleted. Explicitly deleting the item by calling the [- removeItemAtURL:error:](<removeitem(at_).md>) or [- removeItemAtPath:error:](<removeitem(atpath_).md>) method also deletes all old versions of the item, invalidating URLs to those versions returned by this method.

Your app must have access to the network for this call to succeed. If the specified file is in the process of being uploaded to iCloud, you must not call this method until the upload has finished.

> [!important] Important
> As of iOS 8.0 and macOS 10.10 The `url` must specify a flat file, not a bundle. Bundles have a folder as the root item.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Managing iCloud-based items

- [ubiquityIdentityToken](ubiquityidentitytoken.md) — An opaque token that represents the current user’s iCloud Drive Documents identity.
- [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) — Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [- isUbiquitousItemAtURL:](<isubiquitousitem(at_).md>) — Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [- setUbiquitous:itemAtURL:destinationURL:error:](<setubiquitous(__itemat_destinationurl_).md>) — Indicates whether the item at the specified URL should be stored in iCloud.
- [- startDownloadingUbiquitousItemAtURL:error:](<startdownloadingubiquitousitem(at_).md>) — Starts downloading (if necessary) the specified item to the local system.
- [- evictUbiquitousItemAtURL:error:](<evictubiquitousitem(at_).md>) — Removes the local copy of the specified item that’s stored in iCloud.
