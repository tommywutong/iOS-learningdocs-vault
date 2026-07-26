---
title: underlyingErrors
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 11.3+, tvOS 14.5+, visionOS 1.0+, watchOS 7.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/cocoaerror/underlyingerrors
source_url: 'https://developer.apple.com/documentation/foundation/cocoaerror/underlyingerrors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/cocoaerror/underlyingerrors.json'
content_hash: 'sha256:e6a3cb97e42852f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CocoaError](../cocoaerror.md)

# underlyingErrors

<sub>Instance Property</sub>

A list of underlying errors, if any. It includes the values of both NSUnderlyingErrorKey and NSMultipleUnderlyingErrorsKey. If there are no underlying errors, returns an empty array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var underlyingErrors: [any Error] { get }
```
