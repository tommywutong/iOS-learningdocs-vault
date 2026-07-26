---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbartitledisplaymode/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/toolbartitledisplaymode/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbartitledisplaymode/automatic.json'
content_hash: 'sha256:e72e2654772b696b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarTitleDisplayMode](../toolbartitledisplaymode.md)

# automatic

<sub>Type Property</sub>

The automatic mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: ToolbarTitleDisplayMode { get }
```

## Discussion

For root content in a navigation stack in iOS, iPadOS, or tvOS this behavior will:

- Default to [large](large.md) when a navigation title is configured.
- Default to [inline](inline.md) when no navigation title is provided.

In all platforms, content pushed onto a navigation stack will use the behavior of the content already on the navigation stack. This has no effect in macOS.

## See Also

### Getting display modes

- [inline](inline.md) — The inline mode.
- [inlineLarge](inlinelarge.md) — The inline large mode.
- [large](large.md) — The large mode.
