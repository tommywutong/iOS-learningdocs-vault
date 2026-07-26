---
title: 'init(host:port:protocol:realm:authenticationMethod:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlprotectionspace/init(host:port:protocol:realm:authenticationmethod:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlprotectionspace/init(host:port:protocol:realm:authenticationmethod:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlprotectionspace/init%28host%3Aport%3Aprotocol%3Arealm%3Aauthenticationmethod%3A%29.json'
content_hash: 'sha256:ca51d6b62425faca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLProtectionSpace](../urlprotectionspace.md)

# init(host:port:protocol:realm:authenticationMethod:)

<sub>Initializer</sub>

Creates a protection space object from the given host, port, protocol, realm, and authentication method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(host: String, port: Int, protocol: String?, realm: String?, authenticationMethod: String?)
```

## Parameters

- `host` — The host name for the [URLProtectionSpace](../urlprotectionspace.md) object.

- `port` — The port for the protection space object. If `port` is 0, the default port for the specified protocol is used, for example, port 80 for HTTP. Note that servers can, and do, treat these values differently.

- `protocol` — The protocol for the protection space object. The value of `protocol` is equivalent to the scheme for a URL in the protection space, for example, “http”, “https”,  “ftp”, etc.

- `realm` — A string indicating a protocol-specific subdivision of the host. `realm` may be `nil` if there is no specified realm or if the protocol doesn’t support realms.

- `authenticationMethod` — The type of authentication to use. `authenticationMethod` should be set to one of the values in [NSURLProtectionSpace authentication method constants](../nsurlprotectionspace-authentication-method-constants.md) or `nil` to use the default, [NSURLAuthenticationMethodDefault](../nsurlauthenticationmethoddefault.md).

## Return Value

A new protection space object, initialized with the given host, port, protocol, realm, and authentication method.

## See Also

### Creating a protection space

- [- initWithProxyHost:port:type:realm:authenticationMethod:](<init(proxyhost_port_type_realm_authenticationmethod_).md>) — Creates a protection space object representing a proxy server.
