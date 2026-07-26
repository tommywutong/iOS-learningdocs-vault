---
title: 'download(from:delegate:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/download(from:delegate:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/download(from:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/download%28from%3Adelegate%3A%29.json'
content_hash: 'sha256:9b7226be99d7dbb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# download(from:delegate:)

<sub>Instance Method</sub>

Retrieves the contents of a URL and delivers the URL of the saved file asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func download(from url: URL, delegate: (any URLSessionTaskDelegate)? = nil) async throws -> (URL, URLResponse)
```

## Parameters

- `url` — The URL to retrieve.

- `delegate` — A delegate that receives life cycle and authentication challenge callbacks as the transfer progresses.

## Return Value

An asynchronously-delivered tuple that contains the location of the downloaded file as a URL, and a [URLResponse](../urlresponse.md).

## See Also

### Performing asynchronous transfers

- [bytes(for:delegate:)](<bytes(for_delegate_).md>) — Retrieves the contents of a URL based on the specified URL request and delivers an asynchronous sequence of bytes.
- [bytes(from:delegate:)](<bytes(from_delegate_).md>) — Retrieves the contents of a given URL and delivers an asynchronous sequence of bytes.
- [AsyncBytes](asyncbytes.md) — An asynchronous sequence of bytes.
- [data(for:delegate:)](<data(for_delegate_).md>) — Downloads the contents of a URL based on the specified URL request and delivers the data asynchronously.
- [data(from:delegate:)](<data(from_delegate_).md>) — Retrieves the contents of a URL and delivers the data asynchronously.
- [data(for:)](<data(for_).md>) — Convenience method to load data using a URLRequest, creates and resumes a URLSessionDataTask internally.
- [data(from:)](<data(from_).md>) — Convenience method to load data using a URL, creates and resumes a URLSessionDataTask internally.
- [download(for:delegate:)](<download(for_delegate_).md>) — Retrieves the contents of a URL based on the specified URL request and delivers the URL of the saved file asynchronously.
- [download(resumeFrom:delegate:)](<download(resumefrom_delegate_).md>) — Resumes a previously-paused download and delivers the URL of the saved file asynchronously.
- [upload(for:from:delegate:)](<upload(for_from_delegate_).md>) — Uploads data to a URL based on the specified URL request and delivers the result asynchronously.
- [upload(for:fromFile:delegate:)](<upload(for_fromfile_delegate_).md>) — Uploads data to a URL and delivers the result asynchronously.
- [upload(for:from:)](<upload(for_from_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [upload(for:fromFile:)](<upload(for_fromfile_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
