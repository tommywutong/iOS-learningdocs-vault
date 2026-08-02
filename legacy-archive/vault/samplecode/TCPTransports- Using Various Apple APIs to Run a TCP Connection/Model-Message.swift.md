---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/Model_Message_swift.html
archived_at: '2026-07-18T03:26:00.248772Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](Document%20Revision%20History.md)[Previous](Model-Conversation.swift.md)

# Model/Message.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A model object representing a message in a conversation.
 */

import Foundation

/// A model object representing a message in a conversation.

struct Message {

    /// The text of the message.

    var text: String

    /// The date that the message was sent or received.

    var date: Date

    /// The direction of the message, either incoming or outgoing.

    var direction: Direction

    /// Describes the direction of the message.
    ///
    /// - incoming: The message was received by this device.
    /// - outgoing: The message was sent by this device.

    enum Direction {
        case incoming
        case outgoing
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Model-Conversation.swift.md)

