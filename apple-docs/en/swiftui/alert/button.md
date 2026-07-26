---
title: Alert.Button
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/alert/button
source_url: 'https://developer.apple.com/documentation/swiftui/alert/button'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alert/button.json'
content_hash: 'sha256:4d848e0864524ef8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Alert](../alert.md)

# Alert.Button

<sub>Structure</sub>

A button that represents an operation of an alert presentation.

> [!warning] Deprecated
> Use a [View](../view.md) modifier like [alert(_:isPresented:presenting:actions:message:)](<../view/alert(__ispresented_presenting_actions_message_)-8584l.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Button
```

## Topics

### Getting a button

- [default(_:action:)](<button/default(__action_).md>) — Creates an alert button with the default style. _(deprecated)_
- [cancel(_:)](<button/cancel(__).md>) — Creates an alert button that indicates cancellation, with a system-provided label. _(deprecated)_
- [cancel(_:action:)](<button/cancel(__action_).md>) — Creates an alert button that indicates cancellation, with a custom label. _(deprecated)_
- [destructive(_:action:)](<button/destructive(__action_).md>) — Creates an alert button with a style that indicates a destructive action. _(deprecated)_
