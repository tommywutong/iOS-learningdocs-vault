---
title: 'isEqual(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/symbolconfiguration-swift.class/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/symbolconfiguration-swift.class/isequal%28to%3A%29.json'
content_hash: 'sha256:7ba7bf65d4a18ab0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImage](../../uiimage.md) · [SymbolConfiguration](../symbolconfiguration-swift.class.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the configuration objects are equivalent.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to otherConfiguration: UIImage.SymbolConfiguration?) -> Bool
```

## Parameters

- `otherConfiguration` — The other configuration object. Specify `nil` to compare the current configuration object to the configuration object in the [unspecifiedConfiguration](unspecified.md) property.

## Return Value

[true](../../../swift/true.md) if the trait collections and image configuration values of both objects match; otherwise, [false](../../../swift/false.md).
