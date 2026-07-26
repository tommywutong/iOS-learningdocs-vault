---
title: preferredContentSize
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingcontrollersizingoptions/preferredcontentsize
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontrollersizingoptions/preferredcontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontrollersizingoptions/preferredcontentsize.json'
content_hash: 'sha256:e959285ac0e02c1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingControllerSizingOptions](../uihostingcontrollersizingoptions.md)

# preferredContentSize

<sub>Type Property</sub>

The hosting controller tracks its content’s ideal size in its preferred content size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let preferredContentSize: UIHostingControllerSizingOptions
```

## Discussion

Use this option when using a hosting controller with a container view controller that requires up-to-date knowledge of the hosting controller’s ideal size.

> [!note] Note
> This option comes with a performance cost because it asks for the ideal size of the content using the [unspecified](../proposedviewsize/unspecified.md) size proposal.

## See Also

### Getting sizing options

- [intrinsicContentSize](intrinsiccontentsize.md) — The hosting controller’s view automatically invalidate its intrinsic content size when its ideal size changes.
