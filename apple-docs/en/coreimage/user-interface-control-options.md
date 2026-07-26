---
title: User Interface Control Options
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/user-interface-control-options
source_url: 'https://developer.apple.com/documentation/coreimage/user-interface-control-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/user-interface-control-options.json'
content_hash: 'sha256:1b581f5afc446101'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIFilter](cifilter-swift.class.md)

# User Interface Control Options

<sub>API Collection</sub>

Sets of controls for various user scenarios.

## Overview

You can use these constants to specify the controls that you want associated with each user scenario. For example, for a filter that has many input parameters you can choose a small set of input parameters that the typical consumer can control and set the other input parameters to default values. For the same filter, however, you can choose to allow professional customers to control all the input parameters.

## Topics

### Constants

- [kCIUIParameterSet](kciuiparameterset.md) — The set of input parameters to use. The associated value can be [kCIUISetBasic](kciuisetbasic.md), [kCIUISetIntermediate](kciuisetintermediate.md), [kCIUISetAdvanced](kciuisetadvanced.md), or [kCIUISetDevelopment](kciuisetdevelopment.md).
- [kCIUISetBasic](kciuisetbasic.md) — Controls that are appropriate for a basic user scenario, that is, the minimum of settings to control the filter.
- [kCIUISetIntermediate](kciuisetintermediate.md) — Controls that are appropriate for an intermediate user scenario.
- [kCIUISetAdvanced](kciuisetadvanced.md) — Controls that are appropriate for an advanced user scenario.
- [kCIUISetDevelopment](kciuisetdevelopment.md) — Controls that should be visible  only for development purposes.

## See Also

### Constants

- [Filter Attribute Keys](filter-attribute-keys.md) — Attributes for a filter and its parameters.
- [Data Type Attributes](data-type-attributes.md) — Numeric data types.
- [Vector Quantity Attributes](vector-quantity-attributes.md) — Vector data types.
- [Color Attribute Keys](color-attribute-keys.md) — Color types.
- [Image Attribute Keys](image-attribute-keys.md) — Image Types
- [Filter Category Keys](filter-category-keys.md) — Categories of filters.
- [Options for Applying a Filter](options-for-applying-a-filter.md) — Options that control the application of a custom Core Image filter.
- [User Interface Options](user-interface-options.md) — Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](filter-parameter-keys.md) — Keys for input parameters to filters.
- [RAW Image Options](raw-image-options.md) — Options for creating a [CIFilter](cifilter-swift.class.md) object from RAW image data.
