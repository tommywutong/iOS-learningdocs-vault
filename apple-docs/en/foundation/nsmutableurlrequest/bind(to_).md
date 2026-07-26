---
title: 'bind(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableurlrequest/bind(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/bind(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/bind%28to%3A%29.json'
content_hash: 'sha256:ebc9437dcb9ab7c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# bind(to:)

<sub>Instance Method</sub>

Binds a URL request to the network interface associated with the hotspot helper command instance.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func bind(to command: NEHotspotHelperCommand)
```

## Parameters

- `command` — The hotspot helper command to bind the request to.

## Discussion

Apps that participate in joining Wi-Fi hotspot networks use the APIs in the [Network Extension](../../networkextension.md) framework to authenticate with hotspots. Ordinarily, [URLSession](../urlsession.md) will use the default interface, which may be WWAN. By binding to a hotspot helper command, you force a request to use Wi-Fi to communicate with the hotspot.

## See Also

### Related Documentation

- [Network Extension](../../networkextension.md) — Customize and extend core networking features.
