---
title: 'SimpleTunnel: Customized Networking Using the NetworkExtension Framework'
apple_id: TP40016140
resource_type: Sample Code
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleTunnel/Listings/SimpleTunnel_ClientTunnelConnection_swift.html
archived_at: '2026-07-18T03:24:23.861546Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleTunnel: Customized Networking Using the NetworkExtension Framework](SimpleTunnel-%20Customized%20Networking%20Using%20the%20NetworkExtension%20Framework.md)


[Next](SimpleTunnel-ProxySettingsController.swift.md)[Previous](SimpleTunnel-TextFieldCell.swift.md)

# SimpleTunnel/ClientTunnelConnection.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file contains the ClientTunnelConnection class. The ClientTunnelConnection class handles the encapsulation and decapsulation of IP packets in the client side of the SimpleTunnel tunneling protocol.
*/

import Foundation
import SimpleTunnelServices
import NetworkExtension

// MARK: Protocols

/// The delegate protocol for ClientTunnelConnection.
protocol ClientTunnelConnectionDelegate {
    /// Handle the connection being opened.
    func tunnelConnectionDidOpen(_ connection: ClientTunnelConnection, configuration: [NSObject: AnyObject])
    /// Handle the connection being closed.
    func tunnelConnectionDidClose(_ connection: ClientTunnelConnection, error: NSError?)
}

/// An object used to tunnel IP packets using the SimpleTunnel protocol.
class ClientTunnelConnection: Connection {

    // MARK: Properties

    /// The connection delegate.
    let delegate: ClientTunnelConnectionDelegate

    /// The flow of IP packets.
    let packetFlow: NEPacketTunnelFlow

    // MARK: Initializers

    init(tunnel: ClientTunnel, clientPacketFlow: NEPacketTunnelFlow, connectionDelegate: ClientTunnelConnectionDelegate) {
        delegate = connectionDelegate
        packetFlow = clientPacketFlow
        let newConnectionIdentifier = arc4random()
        super.init(connectionIdentifier: Int(newConnectionIdentifier), parentTunnel: tunnel)
    }

    // MARK: Interface

    /// Open the connection by sending a "connection open" message to the tunnel server.
    func open() {
        guard let clientTunnel = tunnel as? ClientTunnel else { return }

        let properties = createMessagePropertiesForConnection(identifier, commandType: .open, extraProperties:[
                TunnelMessageKey.TunnelType.rawValue: TunnelLayer.ip.rawValue as AnyObject
            ])

        clientTunnel.sendMessage(properties) { error in
            if let error = error {
                self.delegate.tunnelConnectionDidClose(self, error: error)
            }
        }
    }

    /// Handle packets coming from the packet flow.
    func handlePackets(_ packets: [Data], protocols: [NSNumber]) {
        guard let clientTunnel = tunnel as? ClientTunnel else { return }

        let properties = createMessagePropertiesForConnection(identifier, commandType: .packets, extraProperties:[
                TunnelMessageKey.Packets.rawValue: packets as AnyObject,
                TunnelMessageKey.Protocols.rawValue: protocols as AnyObject
            ])

        clientTunnel.sendMessage(properties) { error in
            if let sendError = error {
                self.delegate.tunnelConnectionDidClose(self, error: sendError)
                return
            }

            // Read more packets.
            self.packetFlow.readPackets { inPackets, inProtocols in
                self.handlePackets(inPackets, protocols: inProtocols)
            }
        }
    }

    /// Make the initial readPacketsWithCompletionHandler call.
    func startHandlingPackets() {
        packetFlow.readPackets { inPackets, inProtocols in
            self.handlePackets(inPackets, protocols: inProtocols)
        }
    }

    // MARK: Connection

    /// Handle the event of the connection being established.
    override func handleOpenCompleted(_ resultCode: TunnelConnectionOpenResult, properties: [NSObject: AnyObject]) {
        guard resultCode == .success else {
            delegate.tunnelConnectionDidClose(self, error: SimpleTunnelError.badConnection as NSError)
            return
        }

        // Pass the tunnel network settings to the delegate.
        if let configuration = properties[TunnelMessageKey.Configuration.rawValue as NSString] as? [NSObject: AnyObject] {
            delegate.tunnelConnectionDidOpen(self, configuration: configuration)
        }
        else {
            delegate.tunnelConnectionDidOpen(self, configuration: [:])
        }
    }

    /// Send packets to the virtual interface to be injected into the IP stack.
    override func sendPackets(_ packets: [Data], protocols: [NSNumber]) {
        packetFlow.writePackets(packets, withProtocols: protocols)
    }
}
```

[Next](SimpleTunnel-ProxySettingsController.swift.md)[Previous](SimpleTunnel-TextFieldCell.swift.md)

