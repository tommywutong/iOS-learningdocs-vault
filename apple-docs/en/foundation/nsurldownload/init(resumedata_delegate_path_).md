---
title: 'init(resumeData:delegate:path:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.3+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsurldownload/init(resumedata:delegate:path:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/init(resumedata:delegate:path:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/init%28resumedata%3Adelegate%3Apath%3A%29.json'
content_hash: 'sha256:2121bf9291085a43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# init(resumeData:delegate:path:)

<sub>Initializer</sub>

Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download.

> [!warning] Deprecated
> Use NSURLSession downloadTask (see NSURLSession.h)

<sub>macOS</sub>

```swift
init(resumeData: Data, delegate: (any NSURLDownloadDelegate)?, path: String)
```

## Parameters

- `resumeData` — Specifies the data to resume downloading.

- `delegate` — The delegate for the download. This object will receive delegate messages as the download progresses. Delegate messages will be sent on the thread which calls this method. For the download to work correctly the calling thread’s run loop must be operating in the default run loop mode. The `NSURLDownload` class maintains a strong reference to this delegate object.

- `path` — The location for the downloaded data.

## Return Value

An initialized NSURLDownload object.

## Discussion

If you want to support pausing and resuming downloads, your app must:

1. Call [deletesFileUponFailure](deletesfileuponfailure.md), passing [false](../../swift/false.md). If you want to support resuming downloads in the event of a lost connection, you should do this immediately after you initialize the download object.
2. If your app needs to pause the transfer for any reason, call [- cancel](<cancel().md>). Because your app previously called [deletesFileUponFailure](deletesfileuponfailure.md) with [false](../../swift/false.md), the in-progress download is not deleted.
3. After your app pauses the transfer or after a transfer error occurs, call [resumeData](resumedata.md) to obtain the data needed to resume the transfer later.

> [!note] Note
> Resume data is returned only if both the protocol and the server support resuming.
>
> In addition, a download of compressed content cannot be resumed if `NSURLDownload` is configured to decompress that data on the fly; for details, read the documentation for the [+ canResumeDownloadDecodedWithEncodingMIMEType:](<canresumedownloaddecoded(withencodingmimetype_).md>) method.

1. If the transfer failed because of a connectivity error, use the `SCNetworkReachability` API to determine an appropriate time to try again. For details, read [SCNetworkReachability](../../systemconfiguration/scnetworkreachability.md).

If your app explicitly paused the download, wait until it is appropriate to continue the transfer (such as when the user clicks or taps a resume button). 5. Call [- initWithResumeData:delegate:path:](<init(resumedata_delegate_path_).md>) and pass the resume data blob that it previously obtained in step 3.

## See Also

### Related Documentation

- [- cancel](<cancel().md>) — Cancels the receiver’s download and deletes the downloaded file.

### Resuming partial downloads

- [+ canResumeDownloadDecodedWithEncodingMIMEType:](<canresumedownloaddecoded(withencodingmimetype_).md>) — Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [resumeData](resumedata.md) — Returns the resume data for a download that is not yet complete.
- [deletesFileUponFailure](deletesfileuponfailure.md) — Returns whether the receiver deletes partially downloaded files when a download stops prematurely.
