---
title: isSelected
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/isselected
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/isselected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/isselected.json'
content_hash: 'sha256:b5c5acf902058d38'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SubscriptionStoreControlStyleConfiguration](../../subscriptionstorecontrolstyleconfiguration.md) · [PickerOption](../pickeroption.md)

# isSelected

<sub>Instance Property</sub>

A Boolean value that indicates whether the picker option is in a selected state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let isSelected: Bool
```

## Discussion

Use the [isSelected](isselected.md) property to display a selection indicator, such as a checkmark, in its correct state. The following code example shows a checkmark when [isSelected](isselected.md) is true:

```swift
SubscriptionPickerOption(option) { pickerOption in 
HStack {
    Text(pickerOption.displayName)
    Spacer()
    Image(systemName: "checkmark")
        .opacity(pickerOption.isSelected ? 1 : 0)
    }
}
```

The [SubscriptionStorePicker](../../subscriptionstorepicker.md) automatically updates the picker’s selection state as customers interact with your picker. However, the [SubscriptionStorePicker](../../subscriptionstorepicker.md) doesn’t display selection indicators. Your app needs to display selection indicators in the picker option label.

Use the [PickerOption](../pickeroption.md) value, which represents the properties of a subscription picker option’s label, to display the selection indicator.

## See Also

### Getting properties of the subscription picker option

- [subscription](subscription.md) — The auto-renewable subscription that the picker option represents.
- [activeOffer](activeoffer.md)
- [icon](icon.md) — The subscription option’s icon.
- [id](id.md)
