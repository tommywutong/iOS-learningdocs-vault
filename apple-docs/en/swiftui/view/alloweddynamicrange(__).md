---
title: 'allowedDynamicRange(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/alloweddynamicrange(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/alloweddynamicrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/alloweddynamicrange%28_%3A%29.json'
content_hash: 'sha256:cec5a380ce1baad5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# allowedDynamicRange(_:)

<sub>Instance Method</sub>

Returns a new view configured with the specified allowed dynamic range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated func allowedDynamicRange(_ range: Image.DynamicRange?) -> some View

```

## Parameters

- `range` — The requested dynamic range, or nil to restore the default allowed range.

## Return Value

A new view.

## Discussion

The following example enables HDR rendering within a view hierarchy:

```swift
MyView().allowedDynamicRange(.high)
```

## See Also

### Colors and patterns

- [backgroundStyle(_:)](<backgroundstyle(__).md>) — Sets the specified style to render backgrounds within the view.
- [foregroundStyle(_:)](<foregroundstyle(__).md>) — Sets a view’s foreground elements to use a given style.
- [foregroundStyle(_:_:)](<foregroundstyle(____).md>) — Sets the primary and secondary levels of the foreground style in the child view.
- [foregroundStyle(_:_:_:)](<foregroundstyle(______).md>) — Sets the primary, secondary, and tertiary levels of the foreground style.
