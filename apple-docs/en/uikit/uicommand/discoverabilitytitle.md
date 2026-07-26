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
doc_path: /documentation/uikit/uicommand/discoverabilitytitle
source_url: 'https://developer.apple.com/documentation/uikit/uicommand/discoverabilitytitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicommand/discoverabilitytitle.json'
content_hash: 'sha256:19a4acc5a924cd0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICommand](../uicommand.md)

# discoverabilityTitle

<sub>Instance Property</sub>

An elaborated title that explains the purpose of the command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var discoverabilityTitle: String? { get set }
```

## Discussion

The system uses this property to display information about the command. In iOS, the system displays this title in the discoverability heads-up display (HUD). If this property is `nil`, the HUD displays the [title](title.md) property.

In Mac apps built with Mac Catalyst, the system displays the discoverability title as a tooltip.

## See Also

### Getting information about the command

- [title](title.md) — The command’s title.
- [image](image.md) — The command’s image.
- [action](action.md) — The selector identifying the action method called after the user selects the command.
- [attributes](attributes.md) — The attributes indicating the style of the command.
- [state](state.md) — The state of the command.
