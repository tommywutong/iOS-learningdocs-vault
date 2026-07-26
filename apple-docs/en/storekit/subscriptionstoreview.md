---
title: SubscriptionStoreView
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/subscriptionstoreview
source_url: 'https://developer.apple.com/documentation/storekit/subscriptionstoreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/subscriptionstoreview.json'
content_hash: 'sha256:bdf8df06dda9eb4b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SubscriptionStoreView

<sub>Structure</sub>

A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct SubscriptionStoreView<Content> where Content : View
```

## Overview

A `SubscriptionStoreView` displays localized information about auto-renewable subscriptions, including their localized names, descriptions, and prices, as well as a purchase button.

Create a subscription store view by using one of the initializers and providing the following information:

- A subscription group identifier
- A collection of product identifiers
- A collection of product values you previously loaded from the App Store

If you provide a subscription group identifier or a collection of product identifiers, the subscription store view automatically loads the subscription data from the App Store, and updates the view when the data is available.

### Provide a background and a decorative icon

The subscription store view doesn’t draw a background by default. You can add a background as follows:

- To layer a background behind the view, use a view modifier, such as `background(alignment:content:)`.
- To set the container background of the subscription store using a view, use the `containerBackground(_:for:)` or `containerBackground(for:alignment:content:)` view modifier and specify a [ContainerBackgroundPlacement](../swiftui/containerbackgroundplacement.md), such as [subscriptionStoreHeader](../swiftui/containerbackgroundplacement/subscriptionstoreheader.md).

You can optionally provide a view as a decorative icon next to each subscription option. Use the [subscriptionStoreControlIcon(icon:)](<../swiftui/view/subscriptionstorecontrolicon(icon_).md>) view modifier to set a view that decorates individual subscription options within a subscription store.

### Order and filter subscriptions

If you create the subscription store view by providing a subscription group identifier, the system orders the subscription options according to their rank. If the customer is already subscribed, you may want to merchandise upgrade or crossgrade options. By default, the subscription store view lists all the subscriptions in the group. To hide certain subscription options, provide the `visibleRelationships` parameter in the initializer. For more information about the visible relationships, see [SubscriptionRelationship](product/subscriptionrelationship.md).

If you create the subscription store view using one of the other initializers, the view orders the subscriptions according to the collection parameter’s order. The view excludes subscriptions that you don’t include in the collection parameter.

### Add terms of service and privacy policies

The `SubscriptionStoreView` automatically displays buttons for the terms of service and privacy policy that you submit in App Store Connect. To override the destination of these buttons with a URL to custom terms of service and privacy policy pages, or a custom view, use the modifiers [subscriptionStorePolicyDestination(url:for:)](<../swiftui/view/subscriptionstorepolicydestination(url_for_).md>) and [subscriptionStorePolicyDestination(for:destination:)](<../swiftui/view/subscriptionstorepolicydestination(for_destination_).md>).

Use modifiers, such as [subscriptionStorePolicyForegroundStyle(_:)](<../swiftui/view/subscriptionstorepolicyforegroundstyle(__).md>), to customize the button’s style, for example, to make the text more readable against your store’s background.

### Add auxiliary buttons

You can show auxiliary buttons in the subscription store using view modifiers. Specify the button’s visibility within the subscription store by using the [storeButton(_:for:)](<../swiftui/view/storebutton(__for_).md>) view modifier.

If you offer your subscription through other services, you can configure the subscription store view to display a sign-in button. Use the [subscriptionStoreSignInAction(_:)](<../swiftui/view/subscriptionstoresigninaction(__).md>) modifier to set the function your app calls when someone uses the sign-in button.

The subscription store view automatically shows a Close button. To override this behavior, use the `storeButton(_:for:)` modifier to unconditionally show, or hide, the Close button.

### Style the subscription store view

You can further customize the subscription store’s appearance using control styles. Use subscription store control styles to customize the display of subscription options, and how people interact with your store. To try out standard styles, such as [PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md), apply the style using the [subscriptionStoreControlStyle(_:)](<../swiftui/view/subscriptionstorecontrolstyle(__).md>) modifier.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating subscription store views with automatic marketing content

- [init(groupID:visibleRelationships:)](<subscriptionstoreview/init(groupid_visiblerelationships_).md>) — Creates a view that loads all subscriptions in a subscription group from the App Store, and merchandises them with automatic marketing content.
- [init(productIDs:)](<subscriptionstoreview/init(productids_).md>) — Creates a view that loads subscriptions based on a collection of product identifiers, and merchandises them with automatic marketing content.
- [init(subscriptions:)](<subscriptionstoreview/init(subscriptions_).md>) — Creates a view that displays a collection of subscription options, and merchandises them with automatic marketing content.

### Creating subscription store views with custom marketing content

- [init(groupID:visibleRelationships:marketingContent:)](<subscriptionstoreview/init(groupid_visiblerelationships_marketingcontent_).md>) — Creates a view that loads all the subscriptions in a subscription group from the App Store, and merchandises them with custom marketing content.
- [init(productIDs:marketingContent:)](<subscriptionstoreview/init(productids_marketingcontent_).md>) — Creates a view that loads a collection of subscriptions from the App Store, and merchandises them with custom marketing content.
- [init(subscriptions:marketingContent:)](<subscriptionstoreview/init(subscriptions_marketingcontent_).md>) — Creates a view that displays a collection of subscription options, and merchandises them with custom marketing content.

### Creating subscription store views with a hierarchichal structure

- [init(groupID:visibleRelationships:content:)](<subscriptionstoreview/init(groupid_visiblerelationships_content_).md>)
- [init(productIDs:content:)](<subscriptionstoreview/init(productids_content_).md>)
- [init(subscriptions:content:)](<subscriptionstoreview/init(subscriptions_content_).md>)

### Supporting types

- [AutomaticSubscriptionStoreMarketingContent](automaticsubscriptionstoremarketingcontent.md) — A view that represents the default marketing content for a subscription store.
- [SubscriptionStoreContentView](subscriptionstorecontentview.md)

## See Also

### Merchandising In-App Purchases, subscriptions, and offers

- [ProductView](productview.md) — A view that merchandises an individual In-App Purchase product.
- [StoreView](storeview.md) — A view that merchandises a collection of In-App Purchase products.
- [SubscriptionOfferView](subscriptionofferview.md)
- [Backyard Birds: Building an app with SwiftData and widgets](../swiftui/backyard-birds-sample.md) — Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
