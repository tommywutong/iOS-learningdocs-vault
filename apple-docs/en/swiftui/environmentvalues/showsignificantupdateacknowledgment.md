---
title: showSignificantUpdateAcknowledgment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/showsignificantupdateacknowledgment
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/showsignificantupdateacknowledgment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/showsignificantupdateacknowledgment.json'
content_hash: 'sha256:6db821cff68400a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# showSignificantUpdateAcknowledgment

<sub>Instance Property</sub>

Presents a system interface to inform people about significant app changes and request their acknowledgment.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var showSignificantUpdateAcknowledgment: SignificantUpdateAction { get }
```

## Discussion

Call this action from a [Button](../button.md) or [onAppear(perform:)](<../view/onappear(perform_).md>) to inform people about significant app changes that require their acknowledgment.
