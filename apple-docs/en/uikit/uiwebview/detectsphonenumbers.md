---
title: detectsPhoneNumbers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/detectsphonenumbers
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/detectsphonenumbers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/detectsphonenumbers.json'
content_hash: 'sha256:ec201882fc56291c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# detectsPhoneNumbers

<sub>Instance Property</sub>

A Boolean value indicating whether telephone number detection is on.

> [!warning] Deprecated
> Use [dataDetectorTypes](datadetectortypes.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) BOOL detectsPhoneNumbers;
```

## Discussion

If [true](../../swift/true.md), telephone number detection is on; otherwise, [false](../../swift/false.md). If a webpage contains numbers that can be interpreted as phone numbers, but are not phone numbers, you can turn off telephone number detection by setting this property to [false](../../swift/false.md). The default value is [true](../../swift/true.md) on devices that have phone capabilities.

### Special considerations

The functionality provided by this property has been superseded by the [dataDetectorTypes](datadetectortypes.md) property.
