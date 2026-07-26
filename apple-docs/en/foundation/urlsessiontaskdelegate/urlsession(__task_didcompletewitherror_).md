---
title: 'urlSession(_:task:didCompleteWithError:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontaskdelegate/urlsession%28_%3Atask%3Adidcompletewitherror%3A%29.json'
content_hash: 'sha256:139c55270455b80b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskDelegate](../urlsessiontaskdelegate.md)

# urlSession(_:task:didCompleteWithError:)

<sub>Instance Method</sub>

Tells the delegate that the task finished transferring data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func urlSession(_ session: URLSession, task: URLSessionTask, didCompleteWithError error: (any Error)?)
```

## Parameters

- `session` — The session containing the task that has finished transferring data.

- `task` — The task that has finished transferring data.

- `error` — If an error occurred, an error object indicating how the transfer failed, otherwise `NULL`.

## Discussion

The only errors your delegate receives through the `error` parameter are client-side errors, such as being unable to resolve the hostname or connect to the host. To check for server-side errors, inspect the [response](../urlsessiontask/response.md) property of the `task` parameter received by this callback.
