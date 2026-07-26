---
title: activeInputModes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputmode/activeinputmodes
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputmode/activeinputmodes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputmode/activeinputmodes.json'
content_hash: 'sha256:d6dfd6f2306282ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputMode](../uitextinputmode.md)

# activeInputModes

<sub>Type Property</sub>

The active text-input modes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var activeInputModes: [UITextInputMode] { get }
```

## Discussion

Each element in the array is an instance of [UITextInputMode](../uitextinputmode.md). Returns an empty array if no such instances have been set by the text input system.

> [!important] Important
> This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [Describing use of required reason API](../../bundleresources/describing-use-of-required-reason-api.md).
