---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/Model_Conversation_swift.html
archived_at: '2026-07-18T03:26:00.111746Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](Model-Message.swift.md)[Previous](Model-Endpoint.swift.md)

# Model/Conversation.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A model object representing a conversation.
 */

import Foundation

/// A model object representing a conversation.

struct Conversation {

    /// The name for this conversation.  This is intended to be shown to the
    /// user, so technically it’s localised, but in reality we actually use the
    /// transport host name.

    var localizedName: String

    /// An array of messages, with the oldest first.

    var messages: [Message]

    /// Indicates whether the conversation is online or not.

    var state: State

    /// Dsecribes the state of the conversation.
    ///
    /// - online: The conversation is online.
    /// - offline: The conversation is offline for the reason described in the
    ///     associated value.

    enum State : Equatable {
        case online
        case offline(localizedStatus: String)

        static func ==(lhs: State, rhs: State) -> Bool {
            switch (lhs, rhs) {
            case (.online, .online): return true
            case (.offline(let l), .offline(let r)): return l == r
            default: return false
            }
        }
    }

    /// A reasonable ’nil’ value for situations where a default value is needed
    /// but `nil` is not allowed.  Note that this is not localised because the
    /// way our app is designed means that it should never be seen by the user.

    static var empty: Conversation = Conversation(localizedName: "_EMPTY_", messages: [], state: .offline(localizedStatus: "_EMPTY_"))
}
```

[Next](Model-Message.swift.md)[Previous](Model-Endpoint.swift.md)

