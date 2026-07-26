---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/delegate
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/delegate.json'
content_hash: 'sha256:7355e05f94e56186'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# delegate

<sub>Instance Property</sub>

The user activity object’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any NSUserActivityDelegate)? { get set }
```

## Discussion

The user activity delegate is informed when the activity is being saved or continued. For more information on how to implement the delegate, see [NSUserActivityDelegate](../nsuseractivitydelegate.md).

## See Also

### Monitoring activity-related behaviors

- [NSUserActivityDelegate](../nsuseractivitydelegate.md) — The interface through which a user activity instance notifies its delegate of updates.
