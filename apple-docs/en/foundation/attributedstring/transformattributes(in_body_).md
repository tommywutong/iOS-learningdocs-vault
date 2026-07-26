---
title: 'transformAttributes(in:body:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/transformattributes(in:body:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/transformattributes(in:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/transformattributes%28in%3Abody%3A%29.json'
content_hash: 'sha256:1cac6f124f4ae3d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# transformAttributes(in:body:)

<sub>Instance Method</sub>

Apply a change to the attributes in the entire selection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func transformAttributes<E>(in selection: inout AttributedTextSelection, body: (inout AttributeContainer) throws(E) -> Void) throws(E) where E : Error
```

## Discussion

Applies the given `body` to the selection. Specifically, in the case of a selection spanning one or multiple characters, the `body` is applied to every run in the selection individually, modifying only the part of the run that is in the selection.

In the case of an insertion point, the `body` is applied to the attribute container defining the typing attributes. After that, attributes that are bound to the whole paragraph or the character immediately preceding the caret via [AttributedString.AttributeRunBoundaries](attributerunboundaries.md) are applied directly to attributed string at the respective range.

Use this function to implement controls that operate on the user’s current selection. Some controls define the new value relative to the current state of each individual run in the selection, e.g. a stepper for the font size:

```
Stepper("Font Size", onIncrement: {
    text.transformAttributes(in: &selection) {
        $0.font = ($0.font ?? .default).scaled(by: 1.2)
    }
}, onDecrement: {
    text.transformAttributes(in: &selection) {
        $0.font = ($0.font ?? .default).scaled(by: 1 / 1.2)
    }
})
```

Other controls, such as toggles for boldness, italics, or underline usually define the new value for all ranges as the opposite of the value in the typing attributes, as defined by `AttributedTextSelection/typingAttributes(in:)`:

```
Toggle("B", isOn: .init(get: {
    let font = selection.typingAttributes(in: text).font ?? .default
    return font.resolve(in: environment).isBold
}, set: { isBold in
    text.transformAttributes(in: &selection) {
        $0.font = ($0.font ?? .default).bold(isBold)
    }
}))
```
