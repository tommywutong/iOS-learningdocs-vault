---
title: UTTypeApplicationExtension
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeapplicationextension
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeapplicationextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeapplicationextension.json'
content_hash: 'sha256:0ca6433c16292916'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeApplicationExtension

<sub>Global Variable</sub>

A type that represents an app extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeApplicationExtension;
```

## Discussion

The identifier for this type is `com.apple.application-and-system-extension`.

This type conforms to [UTTypeXPCService](uttypexpcservice.md).

## See Also

### Apple system types

- [UTTypeFramework](uttypeframework.md) — A type that represents an Apple framework bundle.
- [UTTypeApplicationBundle](uttypeapplicationbundle.md) — A type that represents a bundled app.
- [UTTypeSpotlightImporter](uttypespotlightimporter.md) — A type that represents a Spotlight metadata importer bundle.
- [UTTypeQuickLookGenerator](uttypequicklookgenerator.md) — A type that represents a QuickLook preview generator bundle.
- [UTTypeXPCService](uttypexpcservice.md) — A type that represents an XPC service bundle.
- [UTTypeSystemPreferencesPane](uttypesystempreferencespane.md) — A type that represents a System Preferences pane.
