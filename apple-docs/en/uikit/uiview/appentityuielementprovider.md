---
title: appEntityUIElementProvider
framework: AppIntents
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, tvOS 18.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/appentityuielementprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiview/appentityuielementprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/appentityuielementprovider.json'
content_hash: 'sha256:348352911ca1b746'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# appEntityUIElementProvider

<sub>Instance Property</sub>

return AppEntityUIElement( identifier: EntityIdentifier( for: PhotoModel.self, identifier: photo.id ), bounds: photo.frame, state: State(isSelected: photo.isSelected) ) } } } }

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var appEntityUIElementProvider: ((UIView, AppEntityUIElementsContext) -> [AppEntityUIElement])? { get set }
```

## Discussion

```

> Note: The order of the returned elements isn't relevant.

If your custom view shows content you can describe with a single app entity, use the ``appEntityIdentifier`` property instead to
associate the app entity with your custom view.

For more information, refer to <doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri> and
<doc://com.apple.documentation/documentation/appintents>.
```
