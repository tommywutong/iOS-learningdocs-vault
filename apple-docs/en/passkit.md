---
title: PassKit (Apple Pay and Wallet)
framework: PassKit (Apple Pay and Wallet)
symbol_kind: module
role: collection
role_heading: Technology
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.0+, macOS 11.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/passkit
source_url: 'https://developer.apple.com/documentation/passkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit.json'
content_hash: 'sha256:5505e46f1f1b187e'
translated: false
---

> Navigation: [Technologies](technologies.md)

# PassKit (Apple Pay and Wallet)

<sub>Technology</sub>

Process Apple Pay payments in your app, and create and distribute passes for the Wallet app.

## Overview

The PassKit framework lets you:

- Add Apple Pay to your app
- Manage passes in the user’s Wallet app

![The Apple Pay logo.](../../attachments/65928622a496739ca5949a1771499e5d/media-3975193@2x.png)

Apple Pay is a secure and easy way for users to make purchases in stores, in apps, and on the web. When you use PassKit APIs to support Apple Pay in your iOS and watchOS apps, your users can purchase real-world goods and services, or donate to nonprofit organizations, without ever leaving your app.

> [!note] Note
> To add Apple Pay to your web applications, see [Apple Pay on the Web](applepayontheweb.md).
>
> For digital goods and services delivered within the app, see [In-App Purchase](https://developer.apple.com/in-app-purchase/) instead.

![The icon that respresents Wallet.](../../attachments/1f03432c3578ddd87cc12f1efefebc4e/media-3975195@2x.png)

The Wallet app allows users to organize their boarding passes, tickets, gift cards, and loyalty cards. It also lets users manage their payment cards for Apple Pay. Using the PassKit framework, you can add passes to Wallet and have these passes appear on the user’s lock screen based on the time and place when the pass is relevant. You can also update a pass’s content using push notifications.

## Topics

### Apple pay support

- [Apple Pay](passkit/apple-pay.md) — Request and process Apple Pay payments in your app.

### Wallet support

- [Wallet](passkit/wallet.md) — Manage tickets, boarding passes, payment cards and other passes in the Wallet app.

### Structures

- [ApplePayMerchandisingAction](passkit/applepaymerchandisingaction.md) — Type of action taken when the button is tapped on the ApplePayMerchandisingView _(beta)_
- [ApplePayMerchandisingPartnerConfiguration](passkit/applepaymerchandisingpartnerconfiguration.md) — Defines the partner configuration for the ApplePayMerchandisingView _(beta)_
- [ApplePayMerchandisingStyle](passkit/applepaymerchandisingstyle.md) — Styling layout of the ApplePayMerchandisingView _(beta)_
- [ApplePayMerchandisingView](passkit/applepaymerchandisingview.md) _(beta)_

## See Also

### Related Documentation

- [Wallet Passes](walletpasses.md) — Create, distribute, and update passes for the Wallet app.
