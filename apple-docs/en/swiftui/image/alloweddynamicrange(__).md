---
title: 'allowedDynamicRange(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/image/alloweddynamicrange(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/image/alloweddynamicrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/image/alloweddynamicrange%28_%3A%29.json'
content_hash: 'sha256:2ce457c0780e9de5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Image](../image.md)

# allowedDynamicRange(_:)

<sub>Instance Method</sub>

Returns a new image configured with the specified allowed dynamic range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func allowedDynamicRange(_ range: Image.DynamicRange?) -> Image
```

## Parameters

- `range` — The requested dynamic range, or nil to restore the default allowed range.

## Return Value

A new image.

## Discussion

The following example enables HDR rendering for a specific image view, assuming that the image has an HDR (ITU-R 2100) color space and the output device supports it:

```swift
Image("hdr-asset").allowedDynamicRange(.high)
```

## See Also

### Specifying dynamic range

- [allowedDynamicRange](../environmentvalues/alloweddynamicrange.md) — The allowed dynamic range for the view, or nil.
- [DynamicRange](dynamicrange.md)
