---
title: 'upload(for:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/upload(for:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/upload(for:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/upload%28for%3Afrom%3A%29.json'
content_hash: 'sha256:44eaeb9634edfda2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# upload(for:from:)

<sub>Instance Method</sub>

Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func upload(for request: URLRequest, from bodyData: Data) async throws -> (Data, URLResponse)
```

## Parameters

- `request` — The URLRequest for which to upload data.

- `bodyData` — Data to upload.

## Return Value

Data and response.

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
- [download(from:delegate:)](<download(from_delegate_).md>) — Retrieves the contents of a URL and delivers the URL of the saved file asynchronously.
- [download(resumeFrom:delegate:)](<download(resumefrom_delegate_).md>) — Resumes a previously-paused download and delivers the URL of the saved file asynchronously.
- [upload(for:from:delegate:)](<upload(for_from_delegate_).md>) — Uploads data to a URL based on the specified URL request and delivers the result asynchronously.
- [upload(for:fromFile:delegate:)](<upload(for_fromfile_delegate_).md>) — Uploads data to a URL and delivers the result asynchronously.
- [upload(for:fromFile:)](<upload(for_fromfile_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
