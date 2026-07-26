---
title: 'download(resumeFrom:delegate:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsession/download(resumefrom:delegate:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/download(resumefrom:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/download%28resumefrom%3Adelegate%3A%29.json'
content_hash: 'sha256:e71c701aa55e13bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# download(resumeFrom:delegate:)

<sub>Instance Method</sub>

Resumes a previously-paused download and delivers the URL of the saved file asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func download(resumeFrom resumeData: Data, delegate: (any URLSessionTaskDelegate)? = nil) async throws -> (URL, URLResponse)
```

## Parameters

- `resumeData` — A data object that provides the data necessary to resume a download.

- `delegate` — A delegate that receives life cycle and authentication challenge callbacks as the transfer progresses.

## Return Value

An asynchronously-delivered tuple that contains the location of the downloaded file as a URL, and a [URLResponse](../urlresponse.md).

## Discussion

Your app can obtain a `resumeData` object in two ways:

- If your app cancels an existing transfer by calling [- cancelByProducingResumeData:](<../urlsessiondownloadtask/cancel(byproducingresumedata_).md>), the session object passes a `resumeData` object to the completion handler that you provided in that call.
- If a transfer fails, the session object provides an `NSError` object either to its delegate or to the task’s completion handler. In that object, the [NSURLSessionDownloadTaskResumeData](../nsurlsessiondownloadtaskresumedata.md) key in the `userInfo` dictionary contains a `resumeData` object.

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
- [upload(for:from:delegate:)](<upload(for_from_delegate_).md>) — Uploads data to a URL based on the specified URL request and delivers the result asynchronously.
- [upload(for:fromFile:delegate:)](<upload(for_fromfile_delegate_).md>) — Uploads data to a URL and delivers the result asynchronously.
- [upload(for:from:)](<upload(for_from_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [upload(for:fromFile:)](<upload(for_fromfile_).md>) — Convenience method to upload data using a URLRequest, creates and resumes a URLSessionUploadTask internally.
- [URLSessionTaskDelegate](../urlsessiontaskdelegate.md) — A protocol that defines methods that URL session instances call on their delegates to handle task-level events.
