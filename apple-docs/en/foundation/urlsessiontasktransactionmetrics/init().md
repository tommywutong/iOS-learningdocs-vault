---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.12+（10.15 起废弃）, tvOS 10.0+（13.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 3.0+（6.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/init()
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/init%28%29.json'
content_hash: 'sha256:8ea5efe10c80e627'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# init()

<sub>Initializer</sub>

Creates a transaction metrics instance.

> [!warning] Deprecated
> Not supported

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init()
```

## Discussion

You should never need to create your own [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md) instances. The [URLSession](../urlsession.md) creates task transaction metrics as part of the [URLSessionTaskMetrics](../urlsessiontaskmetrics.md) instance that it delivers to the [- URLSession:task:didFinishCollectingMetrics:](<../urlsessiontaskdelegate/urlsession(__task_didfinishcollecting_).md>) method of [URLSessionTaskDelegate](../urlsessiontaskdelegate.md).

## See Also

### Creating transaction metrics

- [+ new](<new().md>) — Creates a new transaction metrics instance. _(deprecated)_
