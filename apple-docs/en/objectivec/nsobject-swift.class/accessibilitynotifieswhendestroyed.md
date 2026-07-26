---
title: accessibilityNotifiesWhenDestroyed
framework: Objective-C Runtime
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.9+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/nsobject-swift.class/accessibilitynotifieswhendestroyed
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitynotifieswhendestroyed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/accessibilitynotifieswhendestroyed.json'
content_hash: 'sha256:fb420fd97e8ed1bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# accessibilityNotifiesWhenDestroyed

<sub>Instance Property</sub>

A Boolean value that indicates whether a custom accessibility object sends a notification when its corresponding UI element is destroyed.

<sub>macOS</sub>

```swift
var accessibilityNotifiesWhenDestroyed: Bool { get }
```

## Discussion

In macOS 10.9 and later, a custom accessibility object that is an [NSObject](../nsobject-swift.class.md) subclass can post accessibility notifications if it meets the following criteria:

- The lifetime of the custom accessibility object must match the lifetime of the corresponding element in the app’s UI.

Typically, a custom accessibility object that acts as a proxy for an onscreen UI element gets autoreleased and deallocated immediately after the app responds to an accessibility request. Such an object can’t post accessibility notifications, because all registered observers get removed as soon as the object is deallocated. To correct this, an app must guarantee that a custom accessibility object remains allocated for as long as its corresponding UI element remains visible.

- The object must post the [uiElementDestroyed](../../appkit/nsaccessibility-swift.struct/notification/uielementdestroyed.md)  notification at the appropriate time. The appropriate time is most likely to be when the corresponding UI element is removed from the screen, but it can also be when the object itself is deallocated.
- The object must implement `accessibilityNotifiesWhenDestroyed` and return [YES](../yes.md).
