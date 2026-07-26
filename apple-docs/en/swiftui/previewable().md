---
title: Previewable()
framework: SwiftUI
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/previewable()
source_url: 'https://developer.apple.com/documentation/swiftui/previewable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewable%28%29.json'
content_hash: 'sha256:4e6c12743761abcc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Previewable()

<sub>Macro</sub>

Tag allowing a dynamic property to appear inline in a preview.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(peer) macro Previewable()
```

## Overview

Tagging a variable declaration at root scope in your `#Preview` body with ‘@Previewable’ allows you to use dynamic properties inline in previews. The `#Preview` macro will generate an embedded SwiftUI view; tagged declarations become properties on the view, and all remaining statements form the view’s body.

```swift
#Preview("toggle") {
    @Previewable @State var toggled = true
    return Toggle("Loud Noises", isOn: $toggled)
}
```

It is an error to use `@Previewable` outside of a `#Preview` body closure.

## See Also

### Customizing a preview

- [PreviewModifier](previewmodifier.md) — A type that defines an environment in which previews can appear.
- [PreviewModifierContent](previewmodifiercontent.md) — The type-erased content of a preview.
