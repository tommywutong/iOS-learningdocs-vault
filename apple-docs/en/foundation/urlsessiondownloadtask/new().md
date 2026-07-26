---
title: new()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+（13.0 起废弃）, iPadOS 7.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.15 起废弃）, tvOS 9.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（6.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessiondownloadtask/new()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiondownloadtask/new()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiondownloadtask/new%28%29.json'
content_hash: 'sha256:56839299a9248e4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionDownloadTask](../urlsessiondownloadtask.md)

# new()

<sub>Type Method</sub>

Creates and initializes a download task.

> [!warning] Deprecated
> Please use -[NSURLSession downloadTaskWithRequest:] or other NSURLSession methods to create instances

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func new() -> Self
```

## Discussion

Don’t use this method to manually create download tasks. Instead, use the factory methods on [URLSession](../urlsession.md) to add tasks to an existing URL session.

## See Also

### Creating download tasks

- [- init](<init().md>) — Initializes a download task. _(deprecated)_
