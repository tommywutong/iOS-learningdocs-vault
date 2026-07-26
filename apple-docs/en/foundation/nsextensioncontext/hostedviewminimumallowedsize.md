---
title: hostedViewMinimumAllowedSize
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/hostedviewminimumallowedsize
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/hostedviewminimumallowedsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/hostedviewminimumallowedsize.json'
content_hash: 'sha256:6789cd8e7b5dc037'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# hostedViewMinimumAllowedSize

<sub>Instance Property</sub>

The minimum size for a Siri hosted view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hostedViewMinimumAllowedSize: CGSize { get }
```

## Discussion

Apps can customize the Siri interface using an Intents UI extension. The extension vends a view controller whose view contains the custom content that you want Siri to display. The size of that view controller’s view must be at least as large as the size value in this property.

## See Also

### Getting Siri-related information

- [hostedViewMaximumAllowedSize](hostedviewmaximumallowedsize.md) — The maximum size for a Siri hosted view.
- [- interfaceParametersDescription](<interfaceparametersdescription().md>) — Returns a human-readable string describing the data that SiriKit displays to the user when you handle an intent.
