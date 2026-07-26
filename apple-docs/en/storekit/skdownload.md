---
title: SKDownload
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+（16.0 起废弃）, iPadOS 6.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, watchOS 6.2+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skdownload
source_url: 'https://developer.apple.com/documentation/storekit/skdownload'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload.json'
content_hash: 'sha256:9c2c55faf0c90f01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKDownload

<sub>Class</sub>

Downloadable content associated with a product.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
class SKDownload
```

## Overview

When you create a product in App Store Connect, you can associate one or more pieces of downloadable content with it. At runtime, when a product is purchased by a user, your app uses [SKDownload](skdownload.md) objects to download the content from the App Store.

Your app never directly creates a [SKDownload](skdownload.md) object. Instead, after a payment is processed, your app reads the transaction object’s [downloads](skpaymenttransaction/downloads.md) property to retrieve an array of [SKDownload](skdownload.md) objects associated with the transaction.

To download the content, you queue a download object on the payment queue and wait for the content to be downloaded. After a download completes, read the download object’s [contentURL](skdownload/contenturl.md) property to get a URL to the downloaded content. Your app must process the downloaded file before completing the transaction. For example, it might copy the file into a directory whose contents are persistent. When all downloads are complete, you finish the transaction. After the transaction is finished, the download objects cannot be queued to the payment queue and any URLs to the downloaded content are invalid.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting Content Information

- [expectedContentLength](skdownload/expectedcontentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_
- [contentIdentifier](skdownload/contentidentifier.md) — A string that uniquely identifies the downloadable content. _(deprecated)_
- [contentVersion](skdownload/contentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [transaction](skdownload/transaction.md) — The transaction associated with the downloadable file. _(deprecated)_
- [contentLength](skdownload/contentlength.md) — The length of the downloadable content, in bytes. _(deprecated)_

### Getting State Information

- [state](skdownload/state.md) — The current state of the download object. _(deprecated)_
- [progress](skdownload/progress.md) — A value that indicates how much of the file has been downloaded. _(deprecated)_
- [timeRemaining](skdownload/timeremaining.md) — An estimated time, in seconds, to finish downloading the content. _(deprecated)_
- [SKDownloadTimeRemainingUnknown](skdownloadtimeremainingunknown.md) — Indicates that the system cannot determine how much time is needed to finish downloading the content. _(deprecated)_
- [SKDownloadState](skdownloadstate.md) — The states that a download operation can be in. _(deprecated)_
- [downloadState](skdownload/downloadstate.md) — The current state of the download object. _(deprecated)_

### Accessing a Completed Download

- [error](skdownload/error.md) — The error that prevented the content from being downloaded. _(deprecated)_
- [contentURL](skdownload/contenturl.md) — The local location of the downloaded file. _(deprecated)_

### Managing Downloaded Content

- [+ contentURLForProductID:](<skdownload/contenturl(forproductid_).md>) — Returns the local location for the previously downloaded flie. _(deprecated)_
- [+ deleteContentForProductID:](<skdownload/deletecontent(forproductid_).md>) — Deletes the previously downloaded file. _(deprecated)_

## See Also

### Content delivery

- [Unlocking purchased content](unlocking-purchased-content.md) — Deliver content to the customer after validating the purchase.
- [Persisting a purchase](persisting-a-purchase.md) — Keep a persistent record of a purchase to continue making the product available as needed.
- [Finishing a transaction](finishing-a-transaction.md) — Finish the transaction to complete the purchase process.
