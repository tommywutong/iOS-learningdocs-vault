---
title: 'download(_:didReceiveDataOfLength:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:didreceivedataoflength:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didreceivedataoflength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Adidreceivedataoflength%3A%29.json'
content_hash: 'sha256:f3b20e313b836818'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:didReceiveDataOfLength:)

<sub>Instance Method</sub>

Sent as a download object receives data incrementally.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, didReceiveDataOfLength length: Int)
```

## Parameters

- `download` — The URL download object sending the message.

- `length` — The amount of data received in this increment of the download, measured in bytes.

## See Also

### Download Data and Responses

- [- download:decideDestinationWithSuggestedFilename:](<download(__decidedestinationwithsuggestedfilename_).md>) — The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [- downloadDidBegin:](<downloaddidbegin(__).md>) — Sent immediately after a download object begins a download.
- [- download:didCreateDestination:](<download(__didcreatedestination_).md>) — Sent when the destination file is created.
- [- download:didReceiveResponse:](<download(__didreceive_)-817z3.md>) — Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [- download:shouldDecodeSourceDataOfMIMEType:](<download(__shoulddecodesourcedataofmimetype_).md>) — Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [- download:willResumeWithResponse:fromByte:](<download(__willresumewith_frombyte_).md>) — Sent when a download object has received a response from the server after attempting to resume a download.
- [- download:willSendRequest:redirectResponse:](<download(__willsend_redirectresponse_).md>) — Sent when the download object determines that it must change URLs in order to continue loading a request.
