---
title: nw_browser_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_browser_t
source_url: 'https://developer.apple.com/documentation/network/nw_browser_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_browser_t.json'
content_hash: 'sha256:b1cd3dd0c875bc4d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_browser_t

<sub>Type Alias</sub>

An object you use to browse for available network services.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_browser_t = any OS_nw_browser
```

## Topics

### Essentials

- [NSBonjourServices](../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.

### Browsing for Services

- [nw_browser_create](<nw_browser_create(____).md>) — Initializes a browser with a type of service to discover.
- [nw_browse_descriptor_t](nw_browse_descriptor_t.md) — A service description used to discover Bonjour services.
- [nw_browser_set_queue](<nw_browser_set_queue(____).md>) — Sets the queue on which all browser events will be delivered.
- [nw_browser_start](<nw_browser_start(__).md>) — Starts browsing for services.
- [nw_browser_set_browse_results_changed_handler](<nw_browser_set_browse_results_changed_handler(____).md>) — Sets the handler to receive updates about discovered services.
- [nw_browser_browse_results_changed_handler_t](nw_browser_browse_results_changed_handler_t.md) — A handler that delivers updates about discovered services.
- [nw_browse_result_t](nw_browse_result_t.md) — A discovered service and metadata about the service.

### Managing Browsers

- [nw_browser_set_state_changed_handler](<nw_browser_set_state_changed_handler(____).md>) — Sets a handler to receive browser state updates.
- [nw_browser_state_changed_handler_t](nw_browser_state_changed_handler_t.md) — A handler that delivers browser state updates with associated errors.
- [nw_browser_state_t](nw_browser_state_t.md) — States indicating whether a browser is able to discover services.
- [nw_browser_cancel](<nw_browser_cancel(__).md>) — Stops browsing for services.

### Inspecting Browsers

- [nw_browser_copy_browse_descriptor](<nw_browser_copy_browse_descriptor(__).md>) — Accesses the service descriptor with which the browser was created.
- [nw_browser_copy_parameters](<nw_browser_copy_parameters(__).md>) — Accesses the parameters with which the browser was created.
