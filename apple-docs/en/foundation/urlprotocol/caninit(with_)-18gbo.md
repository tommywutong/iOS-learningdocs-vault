---
title: 'canInit(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotocol/caninit(with:)-18gbo'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotocol/caninit(with:)-18gbo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotocol/caninit%28with%3A%29-18gbo.json'
content_hash: 'sha256:865f4d8b0d123b99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtocol](../urlprotocol.md)

# canInit(with:)

<sub>Type Method</sub>

Determines whether the protocol subclass can handle the specified task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func canInit(with task: URLSessionTask) -> Bool
```

## Parameters

- `task` — A URL session task containing the request to be handled.

## Discussion

A subclass should inspect the task’s request and determine whether or not the implementation can perform a load with that task.

This is an abstract method and subclasses must provide an implementation.

## See Also

### Determining If a subclass can handle a request

- [+ canInitWithRequest:](<caninit(with_)-76brg.md>) — Determines whether the protocol subclass can handle the specified request.
