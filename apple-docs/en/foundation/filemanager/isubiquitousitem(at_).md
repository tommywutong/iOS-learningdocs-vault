---
title: 'isUbiquitousItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/isubiquitousitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/isubiquitousitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/isubiquitousitem%28at%3A%29.json'
content_hash: 'sha256:d80433b3056c562c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# isUbiquitousItem(at:)

<sub>Instance Method</sub>

Returns a Boolean indicating whether the item is targeted for storage in iCloud.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isUbiquitousItem(at url: URL) -> Bool
```

## Parameters

- `url` — Specify the URL for the file or directory whose status you want to check.

## Return Value

[true](../../swift/true.md) if the item is targeted for iCloud storage or [false](../../swift/false.md) if it is not. This method also returns [false](../../swift/false.md) if no item exists at `url`.

## Discussion

This method reflects only whether the item should be stored in iCloud because a call was made to the  [- setUbiquitous:itemAtURL:destinationURL:error:](<setubiquitous(__itemat_destinationurl_).md>) method with a value of [true](../../swift/true.md) for its `flag` parameter. This method does not reflect whether the file has actually been uploaded to any iCloud servers. To determine a file’s upload status, check the `NSURLUbiquitousItemIsUploadedKey` attribute of the corresponding [NSURL](../nsurl.md) object.

## See Also

### Managing iCloud-based items

- [ubiquityIdentityToken](ubiquityidentitytoken.md) — An opaque token that represents the current user’s iCloud Drive Documents identity.
- [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) — Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [- setUbiquitous:itemAtURL:destinationURL:error:](<setubiquitous(__itemat_destinationurl_).md>) — Indicates whether the item at the specified URL should be stored in iCloud.
- [- startDownloadingUbiquitousItemAtURL:error:](<startdownloadingubiquitousitem(at_).md>) — Starts downloading (if necessary) the specified item to the local system.
- [- evictUbiquitousItemAtURL:error:](<evictubiquitousitem(at_).md>) — Removes the local copy of the specified item that’s stored in iCloud.
- [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<url(forpublishingubiquitousitemat_expiration_).md>) — Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.
