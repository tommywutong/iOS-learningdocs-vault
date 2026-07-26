---
title: 'connectionDidFinishDownloading(_:destinationURL:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondownloaddelegate/connectiondidfinishdownloading(_:destinationurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondownloaddelegate/connectiondidfinishdownloading(_:destinationurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondownloaddelegate/connectiondidfinishdownloading%28_%3Adestinationurl%3A%29.json'
content_hash: 'sha256:e445bdbf7837fe05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDownloadDelegate](../nsurlconnectiondownloaddelegate.md)

# connectionDidFinishDownloading(_:destinationURL:)

<sub>Instance Method</sub>

Sent to the delegate when the URL connection has successfully downloaded the URL asset to a destination file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func connectionDidFinishDownloading(_ connection: NSURLConnection, destinationURL: URL)
```

## Parameters

- `connection` — The URL connection object that downloaded the asset.

- `destinationURL` — A file URL specifying a destination in the file system. For iOS applications, this is a location in the application sandbox.

## Discussion

This method will be called once after a successful download. The file downloaded to `destinationURL` is guaranteed to exist there only for the duration of this method implementation; the delegate should copy or move the file to a more persistent and appropriate location.

## See Also

### Managing Downloads of URL Assets

- [- connection:didWriteData:totalBytesWritten:expectedTotalBytes:](<connection(__didwritedata_totalbyteswritten_expectedtotalbytes_).md>) — Sent to the delegate to deliver progress information for a download of a URL asset to a destination file.
- [- connectionDidResumeDownloading:totalBytesWritten:expectedTotalBytes:](<connectiondidresumedownloading(__totalbyteswritten_expectedtotalbytes_).md>) — Sent to the delegate when an URL connection resumes downloading a URL asset that was earlier suspended.
