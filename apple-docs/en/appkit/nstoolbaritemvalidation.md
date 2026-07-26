---
title: NSToolbarItemValidation
framework: AppKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstoolbaritemvalidation
source_url: 'https://developer.apple.com/documentation/appkit/nstoolbaritemvalidation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstoolbaritemvalidation.json'
content_hash: 'sha256:8883d87505c26a91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSToolbarItemValidation

<sub>Protocol</sub>

Validation of a toolbar item.

<sub>macOS</sub>

```swift
protocol NSToolbarItemValidation : NSObjectProtocol
```

## Overview

A toolbar item with a valid target and action is enabled by default. To allow a toolbar item to be disabled in certain situations, a toolbar item’s target can implement the [- validateToolbarItem:](<nstoolbaritemvalidation/validatetoolbaritem(__).md>) method.

> [!note] Note
> The [NSToolbarItem](nstoolbaritem.md) [- validate](<nstoolbaritem/validate().md>) method is called only if the item’s target has a valid action defined on its target and if the item isn’t a custom view item. If you want to validate a custom view item, then you have to subclass [NSToolbarItem](nstoolbaritem.md) and override [- validate](<nstoolbaritem/validate().md>).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Enabling and disabling toolbar items

- [- validateToolbarItem:](<nstoolbaritemvalidation/validatetoolbaritem(__).md>) — Determines whether to enable or disable the toolbar item.

## See Also

### View

- [Integrating a Toolbar and Touch Bar into Your App](integrating-a-toolbar-and-touch-bar-into-your-app.md) — Provide users quick access to your app’s features from a toolbar and corresponding Touch Bar.
- [NSToolbar](nstoolbar.md) — An object that manages the space above your app’s custom content and either below or integrated with the window’s title bar.
