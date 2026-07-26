---
title: askPermission
framework: PermissionKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.5+, iPadOS 26.5+, macOS 26.5+, visionOS 26.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/askpermission
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/askpermission'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/askpermission.json'
content_hash: 'sha256:ebe3e768ef17d27d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# askPermission

<sub>Instance Property</sub>

An action that sends a permission question to a parent or guardian.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var askPermission: AskPermissionAction { get }
```

## Discussion

Use this environment value to get an `AskPermissionAction` instance for the current [Environment](../environment.md). Then call the instance to send a permission question. You call the instance directly because it defines a `AskPermissionAction/callAsFunction(_:)` method that Swift calls when you call the instance directly.
