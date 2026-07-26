---
title: ActivityViewContext
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/activityviewcontext
source_url: 'https://developer.apple.com/documentation/widgetkit/activityviewcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/activityviewcontext.json'
content_hash: 'sha256:dede32eb2def478f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# ActivityViewContext

<sub>Structure</sub>

A structure that describes the view context for creating the views of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ActivityViewContext<Attributes> where Attributes : ActivityAttributes
```

## Topics

### Describing a Live Activity

- [attributes](activityviewcontext/attributes.md) — A set of attributes that describe a Live Activity and its content at the time of its creation.
- [state](activityviewcontext/state.md) — The dynamic content of a Live Activity at the time of its creation.
- [isStale](activityviewcontext/isstale.md) — A Boolean value that describes whether the Live Activity is out of date.
- [activityID](activityviewcontext/activityid.md) — A unique identifier for the Live Activity.

## See Also

### Creating a Live Activity configuration

- [init(for:content:dynamicIsland:)](<activityconfiguration/init(for_content_dynamicisland_).md>) — Creates a configuration object for a Live Activity.
