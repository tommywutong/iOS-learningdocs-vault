---
title: UISheetPresentationControllerDetentResolutionContext
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontrollerdetentresolutioncontext.json'
content_hash: 'sha256:36b404675cfc02db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISheetPresentationControllerDetentResolutionContext

<sub>Protocol</sub>

A context for resolving custom detent values.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol UISheetPresentationControllerDetentResolutionContext : NSObjectProtocol
```

## Overview

A context of this type is available in the `resolver` closure of [custom(identifier:resolver:)](<uisheetpresentationcontroller/detent/custom(identifier_resolver_).md>) (Swift) or  [customDetentWithIdentifier:resolver:](uisheetpresentationcontrollerdetent/customdetentwithidentifier_resolver_.md) (Objective-C).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the properties of the context

- [containerTraitCollection](uisheetpresentationcontrollerdetentresolutioncontext/containertraitcollection.md) — The trait collection of the sheet’s container view.
- [maximumDetentValue](uisheetpresentationcontrollerdetentresolutioncontext/maximumdetentvalue.md) — The maximum value of a detent.

## See Also

### Creating a custom detent

- [custom(identifier:resolver:)](<uisheetpresentationcontroller/detent/custom(identifier_resolver_).md>) — Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [resolvedValue(in:)](<uisheetpresentationcontroller/detent/resolvedvalue(in_).md>) — Resolves a detent to its value.
