---
title: 'connectionDidResumeDownloading(_:totalBytesWritten:expectedTotalBytes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondownloaddelegate/connectiondidresumedownloading(_:totalbyteswritten:expectedtotalbytes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/connectiondidresumedownloading(_:totalbyteswritten:expectedtotalbytes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondownloaddelegate/connectiondidresumedownloading%28_%3Atotalbyteswritten%3Aexpectedtotalbytes%3A%29.json'
content_hash: 'sha256:931e5480e860c396'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDownloadDelegate](../nsurlconnectiondownloaddelegate.md)

# connectionDidResumeDownloading(_:totalBytesWritten:expectedTotalBytes:)

<sub>Instance Method</sub>

Sent to the delegate when an URL connection resumes downloading a URL asset that was earlier suspended.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connectionDidResumeDownloading(_ connection: NSURLConnection, totalBytesWritten: Int64, expectedTotalBytes: Int64)
```

## Parameters

- `connection` — The URL connection object downloading the asset.

- `totalBytesWritten` — The total number of bytes of the downloading asset that have been written to the destination file.

- `expectedTotalBytes` — The total number of bytes of the URL asset once it is completely downloaded and written to a file.

## Discussion

This method is invoked once a suspended download of a URL asset resumes downloading. In response, the delegate can display a progress indicator, setting the initial value of the indicator to where it was when downloading was suspended. After the URL-connection object sends this message, it sends one or more [- connection:didWriteData:totalBytesWritten:expectedTotalBytes:](<connection(__didwritedata_totalbyteswritten_expectedtotalbytes_).md>) to the delegate until the download concludes.

## See Also

### Managing Downloads of URL Assets

- [- connection:didWriteData:totalBytesWritten:expectedTotalBytes:](<connection(__didwritedata_totalbyteswritten_expectedtotalbytes_).md>) — Sent to the delegate to deliver progress information for a download of a URL asset to a destination file.
- [- connectionDidFinishDownloading:destinationURL:](<connectiondidfinishdownloading(__destinationurl_).md>) — Sent to the delegate when the URL connection has successfully downloaded the URL asset to a destination file.
