---
title: scalesPageToFit
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/scalespagetofit
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/scalespagetofit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/scalespagetofit.json'
content_hash: 'sha256:9fca1ebfbef18ca4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# scalesPageToFit

<sub>Instance Property</sub>

A Boolean value determining whether the webpage scales to fit the view and the user can change the scale.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var scalesPageToFit: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the webpage is scaled to fit and the user can zoom in and zoom out. If [false](../../swift/false.md), user zooming is disabled. The default value is [false](../../swift/false.md).

## See Also

### Setting web content properties

- [allowsLinkPreview](allowslinkpreview.md) — A Boolean value that determines whether pressing on a link displays a preview of the destination for the link. _(deprecated)_
- [scrollView](scrollview.md) — The scroll view associated with the web view. _(deprecated)_
- [suppressesIncrementalRendering](suppressesincrementalrendering.md) — A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory. _(deprecated)_
- [keyboardDisplayRequiresUserAction](keyboarddisplayrequiresuseraction.md) — A Boolean value indicating whether web content can programmatically display the keyboard. _(deprecated)_
- [dataDetectorTypes](datadetectortypes.md) — The types of data converted to clickable URLs in the web view’s content. _(deprecated)_
