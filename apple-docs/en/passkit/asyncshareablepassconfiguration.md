---
title: AsyncShareablePassConfiguration
framework: PassKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/asyncshareablepassconfiguration
source_url: 'https://developer.apple.com/documentation/passkit/asyncshareablepassconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/asyncshareablepassconfiguration.json'
content_hash: 'sha256:85f78f84bb974e35'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# AsyncShareablePassConfiguration

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency struct AsyncShareablePassConfiguration<Content> where Content : View
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating the configuration

- [init(metadata:action:content:)](<asyncshareablepassconfiguration/init(metadata_action_content_).md>)
- [Result](asyncshareablepassconfiguration/result.md)

## See Also

### General purpose passes

- [PKSecureElementPass](pksecureelementpass.md) — A pass with a credential that the device stores in a certified payment information chip.
- [PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md) — An object that describes the configuration of a secure element payment pass.
- [PKAddSecureElementPassViewController](pkaddsecureelementpassviewcontroller.md) — A view controller that manages the addition of secure element payment passes.
- [PKPass](pkpass.md) — An object that represents a single pass.
- [PKAddPassesViewController](pkaddpassesviewcontroller.md) — Lets your app show a pass and prompt the user to add that pass to the pass library.
- [PKShareSecureElementPassViewController](pksharesecureelementpassviewcontroller.md)
- [PKShareSecureElementPassViewControllerDelegate](pksharesecureelementpassviewcontrollerdelegate.md)
- [Preview](pkshareablepassmetadata/preview-swift.class.md)
- [PKShareSecureElementPassResult](pksharesecureelementpassresult.md)
