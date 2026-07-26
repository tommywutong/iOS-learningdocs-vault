---
title: evaluate
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunctioncallbacks/evaluate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/evaluate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunctioncallbacks/evaluate.json'
content_hash: 'sha256:074aabd8906ac94a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFunctionCallbacks](../cgfunctioncallbacks.md)

# evaluate

<sub>Instance Property</sub>

The callback that evaluates the function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var evaluate: CGFunctionEvaluateCallback?
```

## See Also

### Instance Properties

- [releaseInfo](releaseinfo.md) — If non-`NULL`,the callback used to release the `info` parameterpassed to [CGFunctionCreate](<../cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>).
- [version](version.md) — The structure version number. For this structure,the version should be `0`.
