---
title: 'fastOpenAllowed(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/fastopenallowed(_:)-29iom'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/fastopenallowed(_:)-29iom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/fastopenallowed%28_%3A%29-29iom.json'
content_hash: 'sha256:72b7553dd321aab1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# fastOpenAllowed(_:)

<sub>Instance Method</sub>

Allow fast open to be used on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fastOpenAllowed(_ allowed: Bool) -> Self
```

## Parameters

- `allowed` — True if fast open should be used, false otherwise.

## Discussion

Use fast open for an outbound connection, which may be done at any protocol level. Use of fast open requires that the caller send idempotent data on the connection before the connection may move into the ready state.

> [!warning] Warning
> This may have security implications for application data. In particular, TLS early data is replayable by a network attacker. You must account for this when sending data before the handshake is confirmed. See RFC 8446 for more information. You MUST NOT enable fast open without a specific application profile that defines its use.

As a side effect, this may implicitly enable fast open or early data for protocols in the stack, even if they did not have fast open explicitly enabled on them (such as the option to enable TCP Fast Open).
