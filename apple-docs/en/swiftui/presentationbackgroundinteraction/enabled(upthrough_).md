---
title: 'enabled(upThrough:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/presentationbackgroundinteraction/enabled(upthrough:)'
source_url: 'https://developer.apple.com/documentation/swiftui/presentationbackgroundinteraction/enabled(upthrough:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationbackgroundinteraction/enabled%28upthrough%3A%29.json'
content_hash: 'sha256:a936a5ccb4010c9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PresentationBackgroundInteraction](../presentationbackgroundinteraction.md)

# enabled(upThrough:)

<sub>Type Method</sub>

People can interact with the view behind a presentation up through a specified detent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func enabled(upThrough detent: PresentationDetent) -> PresentationBackgroundInteraction
```

## Parameters

- `detent` — The largest detent at which people can interact with the view behind the presentation.

## Discussion

At detents larger than the one you specify, SwiftUI disables interaction.

## See Also

### Getting interaction types

- [automatic](automatic.md) — The default background interaction for the presentation.
- [disabled](disabled.md) — People can’t interact with the view behind a presentation.
- [enabled](enabled.md) — People can interact with the view behind a presentation.
