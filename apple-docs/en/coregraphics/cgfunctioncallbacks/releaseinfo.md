---
title: releaseInfo
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunctioncallbacks/releaseinfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/releaseinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunctioncallbacks/releaseinfo.json'
content_hash: 'sha256:4e57fa263aa5e6cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGFunctionCallbacks](../cgfunctioncallbacks.md)

# releaseInfo

<sub>Instance Property</sub>

If non-`NULL`,the callback used to release the `info` parameterpassed to [CGFunctionCreate](<../cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var releaseInfo: CGFunctionReleaseInfoCallback?
```

## See Also

### Instance Properties

- [evaluate](evaluate.md) — The callback that evaluates the function.
- [version](version.md) — The structure version number. For this structure,the version should be `0`.
