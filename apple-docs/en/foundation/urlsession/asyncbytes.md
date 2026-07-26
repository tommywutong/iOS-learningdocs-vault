---
title: URLSession.AsyncBytes
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsession/asyncbytes
source_url: 'https://developer.apple.com/documentation/foundation/urlsession/asyncbytes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsession/asyncbytes.json'
content_hash: 'sha256:2121fd09800280e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSession](../urlsession.md)

# URLSession.AsyncBytes

<sub>Structure</sub>

An asynchronous sequence of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AsyncBytes
```

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Adapting textual sequences

- [AsyncCharacterSequence](../asynccharactersequence.md) — An asynchronous sequence of characters.
- [AsyncUnicodeScalarSequence](../asyncunicodescalarsequence.md) — An asychronous sequence of Unicode scalar values.
- [AsyncLineSequence](../asynclinesequence.md) — An asynchronous sequence of lines of text.

### Accessing the URL session task

- [task](asyncbytes/task.md) — The URL session task that performs the data transfer.

### Structures

- [Iterator](asyncbytes/iterator.md)

### Type Aliases

- [AsyncIterator](asyncbytes/asynciterator.md)
- [Element](asyncbytes/element.md) — The type of element produced by this asynchronous sequence.

## See Also

### Performing asynchronous transfers

- [bytes(for:delegate:)](<bytes(for_delegate_).md>) — Retrieves the contents of a URL based on the specified URL request and delivers an asynchronous sequence of bytes.
- [bytes(from:delegate:)](<bytes(from_delegate_).md>) — Retrieves the contents of a given URL and delivers an asynchronous sequence of bytes.
- [data(for:delegate:)](<data(for_delegate_).md>) — Downloads the contents of a URL based on the specified URL request and delivers the data asynchronously.
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
