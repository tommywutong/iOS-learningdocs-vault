---
title: 'nw_parameters_set_privacy_context(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_set_privacy_context(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_set_privacy_context(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_set_privacy_context%28_%3A_%3A%29.json'
content_hash: 'sha256:67ee0739721d3ebe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_set_privacy_context(_:_:)

<sub>Function</sub>

Associates a privacy context with any connections or listeners that use the parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_set_privacy_context(_ parameters: nw_parameters_t, _ privacy_context: nw_privacy_context_t)
```

## See Also

### Configuring Privacy Settings

- [nw_privacy_context_t](nw_privacy_context_t.md) — An object that defines the privacy requirements for a set of connections.
