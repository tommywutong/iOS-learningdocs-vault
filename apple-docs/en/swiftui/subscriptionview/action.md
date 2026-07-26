---
title: action
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/subscriptionview/action
source_url: 'https://developer.apple.com/documentation/swiftui/subscriptionview/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/subscriptionview/action.json'
content_hash: 'sha256:1e91443395d6a965'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SubscriptionView](../subscriptionview.md)

# action

<sub>Instance Property</sub>

The `Action` executed when `publisher` emits an event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var action: (PublisherType.Output) -> Void
```

## See Also

### Managing the subscription

- [publisher](publisher.md) — The `Publisher` that is being subscribed.
- [content](content.md) — The content view.
