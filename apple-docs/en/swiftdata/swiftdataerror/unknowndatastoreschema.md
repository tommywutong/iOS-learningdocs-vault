---
title: unknownDataStoreSchema
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/swiftdataerror/unknowndatastoreschema
source_url: 'https://developer.apple.com/documentation/swiftdata/swiftdataerror/unknowndatastoreschema'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/swiftdataerror/unknowndatastoreschema.json'
content_hash: 'sha256:dedf9bce83e9ea24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [SwiftDataError](../swiftdataerror.md)

# unknownDataStoreSchema

<sub>Type Property</sub>

An error that indicates the data store’s schema is not recognized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let unknownDataStoreSchema: SwiftDataError
```

## Discussion

This error occurs when a `ModelContainer` attempts to load a data store whose schema does not match the current schema or any schema defined in the provided migration plan.

When you encounter this error, the data store likely contains data from a schema version that your app no longer supports. To resolve this:

- Add the missing schema version to your `SchemaMigrationPlan`
- Provide a custom migration stage to handle the unrecognized schema
- Consider whether the data store should be recreated

This error is only thrown on processes linked on or after macOS 27 / iOS 27. On earlier versions, `loadIssueModelContainer` is thrown instead.
