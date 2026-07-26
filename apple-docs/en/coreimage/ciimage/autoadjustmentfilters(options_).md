---
title: 'autoAdjustmentFilters(options:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/autoadjustmentfilters(options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/autoadjustmentfilters(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/autoadjustmentfilters%28options%3A%29.json'
content_hash: 'sha256:8ed3b6b97550a754'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# autoAdjustmentFilters(options:)

<sub>Instance Method</sub>

Returns a subset of automatically selected and configured filters for adjusting the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]? = nil) -> [CIFilter]
```

## Parameters

- `options` — You can control which filters are returned by supplying one or more of the keys described in [Autoadjustment Keys](../autoadjustment-keys.md). The options dictionary can also contain a [CIDetectorImageOrientation](../cidetectorimageorientation.md) key. Because some autoadjustment filters rely on face detection, you should specify an image orientation if you want to enable these filters for an image containing face whose orientation does not match that of the image.

## Return Value

An array of [CIFilter](../cifilter-swift.class.md) instances preconfigured for correcting deficiencies in the supplied image.

## See Also

### Getting Autoadjustment Filters

- [- autoAdjustmentFilters](<autoadjustmentfilters().md>) — Returns all possible automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](../autoadjustment-keys.md) — Constants used as keys in the options dictionary for the [- autoAdjustmentFiltersWithOptions:](<autoadjustmentfilters(options_).md>) method.
