---
title: 'data(for:delegate:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/data(for:delegate:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/data(for:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/data%28for%3Adelegate%3A%29.json'
content_hash: 'sha256:7746d1572e79b183'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# data(for:delegate:)

<sub>Instance Method</sub>

Downloads the contents of a URL based on the specified URL request and delivers the data asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func data(for request: URLRequest, delegate: (any URLSessionTaskDelegate)? = nil) async throws -> (Data, URLResponse)
```

## Parameters

- `request` — A URL request object that provides request-specific information such as the URL, cache policy, request type, and body data or body stream.

- `delegate` — A delegate that receives life cycle and authentication challenge callbacks as the transfer progresses.

## Return Value

An asynchronously-delivered tuple that contains the URL contents as a [Data](../data.md) instance, and a [URLResponse](../urlresponse.md).

## Discussion

Use this method to wait until the session finishes transferring data and receive it in a single [Data](../data.md) instance. To process the bytes as the session receives them, use [bytes(for:delegate:)](<bytes(for_delegate_).md>).

## See Also

### Performing asynchronous transfers

- [bytes(for:delegate:)](<bytes(for_delegate_).md>) — Retrieves the contents of a URL based on the specified URL request and delivers an asynchronous sequence of bytes.
- [bytes(from:delegate:)](<bytes(from_delegate_).md>) — Retrieves the contents of a given URL and delivers an asynchronous sequence of bytes.
- [AsyncBytes](asyncbytes.md) — An asynchronous sequence of bytes.
- [data(from:delegate:)](<data(from_delegate_).md>) — Retrieves the contents of a URL and delivers the data asynchronously.
- [data(for:)](<data(for_).md>) — Convenience method to load data using a URLRequest, creates and resumes a URLSessionDataTask internally.
- [data(from:)](<data(from_).md>) — Convenience method to load data using a URL, creates and resumes a URLSessionDataTask internally.
- [download(for:delegate:)](<download(for_delegate_).md>) — Retrieves the contents of a URL based on the specified URL request and delivers the URL of the saved file asynchronously.
- [download(from:delegate:)](<download(from_delegate_).md>) — Retrieves the contents of a URL and delivers the URL of the saved file asynchronously.
- [download(resumeFrom:delegate:)](<download(resumefrom_delegate_).md>) — Resumes a previously-paused download and delivers the URL of the saved file asynchronously.
- [upload(for:from:delegate:)](<upload(for_from_delegate_).md>) — Uploads data to a URL based on the specified URL request and delivers the result asynchronously.
- [upload(for:fromFile:delegate:)](<upload(for_fromfile_delegate_).md>) — Uploads data to a URL and delivers the result asynchronously.
- [upload(for:from:)](<upload(for_from_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [upload(for:fromFile:)](<upload(for_fromfile_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
