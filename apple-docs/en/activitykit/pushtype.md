---
title: PushType
framework: ActivityKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/pushtype
source_url: 'https://developer.apple.com/documentation/activitykit/pushtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/pushtype.json'
content_hash: 'sha256:2b5e07609698820a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# PushType

<sub>Structure</sub>

The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct PushType
```

## Overview

Pass the [token](pushtype/token.md) constant to the [request(attributes:contentState:pushType:)](<activity/request(attributes_contentstate_pushtype_).md>) function to start a Live Activity that receives content updates with ActivityKit push notifications. Pass [channel(_:)](<pushtype/channel(__).md>) to [request(attributes:contentState:pushType:)](<activity/request(attributes_contentstate_pushtype_).md>) function to specify that you want to use a broadcast channel instead of a token. You can only specify one [PushType](pushtype.md).

To learn more about using ActivityKit push notifications to update your Live Activity, see [Starting and updating Live Activities with ActivityKit push notifications](starting-and-updating-live-activities-with-activitykit-push-notifications.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Supporting ActivityKit push notifications

- [token](pushtype/token.md) — A constant you use to configure a Live Activity that updates its dynamic content by receiving ActivityKit push notifications.
- [channel(_:)](<pushtype/channel(__).md>) — A constant to configure a Live Activity that updates its dynamic content for broadcast channels.

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
- [ActivityContent](activitycontent.md) — A structure that describes the state and configuration of a Live Activity.
- [ContentState](activity/contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [ActivityAuthorizationError](activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.
