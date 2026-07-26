---
title: loadingPriority
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequest/loadingpriority
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/loadingpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/loadingpriority.json'
content_hash: 'sha256:24a4e802d43c3b09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# loadingPriority

<sub>Instance Property</sub>

A hint to the system of the relative priority of the resource request.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var loadingPriority: Double { get set }
```

## Discussion

Possible values are between `0.0` and `1.0` or the special constant [NSBundleResourceRequestLoadingPriorityUrgent](../nsbundleresourcerequestloadingpriorityurgent.md). The default is `0.5`. The system will attempt to give higher priority to requests with higher values. You can change the priority at any time, including during downloading of the managed resources.

## See Also

### Setting the download priority

- [NSBundleResourceRequestLoadingPriorityUrgent](../nsbundleresourcerequestloadingpriorityurgent.md) _(deprecated)_
