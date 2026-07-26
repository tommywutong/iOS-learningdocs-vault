---
title: Autoadjustment Keys
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/autoadjustment-keys
source_url: 'https://developer.apple.com/documentation/coreimage/autoadjustment-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/autoadjustment-keys.json'
content_hash: 'sha256:71e8abf3a7d096ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIImage](ciimage.md)

# Autoadjustment Keys

<sub>API Collection</sub>

Constants used as keys in the options dictionary for the [- autoAdjustmentFiltersWithOptions:](<ciimage/autoadjustmentfilters(options_).md>) method.

## Topics

### Constants

- [kCIImageAutoAdjustEnhance](ciimageautoadjustmentoption/enhance.md) — A key used to specify whether to return enhancement filters.
- [kCIImageAutoAdjustRedEye](ciimageautoadjustmentoption/redeye.md) — A key used to specify whether to return a red eye filter.
- [kCIImageAutoAdjustFeatures](ciimageautoadjustmentoption/features.md) — A key used to specify an array of features that you want to apply enhancement and red eye filters to.
- [kCIImageAutoAdjustCrop](ciimageautoadjustmentoption/crop.md) — A key used to specify whether to return a filter that crops the image to focus on detected features.
- [kCIImageAutoAdjustLevel](ciimageautoadjustmentoption/level.md) — A key used to specify whether to return a filter that rotates the image to keep a level perspective.

## See Also

### Getting Autoadjustment Filters

- [- autoAdjustmentFilters](<ciimage/autoadjustmentfilters().md>) — Returns all possible automatically selected and configured filters for adjusting the image.
- [- autoAdjustmentFiltersWithOptions:](<ciimage/autoadjustmentfilters(options_).md>) — Returns a subset of automatically selected and configured filters for adjusting the image.
