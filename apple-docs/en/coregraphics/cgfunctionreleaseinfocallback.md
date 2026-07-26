---
title: CGFunctionReleaseInfoCallback
framework: Core Graphics
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunctionreleaseinfocallback
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunctionreleaseinfocallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunctionreleaseinfocallback.json'
content_hash: 'sha256:b5a391225e61234a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFunctionReleaseInfoCallback

<sub>Type Alias</sub>

Performs custom clean-up tasks when Core Graphics deallocates a `CGFunctionRef` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CGFunctionReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

## Parameters

- `info` — The `info` parameter passed to [CGFunctionCreate](<cgfunction/init(info_domaindimension_domain_rangedimension_range_callbacks_).md>).

## See Also

### Callbacks

- [CGFunctionCallbacks](cgfunctioncallbacks.md) — A structure that contains callbacks needed by a `CGFunctionRef` object.
- [CGFunctionEvaluateCallback](cgfunctionevaluatecallback.md) — Performs custom operations on the supplied input data to produce output data.
