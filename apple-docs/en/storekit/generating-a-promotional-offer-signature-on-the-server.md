---
title: Generating a Promotional Offer Signature on the Server
framework: StoreKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/generating-a-promotional-offer-signature-on-the-server
source_url: 'https://developer.apple.com/documentation/storekit/generating-a-promotional-offer-signature-on-the-server'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/generating-a-promotional-offer-signature-on-the-server.json'
content_hash: 'sha256:e62b4f9e57b78c86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Original API for In-App Purchase](original-api-for-in-app-purchase.md) · [Subscriptions and offers](subscriptions-and-offers.md)

# Generating a Promotional Offer Signature on the Server

<sub>Sample Code</sub>

Generate a signature using your private key and lightweight cryptography libraries.

## Overview

> [!note] Note
> This sample code project is associated with WWDC 2019 session [305: Subscription Offers Best Practices](https://developer.apple.com/videos/play/wwdc19/305/).

This sample code is a simple server written using JavaScript and Node.js. It demonstrates how to generate a signature for promotional offers. The sample demonstrates:

- Receiving a request.
- Generating a cryptographic signature using your private key.
- Sending back a response with the signature.

All of the work is done in `routes/index.js`. You set up environment variables for your key ID and your private key in the `start-server` file.

### Configure the Sample Code Project

1. Install the latest stable version of Node.js.
2. Open Terminal.app and navigate to the sample code directory.
3. Run `npm install` from the command line, and make sure it completes successfully.
4. The `start-server` file contains a key ID and private key PEM string. The values provided in the sample are for example purposes only and will not generate signatures that are valid for your apps. You can optionally open `start-server` with a text editor and replace the example key ID and private key PEM string with your own key ID and private key PEM string that you received from App Store Connect.

### Run a Test on Your Local Server

To test the code on your local machine, from the command line:

- Navigate to the sample code source folder and run `./start-server` from the command line. The server is now running locally and is ready to accept connections on port 3000.
- Open another terminal window and use the `curl` command to send a request. This example command uses the same data listed in the JSON example below:

```swift
curl -X GET -H "Content-type: application/json" -d '{"appBundleID": "com.example.yourapp", "productIdentifier": "com.example.yoursubscription", "offerID": "your_offer_id", "applicationUsername": "8E3DC5F16E13537ADB45FB0F980ACDB6B55839870DBCE7E346E1826F5B0296CA"}' http://127.0.0.1:3000/offer
```

You will get a response that includes the signature.

### Send a Request

To run this sample code, send a request to this URL: `GET http://<yourdomain>/offer`, where `<yourdomain>` is the domain name or IP address of the server this sample code is running on.

The request must have a `Content-type` header of `application/json`, and JSON body data with the following format:

```swift
{
    "appBundleID": "com.example.yourapp",
    "productIdentifier": "com.example.yoursubscription",
    "offerID": "your_offer_id",
    "applicationUsername": "8E3DC5F16E13537ADB45FB0F980ACDB6B55839870DBCE7E346E1826F5B0296CA"
}
```

## See Also

### Promotional offers

- [Setting up promotional offers](setting-up-promotional-offers.md) — Generate a key and configure offers for auto-renewable subscriptions in App Store Connect.
- [Implementing promotional offers in your app](implementing-promotional-offers-in-your-app.md) — Offer discounted pricing for auto-renewable subscription products to eligible subscribers.
- [Generating a signature for promotional offers](generating-a-signature-for-promotional-offers.md) — Create a signature to validate a promotional offer using your private key.
- [SKPaymentDiscount](skpaymentdiscount.md) — The signed discount to apply to a payment. _(deprecated)_

## Download

- [GeneratingAPromotionalOfferSignatureOnTheServer.zip](https://docs-assets.developer.apple.com/published/6c875bdd27a7/GeneratingAPromotionalOfferSignatureOnTheServer.zip)
