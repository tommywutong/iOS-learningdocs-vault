---
title: resumeData
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurldownload/resumedata
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/resumedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/resumedata.json'
content_hash: 'sha256:728a8ca3f6ffded4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# resumeData

<sub>Instance Property</sub>

Returns the resume data for a download that is not yet complete.

<sub>macOS</sub>

```swift
var resumeData: Data? { get }
```

## Return Value

The resume data for a download that is not yet complete. This data represents the necessary state information that an `NSURLDownload` object needs to resume a download. The resume data can later be used when initializing a download with [- initWithResumeData:delegate:path:](<init(resumedata_delegate_path_).md>). Returns `nil` if the download is not able to be resumed.

## Discussion

Resume data is returned only if both the protocol and the server support resuming. For details on how to resume a connection, see the documentation for [- initWithResumeData:delegate:path:](<init(resumedata_delegate_path_).md>).

## See Also

### Resuming partial downloads

- [+ canResumeDownloadDecodedWithEncodingMIMEType:](<canresumedownloaddecoded(withencodingmimetype_).md>) — Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [- initWithResumeData:delegate:path:](<init(resumedata_delegate_path_).md>) — Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download. _(deprecated)_
- [deletesFileUponFailure](deletesfileuponfailure.md) — Returns whether the receiver deletes partially downloaded files when a download stops prematurely.
