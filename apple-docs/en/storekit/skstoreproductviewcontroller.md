---
title: SKStoreProductViewController
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.0+, macOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductviewcontroller
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductviewcontroller.json'
content_hash: 'sha256:009a4f7c7e7a7342'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductViewController

<sub>Class</sub>

A view controller that provides a page where customers can purchase media from the App Store.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
@MainActor class SKStoreProductViewController
```

## Overview

To display a store for customers to purchase media from the App Store, follow these steps:

1. Create an `SKStoreProductViewController` object and set its [delegate](skstoreproductviewcontroller/delegate.md).
2. Indicate a specific product to sell by passing its iTunes item identifier to the [- loadProductWithParameters:completionBlock:](<skstoreproductviewcontroller/loadproduct(withparameters_completionblock_).md>) method.
3. Present the view controller modally from another view controller in your app. Your delegate dismisses the view controller when the customer completes the purchase.

Present the `SKStoreProductViewController` object immediately when someone triggers an interaction, such as tapping a Buy button. Load the product information before presenting the view controller to ensure a seamless user experience.

This class ignores [modalPresentationStyle](../uikit/uiviewcontroller/modalpresentationstyle.md) settings, and those settings have no impact on the sheet’s presentation.

To recommend another app without displaying a full product page, and to recommend an App Clip’s corresponding app from within the App Clip, use [SKOverlay](skoverlay.md).

> [!note] Note
> In a compatible iPad or iPhone app running in visionOS, this method displays a minimal sheet to enable an app purchase or to launch the App Store for more information. For an in-line experience that’s consistent across platforms, use [SKOverlay](skoverlay.md) instead.

### Prevent exceptions

The `SKStoreProductViewController` class doesn’t support subclassing or embedding, and must be used as-is.

> [!important] Important
> If you compile with the iOS 13 SDK, attempting to instantiate a subclass of `SKStoreProductViewController` results in a runtime exception.

This class throws the following runtime exceptions:

- **SKUnsupportedClassException** — Occurs if the app attempts to instantiate a subclass of `SKStoreProductViewController`.
- **SKUnsupportedPresentationException** — Occurs if the app attempts to use an unsupported presentation mode for `SKStoreProductViewController`, such as embedding it as a subview controller or attempting to use it in a popover.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md), [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Setting a delegate

- [delegate](skstoreproductviewcontroller/delegate.md) — The store view controller’s delegate.
- [SKStoreProductViewControllerDelegate](skstoreproductviewcontrollerdelegate.md) — A protocol to call when the customer dismisses the store screen.

### Loading a new product screen

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md) — Allow users to purchase media in the App Store from within your app.
- [- loadProductWithParameters:completionBlock:](<skstoreproductviewcontroller/loadproduct(withparameters_completionblock_).md>) — Loads a new product screen to display.
- [- loadProductWithParameters:impression:completionBlock:](<skstoreproductviewcontroller/loadproduct(withparameters_impression_completionblock_).md>)
- [loadProduct(parameters:impression:)](<skstoreproductviewcontroller/loadproduct(parameters_impression_).md>)
- [loadProduct(parameters:impression:reengagementURL:)](<skstoreproductviewcontroller/loadproduct(parameters_impression_reengagementurl_).md>)
- [Product Dictionary Keys](product-dictionary-keys.md) — Keys for identifying products and the tokens for affiliates and campaigns.

## See Also

### Recommendations

- [Offering media for sale in your app](offering-media-for-sale-in-your-app.md) — Allow users to purchase media in the App Store from within your app.
- [SKOverlay](skoverlay.md) — A class that displays an overlay you can use to recommend another app or an App Clip’s corresponding full app.
