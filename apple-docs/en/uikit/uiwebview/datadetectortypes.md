---
title: dataDetectorTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（12.0 起废弃）, iPadOS 3.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/datadetectortypes
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/datadetectortypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/datadetectortypes.json'
content_hash: 'sha256:0ca310b796896d1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# dataDetectorTypes

<sub>Instance Property</sub>

The types of data converted to clickable URLs in the web view’s content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var dataDetectorTypes: UIDataDetectorTypes { get set }
```

## Discussion

Use this property to specify the types of data (phone numbers, HTTP links, email address, and so on) that should be automatically converted to clickable URLs in the web view. When clicked, the web view opens the app responsible for handling the URL type and passes it the URL.

See the [UIDataDetectorTypes](../uidatadetectortypes.md) enumeration for the types of data available for automatic detection.

## See Also

### Setting web content properties

- [allowsLinkPreview](allowslinkpreview.md) — A Boolean value that determines whether pressing on a link displays a preview of the destination for the link. _(deprecated)_
- [scalesPageToFit](scalespagetofit.md) — A Boolean value determining whether the webpage scales to fit the view and the user can change the scale. _(deprecated)_
- [scrollView](scrollview.md) — The scroll view associated with the web view. _(deprecated)_
- [suppressesIncrementalRendering](suppressesincrementalrendering.md) — A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory. _(deprecated)_
- [keyboardDisplayRequiresUserAction](keyboarddisplayrequiresuseraction.md) — A Boolean value indicating whether web content can programmatically display the keyboard. _(deprecated)_
