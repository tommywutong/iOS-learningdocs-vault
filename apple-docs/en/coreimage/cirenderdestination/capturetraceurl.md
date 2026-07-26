---
title: captureTraceURL
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirenderdestination/capturetraceurl
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestination/capturetraceurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestination/capturetraceurl.json'
content_hash: 'sha256:ecfc2946a2b4b5e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderDestination](../cirenderdestination.md)

# captureTraceURL

<sub>Instance Property</sub>

Tell the next render using this destination to capture a Metal trace.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var captureTraceURL: URL? { get set }
```

## Discussion

If this property is set to a file-based URL, then the next render using this destination will capture a Metal trace, deleting any existing file if present. This property is nil by default.
