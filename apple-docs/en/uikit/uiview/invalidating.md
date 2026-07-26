---
title: UIView.Invalidating
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/invalidating
source_url: 'https://developer.apple.com/documentation/uikit/uiview/invalidating'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/invalidating.json'
content_hash: 'sha256:4a126bc3554fac21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# UIView.Invalidating

<sub>Structure</sub>

A property wrapper that notifies the system that a property value change has invalidated an aspect of the containing view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@propertyWrapper struct Invalidating<Value, InvalidationType> where Value : Equatable, InvalidationType : UIViewInvalidating
```

## Overview

Use this wrapper when a change in the property value invalidates the display, layout, configuration, constraints, or intrinsic sizing of a view. This wrapper performs any actions necessary to notify the system that your view is invalid and requires an update. The actions depend on the invalidation types you specify. For more information on available invalidation types, see [UIViewInvalidating](../uiviewinvalidating.md).

The following example uses the [Invalidating](invalidating.md) wrapper with the `display` type on the property `badgeColor` and the `display` and `layout` type on the property `badgePosition`.

```swift
class MyView: UIView {
    @Invalidating(.display) var badgeColor: UIColor
    
    @Invalidating(.display, .layout) var badgePosition: UIRectEdge
}

```

When you change the badge color, the property wrapper calls [- setNeedsDisplay](<setneedsdisplay().md>), causing the system to redraw the view. When you change the badge position, the property wrapper also calls [- setNeedsLayout](<setneedslayout().md>), causing the system to update the view’s subviews before it redraws.

Functions such as [- setNeedsDisplay](<setneedsdisplay().md>) and [- setNeedsLayout](<setneedslayout().md>) perform changes on the next update cycle. You can make changes to multiple properties and views before any of those views update. Consolidating the updates to one update cycle is usually better for performance.

> [!note] Note
> You only use [Invalidating](invalidating.md) on subclasses of [UIView](../uiview.md).

## Topics

### Creating an Invalidating Property Wrapper

- [init(wrappedValue:_:)](<invalidating/init(wrappedvalue___).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates an aspect of the containing view.
- [init(wrappedValue:_:_:)](<invalidating/init(wrappedvalue_____).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:)](<invalidating/init(wrappedvalue_______).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:)](<invalidating/init(wrappedvalue_________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:)](<invalidating/init(wrappedvalue___________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:)](<invalidating/init(wrappedvalue_____________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:)](<invalidating/init(wrappedvalue_______________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:_:)](<invalidating/init(wrappedvalue_________________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:_:_:)](<invalidating/init(wrappedvalue___________________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:_:_:_:)](<invalidating/init(wrappedvalue_____________________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.

## See Also

### Updating the view when property values change

- [UIViewInvalidating](../uiviewinvalidating.md) — Implements a type of invalidation that can occur on a view that requires an update.
