---
title: 'appStoreMerchandising(isPresented:kind:onDismiss:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.2+, tvOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/appstoremerchandising(ispresented:kind:ondismiss:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/appstoremerchandising(ispresented:kind:ondismiss:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/appstoremerchandising%28ispresented%3Akind%3Aondismiss%3A%29.json'
content_hash: 'sha256:1ef78c16a41edd5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# appStoreMerchandising(isPresented:kind:onDismiss:)

<sub>Instance Method</sub>

Display a merchandising view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
nonisolated func appStoreMerchandising(isPresented: Binding<Bool>, kind: AppStoreMerchandisingKind, onDismiss: ((Result<AppStoreMerchandisingKind.PresentationResult, any Error>) async -> ())? = nil) -> some View

```

## Parameters

- `isPresented` — A binding to a Boolean value that determines whether the App Store merchandising view is presented.

- `kind` — The merchandising kind to merchandise.

- `onDismiss` — The closure to execute when the merchandising view is dismissed, with the presetation result of the App Store merchandising view provided as a parameter.

## See Also

### StoreKit

- [appStoreOverlay(isPresented:configuration:)](<appstoreoverlay(ispresented_configuration_).md>) — Presents a StoreKit overlay when a given condition is true.
- [manageSubscriptionsSheet(isPresented:)](<managesubscriptionssheet(ispresented_).md>)
- [refundRequestSheet(for:isPresented:onDismiss:)](<refundrequestsheet(for_ispresented_ondismiss_).md>) — Display the refund request sheet for the given transaction.
- [offerCodeRedemption(options:isPresented:onCompletion:)](<offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_
