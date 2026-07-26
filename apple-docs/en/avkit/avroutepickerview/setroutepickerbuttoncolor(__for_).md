---
title: 'setRoutePickerButtonColor(_:for:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avroutepickerview/setroutepickerbuttoncolor(_:for:)'
source_url: 'https://developer.apple.com/documentation/avkit/avroutepickerview/setroutepickerbuttoncolor(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avroutepickerview/setroutepickerbuttoncolor%28_%3Afor%3A%29.json'
content_hash: 'sha256:9c8efb5fa42191b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVRoutePickerView](../avroutepickerview.md)

# setRoutePickerButtonColor(_:for:)

<sub>Instance Method</sub>

Sets the route picker button color for the specified state.

<sub>macOS</sub>

```swift
func setRoutePickerButtonColor(_ color: NSColor?, for state: AVRoutePickerView.ButtonState)
```

## Parameters

- `color` — The route picker button color to set.

- `state` — The button state.

## See Also

### Configuring the route picker view

- [activeTintColor](activetintcolor.md) — The view’s tint color when AirPlay is active.
- [routePickerButtonBordered](isroutepickerbuttonbordered.md) — A Boolean value that indicates whether the route picker button has a border.
- [prioritizesVideoDevices](prioritizesvideodevices.md) — A Boolean value that indicates whether the route picker sorts video output devices to the top of the list.
- [routePickerButtonStyle](routepickerbuttonstyle.md) — The button style for the route picker.
- [AVRoutePickerViewButtonStyle](../avroutepickerviewbuttonstyle.md) — Constants that define the button styles a route picker view supports.
- [- routePickerButtonColorForState:](<routepickerbuttoncolor(for_).md>) — Returns the color of the picker button for the specified state.
- [ButtonState](buttonstate.md) — Constants that describe the available button states.
