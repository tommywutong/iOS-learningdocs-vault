---
title: subtitleColor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wkusernotificationhostingcontroller/subtitlecolor
source_url: 'https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller/subtitlecolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wkusernotificationhostingcontroller/subtitlecolor.json'
content_hash: 'sha256:a3931e8e5dd79ea7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKUserNotificationHostingController](../wkusernotificationhostingcontroller.md)

# subtitleColor

<sub>Type Property</sub>

The color to apply to the subtitle text displayed in the short look interface. If `nil` the text will be the default system color.

<sub>watchOS</sub>

```swift
@MainActor @preconcurrency class var subtitleColor: Color? { get }
```

## Discussion

Default value is `nil`

## See Also

### Configuring the notification

- [coalescedDescriptionFormat](coalesceddescriptionformat.md) — The format string to display when multiple notifications of the same type arrive simultaneously. If you specify a custom string, you can use the %d variable to reflect the number of notifications. If `nil` format will be the system default.
- [isInteractive](isinteractive.md) — If the notification should accept user input.
- [sashColor](sashcolor.md) — Color to use within the sash of the long look interface. If `nil` the sash will be the default system color.
- [titleColor](titlecolor.md) — The color to apply to the text displayed in the sash. If `nil` the text will be the default system color.
- [wantsSashBlur](wantssashblur.md) — If the sash should include a blur over the background.
