---
title: attributes
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activity/attributes
source_url: 'https://developer.apple.com/documentation/activitykit/activity/attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/attributes.json'
content_hash: 'sha256:428febffb9ed90ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# attributes

<sub>Instance Property</sub>

A set of attributes that describe a Live Activity and its content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
final let attributes: Attributes
```

## See Also

### Starting a Live Activity

- [request(attributes:content:pushType:)](<request(attributes_content_pushtype_).md>) — Requests and starts a standard Live Activity.
- [request(attributes:content:pushType:style:)](<request(attributes_content_pushtype_style_).md>) — Requests and starts a Live Activity.
- [request(attributes:content:pushType:style:alertConfiguration:start:)](<request(attributes_content_pushtype_style_alertconfiguration_start_).md>) — Requests and schedules a Live Activity for a specific date.
- [request(attributes:content:pushType:style:alertConfiguration:startDate:)](<request(attributes_content_pushtype_style_alertconfiguration_startdate_).md>) _(deprecated)_
- [ActivityAttributes](../activityattributes.md) — The protocol you implement to describe the content of a Live Activity.
- [ActivityStyle](../activitystyle.md)
- [content](content.md) — The dynamic content of a Live Activity.
- [ActivityContent](../activitycontent.md) — A structure that describes the state and configuration of a Live Activity.
- [ContentState](contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [PushType](../pushtype.md) — The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [ActivityAuthorizationError](../activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.
