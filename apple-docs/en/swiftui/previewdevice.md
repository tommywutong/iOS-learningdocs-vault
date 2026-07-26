---
title: PreviewDevice
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewdevice
source_url: 'https://developer.apple.com/documentation/swiftui/previewdevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewdevice.json'
content_hash: 'sha256:733bacc9090d7f78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PreviewDevice

<sub>Structure</sub>

A simulator device that runs a preview.

> [!warning] Deprecated
> Use the device picker in the Xcode preview canvas instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PreviewDevice
```

## Overview

Create a preview device by name, like “iPhone X”, or by model number, like “iPad8,1”. Use the device in a call to the [previewDevice(_:)](<view/previewdevice(__).md>) modifier to set a preview device that doesn’t change when you change the run destination in Xcode:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
    }
}
```

You can get a list of supported preview device names by using the `xcrun` command in the Terminal app:

```swift
% xcrun simctl list devicetypes
```

Additionally, you can use the following values for macOS platform development:

- “Mac”
- “Mac Catalyst”

## Relationships

- **Conforms To**: [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## See Also

### Customizing a preview

- [previewDevice(_:)](<view/previewdevice(__).md>) — Overrides the device for a preview. _(deprecated)_
- [previewLayout(_:)](<view/previewlayout(__).md>) — Overrides the size of the container for the preview. _(deprecated)_
- [previewInterfaceOrientation(_:)](<view/previewinterfaceorientation(__).md>) — Overrides the orientation of the preview. _(deprecated)_
- [InterfaceOrientation](interfaceorientation.md) — The orientation of the interface from the user’s perspective.
