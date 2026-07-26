---
title: 'init(wrappedValue:_:_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/invalidating/init(wrappedvalue:_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/invalidating/init(wrappedvalue:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/invalidating/init%28wrappedvalue%3A_%3A_%3A%29.json'
content_hash: 'sha256:99b5aeee4ddb6545'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIView](../../uiview.md) · [Invalidating](../invalidating.md)

# init(wrappedValue:_:_:)

<sub>Initializer</sub>

Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init<InvalidationType1, InvalidationType2>(wrappedValue: Value, _ invalidation1: InvalidationType1, _ invalidation2: InvalidationType2) where InvalidationType == UIView.Invalidations.Tuple<InvalidationType1, InvalidationType2>, InvalidationType1 : UIViewInvalidating, InvalidationType2 : UIViewInvalidating
```

## Parameters

- `wrappedValue` — The underlying value referenced by the invalidating variable.

- `invalidation1` — A type of invalidation.

- `invalidation2` — A type of invalidation.

## See Also

### Creating an Invalidating Property Wrapper

- [init(wrappedValue:_:)](<init(wrappedvalue___).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates an aspect of the containing view.
- [init(wrappedValue:_:_:_:)](<init(wrappedvalue_______).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:)](<init(wrappedvalue_________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:)](<init(wrappedvalue___________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:)](<init(wrappedvalue_____________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:)](<init(wrappedvalue_______________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:_:)](<init(wrappedvalue_________________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:_:_:)](<init(wrappedvalue___________________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
- [init(wrappedValue:_:_:_:_:_:_:_:_:_:_:)](<init(wrappedvalue_____________________).md>) — Creates a property wrapper that notifies the system when a change in the property value invalidates aspects of the containing view.
