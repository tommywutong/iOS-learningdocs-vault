---
title: SwiftData updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/swiftdata
source_url: 'https://developer.apple.com/documentation/updates/swiftdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/swiftdata.json'
content_hash: 'sha256:ce1eff6a8131e491'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# SwiftData updates

<sub>Article</sub>

Learn about important changes to SwiftData.

## Overview

Browse notable changes in [SwiftData](../swiftdata.md).

## June 2026

- Section your query results by creating your query with a macro that takes a `sectionBy` parameter, as listed on the [Additional query macros](../swiftdata/additionalquerymacros.md) page.
- Use types that conform to [Codable](../swift/codable.md) in a model, including types you don’t control directly, by using the  [codable](../swiftdata/schema/attribute/option/codable.md) option for [Schema.Attribute](../swiftdata/schema/attribute.md).
- Receive real-time updates to models that match specified fetch criteria by using the [ResultsObserver](../swiftdata/resultsobserver.md) type.
- Observe remote model changes with the [HistoryObserver](../swiftdata/historyobserver.md) type.

## June 2025

- Increase the flexibility of your models by adopting inheritance through the [Model()](<../swiftdata/model().md>) macro.
- Gain added flexibility in accessing and sorting transaction history using [sortBy](../swiftdata/historydescriptor/sortby.md) in the [HistoryDescriptor](../swiftdata/historydescriptor.md).

## June 2024

### Macros

- Improve performance of sorts and predicate-based fetches by using the [Index(_:)](<../swiftdata/index(__)-74ia2.md>) macro to define individual and compound indexes.
- Define a unique constraint that includes one or more model attributes using the [Unique(_:)](<../swiftdata/unique(__).md>) macro, enabling SwiftData to regard tuples of attributes as unique.
- Specify `nil` as a relationship’s `inverse` to create a unidirectional relationship.

### Persistent history

- Fetch historical changes for one or more persistent models using the model context’s [fetchHistory(_:)](<../swiftdata/modelcontext/fetchhistory(__).md>) method.
- Delete stale model history from a persistent store by calling the context’s [deleteHistory(_:)](<../swiftdata/modelcontext/deletehistory(__).md>) method.
- Provide an alternate change tracking strategy for your custom persistent store by adopting the [HistoryProviding](../swiftdata/historyproviding.md) protocol.

### Custom persistent stores

- Adopt the [DataStore](../swiftdata/datastore.md) protocol (and related protocols) to provide custom storage for your app’s persistent models.

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
