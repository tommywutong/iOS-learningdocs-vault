---
title: update()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fetchrequest/update()
source_url: 'https://developer.apple.com/documentation/swiftui/fetchrequest/update()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fetchrequest/update%28%29.json'
content_hash: 'sha256:b7290d0bdfca2197'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FetchRequest](../fetchrequest.md)

# update()

<sub>Instance Method</sub>

Updates the fetched results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency mutating func update()
```

## Discussion

SwiftUI calls this function before rendering a view’s [body](../view/body-8kl5o.md) to ensure the view has the most recent fetched results.

## See Also

### Getting the fetched results

- [wrappedValue](wrappedvalue.md) — The fetched results of the fetch request.
