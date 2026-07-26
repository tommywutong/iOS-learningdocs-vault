---
title: Displaying a checkbox in your Mac app built with Mac Catalyst
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst
source_url: 'https://developer.apple.com/documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.json'
content_hash: 'sha256:ae420f8732f6a32b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Mac Catalyst](mac-catalyst.md)

# Displaying a checkbox in your Mac app built with Mac Catalyst

<sub>Article</sub>

Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.

## Overview

A Mac app built with Mac Catalyst that uses the Mac user interface idiom displays a [UISwitch](uiswitch.md) as a checkbox when the [preferredStyle](uiswitch/preferredstyle.md) value is [UISwitchStyleAutomatic](uiswitch/style-swift.enum/automatic.md) (the default value) or [UISwitchStyleCheckbox](uiswitch/style-swift.enum/checkbox.md). If your app doesn’t use the [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md) idiom, the switch appears as a slider switch. To learn more, see [Choosing a user interface idiom for your Mac app](choosing-a-user-interface-idiom-for-your-mac-app.md).

### Add text to the checkbox

To display text alongside the checkbox, set the [title](uiswitch/title.md) property.

```swift
let showFavoritesAtTop = UISwitch()
showFavoritesAtTop.title = "Always show favorite recipes at the top"
```

### Resize the checkbox

A checkbox-style switch has a default frame size of zero. If you’re not using Auto Layout to determine the size and position of the switch, call [- sizeToFit](<uiview/sizetofit().md>) to resize it so that it uses the appropriate amount of space needed to display the checkbox and its title.

## See Also

### User interface

- [UIKit Catalog: Creating and customizing views and controls](uikit-catalog-creating-and-customizing-views-and-controls.md) — Customize your app’s user interface with views and controls.
- [Building and improving your app with Mac Catalyst](building-and-improving-your-app-with-mac-catalyst.md) — Improve your iPadOS app with Mac Catalyst by supporting native controls, multiple windows, sharing, printing, menus and keyboard shortcuts.
- [Removing the title bar in your Mac app built with Mac Catalyst](removing-the-title-bar-in-your-mac-app-built-with-mac-catalyst.md) — Display content that fills the entire height of a window by removing the title bar.
- [Toolbar](toolbar.md) — Provide a space for controls under a window’s title bar and above your custom content.
- [Touch Bar](../appkit/touch-bar.md) — Display interactive content and controls in the Touch Bar.
