---
title: wifiAware
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwerror/wifiaware
source_url: 'https://developer.apple.com/documentation/network/nwerror/wifiaware'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwerror/wifiaware.json'
content_hash: 'sha256:a66c726f8ab60d25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWError](../nwerror.md)

# wifiAware

<sub>Instance Property</sub>

The underlying error that occurred, if applicable.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var wifiAware: WAError? { get }
```

## Discussion

If the underlying connection is over Wi-Fi Aware and an error occurred, provide details on the specific error. Otherwise `nil`.
