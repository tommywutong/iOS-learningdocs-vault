---
title: NSURLDownload
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurldownload
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload.json'
content_hash: 'sha256:51a5453c71147c43'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLDownload

<sub>Class</sub>

An object that downloads a resource asynchronously and saves the data to a file.

<sub>macOS</sub>

```swift
class NSURLDownload
```

## Overview

> [!important] Important
> This API is considered legacy. Use [URLSession](urlsession.md) instead.

The interface for [NSURLDownload](nsurldownload.md) provides methods to initialize a download, set the destination path and cancel loading the request.

The delegate object assigned to each instance of this class should implement the methods defined by the [NSURLDownloadDelegate](nsurldownloaddelegate.md) protocol. These methods provide the delegate with the current status of in-progress asynchronous downloads and allow the delegate to customize the URL loading process. These delegate methods are called on the thread that started the asynchronous load operation for the associated [NSURLDownload](nsurldownload.md) object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating and configuring a download instance

- [- initWithRequest:delegate:](<nsurldownload/init(request_delegate_).md>) — Returns an initialized URL download for a URL request and begins to download the data for the request. _(deprecated)_
- [- setDestination:allowOverwrite:](<nsurldownload/setdestination(__allowoverwrite_).md>) — Sets the destination path of the downloaded file.

### Resuming partial downloads

- [+ canResumeDownloadDecodedWithEncodingMIMEType:](<nsurldownload/canresumedownloaddecoded(withencodingmimetype_).md>) — Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [- initWithResumeData:delegate:path:](<nsurldownload/init(resumedata_delegate_path_).md>) — Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download. _(deprecated)_
- [resumeData](nsurldownload/resumedata.md) — Returns the resume data for a download that is not yet complete.
- [deletesFileUponFailure](nsurldownload/deletesfileuponfailure.md) — Returns whether the receiver deletes partially downloaded files when a download stops prematurely.

### Canceling a download

- [- cancel](<nsurldownload/cancel().md>) — Cancels the receiver’s download and deletes the downloaded file.

### Getting download properties

- [request](nsurldownload/request.md) — Returns the request that initiated the receiver’s download.
- [deletesFileUponFailure](nsurldownload/deletesfileuponfailure.md) — Returns whether the receiver deletes partially downloaded files when a download stops prematurely.

## See Also

### URL Download

- [NSURLDownloadDelegate](nsurldownloaddelegate.md) — A protocol that URL download delegates implement to interact with a URL download request.
