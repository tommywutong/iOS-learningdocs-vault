---
title: com.apple.security.network.server
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/entitlements/com.apple.security.network.server
source_url: 'https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.network.server'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/entitlements/com.apple.security.network.server.json'
content_hash: 'sha256:5687f9bd8cd72407'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Entitlements](../entitlements.md)

# com.apple.security.network.server

<sub>Property List Key</sub>

A Boolean value indicating whether your app may listen for incoming network connections.

## Discussion

Use this key to allow other computers to initiate network connections to your sandboxed app.

> [!note] Note
> For TCP sockets, the `com.apple.security.network.server` and [com.apple.security.network.client](com.apple.security.network.client.md) entitlements restrict only the initiation of a network connection, not the flow of data. Outgoing and incoming connections can both send and receive data.
>
> For UDP sockets, the network entitlements restrict both initiation and data flow. For example, an app with only the server entitlement enabled can receive, but not send, data. Apps using UDP usually require both entitlements.

To add this entitlement to your app, enable the App Sandbox capability in Xcode, and under Network, select Incoming Connections (Server).

## See Also

### Networking

- [com.apple.security.network.client](com.apple.security.network.client.md) — A Boolean value indicating whether your app may open outgoing network connections.
- [App Attest Environment](com.apple.developer.devicecheck.appattest-environment.md) — The environment for an app that uses the App Attest service to validate itself.
