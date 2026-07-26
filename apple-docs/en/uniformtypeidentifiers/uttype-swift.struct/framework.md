---
title: framework
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/framework
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/framework'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/framework.json'
content_hash: 'sha256:86cd85df4c8d3d4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# framework

<sub>Type Property</sub>

A type that represents an Apple framework bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var framework: UTType { get }
```

## Discussion

The identifier for this type is `com.apple.framework`.

This type conforms to [UTTypePluginBundle](../uttypepluginbundle.md).

## See Also

### Apple system types

- [applicationBundle](applicationbundle.md) — A type that represents a bundled app.
- [applicationExtension](applicationextension.md) — A type that represents an app extension.
- [spotlightImporter](spotlightimporter.md) — A type that represents a Spotlight metadata importer bundle.
- [quickLookGenerator](quicklookgenerator.md) — A type that represents a QuickLook preview generator bundle.
- [xpcService](xpcservice.md) — A type that represents an XPC service bundle.
- [systemPreferencesPane](systempreferencespane.md) — A type that represents a System Preferences pane.
