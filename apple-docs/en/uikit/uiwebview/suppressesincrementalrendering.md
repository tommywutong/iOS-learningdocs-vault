---
title: suppressesIncrementalRendering
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（12.0 起废弃）, iPadOS 6.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/suppressesincrementalrendering
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/suppressesincrementalrendering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/suppressesincrementalrendering.json'
content_hash: 'sha256:c44d70ec70aff65c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# suppressesIncrementalRendering

<sub>Instance Property</sub>

A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var suppressesIncrementalRendering: Bool { get set }
```

## Discussion

When set to [true](../../swift/true.md), the web view does not attempt to render incoming content as it arrives. Instead, the view’s current contents remain in place until all of the new content has been received, at which point the new content is rendered. This property does not affect the rendering of content retrieved after a frame finishes loading.

The value of this property is [false](../../swift/false.md) by default.

## See Also

### Setting web content properties

- [allowsLinkPreview](allowslinkpreview.md) — A Boolean value that determines whether pressing on a link displays a preview of the destination for the link. _(deprecated)_
- [scalesPageToFit](scalespagetofit.md) — A Boolean value determining whether the webpage scales to fit the view and the user can change the scale. _(deprecated)_
- [scrollView](scrollview.md) — The scroll view associated with the web view. _(deprecated)_
- [keyboardDisplayRequiresUserAction](keyboarddisplayrequiresuseraction.md) — A Boolean value indicating whether web content can programmatically display the keyboard. _(deprecated)_
- [dataDetectorTypes](datadetectortypes.md) — The types of data converted to clickable URLs in the web view’s content. _(deprecated)_
