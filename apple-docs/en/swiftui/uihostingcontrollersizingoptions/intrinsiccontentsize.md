---
title: intrinsicContentSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingcontrollersizingoptions/intrinsiccontentsize
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontrollersizingoptions/intrinsiccontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontrollersizingoptions/intrinsiccontentsize.json'
content_hash: 'sha256:0adbfdd3df0510f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingControllerSizingOptions](../uihostingcontrollersizingoptions.md)

# intrinsicContentSize

<sub>Type Property</sub>

The hosting controller’s view automatically invalidate its intrinsic content size when its ideal size changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let intrinsicContentSize: UIHostingControllerSizingOptions
```

## Discussion

Use this option when the hosting controller’s view is being laid out with Auto Layout.

> [!note] Note
> This option comes with a performance cost because it asks for the ideal size of the content using the [unspecified](../proposedviewsize/unspecified.md) size proposal.

## See Also

### Getting sizing options

- [preferredContentSize](preferredcontentsize.md) — The hosting controller tracks its content’s ideal size in its preferred content size.
