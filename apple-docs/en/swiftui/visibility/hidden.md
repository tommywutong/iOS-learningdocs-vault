---
title: Visibility.hidden
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/visibility/hidden
source_url: 'https://developer.apple.com/documentation/swiftui/visibility/hidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visibility/hidden.json'
content_hash: 'sha256:5249888731489f3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Visibility](../visibility.md)

# Visibility.hidden

<sub>Case</sub>

The element may be hidden.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case hidden
```

## Discussion

Some APIs may use this value to represent a hint or preference, rather than a mandatory assertion. For example, setting confirmation dialog title visibility to `hidden` using the [confirmationDialog(_:isPresented:titleVisibility:actions:)](<../view/confirmationdialog(__ispresented_titlevisibility_actions_).md>) modifier may not always hide the dialog title, which is required on some platforms.

## See Also

### Getting visibility options

- [Visibility.automatic](automatic.md) — The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.visible](visible.md) — The element may be visible.
