---
title: restorationIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/restorationidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiview/restorationidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/restorationidentifier.json'
content_hash: 'sha256:bc3cb503186b7e4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# restorationIdentifier

<sub>Instance Property</sub>

The identifier that determines whether the view supports state restoration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var restorationIdentifier: String? { get set }
```

## Discussion

This property indicates whether state information in the view should be preserved; it is also used to identify the view during the restoration process. The value of this property is `nil` by default, which indicates that the view’s state does not need to be saved. Assigning a string object to the property lets the owning view controller know that the view has relevant state information to save.

Assign a value to this property only if you are implementing a custom view that implements the [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) and [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) methods for saving and restoring state. You use those methods to write any view-specific state information and subsequently use that data to restore the view to its previous configuration.

> [!important] Important
> Simply setting the value of this property is not enough to ensure that the view is preserved and restored. Its owning view controller, and all of that view controller’s parent view controllers, must also have a restoration identifier. For more information about the preservation and restoration process, see [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

## See Also

### Preserving and restoring state

- [- encodeRestorableStateWithCoder:](<encoderestorablestate(with_).md>) — Encodes state-related information for the view.
- [- decodeRestorableStateWithCoder:](<decoderestorablestate(with_).md>) — Decodes and restores state-related information for the view.
