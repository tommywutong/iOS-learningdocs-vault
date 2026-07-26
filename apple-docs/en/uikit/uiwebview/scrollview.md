---
title: scrollView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（12.0 起废弃）, iPadOS 5.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/scrollview
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/scrollview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/scrollview.json'
content_hash: 'sha256:ca770df71b795cb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# scrollView

<sub>Instance Property</sub>

The scroll view associated with the web view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var scrollView: UIScrollView { get }
```

## Discussion

Your app can access the scroll view if it wants to customize the scrolling behavior of the web view.

## See Also

### Setting web content properties

- [allowsLinkPreview](allowslinkpreview.md) — A Boolean value that determines whether pressing on a link displays a preview of the destination for the link. _(deprecated)_
- [scalesPageToFit](scalespagetofit.md) — A Boolean value determining whether the webpage scales to fit the view and the user can change the scale. _(deprecated)_
- [suppressesIncrementalRendering](suppressesincrementalrendering.md) — A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory. _(deprecated)_
- [keyboardDisplayRequiresUserAction](keyboarddisplayrequiresuseraction.md) — A Boolean value indicating whether web content can programmatically display the keyboard. _(deprecated)_
- [dataDetectorTypes](datadetectortypes.md) — The types of data converted to clickable URLs in the web view’s content. _(deprecated)_
