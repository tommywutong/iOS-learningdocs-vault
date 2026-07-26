---
title: volumetric
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowstyle/volumetric
source_url: 'https://developer.apple.com/documentation/swiftui/windowstyle/volumetric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowstyle/volumetric.json'
content_hash: 'sha256:d62a0b6cc6c44c11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowStyle](../windowstyle.md)

# volumetric

<sub>Type Property</sub>

A window style that creates a 3D volumetric window.

<sub>visionOS</sub>

```swift
static var volumetric: VolumetricWindowStyle { get }
```

## Discussion

Use a volumetric window — or a _volume_ — to display 3D content within a bounded region. For example, [Hello World](../../visionos/world.md) uses a volume to present a `Globe` model that people can pick up and move around the Shared Space using the window bar:

```swift
WindowGroup(id: Module.globe.name) {
    Globe()
        .environment(model)
}
.windowStyle(.volumetric)
.defaultSize(width: 0.6, height: 0.6, depth: 0.6, in: .meters)
```

A volume enables someone to view content from all angles, unlike other windows which fade out as people move around the window. Also unlike other windows, a volume uses fixed scale, which means that objects in the volume appear smaller when the volume is farther away, like real objects would. For a comparison of fixed and dynamic scale, see [Spatial layout](../../design/human-interface-guidelines/spatial-layout.md#Scale) in the Human Interface Guidelines.

You can specify a size for the volume using one of the default size scene modifiers, like [defaultSize(width:height:depth:in:)](<../scene/defaultsize(width_height_depth_in_).md>). Because volumes use fixed scale, it’s typically convenient to specify a size in physical units — like meters, as the above code demonstrates. People can’t change the size of the volume after it appears.

For design guidance, see [Windows](../../design/human-interface-guidelines/windows.md#Volumes) in the Human Interface Guidelines. If you want to place 3D objects arbitrarily throughout the Shared Space or in a Full Space, use an [ImmersiveSpace](../immersivespace.md) instead.

## See Also

### Getting built-in window styles

- [automatic](automatic.md) — The default window style.
- [hiddenTitleBar](hiddentitlebar.md) — A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [plain](plain.md) — The plain window style.
- [titleBar](titlebar.md) — A window style which displays the title bar section of the window.
