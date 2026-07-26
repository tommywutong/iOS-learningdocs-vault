---
title: interfaceParametersDescription()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensioncontext/interfaceparametersdescription()
source_url: 'https://developer.apple.com/documentation/foundation/nsextensioncontext/interfaceparametersdescription()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensioncontext/interfaceparametersdescription%28%29.json'
content_hash: 'sha256:7c78b4dd922ad121'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExtensionContext](../nsextensioncontext.md)

# interfaceParametersDescription()

<sub>Instance Method</sub>

Returns a human-readable string describing the data that SiriKit displays to the user when you handle an intent.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func interfaceParametersDescription() -> String
```

## Discussion

If you provide an Intents UI app extension, you can customize all or some of the interface that SiriKit displays to the user for a given intent. The information displayed by SiriKit is different for each intent, and can change in the future. During development, use this method to retrieve a human-readable description of the contents of the [INParameter](../../intents/inparameter.md) objects that SiriKit intends to display for the current intent. Use that information to plan your custom interface.

For information about customizing the Siri and Maps interfaces, see [Creating an Intents App Extension](../../sirikit/creating-an-intents-app-extension.md).

## See Also

### Getting Siri-related information

- [hostedViewMinimumAllowedSize](hostedviewminimumallowedsize.md) — The minimum size for a Siri hosted view.
- [hostedViewMaximumAllowedSize](hostedviewmaximumallowedsize.md) — The maximum size for a Siri hosted view.
