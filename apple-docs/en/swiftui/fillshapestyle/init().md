---
title: init()
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/fillshapestyle/init()
source_url: 'https://developer.apple.com/documentation/swiftui/fillshapestyle/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/fillshapestyle/init%28%29.json'
content_hash: 'sha256:fd2b50b45fc0165a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FillShapeStyle](../fillshapestyle.md)

# init()

<sub>Initializer</sub>

An overlay fill style for filling shapes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) init()
```

## Discussion

This shape style is appropriate for items situated on top of an existing background color. It incorporates transparency to allow the background color to show through.

Use the primary version of this style to fill thin or small shapes, such as the track of a slider. Use the secondary version of this style to fill medium-size shapes, such as the background of a switch. Use the tertiary version of this style to fill large shapes, such as input fields, search bars, or buttons. Use the quaternary version of this style to fill large areas that contain complex content, such as an expanded table cell.
