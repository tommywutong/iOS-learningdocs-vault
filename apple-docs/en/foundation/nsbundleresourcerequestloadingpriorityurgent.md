---
title: NSBundleResourceRequestLoadingPriorityUrgent
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequestloadingpriorityurgent
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequestloadingpriorityurgent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequestloadingpriorityurgent.json'
content_hash: 'sha256:b58c34bb32e78698'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSBundleResourceRequestLoadingPriorityUrgent

<sub>Global Variable</sub>

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
let NSBundleResourceRequestLoadingPriorityUrgent: Double
```

## Discussion

A special value for loading priority informing the system that the user cannot continue until the resources marked with the tags managed by the request are downloaded. The system will dedicate the maximum amount of capacity to completing the resource request.

## See Also

### Setting the download priority

- [loadingPriority](nsbundleresourcerequest/loadingpriority.md) — A hint to the system of the relative priority of the resource request. _(deprecated)_
