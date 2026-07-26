---
title: 'download(_:decideDestinationWithSuggestedFilename:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:decidedestinationwithsuggestedfilename:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:decidedestinationwithsuggestedfilename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Adecidedestinationwithsuggestedfilename%3A%29.json'
content_hash: 'sha256:7aced50395769d14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:decideDestinationWithSuggestedFilename:)

<sub>Instance Method</sub>

The delegate receives this message when `download` has determined a suggested filename for the downloaded file.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, decideDestinationWithSuggestedFilename filename: String)
```

## Parameters

- `download` — The URL download object sending the message.

- `filename` — The suggested filename for the download.

## Discussion

The suggested filename is either derived from the last path component of the URL and the MIME type or, if the download was encoded, from the encoding. If the delegate wishes to modify the path, it should send [- setDestination:allowOverwrite:](<../nsurldownload/setdestination(__allowoverwrite_).md>) to `download`.

### Special Considerations

The delegate will not receive this message if `setDestination:allowOverwrite:` has already been called for the download.

## See Also

### Download Data and Responses

- [- downloadDidBegin:](<downloaddidbegin(__).md>) — Sent immediately after a download object begins a download.
- [- download:didCreateDestination:](<download(__didcreatedestination_).md>) — Sent when the destination file is created.
- [- download:didReceiveResponse:](<download(__didreceive_)-817z3.md>) — Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [- download:didReceiveDataOfLength:](<download(__didreceivedataoflength_).md>) — Sent as a download object receives data incrementally.
- [- download:shouldDecodeSourceDataOfMIMEType:](<download(__shoulddecodesourcedataofmimetype_).md>) — Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [- download:willResumeWithResponse:fromByte:](<download(__willresumewith_frombyte_).md>) — Sent when a download object has received a response from the server after attempting to resume a download.
- [- download:willSendRequest:redirectResponse:](<download(__willsend_redirectresponse_).md>) — Sent when the download object determines that it must change URLs in order to continue loading a request.
