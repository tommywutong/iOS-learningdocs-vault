---
title: currentControlTintDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nscolor/currentcontroltintdidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nscolor/currentcontroltintdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscolor/currentcontroltintdidchangenotification.json'
content_hash: 'sha256:58c9ab31ab8e4e7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSColor](../nscolor.md)

# currentControlTintDidChangeNotification

<sub>Type Property</sub>

Sent after the user changes control tint preference.

> [!warning] Deprecated
> Changes to the accent color can be manually observed by implementing -viewDidChangeEffectiveAppearance in a NSView subclass, or by Key-Value Observing the -effectiveAppearance property on NSApplication. Views are automatically redisplayed when the accent color changes.

<sub>macOS</sub>

```swift
class let currentControlTintDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is `NSApp`. This notification does not contain a `userInfo` dictionary.

## See Also

### Deprecated

- [ignoresAlpha](ignoresalpha.md) — A Boolean value that indicates whether the app supports alpha. _(deprecated)_
- [colorSpaceName](colorspacename.md) — The name of the color space associated with the color. _(deprecated)_
- [- colorUsingColorSpaceName:](<usingcolorspacename(__).md>) — Creates a new color object whose color is the same as the receiver’s, except that the new color object is in the specified color space. _(deprecated)_
- [- colorUsingColorSpaceName:device:](<usingcolorspacename(__device_).md>) — Creates a new color object for the same color, but in the specified color space and specific to the provided device. _(deprecated)_
