---
title: Handling errors
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/handling-errors
source_url: 'https://developer.apple.com/documentation/storekit/handling-errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/handling-errors.json'
content_hash: 'sha256:a01701407739d4ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md)

# Handling errors

<sub>Article</sub>

Determine the underlying cause of errors that result from StoreKit requests.

## Overview

A StoreKit request may fail for one of many possible reasons, including invalid product information, invalid payment details, problems with your App Store Connect account, or networking issues. When an error occurs, check the error code to find out what went wrong.

### Determine the cause of the error

When handling errors, such as with the [- request:didFailWithError:](<skrequestdelegate/request(__didfailwitherror_).md>) delegate method, it’s important to use the [domain](../foundation/nserror/domain.md) and [code](../foundation/nserror/code.md) of the resulting error to determine the underlying cause of failure.

StoreKit uses [SKErrorDomain](skerrordomain.md) for errors related to payments, store products, and cloud services, as described in [Code](skerror/code.md). For additional information on troubleshooting StoreKit framework issues, see the [In-App Purchase FAQ](https://developer.apple.com/library/archive/technotes/tn2413/_index.html#//apple_ref/doc/uid/DTS40016228).

Errors related to networking use [NSURLErrorDomain](../foundation/nsurlerrordomain.md). The following table describes some of the most common networking errors that may occur when using StoreKit:

| Error code | Description |
|---|---|
| [NSURLErrorTimedOut](../foundation/nsurlerrortimedout-swift.var.md) (`-1001`) | The connection timed out. |
| [NSURLErrorCannotFindHost](../foundation/nsurlerrorcannotfindhost-swift.var.md) (`-1003`) | The connection failed because it can’t find the host. |
| [NSURLErrorCannotConnectToHost](../foundation/nsurlerrorcannotconnecttohost-swift.var.md) (`-1004`) | The connection failed because it can’t connect to the host. |
| [NSURLErrorNetworkConnectionLost](../foundation/nsurlerrornetworkconnectionlost-swift.var.md) (`-1005`) | The connection failed because it lost the network connection. |
| [NSURLErrorNotConnectedToInternet](../foundation/nsurlerrornotconnectedtointernet-swift.var.md) (`-1009`) | The connection failed because the device isn’t connected to the internet. |
| [NSURLErrorUserCancelledAuthentication](../foundation/nsurlerrorusercancelledauthentication-swift.var.md) (`-1012`) | The connection failed because the user canceled required authentication. |
| [NSURLErrorSecureConnectionFailed](../foundation/nsurlerrorsecureconnectionfailed-swift.var.md) (`-1200`) | The secure connection failed for an unknown reason. |

## See Also

### Errors

- [Code](skerror/code.md) — Error codes for StoreKit errors.
- [SKError](skerror.md) — StoreKit error descriptions, codes, and domains.
- [SKErrorDomain](skerrordomain.md) — The error domain name for StoreKit errors.
