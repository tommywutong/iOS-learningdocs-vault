---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturescope/label
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturescope/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturescope/label.json'
content_hash: 'sha256:f9ea6748eb534902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureScope](../mtlcapturescope.md)

# label

<sub>Instance Property</sub>

A string that helps you identify the capture scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Setting a capture scope’s label makes it easier to find in Xcode. See [Creating and using custom capture scopes](../../xcode/creating-and-using-custom-capture-scopes.md) for more information.

## See Also

### Identifying the capture scope

- [device](device.md) — The device object from which you created the capture scope.
- [commandQueue](commandqueue.md) — The command queue that this capture scope uses to limit which commands are recorded.
