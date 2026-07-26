---
title: environment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/animationcontext/environment
source_url: 'https://developer.apple.com/documentation/swiftui/animationcontext/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/animationcontext/environment.json'
content_hash: 'sha256:510e09ccc69b7d3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnimationContext](../animationcontext.md)

# environment

<sub>Instance Property</sub>

The current environment of the view that created the custom animation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var environment: EnvironmentValues { get }
```

## Discussion

An instance of [CustomAnimation](../customanimation.md) uses this property to read environment values from the view that created the animation. To learn more about environment values including how to define custom environment values, see [EnvironmentValues](../environmentvalues.md).
