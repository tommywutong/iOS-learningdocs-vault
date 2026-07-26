---
title: 'command(for:propertyList:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/command(for:propertylist:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/command(for:propertylist:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/command%28for%3Apropertylist%3A%29.json'
content_hash: 'sha256:7e4ed893030ce413'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# command(for:propertyList:)

<sub>Instance Method</sub>

Gets the command for the specified selector and property list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func command(for action: Selector, propertyList: Any? = nil) -> UICommand?
```

## Parameters

- `action` — The selector of the command to retrieve.

- `propertyList` — The property list object that identifies the command when more than one command uses the same action.

## Return Value

A command object; otherwise, `nil` if there is no such command.

## See Also

### Getting menu systems and elements

- [system](system.md) — The menu system that the menu builder modifies.
- [- menuForIdentifier:](<menu(for_).md>) — Gets the menu for the specified menu identifier.
- [- actionForIdentifier:](<action(for_).md>) — Gets the action for the specified action identifier.
