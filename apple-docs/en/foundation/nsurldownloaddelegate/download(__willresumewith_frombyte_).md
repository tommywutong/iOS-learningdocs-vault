---
title: 'download(_:willResumeWith:fromByte:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:willresumewith:frombyte:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:willresumewith:frombyte:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Awillresumewith%3Afrombyte%3A%29.json'
content_hash: 'sha256:ad3e1151cdeb1d24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:willResumeWith:fromByte:)

<sub>Instance Method</sub>

Sent when a download object has received a response from the server after attempting to resume a download.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, willResumeWith response: URLResponse, fromByte startingByte: Int64)
```

## Parameters

- `download` — The URL download object sending the message.

- `response` — The URL response received from the server in response to an attempt to resume a download.

- `startingByte` — The location of the start of the resumed data, in bytes.

## See Also

### Download Data and Responses

- [- download:decideDestinationWithSuggestedFilename:](<download(__decidedestinationwithsuggestedfilename_).md>) — The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [- downloadDidBegin:](<downloaddidbegin(__).md>) — Sent immediately after a download object begins a download.
- [- download:didCreateDestination:](<download(__didcreatedestination_).md>) — Sent when the destination file is created.
- [- download:didReceiveResponse:](<download(__didreceive_)-817z3.md>) — Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [- download:didReceiveDataOfLength:](<download(__didreceivedataoflength_).md>) — Sent as a download object receives data incrementally.
- [- download:shouldDecodeSourceDataOfMIMEType:](<download(__shoulddecodesourcedataofmimetype_).md>) — Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [- download:willSendRequest:redirectResponse:](<download(__willsend_redirectresponse_).md>) — Sent when the download object determines that it must change URLs in order to continue loading a request.
