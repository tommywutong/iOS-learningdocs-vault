---
title: usesHyphenation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/useshyphenation
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/useshyphenation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/useshyphenation.json'
content_hash: 'sha256:71913c4c480951cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# usesHyphenation

<sub>Instance Property</sub>

A Boolean values that controls whether the text layout manager attempts to hyphenate when wrapping lines.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var usesHyphenation: Bool { get set }
```

## Discussion

Defaults to `true`.

## See Also

### Configuring global layout manager options

- [layoutQueue](layoutqueue.md) — The queue that the framework dispatches layout operations on.
- [renderingAttributesValidator](renderingattributesvalidator.md) — A callback block that the framework invokes whenever the text layout manager needs to validate the rendering attributes for the range.
- [usesFontLeading](usesfontleading.md) — A Boolean value that controls whether the framework uses the leading information specified by the font when laying out text.
- [limitsLayoutForSuspiciousContents](limitslayoutforsuspiciouscontents.md) — A Boolean value that controls internal security analysis for malicious inputs and activates defensive behaviors.
