---
title: 'channel(_:)'
framework: ActivityKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/activitykit/pushtype/channel(_:)'
source_url: 'https://developer.apple.com/documentation/activitykit/pushtype/channel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/pushtype/channel%28_%3A%29.json'
content_hash: 'sha256:2f15462c4e740434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [PushType](../pushtype.md)

# channel(_:)

<sub>Type Method</sub>

A constant to configure a Live Activity that updates its dynamic content for broadcast channels.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func channel(_ name: String) -> PushType
```

## Overview

The channel ID is a base64-encoded string. For information on creating a channel, refer to [Sending channel management requests to APNs](../../usernotifications/sending-channel-management-requests-to-apns.md). The code snippet below is an example of how to specify that you want to use a broadcast push channel.

```swift
Activity.request(attributes: attributes, 
content: content,
pushType: .channel("c29tZUNoYW5uZWw="))
```

## See Also

### Supporting ActivityKit push notifications

- [token](token.md) — A constant you use to configure a Live Activity that updates its dynamic content by receiving ActivityKit push notifications.
