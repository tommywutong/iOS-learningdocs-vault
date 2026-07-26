---
title: UIPasteConfiguration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration.json'
content_hash: 'sha256:4124f2b41af75c74'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPasteConfiguration

<sub>Class</sub>

The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPasteConfiguration
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a paste configuration

- [- init](<uipasteconfiguration/init().md>) — Initializes a new paste configuration.
- [- initWithAcceptableTypeIdentifiers:](<uipasteconfiguration/init(acceptabletypeidentifiers_).md>) — Initializes a new paste configuration with a specified array of acceptable UTIs.
- [- initWithTypeIdentifiersForAcceptingClass:](<uipasteconfiguration/init(foraccepting_)-6is3h.md>) — Initializes a new paste configuration with the UTIs declared as supported by a specified class.
- [init(forAccepting:)](<uipasteconfiguration/init(foraccepting_)-84r2r.md>)

### Getting acceptable type identifiers

- [acceptableTypeIdentifiers](uipasteconfiguration/acceptabletypeidentifiers.md) — An array of UTI strings that specify the types accepted by the paste configuration.

### Adding acceptable type identifiers

- [- addAcceptableTypeIdentifiers:](<uipasteconfiguration/addacceptabletypeidentifiers(__).md>) — Adds an array of UTI strings to a paste configuration, increasing the variety of types the paste configuration accepts.
- [- addTypeIdentifiersForAcceptingClass:](<uipasteconfiguration/addtypeidentifiers(foraccepting_)-4fvd6.md>) — Expands the array of accepted UTIs for a paste configuration, based on those declared as supported by a specified class.
- [addTypeIdentifiers(forAccepting:)](<uipasteconfiguration/addtypeidentifiers(foraccepting_)-8af7o.md>)

### Initializers

- [init(coder:)](<uipasteconfiguration/init(coder_).md>)
- [init(typeIdentifiersForAcceptingClass:)](<uipasteconfiguration/init(typeidentifiersforacceptingclass_).md>)

## See Also

### Pasteboard

- [UIPasteControl](uipastecontrol.md) — A button that a person taps to place pasteboard contents in your app.
- [Configuration](uipastecontrol/configuration-swift.class.md) — An object that determines a paste button’s color, corner style, icon, and text.
- [DisplayMode](uipastecontrol/displaymode.md) — Options that determine whether a paste button composes an icon, textual label, or both.
- [UIPasteboard](uipasteboard.md) — An object that helps a user share data from one place to another within your app, and from your app to other apps.
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md) — The interface that determines whether a responder object supports paste configuration.
