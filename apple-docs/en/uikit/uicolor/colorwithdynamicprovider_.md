---
title: 'colorWithDynamicProvider:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/colorwithdynamicprovider:'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/colorwithdynamicprovider:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/colorwithdynamicprovider%3A.json'
content_hash: 'sha256:c7a3c175f7c17341'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# colorWithDynamicProvider:

<sub>Type Method</sub>

Returns a color object that uses the specified block to generate its color data dynamically.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIColor *) colorWithDynamicProvider:(UIColor * (^)(UITraitCollection *traitCollection)) dynamicProvider;
```

## Parameters

- `dynamicProvider` — A block that determines the appropriate color values based on the specified traits. This block returns a [UIColor](../uicolor.md) object and takes a single parameter: - **traits** — The trait collection to use when generating the color information. Always use the traits in this collection, and not the traits of the current environment, when determining the color information.

## Return Value

A color object whose color information is provided by the specified block.

## Discussion

Use this method to create a color object whose component values change based on the currently active traits. The block you provide creates a new color object based on the traits in the provided trait collection.

## See Also

### Creating a color dynamically

- [- initWithDynamicProvider:](<init(dynamicprovider_).md>) — Creates a color object that uses the specified block to generate its color data dynamically.
