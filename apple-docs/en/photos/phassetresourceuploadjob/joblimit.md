---
title: jobLimit
framework: Photos
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.1+, iPadOS 26.1+, Mac Catalyst 27.0+ beta, macOS 27.0+ beta]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourceuploadjob/joblimit
source_url: 'https://developer.apple.com/documentation/photos/phassetresourceuploadjob/joblimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourceuploadjob/joblimit.json'
content_hash: 'sha256:d5ca7ae811d293c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceUploadJob](../phassetresourceuploadjob.md)

# jobLimit

<sub>Type Property</sub>

The maximum number of unacknowledged upload jobs allowed.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class var jobLimit: Int { get }
```

## Discussion

This includes jobs that are in-flight and those that have succeeded or failed.

## See Also

### Fetching jobs

- [+ fetchJobsWithAction:options:](<fetchjobs(action_options_).md>) — Returns all asset resource upload jobs applicable for a given action.
- [Action](action.md) — An action to perform on an upload job.
