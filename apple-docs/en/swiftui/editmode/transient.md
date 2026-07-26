---
title: EditMode.transient
framework: SwiftUI
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/editmode/transient
source_url: 'https://developer.apple.com/documentation/swiftui/editmode/transient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/editmode/transient.json'
content_hash: 'sha256:7adaee8776354bac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EditMode](../editmode.md)

# EditMode.transient

<sub>Case</sub>

The view is in a temporary edit mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case transient
```

## Discussion

The use of this state varies by platform and for different controls. As an example, SwiftUI might engage temporary edit mode over the duration of a swipe gesture.

The [isEditing](isediting.md) property is `true` in this state.

## See Also

### Getting edit modes

- [EditMode.active](active.md) — The user can edit the view content.
- [EditMode.inactive](inactive.md) — The user can’t edit the view content.
