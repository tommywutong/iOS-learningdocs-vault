---
title: AVRoutePickerView.ButtonState
framework: AVKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avroutepickerview/buttonstate
source_url: 'https://developer.apple.com/documentation/avkit/avroutepickerview/buttonstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avroutepickerview/buttonstate.json'
content_hash: 'sha256:6e506ac66035b227'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVRoutePickerView](../avroutepickerview.md)

# AVRoutePickerView.ButtonState

<sub>Enumeration</sub>

Constants that describe the available button states.

<sub>macOS</sub>

```swift
enum ButtonState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a button state

- [init(rawValue:)](<buttonstate/init(rawvalue_).md>)

### Button States

- [AVRoutePickerViewButtonStateNormal](buttonstate/normal.md) — The normal, or default, button state.
- [AVRoutePickerViewButtonStateNormalHighlighted](buttonstate/normalhighlighted.md) — The highlighted button state when a mouse-down event occurs inside the button.
- [AVRoutePickerViewButtonStateActive](buttonstate/active.md) — The button state when AirPlay is active.
- [AVRoutePickerViewButtonStateActiveHighlighted](buttonstate/activehighlighted.md) — The highlighted button state when AirPlay is active.

## See Also

### Configuring the route picker view

- [activeTintColor](activetintcolor.md) — The view’s tint color when AirPlay is active.
- [routePickerButtonBordered](isroutepickerbuttonbordered.md) — A Boolean value that indicates whether the route picker button has a border.
- [prioritizesVideoDevices](prioritizesvideodevices.md) — A Boolean value that indicates whether the route picker sorts video output devices to the top of the list.
- [routePickerButtonStyle](routepickerbuttonstyle.md) — The button style for the route picker.
- [AVRoutePickerViewButtonStyle](../avroutepickerviewbuttonstyle.md) — Constants that define the button styles a route picker view supports.
- [- routePickerButtonColorForState:](<routepickerbuttoncolor(for_).md>) — Returns the color of the picker button for the specified state.
- [- setRoutePickerButtonColor:forState:](<setroutepickerbuttoncolor(__for_).md>) — Sets the route picker button color for the specified state.
