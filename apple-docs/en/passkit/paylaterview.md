---
title: PayLaterView
framework: PassKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/passkit/paylaterview
source_url: 'https://developer.apple.com/documentation/passkit/paylaterview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/paylaterview.json'
content_hash: 'sha256:771c4d20ff0a56ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# PayLaterView

<sub>Structure</sub>

A view that displays the Apple Pay Later visual merchandising widget.

> [!warning] Deprecated
> Apple Pay Later is deprecated.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency struct PayLaterView<FallbackView> where FallbackView : View
```

## Overview

Use this view to display a widget that allows people to learn more about the Apple Pay Later feature.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Setting the view’s action

- [PayLaterViewAction](paylaterviewaction.md) — Values you use to set the Apple Pay Later action. _(deprecated)_

### Styling the view

- [PayLaterViewDisplayStyle](paylaterviewdisplaystyle.md) — Values you use to style an Apple Pay Later visual merchandising widget. _(deprecated)_

### Initializers

- [init(amount:currency:)](<paylaterview/init(amount_currency_).md>)

## See Also

### Deprecated

- [PKPayLaterView](pkpaylaterview.md) — A view that displays the Apple Pay Later visual merchandising widget. _(deprecated)_
