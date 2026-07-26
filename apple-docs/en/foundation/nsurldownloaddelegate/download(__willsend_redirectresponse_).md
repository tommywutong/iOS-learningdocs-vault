---
title: 'download(_:willSend:redirectResponse:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurldownloaddelegate/download(_:willsend:redirectresponse:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurldownloaddelegate/download(_:willsend:redirectresponse:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurldownloaddelegate/download%28_%3Awillsend%3Aredirectresponse%3A%29.json'
content_hash: 'sha256:4343decd2a461505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLDownloadDelegate](../nsurldownloaddelegate.md)

# download(_:willSend:redirectResponse:)

<sub>Instance Method</sub>

Sent when the download object determines that it must change URLs in order to continue loading a request.

<sub>macOS</sub>

```swift
optional func download(_ download: NSURLDownload, willSend request: URLRequest, redirectResponse: URLResponse?) -> URLRequest?
```

## Parameters

- `download` — The URL download object sending the message.

- `request` — The proposed redirected request. The delegate should inspect the redirected request to verify that it meets its needs, and create a copy with new attributes to return to the connection if necessary.

- `redirectResponse` — The URL response that caused the redirect. May be `nil` in cases where this method is not being sent as a result of involving the delegate in redirect processing.

## Return Value

The actual URL request to use in light of the redirection response. The delegate may copy and modify `request` as necessary to change its attributes, return `request` unmodified, or return `nil`.

## Discussion

If the delegate wishes to cancel the redirect, it should call the `download` object’s [- cancel](<../nsurldownload/cancel().md>) method. Alternatively, the delegate method can return `nil` to cancel the redirect, and the download will continue to process. This has special relevance in the case where `redirectResponse` is not `nil`. In this case, any data that is loaded for the download will be sent to the delegate, and the delegate will receive a [- downloadDidFinish:](<downloaddidfinish(__).md>) or [- download:didFailWithError:](<download(__didfailwitherror_).md>) message, as appropriate.

### Special Considerations

The delegate can receive this message as a result of transforming a request’s URL to its canonical form, or for protocol-specific reasons, such as an HTTP redirect. The delegate implementation should be prepared to receive this message multiple times.

## See Also

### Download Data and Responses

- [- download:decideDestinationWithSuggestedFilename:](<download(__decidedestinationwithsuggestedfilename_).md>) — The delegate receives this message when `download` has determined a suggested filename for the downloaded file.
- [- downloadDidBegin:](<downloaddidbegin(__).md>) — Sent immediately after a download object begins a download.
- [- download:didCreateDestination:](<download(__didcreatedestination_).md>) — Sent when the destination file is created.
- [- download:didReceiveResponse:](<download(__didreceive_)-817z3.md>) — Sent when a download object has received sufficient load data to construct the NSURLResponse object for the download.
- [- download:didReceiveDataOfLength:](<download(__didreceivedataoflength_).md>) — Sent as a download object receives data incrementally.
- [- download:shouldDecodeSourceDataOfMIMEType:](<download(__shoulddecodesourcedataofmimetype_).md>) — Sent when a download object determines that the downloaded file is encoded to inquire whether the file should be automatically decoded.
- [- download:willResumeWithResponse:fromByte:](<download(__willresumewith_frombyte_).md>) — Sent when a download object has received a response from the server after attempting to resume a download.
