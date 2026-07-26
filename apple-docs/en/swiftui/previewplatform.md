---
title: PreviewPlatform
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewplatform
source_url: 'https://developer.apple.com/documentation/swiftui/previewplatform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewplatform.json'
content_hash: 'sha256:5d0be9d5b901b701'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PreviewPlatform

<sub>Enumeration</sub>

Platforms that can run the preview.

> [!warning] Deprecated
> Use [Preview(_:body:)](<preview(__body_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PreviewPlatform
```

## Overview

Xcode infers the platform for a preview based on the currently selected target. If you have a multiplatform target and want to suggest a particular target for a preview, implement the [platform](previewprovider/platform.md) computed property as a hint, and specify one of the preview platforms:

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

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting an operating system

- [PreviewPlatform.iOS](previewplatform/ios.md) — Specifies iOS as the preview platform. _(deprecated)_
- [PreviewPlatform.macOS](previewplatform/macos.md) — Specifies macOS as the preview platform. _(deprecated)_
- [PreviewPlatform.tvOS](previewplatform/tvos.md) — Specifies tvOS as the preview platform. _(deprecated)_
- [PreviewPlatform.watchOS](previewplatform/watchos.md) — Specifies watchOS as the preview platform. _(deprecated)_

## See Also

### Defining a preview

- [PreviewProvider](previewprovider.md) — A type that produces view previews in Xcode. _(deprecated)_
- [previewDisplayName(_:)](<view/previewdisplayname(__).md>) — Sets a user visible name to show in the canvas for a preview. _(deprecated)_
