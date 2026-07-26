---
title: touchBar
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/touchbar
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/touchbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/touchbar.json'
content_hash: 'sha256:050de73bc545ab2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# touchBar

<sub>Instance Property</sub>

The Touch Bar object for the responder.

<sub>Mac Catalyst</sub>

```swift
var touchBar: NSTouchBar? { get set }
```

## Discussion

This property’s default value — on devices with a Touch Bar — is the [NSTouchBar](../../appkit/nstouchbar.md) instance that the responder’s [- makeTouchBar](<maketouchbar().md>) method returns. Otherwise, the default value is `nil`.

## See Also

### Managing the Touch Bar

- [- makeTouchBar](<maketouchbar().md>) — Asks the receiving responder to create and configure a Touch Bar object.
