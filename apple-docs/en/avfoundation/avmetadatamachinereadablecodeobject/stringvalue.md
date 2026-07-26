---
title: stringValue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetadatamachinereadablecodeobject/stringvalue
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetadatamachinereadablecodeobject/stringvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetadatamachinereadablecodeobject/stringvalue.json'
content_hash: 'sha256:0c83627e87a9e566'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetadataMachineReadableCodeObject](../avmetadatamachinereadablecodeobject.md)

# stringValue

<sub>Instance Property</sub>

Returns the error-corrected data decoded into a human-readable string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var stringValue: String? { get }
```

## Discussion

The value of this property is an `NSString` created by decoding the binary payload according to the format of the machine-readable code, or `nil` if a string representation cannot be created.

## See Also

### Getting machine-readable code values

- [corners](corners-58qbe.md) — A Swift array of corner points.
- [descriptor](descriptor.md) — A barcode description for use in Core Image.
