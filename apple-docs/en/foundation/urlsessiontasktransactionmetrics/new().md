---
title: new()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12+（10.15 起废弃）, tvOS 10.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.0+（6.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/new()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/new()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/new%28%29.json'
content_hash: 'sha256:17d33014b0381d0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# new()

<sub>Type Method</sub>

Creates a new transaction metrics instance.

> [!warning] Deprecated
> Not supported

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func new() -> Self
```

## Discussion

You should never need to create your own [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md) instances. The [URLSession](../urlsession.md) creates task transaction metrics as part of the [URLSessionTaskMetrics](../urlsessiontaskmetrics.md) instance that it delivers to the [- URLSession:task:didFinishCollectingMetrics:](<../urlsessiontaskdelegate/urlsession(__task_didfinishcollecting_).md>) method of [URLSessionTaskDelegate](../urlsessiontaskdelegate.md).

## See Also

### Creating transaction metrics

- [- init](<init().md>) — Creates a transaction metrics instance. _(deprecated)_
