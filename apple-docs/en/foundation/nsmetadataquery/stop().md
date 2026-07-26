---
title: stop()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquery/stop()
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquery/stop()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquery/stop%28%29.json'
content_hash: 'sha256:61f38b8253529c6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQuery](../nsmetadataquery.md)

# stop()

<sub>Instance Method</sub>

Stops the receiver’s current query from gathering any further results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stop()
```

## Discussion

The receiver first completes gathering any unprocessed results. If a query is stopped before the gathering phase finishes, it does not post an `NSMetadataQueryDidStartGatheringNotification` notification.

You call this function to stop a query that is generating too many results to be useful but you still want to access the available results. If the receiver is sent a `startQuery` message after performing this method, the existing results are discarded.

## See Also

### Running queries

- [started](isstarted.md) — A Boolean value that indicates whether the query has started. (read-only)
- [- startQuery](<start().md>) — Attempts to start the query.
- [gathering](isgathering.md) — A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [stopped](isstopped.md) — A Boolean value that indicates whether the query has stopped.
