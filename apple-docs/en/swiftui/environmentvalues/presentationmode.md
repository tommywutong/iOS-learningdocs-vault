---
title: presentationMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/environmentvalues/presentationmode
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/presentationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/presentationmode.json'
content_hash: 'sha256:b023b4dec31c8f8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# presentationMode

<sub>Instance Property</sub>

A binding to the current presentation mode of the view associated with this environment.

> [!warning] Deprecated
> Use [isPresented](ispresented.md) or [dismiss](dismiss.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var presentationMode: Binding<PresentationMode> { get }
```

## See Also

### Deprecated environment values

- [disableAutocorrection](disableautocorrection.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled. _(deprecated)_
- [sizeCategory](sizecategory.md) — The size of content. _(deprecated)_
- [PresentationMode](../presentationmode.md) — An indication whether a view is currently presented by another view. _(deprecated)_
- [complicationRenderingMode](complicationrenderingmode.md) — The complication rendering mode for the current environment. _(deprecated)_
- [controlActiveState](controlactivestate.md) — The active appearance expected of controls in a window. _(deprecated)_
