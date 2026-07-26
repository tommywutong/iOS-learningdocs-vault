---
title: AssistiveAccess
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/assistiveaccess
source_url: 'https://developer.apple.com/documentation/swiftui/assistiveaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/assistiveaccess.json'
content_hash: 'sha256:c0aaf562943304dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AssistiveAccess

<sub>Structure</sub>

A scene that presents an interface appropriate for Assistive Access on iOS and iPadOS. On other platforms, this scene is unused.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct AssistiveAccess<Content> where Content : View
```

## Relationships

- **Conforms To**: [Scene](scene.md)

## Topics

### Initializers

- [init(content:)](<assistiveaccess/init(content_).md>) — Creates an Assistive Access scene.

## See Also

### Using assistive access

- [accessibilityAssistiveAccessEnabled](environmentvalues/accessibilityassistiveaccessenabled.md) — A Boolean value that indicates whether Assistive Access is in use.
- [assistiveAccessNavigationIcon(_:)](<view/assistiveaccessnavigationicon(__).md>) — Configures the view’s icon for purposes of navigation.
- [assistiveAccessNavigationIcon(systemImage:)](<view/assistiveaccessnavigationicon(systemimage_).md>) — Configures the view’s icon for purposes of navigation.
