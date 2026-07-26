---
title: always
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/formatstyle/componentdisplayoption/always
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle/componentdisplayoption/always'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle/componentdisplayoption/always.json'
content_hash: 'sha256:f06119b3176b0d8f'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [URL](../../../url.md) · [FormatStyle](../../formatstyle.md) · [ComponentDisplayOption](../componentdisplayoption.md)

# always

<sub>Type Property</sub>

A display option that always displays the component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var always: URL.FormatStyle.ComponentDisplayOption { get }
```

## See Also

### Display options

- [never](never.md) — A display option that never displays the component.
- [omitIfHTTPFamily](omitifhttpfamily.md) — A display option that omits the component if the URL scheme is any flavor of HTTP.
- [displayWhen(_:matches:)](<displaywhen(__matches_).md>) — Returns a display option that displays the component when a specified component meets the specified requirements.
- [omitWhen(_:matches:)](<omitwhen(__matches_).md>) — Returns a display option that omits the component when a specified component meets the specified requirements.
- [Component](../component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.
