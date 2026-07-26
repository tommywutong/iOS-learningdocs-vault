---
title: 'request(attributes:content:pushType:style:alertConfiguration:startDate:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+（26.0 起废弃）, iPadOS 26.0+（26.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/activitykit/activity/request(attributes:content:pushtype:style:alertconfiguration:startdate:)'
source_url: 'https://developer.apple.com/documentation/activitykit/activity/request(attributes:content:pushtype:style:alertconfiguration:startdate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activity/request%28attributes%3Acontent%3Apushtype%3Astyle%3Aalertconfiguration%3Astartdate%3A%29.json'
content_hash: 'sha256:bf85fb3d4b8953dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [Activity](../activity.md)

# request(attributes:content:pushType:style:alertConfiguration:startDate:)

<sub>Type Method</sub>

> [!warning] Deprecated
> Use `request(attributes:content:pushType:style:alertConfiguration:start:)` instead

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func request(attributes: Attributes, content: ActivityContent<Activity<Attributes>.ContentState>, pushType: PushType? = nil, style: ActivityStyle, alertConfiguration: AlertConfiguration, startDate: Date) throws -> Activity<Attributes>
```

## See Also

### Starting a Live Activity

- [request(attributes:content:pushType:)](<request(attributes_content_pushtype_).md>) — Requests and starts a standard Live Activity.
- [request(attributes:content:pushType:style:)](<request(attributes_content_pushtype_style_).md>) — Requests and starts a Live Activity.
- [request(attributes:content:pushType:style:alertConfiguration:start:)](<request(attributes_content_pushtype_style_alertconfiguration_start_).md>) — Requests and schedules a Live Activity for a specific date.
- [attributes](attributes.md) — A set of attributes that describe a Live Activity and its content.
- [ActivityAttributes](../activityattributes.md) — The protocol you implement to describe the content of a Live Activity.
- [ActivityStyle](../activitystyle.md)
- [content](content.md) — The dynamic content of a Live Activity.
- [ActivityContent](../activitycontent.md) — A structure that describes the state and configuration of a Live Activity.
- [ContentState](contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [PushType](../pushtype.md) — The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [ActivityAuthorizationError](../activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.
