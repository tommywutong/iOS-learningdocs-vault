---
title: ActivityContent
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.2+, iPadOS 16.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activitycontent
source_url: 'https://developer.apple.com/documentation/activitykit/activitycontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activitycontent.json'
content_hash: 'sha256:f9f979e24629be19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# ActivityContent

<sub>Structure</sub>

A structure that describes the state and configuration of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct ActivityContent<State> where State : Decodable, State : Encodable, State : Hashable
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Describing a Live Activity

- [init(state:staleDate:relevanceScore:)](<activitycontent/init(state_staledate_relevancescore_).md>) — Creates the object that describes the state and configuration of a Live Activity.
- [state](activitycontent/state.md) — The current state of a Live Activity in its life cycle.
- [staleDate](activitycontent/staledate.md) — The date when the system considers the Live Activity to be out of date.
- [relevanceScore](activitycontent/relevancescore.md) — A score you assign that determines the order in which your Live Activities appear when you start several Live Activities for your app.

## See Also

### Starting a Live Activity

- [request(attributes:content:pushType:)](<activity/request(attributes_content_pushtype_).md>) — Requests and starts a standard Live Activity.
- [request(attributes:content:pushType:style:)](<activity/request(attributes_content_pushtype_style_).md>) — Requests and starts a Live Activity.
- [request(attributes:content:pushType:style:alertConfiguration:start:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_start_).md>) — Requests and schedules a Live Activity for a specific date.
- [request(attributes:content:pushType:style:alertConfiguration:startDate:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_startdate_).md>) _(deprecated)_
- [attributes](activity/attributes.md) — A set of attributes that describe a Live Activity and its content.
- [ActivityAttributes](activityattributes.md) — The protocol you implement to describe the content of a Live Activity.
- [ActivityStyle](activitystyle.md)
- [content](activity/content.md) — The dynamic content of a Live Activity.
- [ContentState](activity/contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [PushType](pushtype.md) — The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [ActivityAuthorizationError](activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.
