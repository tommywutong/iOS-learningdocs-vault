---
title: 'init(width:height:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/proposedviewsize/init(width:height:)'
source_url: 'https://developer.apple.com/documentation/swiftui/proposedviewsize/init(width:height:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/proposedviewsize/init%28width%3Aheight%3A%29.json'
content_hash: 'sha256:2b2e2b124903bd5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProposedViewSize](../proposedviewsize.md)

# init(width:height:)

<sub>Initializer</sub>

Creates a new proposed size using the specified width and height.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(width: CGFloat?, height: CGFloat?)
```

## Parameters

- `width` — A proposed width in points. Use a value of `nil` to indicate that the width is unspecified for this proposal.

- `height` — A proposed height in points. Use a value of `nil` to indicate that the height is unspecified for this proposal.

## See Also

### Creating a custom size proposal

- [init(_:)](<init(__).md>) — Creates a new proposed size from a specified size.
