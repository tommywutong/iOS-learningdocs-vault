---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationsizing/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/presentationsizing/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationsizing/automatic.json'
content_hash: 'sha256:19aa9029f52f05e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PresentationSizing](../presentationsizing.md)

# automatic

<sub>Type Property</sub>

The default presentation sizing, appropriate for the platform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: AutomaticPresentationSizing { get }
```

## Discussion

On macOS, `.automatic` resolves to `.form.fitted(horizontal: false, vertical: true)`. On all other platforms, including Mac Catalyst, it resolves to `.form`.

> [!info] See Also
> [AutomaticPresentationSizing](../automaticpresentationsizing.md)

## See Also

### Getting built-in presentation size

- [fitted](fitted.md) — The presentation sizing is dictated by the ideal size of the content
- [form](form.md) — The size is appropriate for forms and slightly less wide than`.page`
- [page](page.md) — The size is roughly the size of a page of paper, appropriate for informational or compositional content.
