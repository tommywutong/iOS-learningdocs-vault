---
title: current
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/current
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/current'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/current.json'
content_hash: 'sha256:268895a05069db85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# current

<sub>Type Property</sub>

The trait collection for the current execution context.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var current: UITraitCollection { get set }
```

## Discussion

This property provides a way to get a trait collection from the currently updating trait environment when your code doesn’t have direct access to the trait environment. UIKit updates the value of this property before calling the following methods of [UIView](../uiview.md), [UIViewController](../uiviewcontroller.md), and [UIPresentationController](../uipresentationcontroller.md). Inside these methods, the trait collection contains the traits describing the currently updating view or controller.

The following table lists the supported methods where UIKit sets the [currentTraitCollection](current.md) value:

| [UIView](../uiview.md) | [UIViewController](../uiviewcontroller.md) | [UIPresentationController](../uipresentationcontroller.md) |
|---|---|---|
| [- drawRect:](<../uiview/draw(__).md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [- layoutSubviews](<../uiview/layoutsubviews().md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [- tintColorDidChange](<../uiview/tintcolordidchange().md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `action` method of [registerForTraitChanges(_:target:action:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__target_action_).md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `handler` closure of [registerForTraitChanges(_:handler:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__handler_).md>)  ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [- traitCollectionDidChange:](<../uitraitenvironment/traitcollectiondidchange(__).md>) | [- viewWillLayoutSubviews](<../uiviewcontroller/viewwilllayoutsubviews().md>)  ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [- viewDidLayoutSubviews](<../uiviewcontroller/viewdidlayoutsubviews().md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `action` method of [registerForTraitChanges(_:target:action:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__target_action_).md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `handler` closure of [registerForTraitChanges(_:handler:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__handler_).md>)  ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [- traitCollectionDidChange:](<../uitraitenvironment/traitcollectiondidchange(__).md>) | [- containerViewWillLayoutSubviews](<../uipresentationcontroller/containerviewwilllayoutsubviews().md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [- containerViewDidLayoutSubviews](<../uipresentationcontroller/containerviewdidlayoutsubviews().md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `action` method of [registerForTraitChanges(_:target:action:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__target_action_).md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `handler` closure of [registerForTraitChanges(_:handler:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__handler_).md>) ![](../../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [- traitCollectionDidChange:](<../uitraitenvironment/traitcollectiondidchange(__).md>) |

Outside these methods, you’re responsible for ensuring the [currentTraitCollection](current.md) property has a valid trait collection. Otherwise, the contents of the collection are undefined. To ensure that [currentTraitCollection](current.md) contains a valid trait collection, use one of these techniques:

- Use [- performAsCurrentTraitCollection:](<performascurrent(__).md>) to execute your code inside a context with a valid [currentTraitCollection](current.md) property. This is the preferred way to set [currentTraitCollection](current.md).
- Set [currentTraitCollection](current.md) to a known good trait collection. If you set [currentTraitCollection](current.md), you need to save and restore the trait environment, as the code example below shows.

[UIColor](../uicolor.md) implicitly uses the [currentTraitCollection](current.md) trait collection when it resolves a dynamic color to a static color value, such as a [CGColor](../../coregraphics/cgcolor.md) or an RGB value. To resolve a dynamic color, make sure that [currentTraitCollection](current.md) contains a valid collection. Alternatively, the method [- resolvedColorWithTraitCollection:](<../uicolor/resolvedcolor(with_).md>) resolves a color from a given trait collection and doesn’t rely on [currentTraitCollection](current.md).

UIKit stores the value of the [currentTraitCollection](current.md) property as a thread-local variable, so access is lightweight and free of side effects. Changing the traits on a nonmain thread doesn’t affect the current traits on your app’s main thread.

Whenever possible, use [- performAsCurrentTraitCollection:](<performascurrent(__).md>) rather than manually setting [currentTraitCollection](current.md). If you need to set [currentTraitCollection](current.md), keep the following in mind:

- Before modifying [currentTraitCollection](current.md), save the value, and restore it after you’re done.
- Always start with a trait collection from a concrete instance of [UITraitEnvironment](../uitraitenvironment.md) rather than creating a new [UITraitCollection](../uitraitcollection.md) instance.

The [- performAsCurrentTraitCollection:](<performascurrent(__).md>) method handles these tasks for you.

The example below sets the [currentTraitCollection](current.md) property to resolve a dynamic color into a [CGColor](../../coregraphics/cgcolor.md):

```swift
func updateBorderColor(layer: CALayer) {
    let savedTraitCollection = UITraitCollection.current
    // Set the property with a trait collection from a view.
    UITraitCollection.current = view.traitCollection
    // Methods and properties relying on current are safe to use here.
    layer.borderColor = UIColor.label.cgColor
    // Restore the saved collection.
    UITraitCollection.current = savedTraitCollection
}
```
