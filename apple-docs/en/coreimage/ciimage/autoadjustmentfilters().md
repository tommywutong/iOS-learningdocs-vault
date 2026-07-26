---
title: autoAdjustmentFilters()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/autoadjustmentfilters()
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/autoadjustmentfilters()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/autoadjustmentfilters%28%29.json'
content_hash: 'sha256:e980ed84b8b6b725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# autoAdjustmentFilters()

<sub>Instance Method</sub>

Returns all possible automatically selected and configured filters for adjusting the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func autoAdjustmentFilters() -> [CIFilter]
```

## Return Value

An array of [CIFilter](../cifilter-swift.class.md) instances preconfigured for correcting deficiencies in the supplied image.

## See Also

### Getting Autoadjustment Filters

- [- autoAdjustmentFiltersWithOptions:](<autoadjustmentfilters(options_).md>) — Returns a subset of automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](../autoadjustment-keys.md) — Constants used as keys in the options dictionary for the [- autoAdjustmentFiltersWithOptions:](<autoadjustmentfilters(options_).md>) method.
