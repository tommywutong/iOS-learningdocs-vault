---
title: applicationExtension
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/applicationextension
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/applicationextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/applicationextension.json'
content_hash: 'sha256:db7c5fde07d2fef0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# applicationExtension

<sub>Type Property</sub>

A type that represents an app extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var applicationExtension: UTType { get }
```

## Discussion

The identifier for this type is `com.apple.application-and-system-extension`.

This type conforms to [UTTypeXPCService](../uttypexpcservice.md).

## See Also

### Apple system types

- [framework](framework.md) — A type that represents an Apple framework bundle.
- [applicationBundle](applicationbundle.md) — A type that represents a bundled app.
- [spotlightImporter](spotlightimporter.md) — A type that represents a Spotlight metadata importer bundle.
- [quickLookGenerator](quicklookgenerator.md) — A type that represents a QuickLook preview generator bundle.
- [xpcService](xpcservice.md) — A type that represents an XPC service bundle.
- [systemPreferencesPane](systempreferencespane.md) — A type that represents a System Preferences pane.
