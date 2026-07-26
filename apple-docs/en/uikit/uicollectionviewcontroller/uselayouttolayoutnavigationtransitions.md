---
title: useLayoutToLayoutNavigationTransitions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcontroller/uselayouttolayoutnavigationtransitions
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/uselayouttolayoutnavigationtransitions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller/uselayouttolayoutnavigationtransitions.json'
content_hash: 'sha256:23a02a47cd7c0d5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewController](../uicollectionviewcontroller.md)

# useLayoutToLayoutNavigationTransitions

<sub>Instance Property</sub>

A Boolean that indicates whether the collection view controller coordinates with a navigation controller for transitions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var useLayoutToLayoutNavigationTransitions: Bool { get set }
```

## Discussion

This property helps facilitate transitions between two or more collection view controllers using a navigation controller. When configuring your navigation controller, install a collection view controller as the root object on the navigation stack and set its value for this property to [false](../../swift/false.md). When the user selects an item that would require pushing a new collection view controller on the stack, set the value of this property for the new view controller to [true](../../swift/true.md). When you do that, the navigation controller performs an animated layout change between the contents of the two collection view controllers instead of the traditional push animation. Similarly, popping the topmost collection view controller off the stack animates back to the previous layout. The navigation controller drives the transition between the view controllers, including the ability to drive the transition interactively.

You must set the value of this property before pushing the collection view controller onto a navigation stack. Do not change the value of this property after the view controller is already on the navigation stack.
