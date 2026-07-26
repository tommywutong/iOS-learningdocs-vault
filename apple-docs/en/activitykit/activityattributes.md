---
title: ActivityAttributes
framework: ActivityKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityattributes
source_url: 'https://developer.apple.com/documentation/activitykit/activityattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityattributes.json'
content_hash: 'sha256:639658ec709dc0b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ActivityKit](../activitykit.md)

# ActivityAttributes

<sub>Protocol</sub>

The protocol you implement to describe the content of a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
protocol ActivityAttributes : Decodable, Encodable
```

## Overview

The `ActivityAttributes` protocol describes the content that appears in your Live Activity. Its inner type [ContentState](activityattributes/contentstate.md) represents the dynamic content of the Live Activity.

The following example shows an implementation of the `ActivityAttributes` protocol for a pizza delivery app. The app’s Live Activity shows the number of ordered pizzas and the total amount on the bill as static data and the name of the driver and an estimated delivery time as dynamic data that changes over time. Note how the implementation defines the type alias `PizzaDeliveryStatus` to make the code more descriptive and easier to read.

```swift
public import Foundation
import ActivityKit

struct PizzaDeliveryAttributes: ActivityAttributes {
    public typealias PizzaDeliveryStatus = ContentState

    public struct ContentState: Codable, Hashable {
        var driverName: String
        var deliveryTimer: ClosedRange<Date>
    }

    var numberOfPizzas: Int
    var totalAmount: String
    var orderNumber: String
}
```

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md)

## Topics

### Dynamic content

- [ContentState](activityattributes/contentstate.md) — The associated type that describes the dynamic content of a Live Activity.

### Instance Methods

- [previewContext(_:isStale:viewKind:)](<activityattributes/previewcontext(__isstale_viewkind_).md>) — Generates a preview for a Live Activity.

## See Also

### Starting a Live Activity

- [request(attributes:content:pushType:)](<activity/request(attributes_content_pushtype_).md>) — Requests and starts a standard Live Activity.
- [request(attributes:content:pushType:style:)](<activity/request(attributes_content_pushtype_style_).md>) — Requests and starts a Live Activity.
- [request(attributes:content:pushType:style:alertConfiguration:start:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_start_).md>) — Requests and schedules a Live Activity for a specific date.
- [request(attributes:content:pushType:style:alertConfiguration:startDate:)](<activity/request(attributes_content_pushtype_style_alertconfiguration_startdate_).md>) _(deprecated)_
- [attributes](activity/attributes.md) — A set of attributes that describe a Live Activity and its content.
- [ActivityStyle](activitystyle.md)
- [content](activity/content.md) — The dynamic content of a Live Activity.
- [ActivityContent](activitycontent.md) — A structure that describes the state and configuration of a Live Activity.
- [ContentState](activity/contentstate-swift.typealias.md) — The type alias for the structure that describes the dynamic content of a Live Activity.
- [PushType](pushtype.md) — The structure that offers constants you use to configure a Live Activity to receive updates through ActivityKit push notifications.
- [ActivityAuthorizationError](activityauthorizationerror.md) — An error that indicates why the request to start a Live Activity failed.
