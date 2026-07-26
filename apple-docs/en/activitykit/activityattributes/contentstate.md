---
title: ContentState
framework: ActivityKit
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityattributes/contentstate
source_url: 'https://developer.apple.com/documentation/activitykit/activityattributes/contentstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityattributes/contentstate.json'
content_hash: 'sha256:f21144df16adc05e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityAttributes](../activityattributes.md)

# ContentState

<sub>Associated Type</sub>

The associated type that describes the dynamic content of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
associatedtype ContentState : Decodable, Encodable, Hashable
```

## Discussion

The dynamic data of a Live Activity that’s encoded by `ContentState` can’t exceed 4KB.
