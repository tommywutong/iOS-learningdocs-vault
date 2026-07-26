---
title: showsTouchWhenHighlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibutton/showstouchwhenhighlighted
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/showstouchwhenhighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/showstouchwhenhighlighted.json'
content_hash: 'sha256:22229875386e119c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# showsTouchWhenHighlighted

<sub>Instance Property</sub>

A Boolean value that determines whether tapping the button causes it to glow.

> [!warning] Deprecated
> The system ignores this when you use [Configuration](configuration-swift.struct.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var showsTouchWhenHighlighted: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the button glows when tapped; otherwise, it does not. The image and button behavior is not changed by the glow. The default value is [false](../../swift/false.md).

## See Also

### Button presentation

- [adjustsImageWhenHighlighted](adjustsimagewhenhighlighted.md) — A Boolean value that determines whether the image changes when the button is highlighted. _(deprecated)_
- [adjustsImageWhenDisabled](adjustsimagewhendisabled.md) — A Boolean value that determines whether the image changes when the button is disabled. _(deprecated)_
