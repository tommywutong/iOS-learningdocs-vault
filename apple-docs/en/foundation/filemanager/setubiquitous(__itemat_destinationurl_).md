---
title: 'setUbiquitous(_:itemAt:destinationURL:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/setubiquitous(_:itemat:destinationurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/setubiquitous(_:itemat:destinationurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/setubiquitous%28_%3Aitemat%3Adestinationurl%3A%29.json'
content_hash: 'sha256:97d175aca6d5bf51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# setUbiquitous(_:itemAt:destinationURL:)

<sub>Instance Method</sub>

Indicates whether the item at the specified URL should be stored in iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setUbiquitous(_ flag: Bool, itemAt url: URL, destinationURL: URL) throws
```

## Parameters

- `flag` — [true](../../swift/true.md) to move the item to iCloud or [false](../../swift/false.md) to remove it from iCloud (if it is there currently).

- `url` — The URL of the item (file or directory) that you want to store in iCloud.

- `destinationURL` — When moving a file into iCloud, this is the location in iCloud at which to store the file or directory. This URL must be constructed from a URL returned by the [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) method, which you use to retrieve the desired iCloud container directory. The URL you specify may contain additional subdirectories so that you can organize your files hierarchically in iCloud. However, you are responsible for creating those intermediate subdirectories (using the [FileManager](../filemanager.md) class) in your iCloud container directory. When moving a file _out of iCloud_, this is the location on the local device.

## Discussion

Use this method to move a file from its current location to iCloud. For files located in an app’s sandbox, this involves physically removing the file from the sandbox container. (The system extends your app’s sandbox privileges to give it access to files it moves to iCloud.) You can also use this method to move files out of iCloud and back into a local directory.

If your app is presenting the file’s contents to the user, it must have an active file presenter object configured to monitor the specified file or directory before calling this method. When you specify [true](../../swift/true.md) for the `flag` parameter, this method attempts to move the file or directory to the cloud and returns [true](../../swift/true.md) if it is successful. Calling this method also notifies your file presenter of the new location of the file so that your app can continue to operate on it.

> [!important] Important
> Avoid calling this method from your app’s main thread. This method performs a coordinated write operation on the specified file, which can block for a long time. Additionally, if the file presenter that is monitoring the file is incorrectly configured so that it receives messages on the main operation queue, calling this method on the main thread can cause a deadlock. Instead, use a dispatch queue to call this method from background thread. After the method returns, message your main thread to update the rest of your app’s data structures.
>
> After calling this method, you must wait for a file to be fully uploaded to iCloud before attempting to share the file using the [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<url(forpublishingubiquitousitemat_expiration_).md>) method.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Managing iCloud-based items

- [ubiquityIdentityToken](ubiquityidentitytoken.md) — An opaque token that represents the current user’s iCloud Drive Documents identity.
- [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) — Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [- isUbiquitousItemAtURL:](<isubiquitousitem(at_).md>) — Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [- startDownloadingUbiquitousItemAtURL:error:](<startdownloadingubiquitousitem(at_).md>) — Starts downloading (if necessary) the specified item to the local system.
- [- evictUbiquitousItemAtURL:error:](<evictubiquitousitem(at_).md>) — Removes the local copy of the specified item that’s stored in iCloud.
- [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<url(forpublishingubiquitousitemat_expiration_).md>) — Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.
