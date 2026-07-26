---
title: PresentationMode
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/presentationmode
source_url: 'https://developer.apple.com/documentation/swiftui/presentationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationmode.json'
content_hash: 'sha256:64c70d2ea033e641'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PresentationMode

<sub>Structure</sub>

An indication whether a view is currently presented by another view.

> [!warning] Deprecated
> Use [isPresented](environmentvalues/ispresented.md) or [dismiss](environmentvalues/dismiss.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PresentationMode
```

## Topics

### Checking presentation

- [isPresented](presentationmode/ispresented.md) — Indicates whether a view is currently presented. _(deprecated)_

### Dismissing presentation

- [dismiss()](<presentationmode/dismiss().md>) — Dismisses the view if it is currently presented. _(deprecated)_

## See Also

### Deprecated environment values

- [disableAutocorrection](environmentvalues/disableautocorrection.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled. _(deprecated)_
- [sizeCategory](environmentvalues/sizecategory.md) — The size of content. _(deprecated)_
- [presentationMode](environmentvalues/presentationmode.md) — A binding to the current presentation mode of the view associated with this environment. _(deprecated)_
- [complicationRenderingMode](environmentvalues/complicationrenderingmode.md) — The complication rendering mode for the current environment. _(deprecated)_
- [controlActiveState](environmentvalues/controlactivestate.md) — The active appearance expected of controls in a window. _(deprecated)_
