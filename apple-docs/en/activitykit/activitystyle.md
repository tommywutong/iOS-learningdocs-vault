---
title: ActivityStyle
framework: ActivityKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitystyle
source_url: 'https://developer.apple.com/documentation/activitykit/activitystyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitystyle.json'
content_hash: 'sha256:791df46e11842f4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# ActivityStyle

<sub>Enumeration</sub>

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum ActivityStyle
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Style

- [ActivityStyle.standard](activitystyle/standard.md)
- [ActivityStyle.transient](activitystyle/transient.md)

## See Also

### Starting a Live Activity

- [request(attributes:content:pushType:)](<activity/request(attributes_content_pushtype_).md>) — Requests and starts a standard Live Activity.
- [request(attributes:content:pushType:style:)](<activity/request(attributes_content_pushtype_style_).md>) — Requests and starts a Live Activity.
- [request(attributes:content:pushType:style:alertConfiguration:start:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_start_).md>) — Requests and schedules a Live Activity for a specific date.
- [request(attributes:content:pushType:style:alertConfiguration:startDate:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_startdate_).md>) _(deprecated)_
- [attributes](activity/attributes.md) — A set of attributes that describe a Live Activity and its content.
- [ActivityAttributes](activityattributes.md) — The protocol you implement to describe the content of a Live Activity.
- [content](activity/content.md) — The dynamic content of a Live Activity.
- [ActivityContent](activitycontent.md) — A structure that describes the state and configuration of a Live Activity.
- [ContentState](activity/contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [PushType](pushtype.md) — The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [ActivityAuthorizationError](activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.
