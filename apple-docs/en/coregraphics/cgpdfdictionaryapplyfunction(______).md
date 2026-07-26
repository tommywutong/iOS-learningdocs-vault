---
title: 'CGPDFDictionaryApplyFunction(_:_:_:)'
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfdictionaryapplyfunction(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdictionaryapplyfunction(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdictionaryapplyfunction%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0578287f25362eb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPDFDictionaryApplyFunction(_:_:_:)

<sub>Function</sub>

Applies a function to each entry in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionaryRef, _ function: CGPDFDictionaryApplierFunction, _ info: UnsafeMutableRawPointer?)
```

## Parameters

- `dict` — A PDF dictionary. If this parameter is not a valid PDF dictionary, the behavior is undefined.

- `function` — The function to apply to each entry in the dictionary.

- `info` — A pointer to contextual information to pass to the function.

## Discussion

This function enumerates all of the entries in the dictionary, calling the function once for each. The current key, its associated value, and the contextual information are passed to the function (see also [CGPDFDictionaryApplierFunction](cgpdfdictionaryapplierfunction.md)).
