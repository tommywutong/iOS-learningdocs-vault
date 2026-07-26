---
title: 'callAsFunction(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiconfigurationcolortransformer-swift.struct/callasfunction(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/callasfunction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationcolortransformer-swift.struct/callasfunction%28_%3A%29.json'
content_hash: 'sha256:8378562d3bc800d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationColorTransformer](../uiconfigurationcolortransformer-swift.struct.md)

# callAsFunction(_:)

<sub>Instance Method</sub>

Calls the transform closure of the color transformer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func callAsFunction(_ input: UIColor) -> UIColor
```

## Discussion

Using this syntax, you can call the color transformer type as if it were a closure:

```swift
let alphaColorTransformer = UIConfigurationColorTransformer() { baseColor -> UIColor in
    return baseColor.withAlphaComponent(0.5)
}

let baseColor = UIColor.red
let modifiedColor = alphaColorTransformer(baseColor)
```

## See Also

### Calling the color transformer

- [transform](transform.md) — The transform closure of the color transformer.
