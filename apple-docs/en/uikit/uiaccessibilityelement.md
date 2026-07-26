---
title: UIAccessibilityElement
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityelement
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityelement.json'
content_hash: 'sha256:9a71da215e04577a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityElement

<sub>Class</sub>

An element that should be accessible to users with disabilities, but that isn’t accessible by default.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAccessibilityElement
```

## Overview

You can use [UIAccessibilityElement](uiaccessibilityelement.md) to provide information about an icon or text image that isn’t automatically accessible because it doesn’t inherit from [UIView](uiview.md) (or [UIControl](uicontrol.md)). A view that contains such nonview items creates an instance of [UIAccessibilityElement](uiaccessibilityelement.md) to represent each item that needs to be accessible.

The properties of an accessibility element provide information about the element, such as location and current value, to an assistive application. You might need to set an element’s property even if you don’t need to create an instance of `UIAccessibilityElement` to represent it. For example, if your app includes a button with a custom icon that means “solve,” the button itself is already represented by an accessibility element because it’s a subclass of [UIButton](uibutton.md). However, you need to supply information for the label and hint properties because this information is unique to this button. You can do this in Interface Builder or by setting the properties in the [UIAccessibility](uiaccessibility-protocol.md) informal protocol.

## Relationships

- **Inherits From**: [UIResponder](uiresponder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating an accessibility element

- [- initWithAccessibilityContainer:](<uiaccessibilityelement/init(accessibilitycontainer_).md>) — Creates and initializes an accessibility element to represent an item in the specified container.

### Accessing the containing view

- [accessibilityContainer](uiaccessibilityelement/accessibilitycontainer.md) — The view that contains the accessibility element.

### Determining accessibility

- [isAccessibilityElement](uiaccessibilityelement/isaccessibilityelement.md) — A Boolean value indicating whether the item is an accessibility element an assistive application can access.

### Accessing the attributes of an accessibility element

- [accessibilityLabel](uiaccessibilityelement/accessibilitylabel.md) — A string that succinctly identifies the accessibility element.
- [accessibilityHint](uiaccessibilityelement/accessibilityhint.md) — A string that briefly describes the result of performing an action on the accessibility element.
- [accessibilityValue](uiaccessibilityelement/accessibilityvalue.md) — A string that represents the current value of the accessibility element.
- [accessibilityFrame](uiaccessibilityelement/accessibilityframe.md) — The frame of the accessibility element, in screen coordinates.
- [accessibilityFrameInContainerSpace](uiaccessibilityelement/accessibilityframeincontainerspace.md) — The frame of the accessibility element, in the coordinate space of its container view.
- [accessibilityTraits](uiaccessibilityelement/accessibilitytraits.md) — The combination of traits that best characterize the accessibility element.

## See Also

### Elements

- [UIScrollViewAccessibilityDelegate](uiscrollviewaccessibilitydelegate.md) — A set of methods you can implement to provide accessibility information for a scroll view.
- [UIPickerViewAccessibilityDelegate](uipickerviewaccessibilitydelegate.md) — A set of methods you can implement to provide accessibility information for individual components of a picker view.
