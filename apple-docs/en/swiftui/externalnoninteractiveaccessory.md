---
title: ExternalNonInteractiveAccessory
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/externalnoninteractiveaccessory
source_url: 'https://developer.apple.com/documentation/swiftui/externalnoninteractiveaccessory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/externalnoninteractiveaccessory.json'
content_hash: 'sha256:8ea525c7b93b1551'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ExternalNonInteractiveAccessory

<sub>Structure</sub>

A scene accessory that presents non-interactive content on an external display.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated struct ExternalNonInteractiveAccessory<Content> where Content : View
```

## Overview

The scene accessory may be presented when an external display is connected to the device, or when the device is connected to an external display via AirPlay.

For example, you can define a scene accessory for previewing a non-interactive presentation, which may be presented when an external display is connected:

```swift
struct RootView: View {
    var document: PresentationDocument

    var body: some View {
        PresentationDocumentView(document: document)
            .sceneAccessory {
                ExternalNonInteractiveAccessory {
                    PresentationPreview(document: document)
                }
            }
    }
}
```

## Relationships

- **Conforms To**: [SceneAccessoryContent](sceneaccessorycontent.md)

## Topics

### Initializers

- [init(content:)](<externalnoninteractiveaccessory/init(content_).md>) — Creates a scene accessory that presents non-interactive content on an external display. _(beta)_
- [init(isEnabled:content:)](<externalnoninteractiveaccessory/init(isenabled_content_).md>) — Creates a scene accessory that presents non-interactive content on an external display with a binding for programmatic enablement. _(beta)_

## See Also

### Presenting content on an external display

- [sceneAccessory(content:)](<view/sceneaccessory(content_).md>) — Defines any scene accessories associated with `self`. _(beta)_
- [SceneAccessoryContent](sceneaccessorycontent.md) — Conforming types represent items which define content for scene accessories. _(beta)_
