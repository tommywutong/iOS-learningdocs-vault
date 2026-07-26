---
title: 'removeObserver(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/notificationcenter/removeobserver(_:)-2gmm0'
source_url: 'https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2gmm0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/notificationcenter/removeobserver%28_%3A%29-2gmm0.json'
content_hash: 'sha256:e883562db8e29f5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NotificationCenter](../notificationcenter.md)

# removeObserver(_:)

<sub>Instance Method</sub>

Stops the observation represented by the given observation token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ token: NotificationCenter.ObservationToken)
```

## Parameters

- `token` — A unique token representing a specific observer in a specific notification center. You receive this type from prior calls to `addObserver(of:for:using:)`.

## See Also

### Observing concurrency-safe notifications

- [addObserver(of:for:using:)](<addobserver(of_for_using_)-4d19x.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-90os.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-56bn4.md>) — Adds an observer to a center for messages delivered on the main actor with a given subject and message type.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-twm3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and identifier.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-t1wr.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [addObserver(of:for:using:)](<addobserver(of_for_using_)-64uw3.md>) — Adds an observer to a center for messages delivered asynchronously with a given subject and message type.
- [ObservationToken](observationtoken.md) — A unique token representing a single observer registration in a notification center.
