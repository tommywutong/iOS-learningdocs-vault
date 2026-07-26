---
title: 'callAsFunction(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/callasfunction(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/callasfunction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct/callasfunction%28_%3A%29.json'
content_hash: 'sha256:c897a2d6cde597fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationTextAttributesTransformer](../uiconfigurationtextattributestransformer-swift.struct.md)

# callAsFunction(_:)

<sub>Instance Method</sub>

Calls the transform closure of the text attributes transformer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func callAsFunction(_ input: AttributeContainer) -> AttributeContainer
```

## Parameters

- `input` — The current attributes container for a string.

## Return Value

A new, transformed attributes container.

## Discussion

Using this syntax, you can call the text attributes transformer type as if it were a closure:

```swift
var container = AttributeContainer()
container.backgroundColor = UIColor.blue
let transformer = UIConfigurationTextAttributesTransformer { incoming in
    var outgoing = incoming
    outgoing.backgroundColor = incoming.backgroundColor?.withAlphaComponent(0.6)
    return outgoing
}
let transformed = transformer.callAsFunction(container)

```
