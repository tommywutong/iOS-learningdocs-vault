---
title: UTTypeApplicationBundle
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeapplicationbundle
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeapplicationbundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeapplicationbundle.json'
content_hash: 'sha256:59083a6f4649ece9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeApplicationBundle

<sub>Global Variable</sub>

A type that represents a bundled app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeApplicationBundle;
```

## Discussion

The identifier for this type is `com.apple.application-bundle`.

This type conforms to [UTTypeApplication](uttypeapplication.md), [UTTypeBundle](uttypebundle.md), and [UTTypePackage](uttypepackage.md).

## See Also

### Apple system types

- [UTTypeFramework](uttypeframework.md) — A type that represents an Apple framework bundle.
- [UTTypeApplicationExtension](uttypeapplicationextension.md) — A type that represents an app extension.
- [UTTypeSpotlightImporter](uttypespotlightimporter.md) — A type that represents a Spotlight metadata importer bundle.
- [UTTypeQuickLookGenerator](uttypequicklookgenerator.md) — A type that represents a QuickLook preview generator bundle.
- [UTTypeXPCService](uttypexpcservice.md) — A type that represents an XPC service bundle.
- [UTTypeSystemPreferencesPane](uttypesystempreferencespane.md) — A type that represents a System Preferences pane.
