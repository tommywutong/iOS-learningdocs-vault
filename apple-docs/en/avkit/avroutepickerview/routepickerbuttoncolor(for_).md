---
title: 'routePickerButtonColor(for:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avroutepickerview/routepickerbuttoncolor(for:)'
source_url: 'https://developer.apple.com/documentation/avkit/avroutepickerview/routepickerbuttoncolor(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avroutepickerview/routepickerbuttoncolor%28for%3A%29.json'
content_hash: 'sha256:f9d19e661cca037d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVRoutePickerView](../avroutepickerview.md)

# routePickerButtonColor(for:)

<sub>Instance Method</sub>

Returns the color of the picker button for the specified state.

<sub>macOS</sub>

```swift
func routePickerButtonColor(for state: AVRoutePickerView.ButtonState) -> NSColor
```

## Parameters

- `state` — The button state.

## Return Value

A color value for the specified state.

## See Also

### Configuring the route picker view

- [activeTintColor](activetintcolor.md) — The view’s tint color when AirPlay is active.
- [routePickerButtonBordered](isroutepickerbuttonbordered.md) — A Boolean value that indicates whether the route picker button has a border.
- [prioritizesVideoDevices](prioritizesvideodevices.md) — A Boolean value that indicates whether the route picker sorts video output devices to the top of the list.
- [routePickerButtonStyle](routepickerbuttonstyle.md) — The button style for the route picker.
- [AVRoutePickerViewButtonStyle](../avroutepickerviewbuttonstyle.md) — Constants that define the button styles a route picker view supports.
- [- setRoutePickerButtonColor:forState:](<setroutepickerbuttoncolor(__for_).md>) — Sets the route picker button color for the specified state.
- [ButtonState](buttonstate.md) — Constants that describe the available button states.
