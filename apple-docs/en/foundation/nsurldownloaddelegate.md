---
title: NSURLDownloadDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurldownloaddelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate.json'
content_hash: 'sha256:d4a9431c73de262d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLDownloadDelegate

<sub>Protocol</sub>

A protocol that URL download delegates implement to interact with a URL download request.

<sub>macOS</sub>

```swift
protocol NSURLDownloadDelegate : NSObjectProtocol
```

## Overview

The [NSURLDownloadDelegate](nsurldownloaddelegate.md) protocol defines methods that allow an object to receive informational callbacks about the asynchronous load of a download’s URL request. Other delegate methods provide facilities that allow the delegate to customize the process of performing an asynchronous URL load.

Note that these delegate methods will be called on the thread that started the asynchronous load operation for the associated [NSURLDownload](nsurldownload.md) object.

- A [- downloadDidBegin:](<nsurldownloaddelegate/downloaddidbegin(__).md>) message will be sent to the delegate immediately upon starting the download.
- Zero or more [- download:willSendRequest:redirectResponse:](<nsurldownloaddelegate/download(__willsend_redirectresponse_).md>) messages will be sent to the delegate before any further messages are sent if it is determined that the download must redirect to a new location. The delegate can allow the redirect, modify the destination or deny the redirect.
- Zero or more [- download:didReceiveAuthenticationChallenge:](<nsurldownloaddelegate/download(__didreceive_)-1pc0v.md>) messages will be sent to the delegate if it is necessary to authenticate in order to download the request and NSURLDownload does not already have authenticated credentials.
- Zero or more [- download:didCancelAuthenticationChallenge:](<nsurldownloaddelegate/download(__didcancel_).md>) messages will be sent to the delegate if [NSURLDownload](nsurldownload.md) cancels the authentication challenge due to encountering a protocol implementation error.
- Zero or more [- download:didReceiveResponse:](<nsurldownloaddelegate/download(__didreceive_)-817z3.md>) messages will be sent to the delegate before receiving a [- download:didReceiveDataOfLength:](<nsurldownloaddelegate/download(__didreceivedataoflength_).md>) message. The only case where [- download:didReceiveResponse:](<nsurldownloaddelegate/download(__didreceive_)-817z3.md>) is not sent to a delegate is when the protocol implementation encounters an error before a response could be created.
- Zero or more [- download:didReceiveDataOfLength:](<nsurldownloaddelegate/download(__didreceivedataoflength_).md>) messages will be sent before [- downloadDidFinish:](<nsurldownloaddelegate/downloaddidfinish(__).md>) or [- download:didFailWithError:](<nsurldownloaddelegate/download(__didfailwitherror_).md>) is sent to the delegate.
- Zero or one [- download:decideDestinationWithSuggestedFilename:](<nsurldownloaddelegate/download(__decidedestinationwithsuggestedfilename_).md>) will be sent to the delegate when sufficient information has been received to determine the suggested filename for the downloaded file. The delegate will not receive this message if [- setDestination:allowOverwrite:](<nsurldownload/setdestination(__allowoverwrite_).md>) has already been sent to the [NSURLDownload](nsurldownload.md) instance.
- A [- download:didCreateDestination:](<nsurldownloaddelegate/download(__didcreatedestination_).md>) message will be sent to the delegate when the [NSURLDownload](nsurldownload.md) instance creates the file on disk.
- If NSURLDownload determines that the downloaded file is in a format that it is able to decode (MacBinary, Binhex or gzip), the delegate will receive a [- download:shouldDecodeSourceDataOfMIMEType:](<nsurldownloaddelegate/download(__shoulddecodesourcedataofmimetype_).md>). The delegate should return [true](../swift/true.md) to decode the data, [false](../swift/false.md) otherwise.
- Unless an [NSURLDownload](nsurldownload.md) instance receives a [- cancel](<nsurldownload/cancel().md>) message, the delegate will receive one and only one [- downloadDidFinish:](<nsurldownloaddelegate/downloaddidfinish(__).md>) or [- download:didFailWithError:](<nsurldownloaddelegate/download(__didfailwitherror_).md>) message, but never both. In addition, once either of these messages are sent, the delegate will receive no further messages for the given [NSURLDownload](nsurldownload.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Download Authentication

- [- download:canAuthenticateAgainstProtectionSpace:](<nsurldownloaddelegate/download(__canauthenticateagainstprotectionspace_).md>) — Sent to determine whether the delegate is able to respond to a protection space’s form of authentication.
- [- download:didCancelAuthenticationChallenge:](<nsurldownloaddelegate/download(__didcancel_).md>) — Sent if an authentication challenge is canceled due to the protocol implementation encountering an error.
- [- download:didReceiveAuthenticationChallenge:](<nsurldownloaddelegate/download(__didreceive_)-1pc0v.md>) — Sent when the URL download must authenticate a challenge in order to download the request.
- [- downloadShouldUseCredentialStorage:](<nsurldownloaddelegate/downloadshouldusecredentialstorage(__).md>) — Sent to determine whether the URL loader should consult the credential storage to authenticate the download.

### Download Data and Responses

- [- download:decideDestinationWithSuggestedFilename:](<nsurldownloaddelegate/download(__decidedestinationwithsuggestedfilename_).md>) — The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [- downloadDidBegin:](<nsurldownloaddelegate/downloaddidbegin(__).md>) — Sent immediately after a download object begins a download.
- [- download:didCreateDestination:](<nsurldownloaddelegate/download(__didcreatedestination_).md>) — Sent when the destination file is created.
- [- download:didReceiveResponse:](<nsurldownloaddelegate/download(__didreceive_)-817z3.md>) — Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [- download:didReceiveDataOfLength:](<nsurldownloaddelegate/download(__didreceivedataoflength_).md>) — Sent as a download object receives data incrementally.
- [- download:shouldDecodeSourceDataOfMIMEType:](<nsurldownloaddelegate/download(__shoulddecodesourcedataofmimetype_).md>) — Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [- download:willResumeWithResponse:fromByte:](<nsurldownloaddelegate/download(__willresumewith_frombyte_).md>) — Sent when a download object has received a response from the server after attempting to resume a download.
- [- download:willSendRequest:redirectResponse:](<nsurldownloaddelegate/download(__willsend_redirectresponse_).md>) — Sent when the download object determines that it must change URLs in order to continue loading a request.

### Download Completion

- [- download:didFailWithError:](<nsurldownloaddelegate/download(__didfailwitherror_).md>) — Sent if the download fails or if an I/O error occurs when the file is written to disk.
- [- downloadDidFinish:](<nsurldownloaddelegate/downloaddidfinish(__).md>) — Sent when a download object has completed downloading successfully and has written its results to disk.

## See Also

### URL Download

- [NSURLDownload](nsurldownload.md) — An object that downloads a resource asynchronously and saves the data to a file.
