---
title: adjustsImageWhenHighlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 2.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uibutton/adjustsimagewhenhighlighted
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/adjustsimagewhenhighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/adjustsimagewhenhighlighted.json'
content_hash: 'sha256:8729fec3e19a6f9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# adjustsImageWhenHighlighted

<sub>Instance Property</sub>

A Boolean value that determines whether the image changes when the button is highlighted.

> [!warning] Deprecated
> Use [configurationUpdateHandler](configurationupdatehandler-swift.property.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var adjustsImageWhenHighlighted: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the image is drawn lighter when the button is highlighted. The default value is [true](../../swift/true.md).

## See Also

### Button presentation

- [adjustsImageWhenDisabled](adjustsimagewhendisabled.md) — A Boolean value that determines whether the image changes when the button is disabled. _(deprecated)_
- [showsTouchWhenHighlighted](showstouchwhenhighlighted.md) — A Boolean value that determines whether tapping the button causes it to glow. _(deprecated)_
