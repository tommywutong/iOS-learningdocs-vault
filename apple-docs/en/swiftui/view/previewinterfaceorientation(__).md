---
title: 'previewInterfaceOrientation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+（27.0 起废弃）, iPadOS 15.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）, tvOS 15.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 8.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/previewinterfaceorientation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/previewinterfaceorientation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/previewinterfaceorientation%28_%3A%29.json'
content_hash: 'sha256:fffd4efee19f2189'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# previewInterfaceOrientation(_:)

<sub>Instance Method</sub>

Overrides the orientation of the preview.

> [!warning] Deprecated
> Use [Preview(_:traits:_:body:)](<../preview(__traits___body_).md>) with [landscapeLeft](../../developertoolssupport/previewtrait/landscapeleft.md) or other orientation traits instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func previewInterfaceOrientation(_ value: InterfaceOrientation) -> some View

```

## Parameters

- `value` — An orientation to use for preview.

## Return Value

A preview that uses the given orientation.

## Discussion

By default, device previews appear right side up, using orientation [portrait](../interfaceorientation/portrait.md). You can change the orientation of a preview using one of the values in the [InterfaceOrientation](../interfaceorientation.md) structure:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewInterfaceOrientation(.landscapeRight)
    }
}
```

## See Also

### Customizing a preview

- [previewDevice(_:)](<previewdevice(__).md>) — Overrides the device for a preview. _(deprecated)_
- [PreviewDevice](../previewdevice.md) — A simulator device that runs a preview. _(deprecated)_
- [previewLayout(_:)](<previewlayout(__).md>) — Overrides the size of the container for the preview. _(deprecated)_
- [InterfaceOrientation](../interfaceorientation.md) — The orientation of the interface from the user’s perspective.
