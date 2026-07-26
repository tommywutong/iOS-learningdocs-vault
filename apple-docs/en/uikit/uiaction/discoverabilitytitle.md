---
title: discoverabilityTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaction/discoverabilitytitle
source_url: 'https://developer.apple.com/documentation/uikit/uiaction/discoverabilitytitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction/discoverabilitytitle.json'
content_hash: 'sha256:2be29b945ed5fd59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAction](../uiaction.md)

# discoverabilityTitle

<sub>Instance Property</sub>

An elaborated title that explains the purpose of the action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var discoverabilityTitle: String? { get set }
```

## Discussion

The system uses this property to display information about the command. In iOS, the system displays this title in the discoverability heads-up display (HUD). If this property is `nil`, the HUD displays the [title](title.md) property.

In Mac apps built with Mac Catalyst, the system displays the discoverability title as a tooltip.

## See Also

### Getting information about the action

- [title](title.md) — The action’s title.
- [image](image.md) — The action’s image.
- [identifier](identifier-swift.property.md) — The unique identifier for the action.
- [attributes](attributes.md) — The attributes indicating the style of the action.
- [state](state.md) — The state of the action.
- [sender](sender.md) — The object responsible for the action handler.
