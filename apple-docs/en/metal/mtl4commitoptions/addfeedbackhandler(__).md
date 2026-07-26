---
title: 'addFeedbackHandler(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4commitoptions/addfeedbackhandler(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4commitoptions/addfeedbackhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commitoptions/addfeedbackhandler%28_%3A%29.json'
content_hash: 'sha256:64fc99ff393db042'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommitOptions](../mtl4commitoptions.md)

# addFeedbackHandler(_:)

<sub>Instance Method</sub>

Registers a commit feedback handler that Metal calls with feedback data when available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addFeedbackHandler(_ block: @escaping MTL4CommitFeedbackHandler)
```

## Parameters

- `block` — [MTL4CommitFeedbackHandler](../mtl4commitfeedbackhandler.md) that Metal invokes.
