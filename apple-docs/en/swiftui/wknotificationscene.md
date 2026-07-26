---
title: WKNotificationScene
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wknotificationscene
source_url: 'https://developer.apple.com/documentation/swiftui/wknotificationscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wknotificationscene.json'
content_hash: 'sha256:ae0cb3a801c60467'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WKNotificationScene

<sub>Structure</sub>

A scene which appears in response to receiving the specified category of remote or local notifications.

<sub>watchOS</sub>

```swift
nonisolated struct WKNotificationScene<Content, Controller> where Content : View, Controller : WKUserNotificationHostingController<Content>
```

## Relationships

- **Conforms To**: [Scene](scene.md)

## Topics

### Creating a notification scene

- [init(controller:category:)](<wknotificationscene/init(controller_category_).md>) — Creates a scene that appears in response to receiving a specific category of remote or local notifications.
