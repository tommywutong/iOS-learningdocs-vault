---
title: ignoredByLayout()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/geometryeffect/ignoredbylayout()
source_url: 'https://developer.apple.com/documentation/swiftui/geometryeffect/ignoredbylayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/geometryeffect/ignoredbylayout%28%29.json'
content_hash: 'sha256:6b7e9c94c1b7e76d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GeometryEffect](../geometryeffect.md)

# ignoredByLayout()

<sub>Instance Method</sub>

Returns an effect that produces the same geometry transform as this effect, but only applies the transform while rendering its view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func ignoredByLayout() -> _IgnoredByLayoutEffect<Self>
```

## Discussion

Use this method to disable layout changes during transitions. The view ignores the transform returned by this method while the view is performing its layout calculations.

## See Also

### Applying effects

- [effectValue(size:)](<effectvalue(size_).md>) — Returns the current value of the effect.
