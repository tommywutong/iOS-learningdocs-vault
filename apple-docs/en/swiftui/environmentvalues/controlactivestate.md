---
title: controlActiveState
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/environmentvalues/controlactivestate
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/controlactivestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/controlactivestate.json'
content_hash: 'sha256:fafb0b65579f549e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# controlActiveState

<sub>Instance Property</sub>

The active appearance expected of controls in a window.

> [!warning] Deprecated
> Use `EnvironmentValues.appearsActive` instead.

<sub>macOS</sub>

```swift
var controlActiveState: ControlActiveState { get set }
```

## Discussion

`ControlActiveState` and `EnvironmentValues.controlActiveState` are deprecated, use `EnvironmentValues.appearsActive` instead.

Starting with macOS 15.0, the value of this environment property is strictly mapped to and from `EnvironmentValues.appearsActive` as follows:

- `appearsActive == true`, `controlActiveState` returns `.key`
- `appearsActive == false`, `controlActiveState` returns `.inactive`
- `controlActiveState` is set to `.key` or `.active`, `appearsActive` will be set to `true`.
- `controlActiveState` is set to `.inactive`, `appearsActive` will be set to `false`.

## See Also

### Deprecated environment values

- [disableAutocorrection](disableautocorrection.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled. _(deprecated)_
- [sizeCategory](sizecategory.md) — The size of content. _(deprecated)_
- [presentationMode](presentationmode.md) — A binding to the current presentation mode of the view associated with this environment. _(deprecated)_
- [PresentationMode](../presentationmode.md) — An indication whether a view is currently presented by another view. _(deprecated)_
- [complicationRenderingMode](complicationrenderingmode.md) — The complication rendering mode for the current environment. _(deprecated)_
