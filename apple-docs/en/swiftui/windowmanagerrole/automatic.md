---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/windowmanagerrole/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/windowmanagerrole/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowmanagerrole/automatic.json'
content_hash: 'sha256:a7354a6090bc62de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowManagerRole](../windowmanagerrole.md)

# automatic

<sub>Type Property</sub>

The automatic role. The type and configuration of the scene will be used to determine how its windows behave in full screen and Stage Manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: WindowManagerRole
```

## Discussion

On macOS, [WindowGroup](../windowgroup.md) and [DocumentGroup](../documentgroup.md) scenes will use the `principal` role. [Window](../window.md) scenes will use the `principal` role when they are specified as the first scene in the app’s definition, and use the `associated` role otherwise. [Settings](../settings.md) will use the `associated` role.
