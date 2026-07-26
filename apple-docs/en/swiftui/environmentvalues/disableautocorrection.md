---
title: disableAutocorrection
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 8.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/environmentvalues/disableautocorrection
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/disableautocorrection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/disableautocorrection.json'
content_hash: 'sha256:38f469145b4aae93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# disableAutocorrection

<sub>Instance Property</sub>

A Boolean value that determines whether the view hierarchy has auto-correction enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var disableAutocorrection: Bool? { get set }
```

## Discussion

When the value is `nil`, SwiftUI uses the system default. The default value is `nil`.

## See Also

### Deprecated environment values

- [sizeCategory](sizecategory.md) — The size of content. _(deprecated)_
- [presentationMode](presentationmode.md) — A binding to the current presentation mode of the view associated with this environment. _(deprecated)_
- [PresentationMode](../presentationmode.md) — An indication whether a view is currently presented by another view. _(deprecated)_
- [complicationRenderingMode](complicationrenderingmode.md) — The complication rendering mode for the current environment. _(deprecated)_
- [controlActiveState](controlactivestate.md) — The active appearance expected of controls in a window. _(deprecated)_
