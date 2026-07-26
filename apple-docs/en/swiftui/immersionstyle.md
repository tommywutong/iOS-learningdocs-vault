---
title: ImmersionStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersionstyle
source_url: 'https://developer.apple.com/documentation/swiftui/immersionstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionstyle.json'
content_hash: 'sha256:5fd97e33f4000c35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImmersionStyle

<sub>Protocol</sub>

The styles that an immersive space can have.

<sub>macOS, visionOS</sub>

```swift
protocol ImmersionStyle
```

## Overview

Configure the appearance and behavior of an [ImmersiveSpace](immersivespace.md) by adding the [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>) scene modifier to the space and specifying a style that conforms to this protocol, like [mixed](immersionstyle/mixed.md) or [full](immersionstyle/full.md). For example, the following app defines a solar system scene that uses full immersion:

```swift
@main
struct SolarSystemApp: App {
    @State private var style: ImmersionStyle = .full

    var body: some Scene {
        ImmersiveSpace {
            SolarSystem()
        }
        .immersionStyle(selection: $style, in: .full)
    }
}
```

## Relationships

- **Conforming Types**: [AutomaticImmersionStyle](automaticimmersionstyle.md), [FullImmersionStyle](fullimmersionstyle.md), [MixedImmersionStyle](mixedimmersionstyle.md), [ProgressiveImmersionStyle](progressiveimmersionstyle.md)

## Topics

### Getting built-in styles

- [automatic](immersionstyle/automatic.md) — The default immersion style.
- [full](immersionstyle/full.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [mixed](immersionstyle/mixed.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [progressive](immersionstyle/progressive.md) — An immersion style that displays unbounded content that partially replaces passthrough video.

### Supporting types

- [AutomaticImmersionStyle](automaticimmersionstyle.md) — The default style of immersive spaces.
- [FullImmersionStyle](fullimmersionstyle.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [MixedImmersionStyle](mixedimmersionstyle.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [ProgressiveImmersionStyle](progressiveimmersionstyle.md) — An immersion style that displays unbounded content that partially replaces passthrough video.

### Type Methods

- [progressive(_:initialAmount:)](<immersionstyle/progressive(__initialamount_).md>) — An immersion style that displays unbounded content that partially replaces passthrough video.
- [progressive(_:initialAmount:aspectRatio:)](<immersionstyle/progressive(__initialamount_aspectratio_).md>) — An immersion style that displays unbounded content that partially replaces passthrough video.
- [progressive(aspectRatio:)](<immersionstyle/progressive(aspectratio_).md>) — An immersion style that displays unbounded content that partially replaces passthrough video.

## See Also

### Creating an immersive space

- [ImmersiveSpace](immersivespace.md) — A scene that presents its content in an unbounded space.
- [ImmersiveSpaceContentBuilder](immersivespacecontentbuilder.md) — A result builder for composing a collection of immersive space elements.
- [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>) — Sets the style for an immersive space.
- [immersiveSpaceDisplacement](environmentvalues/immersivespacedisplacement.md) — The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [ImmersiveEnvironmentBehavior](immersiveenvironmentbehavior.md) — The behavior of the system-provided immersive environments when a scene is opened by your app.
- [ProgressiveImmersionAspectRatio](progressiveimmersionaspectratio.md)
