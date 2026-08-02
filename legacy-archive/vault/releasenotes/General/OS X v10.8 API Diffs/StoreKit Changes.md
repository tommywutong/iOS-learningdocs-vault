---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/StoreKit.html
archived_at: '2026-07-18T02:54:06.824621Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# StoreKit Changes

## StoreKit

SKDownload.hAdded [SKDownload](https://developer.apple.com/documentation/storekit/skdownload)Added [SKDownload.contentIdentifier](https://developer.apple.com/documentation/storekit/skdownload/1458941-contentidentifier)Added [SKDownload.contentLength](https://developer.apple.com/documentation/storekit/skdownload/1458932-contentlength)Added [SKDownload.contentURL](https://developer.apple.com/documentation/storekit/skdownload/1458930-contenturl)Added [+[SKDownload contentURLForProductID:]](https://developer.apple.com/documentation/storekit/skdownload/1458924-contenturlforproductid)Added [SKDownload.contentVersion](https://developer.apple.com/documentation/storekit/skdownload/1458916-contentversion)Added [+[SKDownload deleteContentForProductID:]](https://developer.apple.com/documentation/storekit/skdownload/1458926-deletecontent)Added [SKDownload.error](https://developer.apple.com/documentation/storekit/skdownload/1458914-error)Added [SKDownload.progress](https://developer.apple.com/documentation/storekit/skdownload/1458945-progress)Added [SKDownload.state](https://developer.apple.com/documentation/storekit/skdownload/1458937-state)Added [SKDownload.timeRemaining](https://developer.apple.com/documentation/storekit/skdownload/1458943-timeremaining)Added [SKDownloadState](https://developer.apple.com/documentation/storekit/skdownloadstate)Added [SKDownloadStateActive](https://developer.apple.com/documentation/storekit/skdownloadstate/active)Added [SKDownloadStateCancelled](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatecancelled)Added [SKDownloadStateFailed](https://developer.apple.com/documentation/storekit/skdownloadstate/skdownloadstatefailed)Added [SKDownloadStateFinished](https://developer.apple.com/documentation/storekit/skdownloadstate/finished)Added [SKDownloadStatePaused](https://developer.apple.com/documentation/storekit/skdownloadstate/paused)Added [SKDownloadStateWaiting](https://developer.apple.com/documentation/storekit/skdownloadstate/waiting)SKPaymentQueue.hAdded [-[SKPaymentQueue cancelDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506092-cancel)Added [-[SKPaymentQueue pauseDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506053-pause)Added [-[SKPaymentQueue resumeDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1506096-resume)Added [-[SKPaymentQueue startDownloads:]](https://developer.apple.com/documentation/storekit/skpaymentqueue/1505998-start)Added [-[SKPaymentTransactionObserver paymentQueue:updatedDownloads:]](https://developer.apple.com/documentation/storekit/skpaymenttransactionobserver/1506073-paymentqueue)SKPaymentTransaction.hAdded [SKPaymentTransaction.downloads](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411282-downloads)SKProduct.hAdded [SKProduct.contentLengths](https://developer.apple.com/documentation/storekit/skproduct/1506157-contentlengths)Added [SKProduct.contentVersion](https://developer.apple.com/documentation/storekit/skproduct/1505996-contentversion)Added [SKProduct.downloadable](https://developer.apple.com/documentation/storekit/skproduct/1506161-downloadable)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
