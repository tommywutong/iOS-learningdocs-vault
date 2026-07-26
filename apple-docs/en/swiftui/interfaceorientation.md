---
title: InterfaceOrientation
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/interfaceorientation
source_url: 'https://developer.apple.com/documentation/swiftui/interfaceorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/interfaceorientation.json'
content_hash: 'sha256:ea827d45390d1528'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# InterfaceOrientation

<sub>Structure</sub>

The orientation of the interface from the user’s perspective.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct InterfaceOrientation
```

## Overview

By default, device previews appear right side up, using orientation [portrait](interfaceorientation/portrait.md). You can change the orientation with a call to the [previewInterfaceOrientation(_:)](<view/previewinterfaceorientation(__).md>) modifier:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewInterfaceOrientation(.landscapeRight)
    }
}
```

## Relationships

- **Conforms To**: [CaseIterable](../swift/caseiterable.md), [Equatable](../swift/equatable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting an orientation

- [portrait](interfaceorientation/portrait.md) — The device is in portrait mode, with the top of the device on top.
- [portraitUpsideDown](interfaceorientation/portraitupsidedown.md) — The device is in portrait mode, but is upside down.
- [landscapeLeft](interfaceorientation/landscapeleft.md) — The device is in landscape mode, with the top of the device on the left.
- [landscapeRight](interfaceorientation/landscaperight.md) — The device is in landscape mode, with the top of the device on the right.

## See Also

### Customizing a preview

- [previewDevice(_:)](<view/previewdevice(__).md>) — Overrides the device for a preview. _(deprecated)_
- [PreviewDevice](previewdevice.md) — A simulator device that runs a preview. _(deprecated)_
- [previewLayout(_:)](<view/previewlayout(__).md>) — Overrides the size of the container for the preview. _(deprecated)_
- [previewInterfaceOrientation(_:)](<view/previewinterfaceorientation(__).md>) — Overrides the orientation of the preview. _(deprecated)_
