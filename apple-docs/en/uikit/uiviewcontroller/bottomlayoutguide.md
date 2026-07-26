---
title: bottomLayoutGuide
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（11.0 起废弃）, iPadOS 7.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontroller/bottomlayoutguide
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/bottomlayoutguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/bottomlayoutguide.json'
content_hash: 'sha256:9113ed6a31d74c91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# bottomLayoutGuide

<sub>Instance Property</sub>

Indicates the lowest vertical extent for your onscreen content, for use with Auto Layout constraints.

> [!warning] Deprecated
> Use the [safeAreaLayoutGuide](../uiview/safearealayoutguide.md) property of [UIView](../uiview.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var bottomLayoutGuide: any UILayoutSupport { get }
```

## Discussion

The [bottomLayoutGuide](bottomlayoutguide.md) property comes into play when a view controller is frontmost onscreen. It indicates the lowest vertical extent for content that you don’t want to appear behind a translucent or transparent UIKit bar (such as a tab bar or toolbar). This property implements the [UILayoutSupport](../uilayoutsupport.md) protocol and you can employ it as a constraint item when using the [NSLayoutConstraint](../nslayoutconstraint.md) class.

The value of this property is, specifically, the value of the [length](../uilayoutsupport/length.md) property of the object returned when you query this property. This value is constrained by either the view controller or by its enclosing container view controller (such as a navigation or tab bar controller), as follows:

- A view controller **not within** a container view controller constrains this property to indicate the top of the tab bar or toolbar, if one of these is visible, or else to indicate the bottom edge of the view controller’s view.
- A view controller **within** a container view controller does not set this property’s value. Instead, the container view controller constrains the value to indicate the top of the tab bar or toolbar, if one of these is visible, or else to indicate the bottom edge of the view controller’s view.

If a container view controller’s toolbar or tab bar is visible and opaque, the container lays out the frontmost view controller’s view so its bottom edge abuts the top of the bar. In this case, the value of this property is 0.

Query this property within your implementation of the [- viewDidLayoutSubviews](<viewdidlayoutsubviews().md>) method.

When laying out a storyboard scene, the Bottom Layout Guide object is available in the Interface Builder outline view as a child of the View Controller object. Adding a bottom layout guide using Interface Builder provides backward layout compatibility to iOS 6.

As an example of how to programmatically use this property with Auto Layout, say you want to position a control such that its bottom edge is 20 points above the bottom layout guide. This scenario applies to any of the scenarios listed above. Use code similar to the following:

```objc
[button setTranslatesAutoresizingMaskIntoConstraints: NO];
id bottomGuide = myViewController.bottomLayoutGuide;
NSDictionary *viewsDictionary = NSDictionaryOfVariableBindings (button, bottomGuide);
[myViewController.view addConstraints:
    [NSLayoutConstraint constraintsWithVisualFormat: @"V: [button]-20-[bottomGuide]"
                                                 options: 0
                                                 metrics: nil
                                                   views: viewsDictionary]];
[self.view layoutSubviews]; // You must call this method here or the system raises an exception
```

> [!important] Important
> If you define Auto Layout constraints in a storyboard file as well as programmatically, it is your responsibility to ensure the constraints do not conflict. If they do conflict, the system may throw a runtime exception.

To use a bottom layout guide without using constraints, obtain the guide’s position relative to the bottom bound of the containing view. In the case of using a view controller subclass, obtain the numbers you need as follows:

```objc
- (void) viewDidLayoutSubviews {
    CGRect viewBounds = self.view.bounds;
    CGFloat bottomBarOffset = self.bottomLayoutGuide.length;
}
```

In the case of using a view subclass, obtain the numbers you need as follows:

```objc
- (void) layoutSubviews {
    [super layoutSubviews]; // You must call super here or the system raises an exception
    CGRect bounds = self.bounds;
    CGFloat bottomBarOffset = myVCReference.bottomLayoutGuide.length;
}
```

## See Also

### Deprecated properties

- [shouldAutorotate](shouldautorotate.md) — A Boolean value that indicates whether the view controller’s contents should autorotate. _(deprecated)_
- [previewActionItems](previewactionitems.md) — The quick actions displayed when a user swipes upward on a 3D Touch preview. _(deprecated)_
- [automaticallyAdjustsScrollViewInsets](automaticallyadjustsscrollviewinsets.md) — A Boolean value that indicates whether the view controller should automatically adjust its scroll view insets. _(deprecated)_
- [interfaceOrientation](interfaceorientation.md) — Convenience property that provides the current orientation of the interface, meaningful only if the view controller is taking up the full screen. _(deprecated)_
- [modalInPopover](ismodalinpopover.md) — A Boolean value indicating whether the view controller should be presented modally by a popover. _(deprecated)_
- [searchDisplayController](searchdisplaycontroller.md) — The search display controller associated with the view controller. _(deprecated)_
- [topLayoutGuide](toplayoutguide.md) — Indicates the highest vertical extent for your onscreen content, for use with Auto Layout constraints. _(deprecated)_
