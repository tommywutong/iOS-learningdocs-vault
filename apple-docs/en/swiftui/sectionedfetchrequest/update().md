---
title: update()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionedfetchrequest/update()
source_url: 'https://developer.apple.com/documentation/swiftui/sectionedfetchrequest/update()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionedfetchrequest/update%28%29.json'
content_hash: 'sha256:7e79bf0b34f19dcd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionedFetchRequest](../sectionedfetchrequest.md)

# update()

<sub>Instance Method</sub>

Updates the fetched results.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func update()
```

## Discussion

SwiftUI calls this function before rendering a view’s [body](../view/body-8kl5o.md) to ensure the view has the most recent fetched results.

## See Also

### Getting the fetched results

- [wrappedValue](wrappedvalue.md) — The fetched results of the fetch request.
