---
title: allowsLinkPreview
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（12.0 起废弃）, iPadOS 9.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/allowslinkpreview
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/allowslinkpreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/allowslinkpreview.json'
content_hash: 'sha256:9b058a88eef37da0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# allowsLinkPreview

<sub>Instance Property</sub>

A Boolean value that determines whether pressing on a link displays a preview of the destination for the link.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var allowsLinkPreview: Bool { get set }
```

## Discussion

This property is available on devices that support 3D Touch. Default value is [false](../../swift/false.md).

If you set this value to [true](../../swift/true.md) for a web view, users (with devices that support 3D Touch) can preview link destinations, and can preview detected data such as addresses, by pressing on links. Such previews are known to users as _peeks_. If a user presses deeper, the preview navigates (or _pops_, in user terminology) to the destination. Because pop navigation switches the user from your app to Safari, it is opt-in, by way of this property, rather default behavior for this class.

If you want to support link preview but also want to keep users within your app, you can switch from using the [UIWebView](../uiwebview.md) class to the [SFSafariViewController](../../safariservices/sfsafariviewcontroller.md) class. If you are using a web view as an in-app browser, making this change is best practice. The Safari view controller class automatically supports link previews.

## See Also

### Setting web content properties

- [scalesPageToFit](scalespagetofit.md) — A Boolean value determining whether the webpage scales to fit the view and the user can change the scale. _(deprecated)_
- [scrollView](scrollview.md) — The scroll view associated with the web view. _(deprecated)_
- [suppressesIncrementalRendering](suppressesincrementalrendering.md) — A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory. _(deprecated)_
- [keyboardDisplayRequiresUserAction](keyboarddisplayrequiresuseraction.md) — A Boolean value indicating whether web content can programmatically display the keyboard. _(deprecated)_
- [dataDetectorTypes](datadetectortypes.md) — The types of data converted to clickable URLs in the web view’s content. _(deprecated)_
