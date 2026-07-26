---
title: deletesFileUponFailure
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurldownload/deletesfileuponfailure
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/deletesfileuponfailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/deletesfileuponfailure.json'
content_hash: 'sha256:b7ba0bdda55b6cc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# deletesFileUponFailure

<sub>Instance Property</sub>

Returns whether the receiver deletes partially downloaded files when a download stops prematurely.

<sub>macOS</sub>

```swift
var deletesFileUponFailure: Bool { get set }
```

## Return Value

[true](../../swift/true.md) if partially downloaded files should be deleted when a download stops prematurely, [false](../../swift/false.md) otherwise. The default is [true](../../swift/true.md).

## See Also

### Resuming partial downloads

- [+ canResumeDownloadDecodedWithEncodingMIMEType:](<canresumedownloaddecoded(withencodingmimetype_).md>) — Returns whether a URL download object can resume a download that was decoded with the specified MIME type.
- [- initWithResumeData:delegate:path:](<init(resumedata_delegate_path_).md>) — Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download. _(deprecated)_
- [resumeData](resumedata.md) — Returns the resume data for a download that is not yet complete.
