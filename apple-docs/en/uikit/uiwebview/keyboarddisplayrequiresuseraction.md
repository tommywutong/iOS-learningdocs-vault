---
title: keyboardDisplayRequiresUserAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（12.0 起废弃）, iPadOS 6.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/keyboarddisplayrequiresuseraction
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/keyboarddisplayrequiresuseraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/keyboarddisplayrequiresuseraction.json'
content_hash: 'sha256:5750ac4f7ea347c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# keyboardDisplayRequiresUserAction

<sub>Instance Property</sub>

A Boolean value indicating whether web content can programmatically display the keyboard.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var keyboardDisplayRequiresUserAction: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), the user must explicitly tap the elements in the web view to display the keyboard (or other relevant input view) for that element. When set to [false](../../swift/false.md), a focus event on an element causes the input view to be displayed and associated with that element automatically.

The default value for this property is [true](../../swift/true.md).

## See Also

### Setting web content properties

- [allowsLinkPreview](allowslinkpreview.md) — A Boolean value that determines whether pressing on a link displays a preview of the destination for the link. _(deprecated)_
- [scalesPageToFit](scalespagetofit.md) — A Boolean value determining whether the webpage scales to fit the view and the user can change the scale. _(deprecated)_
- [scrollView](scrollview.md) — The scroll view associated with the web view. _(deprecated)_
- [suppressesIncrementalRendering](suppressesincrementalrendering.md) — A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory. _(deprecated)_
- [dataDetectorTypes](datadetectortypes.md) — The types of data converted to clickable URLs in the web view’s content. _(deprecated)_
