---
title: platform
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewprovider/platform
source_url: 'https://developer.apple.com/documentation/swiftui/previewprovider/platform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewprovider/platform.json'
content_hash: 'sha256:7119c7b735309665'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreviewProvider](../previewprovider.md)

# platform

<sub>Type Property</sub>

The platform on which to run the provider.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency static var platform: PreviewPlatform? { get }
```

## Discussion

Xcode infers the platform for a preview based on the currently selected target. If you have a multiplatform target and want to suggest a particular target for a preview, implement the `platform` computed property to provide a hint, and specify one of the [PreviewPlatform](../previewplatform.md) values:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
    }

    static var platform: PreviewPlatform? {
        PreviewPlatform.tvOS
    }
}
```

Xcode ignores this value unless you have a multiplatform target.

## Default Implementations

### PreviewProvider Implementations

- [platform](platform-5gkzc.md) — The platform to run the provider on. _(deprecated)_
