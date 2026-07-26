---
title: renderingAttributesValidator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/renderingattributesvalidator
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/renderingattributesvalidator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/renderingattributesvalidator.json'
content_hash: 'sha256:7610866bd2a53fda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# renderingAttributesValidator

<sub>Instance Property</sub>

A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var renderingAttributesValidator: ((NSTextLayoutManager, NSTextLayoutFragment) -> Void)? { get set }
```

## Discussion

The validator uses [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>) to fill the rendering attributes appropriate for the range inside `textLayoutFragment`.

## See Also

### Configuring global layout manager options

- [layoutQueue](layoutqueue.md) — The queue that the framework dispatches layout operations on.
- [usesFontLeading](usesfontleading.md) — A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [usesHyphenation](useshyphenation.md) — A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.
- [limitsLayoutForSuspiciousContents](limitslayoutforsuspiciouscontents.md) — A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.
