---
title: 'textElements(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextcontentmanager/textelements(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/textelements(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/textelements%28for%3A%29.json'
content_hash: 'sha256:0211260fac82aa12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# textElements(for:)

<sub>Instance Method</sub>

Returns an array of text elements that intersect with the range you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textElements(for range: NSTextRange) -> [NSTextElement]
```

## Parameters

- `range` — An [NSTextRange](../nstextrange.md) that describes the range of text to process.

## Return Value

An array of [NSTextElement](../nstextelement.md).

## Discussion

This method can return a set of elements that don’t fill the entire range if the entire range isn’t synchronously available. Uses [- enumerateTextElementsFromLocation:options:usingBlock:](<../nstextelementprovider/enumeratetextelements(from_options_using_).md>) to fill the array.
