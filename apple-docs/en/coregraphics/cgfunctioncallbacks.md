---
title: CGFunctionCallbacks
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunctioncallbacks
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunctioncallbacks.json'
content_hash: 'sha256:7ebddbf7efbfbca1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFunctionCallbacks

<sub>Structure</sub>

A structure that contains callbacks needed by a `CGFunctionRef` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGFunctionCallbacks
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Initializers

- [init()](<cgfunctioncallbacks/init().md>)
- [init(version:evaluate:releaseInfo:)](<cgfunctioncallbacks/init(version_evaluate_releaseinfo_).md>)

### Instance Properties

- [evaluate](cgfunctioncallbacks/evaluate.md) — The callback that evaluates the function.
- [releaseInfo](cgfunctioncallbacks/releaseinfo.md) — If non-`NULL`,the callback used to release the `info` parameterpassed to [CGFunctionCreate](<cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>).
- [version](cgfunctioncallbacks/version.md) — The structure version number. For this structure,the version should be `0`.

## See Also

### Callbacks

- [CGFunctionEvaluateCallback](cgfunctionevaluatecallback.md) — Performs custom operations on the supplied input data to produce output data.
- [CGFunctionReleaseInfoCallback](cgfunctionreleaseinfocallback.md) — Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.
