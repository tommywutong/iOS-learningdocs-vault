---
title: 'token(for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.1+, iPadOS 18.1+, macOS 15.1+, tvOS 18.1+, visionOS 2.1+, watchOS 11.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/externalpurchasecustomlink/token(for:)'
source_url: 'https://developer.apple.com/documentation/storekit/externalpurchasecustomlink/token(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/externalpurchasecustomlink/token%28for%3A%29.json'
content_hash: 'sha256:721271af9d3b875c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md)

# token(for:)

<sub>Type Method</sub>

Requests an external purchase token of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func token(for tokenType: String) async throws -> ExternalPurchaseCustomLink.Token?
```

## Parameters

- `tokenType` — A string that indicates the token type. Valid string values are: `ACQUISITION`, `SERVICES`, `IN_APP`, `LINK_OUT`.

## Return Value

Returns an external purchase token of the type you specify, or returns `nil` if there isn’t an active token of the specified type. This method throws an error if your app isn’t eligible to use this API.

## Discussion

Use this method to request tokens when your app uses the [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md) API.

The token types you request depend on the region in which your app offers external purchases:

- For external purchases in the European Union (EU), request the `ACQUISITION` and `SERVICES` token types when your app launches and immediately associate the tokens with a customer account on your server. You can also call this method at any other time, such as before communicating or promoting offers. The method returns the token, of each type, until it expires.
- For external purchases in Japan, request the `IN_APP` or `LINK_OUT` token types. Request an `IN_APP` token type for flows that use an alternative payment provider inside the app.  Request a `LINK_OUT` token type for flows where customers can complete transactions on your website, outside of the app. For more information, see [Payment options on the App Store in Japan](https://developer.apple.com/support/payment-options-on-the-app-store-in-japan).

The `IN_APP` and `LINK_OUT` token types for Japan are available starting in iOS 26.4.

> [!tip] Tip
> Request tokens before every potential transaction to ensure you have current tokens.

### Read and report tokens

Decode the token to read its contents, including its expiration date. For more information, see [Receiving and decoding external purchase tokens](../receiving-and-decoding-external-purchase-tokens.md). For a code example that shows requesting tokens, see [ExternalPurchaseCustomLink](../externalpurchasecustomlink.md).

Report tokens and all transactions associated with the tokens from your server, using the [External Purchase Server API](../../externalpurchaseserverapi.md).

## See Also

### Getting external purchase tokens

- [Token](token.md) — A token you use with the External Purchase custom link API.
- [Receiving and decoding external purchase tokens](../receiving-and-decoding-external-purchase-tokens.md) — Receive tokens for external purchases that you use to report transactions to Apple.
