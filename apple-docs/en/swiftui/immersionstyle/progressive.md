---
title: progressive
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersionstyle/progressive
source_url: 'https://developer.apple.com/documentation/swiftui/immersionstyle/progressive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionstyle/progressive.json'
content_hash: 'sha256:5e427764302cd734'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersionStyle](../immersionstyle.md)

# progressive

<sub>Type Property</sub>

An immersion style that displays unbounded content that partially replaces passthrough video.

<sub>macOS, visionOS</sub>

```swift
@export(implementation) static var progressive: ProgressiveImmersionStyle { get }
```

## Discussion

The system initially uses a radial portal effect that replaces passthrough in a portion of the field of view. People can interactively adjust the size of the portal by turning the Digital Crown, including down to a minimum amount of immersion defined by the system and up to the point where the portal fully covers passthrough. If someone tries to reduce the portal size below the minimum value, the portal smoothly bounces back to the minimum size. The portal’s behavior at the maximum size matches the behavior of the [full](full.md) immersion style, including the configurable visibility of the viewer’s upper limbs.

When this immersion style is selected, the immersion amount reported by the closure of [onImmersionChange(initial:_:)](<../view/onimmersionchange(initial___).md>) is within the range of the immersion that this style uses.

Use the [immersionStyle(selection:in:)](<../scene/immersionstyle(selection_in_).md>) scene modifier to specify this style for an [ImmersiveSpace](../immersivespace.md):

```swift
@main
struct ImmersiveApp: App {
    @State private var immersionStyle: ImmersionStyle = .progressive
    var body: some Scene {
        ImmersiveSpace { ... }
        .immersionStyle(selection: $immersionStyle, in: .progressive))
    }
}
```

The immersion style affects how windows interact with virtual objects in the environment. In `progressive` immersion, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people avoid losing track of windows behind virtual content when passthrough is off.

## See Also

### Getting built-in styles

- [automatic](automatic.md) — The default immersion style.
- [full](full.md) — An immersion style that displays unbounded content that completely replaces passthrough video.
- [mixed](mixed.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
