---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/progressviewstyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/progressviewstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressviewstyle/automatic.json'
content_hash: 'sha256:2fbb97c2aca4c4fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressViewStyle](../progressviewstyle.md)

# automatic

<sub>Type Property</sub>

The default progress view style in the current context of the view being styled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var automatic: DefaultProgressViewStyle { get }
```

## Discussion

The default style represents the recommended style based on the original initialization parameters of the progress view, and the progress view’s context within the view hierarchy.

## See Also

### Getting built-in progress view styles

- [circular](circular.md) — The style of a progress view that uses a circular gauge to indicate the partial completion of an activity.
- [linear](linear.md) — A progress view that visually indicates its progress using a horizontal bar.
