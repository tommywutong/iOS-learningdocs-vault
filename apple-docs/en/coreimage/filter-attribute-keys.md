---
title: Filter Attribute Keys
framework: Core Image
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/filter-attribute-keys
source_url: 'https://developer.apple.com/documentation/coreimage/filter-attribute-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/filter-attribute-keys.json'
content_hash: 'sha256:e0111c7fe5d6d194'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md) · [CIFilter](cifilter-swift.class.md)

# Filter Attribute Keys

<sub>API Collection</sub>

Attributes for a filter and its parameters.

## Overview

Attribute keys are used for the attribute dictionary of a filter.  Most entries in the attribute dictionary are optional. The attribute [kCIAttributeFilterName](kciattributefiltername.md) is mandatory. For a parameter, the attribute [kCIAttributeClass](kciattributeclass.md) is mandatory because it specifies the class name of the filter.

A parameter of type [NSNumber](../foundation/nsnumber.md) does not necessarily need the attributes [kCIAttributeMin](kciattributemin.md) and [kCIAttributeMax](kciattributemax.md). These attributes are not present when the parameter has no upper or lower bounds. For example, the Gaussian blur filter has a radius parameter with a minimum of `0` but no maximum value to indicate that all nonnegative values are valid.

## Topics

### Constants

- [kCIAttributeFilterName](kciattributefiltername.md) — The filter name.
- [kCIAttributeFilterDisplayName](kciattributefilterdisplayname.md) — The localized version of the filter name that is displayed in the user interface.
- [kCIAttributeDescription](kciattributedescription.md) — The localized description of the filter. This description should inform the user what the filter does and be short enough to display in the user interface for the filter. It is not intended to be technically detailed.
- [kCIAttributeFilterAvailable_Mac](kciattributefilteravailable_mac.md) — The macOS version in which the filter first became available.
- [kCIAttributeFilterAvailable_iOS](kciattributefilteravailable_ios.md) — The iOS version in which the filter first became available.
- [kCIAttributeReferenceDocumentation](kciattributereferencedocumentation.md) — The localized reference documentation for the filter. The reference should provide developers with technical details.
- [kCIAttributeFilterCategories](kciattributefiltercategories.md) — An array of filter category keys that specifies all the categories in which the filter is a member.
- [kCIAttributeClass](kciattributeclass.md) — The class name of the filter.
- [kCIAttributeType](kciattributetype.md) — The type of an attribute.
- [kCIAttributeMin](kciattributemin.md) — The minimum value for a filter parameter, specified as a floating-point value.
- [kCIAttributeMax](kciattributemax.md) — The maximum value for a filter parameter, specified as a floating-point value.
- [kCIAttributeSliderMin](kciattributeslidermin.md) — The minimum value, specified as a floating-point value, to use for a slider that controls input values for a filter parameter.
- [kCIAttributeSliderMax](kciattributeslidermax.md) — The maximum value, specified as a floating-point value, to use for a slider that controls input values for a filter parameter.
- [kCIAttributeDefault](kciattributedefault.md) — The default value, specified as a floating-point value, for a filter parameter.
- [kCIAttributeIdentity](kciattributeidentity.md) — If supplied as a value for a parameter, the parameter has no effect on the input image.
- [kCIAttributeName](kciattributename.md) — The name of the attribute.
- [kCIAttributeDisplayName](kciattributedisplayname.md) — The localized display name of the attribute.

## See Also

### Constants

- [Data Type Attributes](data-type-attributes.md) — Numeric data types.
- [Vector Quantity Attributes](vector-quantity-attributes.md) — Vector data types.
- [Color Attribute Keys](color-attribute-keys.md) — Color types.
- [Image Attribute Keys](image-attribute-keys.md) — Image Types
- [Filter Category Keys](filter-category-keys.md) — Categories of filters.
- [Options for Applying a Filter](options-for-applying-a-filter.md) — Options that control the application of a custom Core Image filter.
- [User Interface Control Options](user-interface-control-options.md) — Sets of controls for various user scenarios.
- [User Interface Options](user-interface-options.md) — Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](filter-parameter-keys.md) — Keys for input parameters to filters.
- [RAW Image Options](raw-image-options.md) — Options for creating a [CIFilter](cifilter-swift.class.md) object from RAW image data.
