---
title: 'canResumeDownloadDecoded(withEncodingMIMEType:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownload/canresumedownloaddecoded(withencodingmimetype:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownload/canresumedownloaddecoded(withencodingmimetype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownload/canresumedownloaddecoded%28withencodingmimetype%3A%29.json'
content_hash: 'sha256:c97eb3a1d2de8024'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownload](../nsurldownload.md)

# canResumeDownloadDecoded(withEncodingMIMEType:)

<sub>Type Method</sub>

Returns whether a URL download object can resume a download that was decoded with the specified MIME type.

<sub>macOS</sub>

```swift
class func canResumeDownloadDecoded(withEncodingMIMEType MIMEType: String) -> Bool
```

## Parameters

- `MIMEType` — The MIME type the caller wants to know about.

## Return Value

[true](../../swift/true.md) if the URL download object can resume a download that was decoded with the specified MIME type, [false](../../swift/false.md) otherwise.

## Discussion

The MIME type of a file, in conjunction with the value returned by the [- download:shouldDecodeSourceDataOfMIMEType:](<../nsurldownloaddelegate/download(__shoulddecodesourcedataofmimetype_).md>) delegate method, determines whether the `NSURLDownload` class should decode or decompress the incoming data as it is received.

Some compression techniques, such as the `DEFLATE` algorithm (`gzip`) use symbol dictionaries that vary during the compression process, making it impractical to decompress only a portion of the data starting in the middle. For this reason, this method returns [false](../../swift/false.md) unless both of the following conditions are met:

- The MIME type is of a type that the `NSURLDownload` class knows how to decompress or decode.
- The decoding can be safely resumed.

In practice, this method returns [true](../../swift/true.md) for MacBinary and BinHex, otherwise [false](../../swift/false.md).

If your app needs to be able to resume file downloads in `gzip` format, your [- download:shouldDecodeSourceDataOfMIMEType:](<../nsurldownloaddelegate/download(__shoulddecodesourcedataofmimetype_).md>) method must return [false](../../swift/false.md), and you must decode the resulting file yourself after you finish downloading it in its entirety.

## See Also

### Resuming partial downloads

- [- initWithResumeData:delegate:path:](<init(resumedata_delegate_path_).md>) — Returns an initialized NSURLDownload object that will resume downloading the specified data to the specified file and begins the download. _(deprecated)_
- [resumeData](resumedata.md) — Returns the resume data for a download that is not yet complete.
- [deletesFileUponFailure](deletesfileuponfailure.md) — Returns whether the receiver deletes partially downloaded files when a download stops prematurely.
