---
title: 'traitCollectionDidChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（17.0 起废弃）, iPadOS 8.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitraitenvironment/traitcollectiondidchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitenvironment/traitcollectiondidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitenvironment/traitcollectiondidchange%28_%3A%29.json'
content_hash: 'sha256:fda53cd5aae66a95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitEnvironment](../uitraitenvironment.md)

# traitCollectionDidChange(_:)

<sub>Instance Method</sub>

Reports changes in the iOS interface environment.

> [!warning] Deprecated
> In Swift, use [registerForTraitChanges(_:handler:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__handler_).md>) or [registerForTraitChanges(_:target:action:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__target_action_).md>) instead. In Objective-C, use [registerForTraitChanges:withHandler:](../uitraitchangeobservable-7qoet/registerfortraitchanges_withhandler_.md) or [registerForTraitChanges:withTarget:action:](../uitraitchangeobservable-7qoet/registerfortraitchanges_withtarget_action_.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?)
```

## Parameters

- `previousTraitCollection` — The [UITraitCollection](../uitraitcollection.md) object before the interface environment changed.

## Discussion

The system calls this method when the iOS interface environment changes. Implement this method in view controllers and views, according to your app’s needs, to respond to such changes. For example, you might adjust the layout of the subviews of a view controller when someone rotates from portrait to landscape orientation. The default implementation of this method is empty.

At the beginning of your implementation, call `super` to ensure that interface elements higher in the view hierarchy have an opportunity to adjust their layout first. Use code similar to this:

```objc
- (void) traitCollectionDidChange: (UITraitCollection *) previousTraitCollection {
    [super traitCollectionDidChange: previousTraitCollection];
    if ((self.traitCollection.verticalSizeClass != previousTraitCollection.verticalSizeClass)
        || (self.traitCollection.horizontalSizeClass != previousTraitCollection.horizontalSizeClass)) {
        // Your custom implementation here.
    }
}
```
