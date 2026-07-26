---
title: cancel()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/cancellable/cancel()
source_url: 'https://developer.apple.com/documentation/combine/cancellable/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/cancellable/cancel%28%29.json'
content_hash: 'sha256:aac36bd6dc961e82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Cancellable](../cancellable.md)

# cancel()

<sub>Instance Method</sub>

Cancel the activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

When implementing [Cancellable](../cancellable.md) in support of a custom publisher, implement `cancel()` to request that your publisher stop calling its downstream subscribers. Combine doesn’t require that the publisher stop immediately, but the `cancel()` call should take effect quickly. Canceling should also eliminate any strong references it currently holds.

After you receive one call to `cancel()`, subsequent calls shouldn’t do anything. Additionally, your implementation must be thread-safe, and it shouldn’t block the caller.

> [!tip] Tip
> Keep in mind that your `cancel()` may execute concurrently with another call to `cancel()` — including the scenario where an [AnyCancellable](../anycancellable.md) is deallocating — or to [request(_:)](<../subscription/request(__).md>).
