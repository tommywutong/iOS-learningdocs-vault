---
title: 'previewDevice(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/previewdevice(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/previewdevice(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/previewdevice%28_%3A%29.json'
content_hash: 'sha256:182c350896d7f11c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# previewDevice(_:)

<sub>Instance Method</sub>

Overrides the device for a preview.

> [!warning] Deprecated
> Use the device picker in the Xcode preview canvas instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func previewDevice(_ value: PreviewDevice?) -> some View

```

## Parameters

- `value` — A device to use for preview, or `nil` to let Xcode automatically choose a device based on the run destination.

## Return Value

A preview that uses the given device.

## Discussion

By default, Xcode automatically chooses a preview device based on your currently selected run destination. If you want to choose a device that doesn’t change based on Xcode settings, provide a [PreviewDevice](../previewdevice.md) instance that you initialize with the name or model of a specific device:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
    }
}
```

You can get a list of supported preview device names, like “iPhone 11”, “iPad Pro (11-inch)”, and “Apple Watch Series 5 - 44mm”, by using the `xcrun` command in the Terminal app:

```swift
% xcrun simctl list devicetypes
```

Additionally, you can use the following values for macOS platform development:

- “Mac”
- “Mac Catalyst”

## See Also

### Customizing a preview

- [PreviewDevice](../previewdevice.md) — A simulator device that runs a preview. _(deprecated)_
- [previewLayout(_:)](<previewlayout(__).md>) — Overrides the size of the container for the preview. _(deprecated)_
- [previewInterfaceOrientation(_:)](<previewinterfaceorientation(__).md>) — Overrides the orientation of the preview. _(deprecated)_
- [InterfaceOrientation](../interfaceorientation.md) — The orientation of the interface from the user’s perspective.
