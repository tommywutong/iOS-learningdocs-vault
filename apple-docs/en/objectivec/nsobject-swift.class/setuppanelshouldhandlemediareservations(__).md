---
title: 'setupPanelShouldHandleMediaReservations(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/setuppanelshouldhandlemediareservations(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setuppanelshouldhandlemediareservations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/setuppanelshouldhandlemediareservations%28_%3A%29.json'
content_hash: 'sha256:1ff2c3950d35f9a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# setupPanelShouldHandleMediaReservations(_:)

<sub>Instance Method</sub>

This delegate method allows the delegate to control how media reservations are handled.

<sub>macOS</sub>

```swift
func setupPanelShouldHandleMediaReservations(_ aPanel: DRSetupPanel!) -> Bool
```

## Parameters

- `aPanel` — The setup panel sending the message.

## Return Value

## Discussion

Return `NO` to indicate the delegate will handle media reservations. Return `YES` to indicate the setupPanel should handle media reservations itself.
