---
title: adjustsImageWhenDisabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 2.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibutton/adjustsimagewhendisabled
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/adjustsimagewhendisabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/adjustsimagewhendisabled.json'
content_hash: 'sha256:2b8647008269eb7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# adjustsImageWhenDisabled

<sub>Instance Property</sub>

A Boolean value that determines whether the image changes when the button is disabled.

> [!warning] Deprecated
> Use [configurationUpdateHandler](configurationupdatehandler-swift.property.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var adjustsImageWhenDisabled: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the image is drawn darker when the button is disabled. The default value is [true](../../swift/true.md).

## See Also

### Button presentation

- [adjustsImageWhenHighlighted](adjustsimagewhenhighlighted.md) — A Boolean value that determines whether the image changes when the button is highlighted. _(deprecated)_
- [showsTouchWhenHighlighted](showstouchwhenhighlighted.md) — A Boolean value that determines whether tapping the button causes it to glow. _(deprecated)_
