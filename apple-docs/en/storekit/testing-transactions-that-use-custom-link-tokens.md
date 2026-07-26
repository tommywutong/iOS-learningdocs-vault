---
title: Testing transactions that use custom link tokens
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/testing-transactions-that-use-custom-link-tokens
source_url: 'https://developer.apple.com/documentation/storekit/testing-transactions-that-use-custom-link-tokens'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/testing-transactions-that-use-custom-link-tokens.json'
content_hash: 'sha256:77bb708b97649bf7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [External Purchase](external-purchase.md)

# Testing transactions that use custom link tokens

<sub>Article</sub>

Recognize custom link tokens that your app receives in the sandbox testing environment, and use them to test reporting transactions.

## Overview

When you test your app in the sandbox environment, the External Purchase API returns tokens that are valid only in that environment. These tokens have an [externalPurchaseId](../externalpurchaseserverapi/externalpurchaseid.md) that starts with the string `SANDBOX`. For more information about the token format, see [Receiving and decoding external purchase tokens](receiving-and-decoding-external-purchase-tokens.md).

Apps running in the sandbox environment need to satisfy the same requirements as they do in the production environment to receive external purchase tokens, including that they:

- Have an entitlement, such as [com.apple.developer.storekit.external-purchase-link](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md) or  [com.apple.developer.storekit.external-purchase-link-streaming](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link-streaming.md)
- Configure the associated property list key if the entitlement requires one, such as [SKExternalPurchaseCustomLinkRegions](../bundleresources/information-property-list/skexternalpurchasecustomlinkregions.md) or [SKExternalPurchaseLinkStreamingRegions](../bundleresources/information-property-list/skexternalpurchaselinkstreamingregions.md)
- Check their eligibility to use the [External Purchase](external-purchase.md) API at runtime, with [isEligible](externalpurchasecustomlink/iseligible.md) and [canMakePayments](appstore/canmakepayments.md)

### Handle custom link tokens in the sandbox environment

The [ExternalPurchaseCustomLink](externalpurchasecustomlink.md) API generates custom link tokens, which have a token type and an expiration date. There are two possible token types, `ACQUISITION` and `SERVICES`. Your app requests a token by calling the [token(for:)](<externalpurchasecustomlink/token(for_).md>) method and specifying the token type. The first time you request a token in the sandbox environment, the system creates the token and initiates an _active token period_.

> [!note] Note
> In the sandbox environment, custom link tokens expire 1 hour after creation.

Apps can request tokens again at any time. If there’s an active token period, the system returns the token that corresponds to that active period. The returned token can be identical to the original token, or it can be a _refreshed_ token. A refreshed token has the same creation and expiration dates as the original token, but a different `externalPurchaseId`. Use either an original token or a refreshed token to report transactions.

There’s a maximum of one active token period for `ACQUISITION` tokens, for each Sandbox Apple Account, for each app. After the `ACQUISITION` token expires, the Sandbox Apple Account can’t receive another `ACQUISITION` token for the same app. This reflects the behavior in the production environment, where apps have a maximum of one active period for the `ACQUISITION` token for each customer. To repeat tests for this token type after it expires, use another Sandbox Apple Account.

After a `SERVICES` token period expires, your app can request a new `SERVICES` token and you can continue testing. The new token has a new creation and expiration date, and starts a new active token period.

### Test reporting tokens on your server

To test your server’s token reporting implementation, send reports for sandbox tokens to the Sandbox URL of the [Send External Purchase Report](../externalpurchaseserverapi/send-external-purchase-report.md) endpoint. For more information about reporting tokens, see [External Purchase Server API](../externalpurchaseserverapi.md).

To report transactions, you can use any token for the customer that’s active (not expired) at the time of the transaction.

## See Also

### Implementing external purchases in the EU

- [ExternalPurchaseCustomLink](externalpurchasecustomlink.md) — An enumeration that enables qualifying apps to offer custom links for external purchases and use alternative payment service providers.
- [Token](externalpurchasecustomlink/token.md) — A token you use with the External Purchase custom link API.
- [com.apple.developer.storekit.custom-purchase-link.allowed-regions](../bundleresources/entitlements/com.apple.developer.storekit.custom-purchase-link.allowed-regions.md) — An entitlement that enables a qualifying app to offer external purchases within app or at a website, in specific regions.
- [com.apple.developer.storekit.external-purchase-link](../bundleresources/entitlements/com.apple.developer.storekit.external-purchase-link.md) — A Boolean value that indicates whether your app can include a link that directs people to a website to make an external purchase.
- [SKExternalPurchaseCustomLinkRegions](../bundleresources/information-property-list/skexternalpurchasecustomlinkregions.md) — An array of country code strings that indicate the regions where your app supports custom links for the communication and promotion of offers.
