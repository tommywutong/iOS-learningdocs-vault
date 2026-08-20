---
title: 'TCPTransports: Using Various Apple APIs to Run a TCP Connection'
apple_id: TP40017680
resource_type: Sample Code
platform: iOS
topic: null
technology: NetworkExtension
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/samplecode/TCPTransports/Listings/Model_ConversationTransport_swift.html
archived_at: '2026-07-18T03:26:00.058907Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TCPTransports: Using Various Apple APIs to Run a TCP Connection](TCPTransports-%20Using%20Various%20Apple%20APIs%20to%20Run%20a%20TCP%20Connection.md)


[Next](Model-Endpoint.swift.md)[Previous](LICENSE.txt.md)

# Model/ConversationTransport.swift

```swift
/*
    Copyright (C) 2018 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Represents a conversation backed by a TCPTransport.
 */

import Foundation

/// This class represents a conversation that is backed by a TCPTransport, which
/// updates the conversation as events happen on the network.

class ConversationTransport : TCPTransportDelegate {

    /// Create an object, starting with a fresh conversation that’s then updated
    /// by the transport.
    ///
    /// - Parameters:
    ///   - localizedName: The name of the new conversation.
    ///   - transport: The transport that updates it.  At this point this object
    ///     effectively owns the transport, becoming its delegate.

    required init(localizedName: String, transport: TCPTransport) {
        self.transport = transport
        self.conversation = Conversation(
            localizedName: localizedName,
            messages: [],
            state: .offline(localizedStatus: transport.localizedTransportState)
        )
        self.transport.delegate = self
    }

    /// The value passed to the initialiser.

    let transport: TCPTransport

    /// The current state of the conversation; the object posts the
    /// `conversationDidChange` notification after updating this.

    private(set) var conversation: Conversation {
        didSet {
            NotificationCenter.default.post(name: ConversationTransport.conversationDidChange, object: self, userInfo: nil)
        }
    }

    /// Starts the transport.

    func start() {
        self.transport.start()
    }

    /// Stops the transport.

    func stop() {
        self.transport.stop()
    }

    /// Sends a message over the transport.  It's only safe to call this when
    /// the conversation in online.
    ///
    /// - Parameter message: The message to send; this shouldn’t contain any
    ///   line breaks but the presence of line breaks won’t cause a failure.

    func send(message: String) {
        guard case .started = self.transport.transportState else { fatalError() }
        self.add(message:
            Message(text: message, date: Date(), direction: .outgoing)
        )
        self.transport.send(message: message)
    }

    /// Adds a message, either incoming or outgoing, to the conversation.

    private func add(message: Message) {
        self.conversation.messages.append(message)
    }

    func didStart(transport: TCPTransport) {
        self.conversation.state = .online
    }

    func didReceive(message: String, transport: TCPTransport) {
        self.add(message:
            Message(text: message, date: Date(), direction: .incoming)
        )
    }

    func didStop(transport: TCPTransport) {
        self.conversation.state = .offline(localizedStatus: self.transport.localizedTransportState)
    }

    /// Posted after the `conversation` property has been changed, including
    /// online/offline state changes and the addition of both incoming and
    /// outgoing messages.

    static let conversationDidChange = Notification.Name("ConversationTransport.conversationDidChange")
}

private extension TCPTransport {

    /// Returns a localised interpretation of the transport’s state.

    var localizedTransportState: String {
        switch self.transportState {
        case .initialised:  return NSLocalizedString("_not_started_", comment: "Connection status associated with the conversation.")
        case .starting:     return NSLocalizedString("_connecting_", comment: "Connection status associated with the conversation.")
        case .started:      return NSLocalizedString("_connected_", comment: "Connection status associated with the conversation.")
        case .stopped(nil): return NSLocalizedString("_stopped_", comment: "Connection status associated with the conversation.")
        case .stopped(_):   return NSLocalizedString("_failed_", comment: "Connection status associated with the conversation.")
        }
    }
}
```

[Next](Model-Endpoint.swift.md)[Previous](LICENSE.txt.md)

