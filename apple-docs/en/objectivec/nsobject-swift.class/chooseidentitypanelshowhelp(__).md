---
title: 'chooseIdentityPanelShowHelp(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/chooseidentitypanelshowhelp(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/chooseidentitypanelshowhelp(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/chooseidentitypanelshowhelp%28_%3A%29.json'
content_hash: 'sha256:4599e4d11c5021d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# chooseIdentityPanelShowHelp(_:)

<sub>Instance Method</sub>

Implements custom help behavior for the modal panel.

<sub>macOS</sub>

```swift
func chooseIdentityPanelShowHelp(_ sender: SFChooseIdentityPanel!) -> Bool
```

## Parameters

- `sender` — The choose identity panel for which to implement custom help.

## Discussion

You can use this delegate method to implement custom help if you call the [setShowsHelp(_:)](<../../securityinterface/sfchooseidentitypanel/setshowshelp(__).md>) method to display a help button in the sheet or panel. If you are not implementing custom help, do not implement this method.

## See Also

### Related Documentation

- [setShowsHelp(_:)](<../../securityinterface/sfchooseidentitypanel/setshowshelp(__).md>) — Displays a Help button in the sheet or panel.
- [delegate](../../appkit/nswindow/delegate.md) — The window’s delegate.
