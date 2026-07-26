---
title: cancel()
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompleter/cancel()
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompleter/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompleter/cancel%28%29.json'
content_hash: 'sha256:e6eb8da1a87c988d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompleter](../mklocalsearchcompleter.md)

# cancel()

<sub>Instance Method</sub>

Cancels an in-progress search operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

If a search operation is in progress, this method attempts to cancel it. If cancellation is successful, the search completer doesn’t notify its delegate. If no search operation is in progress, this method does nothing.

## See Also

### Canceling the query

- [searching](issearching.md) — A Boolean value that indicates whether a search operation is in progress.
