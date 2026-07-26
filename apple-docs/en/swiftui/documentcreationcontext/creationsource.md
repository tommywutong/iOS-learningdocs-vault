---
title: creationSource
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/documentcreationcontext/creationsource
source_url: 'https://developer.apple.com/documentation/swiftui/documentcreationcontext/creationsource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentcreationcontext/creationsource.json'
content_hash: 'sha256:4e6aaec41610b10a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentCreationContext](../documentcreationcontext.md)

# creationSource

<sub>Instance Property</sub>

The source associated with the button that created this document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var creationSource: DocumentCreationSource? { get }
```

## Discussion

On iOS, you can specify the source using a [NewDocumentButton](../newdocumentbutton.md) in [DocumentGroupLaunchScene](../documentgrouplaunchscene.md). On macOS, this is always `nil`.
