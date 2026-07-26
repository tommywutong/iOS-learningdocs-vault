---
title: SubscriptionStorePolicyKind
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstorepolicykind
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstorepolicykind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstorepolicykind.json'
content_hash: 'sha256:11e55bef1e76fca3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStorePolicyKind

<sub>Structure</sub>

The type of policy, such as the terms of service or privacy policies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SubscriptionStorePolicyKind
```

## Overview

To set the destination of a policy button in a [SubscriptionStoreView](subscriptionstoreview.md), use [subscriptionStorePolicyDestination(url:for:)](<../swiftui/view/subscriptionstorepolicydestination(url_for_).md>) or [subscriptionStorePolicyDestination(for:destination:)](<../swiftui/view/subscriptionstorepolicydestination(for_destination_).md>).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting policy types

- [privacyPolicy](subscriptionstorepolicykind/privacypolicy.md) — The privacy policy type.
- [termsOfService](subscriptionstorepolicykind/termsofservice.md) — The terms of service policy type.

## See Also

### Configuring the subscription store policies

- [subscriptionStorePolicyDestination(for:destination:)](<../swiftui/view/subscriptionstorepolicydestination(for_destination_).md>) — Configures a view as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyDestination(url:for:)](<../swiftui/view/subscriptionstorepolicydestination(url_for_).md>) — Configures a URL as the destination for a policy button action in subscription store views.
- [subscriptionStorePolicyForegroundStyle(_:)](<../swiftui/view/subscriptionstorepolicyforegroundstyle(__).md>) — Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [subscriptionStorePolicyForegroundStyle(_:_:)](<../swiftui/view/subscriptionstorepolicyforegroundstyle(____).md>) — Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
