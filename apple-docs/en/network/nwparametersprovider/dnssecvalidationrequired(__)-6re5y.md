---
title: 'dnssecValidationRequired(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwparametersprovider/dnssecvalidationrequired(_:)-6re5y'
source_url: 'https://developer.apple.com/documentation/network/nwparametersprovider/dnssecvalidationrequired(_:)-6re5y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwparametersprovider/dnssecvalidationrequired%28_%3A%29-6re5y.json'
content_hash: 'sha256:4430e7d2573dd53e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWParametersProvider](../nwparametersprovider.md)

# dnssecValidationRequired(_:)

<sub>Instance Method</sub>

Require DNSSEC validation when resolving an endpoint before making a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dnssecValidationRequired(_ required: Bool) -> Self
```

## Parameters

- `required` — True if DNSSEC validation is required, false otherwise.

## Discussion

DNSSEC validation only takes effect if making a connection to an endpoint that requires domain name resolution, such as a host or URL endpoint.

- If this is not set or is set to `false`, DNSSEC validation will not be required.
- If this is set to `true` and no additional DNSSEC configuration is set, the default behavior will be followed: Only DNSSEC secure and DNSSEC insecure resolved results will be used to establish a connection.
- If this is set to `true` and additional DNSSEC configuration is set on the parameters, the behavior specified by that configuration will be used.
