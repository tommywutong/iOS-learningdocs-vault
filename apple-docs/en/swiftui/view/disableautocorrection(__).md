---
title: 'disableAutocorrection(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 8.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/disableautocorrection(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/disableautocorrection(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/disableautocorrection%28_%3A%29.json'
content_hash: 'sha256:078d058847d18914'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# disableAutocorrection(_:)

<sub>Instance Method</sub>

Sets whether to disable autocorrection for this view.

> [!warning] Deprecated
> Use [autocorrectionDisabled(_:)](<autocorrectiondisabled(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func disableAutocorrection(_ disable: Bool?) -> some View

```

## Parameters

- `disable` — A Boolean value that indicates whether autocorrection is disabled for this view.

## Discussion

Use this method when the effect of autocorrection would make it more difficult for the user to input information. The entry of proper names and street addresses are examples where autocorrection can negatively affect the user’s ability complete a data entry task.

In the example below configures a [TextField](../textfield.md) with the default keyboard. Disabling autocorrection allows the user to enter arbitrary text without the autocorrection system offering suggestions or attempting to override their input.

```swift
TextField("1234 Main St.", text: $address)
    .keyboardType(.default)
    .disableAutocorrection(true)
```

## See Also

### Text modifiers

- [autocapitalization(_:)](<autocapitalization(__).md>) — Sets whether to apply auto-capitalization to this view. _(deprecated)_
