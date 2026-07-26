---
title: environment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/graphicscontext/environment
source_url: 'https://developer.apple.com/documentation/swiftui/graphicscontext/environment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/graphicscontext/environment.json'
content_hash: 'sha256:fb27dabba2f8771e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GraphicsContext](../graphicscontext.md)

# environment

<sub>Instance Property</sub>

The environment associated with the graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var environment: EnvironmentValues { get set }
```

## Discussion

SwiftUI initially sets this to the environment of the context’s enclosing view. The context uses values like display resolution and the color scheme from the environment to resolve types like [Image](../image.md) and [Color](../color.md). You can also access values stored in the environment for your own purposes.
