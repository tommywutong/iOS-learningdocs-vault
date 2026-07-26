---
title: UIAccessibilityCustomRotorItemResult
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomrotoritemresult
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomrotoritemresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomrotoritemresult.json'
content_hash: 'sha256:82d601d2f310a5eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityCustomRotorItemResult

<sub>Class</sub>

A target element that a custom rotor references.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAccessibilityCustomRotorItemResult
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a rotor item result

- [- initWithTargetElement:targetRange:](<uiaccessibilitycustomrotoritemresult/init(targetelement_targetrange_).md>) — Creates a rotor item result from the specified target element and text range.

### Getting information about the target element

- [targetElement](uiaccessibilitycustomrotoritemresult/targetelement.md) — The target element of the rotor.
- [targetRange](uiaccessibilitycustomrotoritemresult/targetrange.md) — The text range (if any) of the target element.

## See Also

### Navigation

- [UIAccessibilityCustomRotor](uiaccessibilitycustomrotor.md) — A context-sensitive function that helps VoiceOver users find the next instance of a related element.
- [UIAccessibilityCustomRotorSearchPredicate](uiaccessibilitycustomrotorsearchpredicate.md) — The search parameters that help determine the next matching custom rotor item result.
