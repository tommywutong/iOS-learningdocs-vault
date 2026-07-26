---
title: 'download(_:didCreateDestination:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:didcreatedestination:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:didcreatedestination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Adidcreatedestination%3A%29.json'
content_hash: 'sha256:2a2f0c4c5cbba1a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:didCreateDestination:)

<sub>Instance Method</sub>

Sent when the destination file is created.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, didCreateDestination path: String)
```

## Parameters

- `download` — The URL download object sending the message.

- `path` — The path to the destination file.

## See Also

### Download Data and Responses

- [- download:decideDestinationWithSuggestedFilename:](<download(__decidedestinationwithsuggestedfilename_).md>) — The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [- downloadDidBegin:](<downloaddidbegin(__).md>) — Sent immediately after a download object begins a download.
- [- download:didReceiveResponse:](<download(__didreceive_)-817z3.md>) — Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [- download:didReceiveDataOfLength:](<download(__didreceivedataoflength_).md>) — Sent as a download object receives data incrementally.
- [- download:shouldDecodeSourceDataOfMIMEType:](<download(__shoulddecodesourcedataofmimetype_).md>) — Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [- download:willResumeWithResponse:fromByte:](<download(__willresumewith_frombyte_).md>) — Sent when a download object has received a response from the server after attempting to resume a download.
- [- download:willSendRequest:redirectResponse:](<download(__willsend_redirectresponse_).md>) — Sent when the download object determines that it must change URLs in order to continue loading a request.
