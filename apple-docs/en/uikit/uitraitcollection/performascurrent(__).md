---
title: 'performAsCurrent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/performascurrent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/performascurrent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/performascurrent%28_%3A%29.json'
content_hash: 'sha256:ff4c3ac9b028176c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# performAsCurrent(_:)

<sub>Instance Method</sub>

Executes custom code using the traits of the receiving trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performAsCurrent(_ actions: () -> Void)
```

## Parameters

- `actions` — A closure containing the code you want to execute. This closure has no return value and takes no parameters.

## Discussion

The [currentTraitCollection](current.md) property is undefined outside the documented methods where UIKit sets it. Use this method when you want to execute code that relies on the [currentTraitCollection](current.md) property from outside these methods. You can also use this method if you want to execute some code using the traits of a different trait environment. Prefer this method over manually setting the [currentTraitCollection](current.md) property yourself.

This method temporarily replaces the traits of the current environment with the ones in the targeted [UITraitCollection](../uitraitcollection.md). After the `actions` block finishes, the method restores the original traits to the environment. You can call this method from any thread of your app.

The example below shows how you can safely resolve dynamic [UIColor](../uicolor.md) that relies on [currentTraitCollection](current.md):

```swift
func updateBorderColor(layer: CALayer) {
    
    // Read the trait collection from the view.
    let traitCollection = view.traitCollection
    traitCollection.performAsCurrent {
        // Inside the closure, the current property is set to traitCollection,
        // which UIColor uses to resolve the dynamic color borderColor.
        layer.borderColor = UIColor.label.cgColor
    }
}
```
