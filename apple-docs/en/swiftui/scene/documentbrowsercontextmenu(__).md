---
title: 'documentBrowserContextMenu(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.1+, iPadOS 18.1+, Mac Catalyst 18.1+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scene/documentbrowsercontextmenu(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scene/documentbrowsercontextmenu(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene/documentbrowsercontextmenu%28_%3A%29.json'
content_hash: 'sha256:f8c6e8fc738783bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Scene](../scene.md)

# documentBrowserContextMenu(_:)

<sub>Instance Method</sub>

Adds to a `DocumentGroupLaunchScene` actions that accept a list of selected files as their parameter.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency func documentBrowserContextMenu(@ContentBuilder _ menu: @escaping ([URL]?) -> some View) -> some Scene

```

## Parameters

- `menu` — Items representing the content of the menu.

## Discussion

The actions are displayed in the document browser navigation bar when a document browser is in Select mode, and also added to context menu for the file items.

## See Also

### Configuring a document launcher scene

- [documentLaunchTitle(_:)](<documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_
