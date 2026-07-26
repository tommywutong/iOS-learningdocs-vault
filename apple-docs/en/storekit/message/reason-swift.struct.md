---
title: Message.Reason
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/message/reason-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/message/reason-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/message/reason-swift.struct.json'
content_hash: 'sha256:0d3984f2076c28a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Message](../message.md)

# Message.Reason

<sub>Structure</sub>

Reasons for the App Store messages.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct Reason
```

## Overview

The message reason informs your app of the purpose of the message. Your app can optionally use this information when it handles the messages.

For information about handling App Store messages, see [Message](../message.md).

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the message reasons

- [billingIssue](reason-swift.struct/billingissue.md) — A message the App Store sends that informs people of a billing problem and enables them to update billing information.
- [generic](reason-swift.struct/generic.md) — A message the App Store sends for a generic reason.
- [priceIncreaseConsent](reason-swift.struct/priceincreaseconsent.md) — A message the App Store sends when you increase the price of an auto-renewable subscription and the price increase requires the customer’s consent.
- [winBackOffer](reason-swift.struct/winbackoffer.md) — A message the App Store sends when the customer is eligible for a win-back offer that you configure in App Store Connect.

### Getting the localized description

- [localizedDescription](reason-swift.struct/localizeddescription.md) — A localized description of the App Store message.

## See Also

### Messages

- [Message](../message.md) — An instance for receiving and displaying App Store messages in your app.
- [DisplayMessageAction](../displaymessageaction.md) — An instance that asks StoreKit to display an App Store message, if appropriate.
