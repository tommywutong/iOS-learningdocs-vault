---
title: ProximityReader
framework: ProximityReader
symbol_kind: module
role: collection
role_heading: Framework
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/proximityreader
source_url: 'https://developer.apple.com/documentation/proximityreader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/proximityreader.json'
content_hash: 'sha256:f5d928643aba4cdd'
translated: false
---

> Navigation: [Technologies](technologies.md)

# ProximityReader

<sub>Framework</sub>

Read contactless physical and digital wallet cards using your iPhone.

## Overview

The ProximityReader framework supports _Tap to Pay on iPhone_, which allows a person’s iPhone to act as a point-of-sale device without additional hardware. ProximityReader also supports the reading of loyalty cards from the Wallet app. Use this framework to initiate the payment process from your app.

The use of this framework requires you to coordinate with a participating payment service provider that is Level 3 certified. Contact your payment provider and work with them to set up a workflow for handling payments. When you’re ready, contact Apple and request the entitlement you need to integrate Tap to Pay on iPhone support into your app. For information on requesting this entitlement, see [Setting up Tap to Pay on iPhone](proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone.md).

> [!note] Note
> Tap to Pay on iPhone follows the PCI CPoC Standard, which uses Level 2 certified payment kernels and a user interface for reading contactless payment cards.

## Topics

### Payment card reader

- [Setting up Tap to Pay on iPhone](proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone.md) — Request and configure the required entitlement to support Tap to Pay on iPhone.
- [Adding support for Tap to Pay on iPhone to your app](proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app.md) — Configure your app to use Tap to Pay on iPhone to read contactless payment cards.
- [PaymentCardReader](proximityreader/paymentcardreader.md) — An object you use to configure Tap to Pay on iPhone on the current device.
- [PaymentCardReaderSession](proximityreader/paymentcardreadersession.md) — The object you use to start reading a contactless payment or loyalty card.

### Payment requests

- [PaymentCardTransactionRequest](proximityreader/paymentcardtransactionrequest.md) — A request for a contactless purchase or refund that includes the purchase amount and currency information.
- [PaymentCardVerificationRequest](proximityreader/paymentcardverificationrequest.md) — A request to verify details for a contactless payment card.
- [PaymentCardReadResult](proximityreader/paymentcardreadresult.md) — The result of a payment card read operation.

### Store and Forward mode

- [StoreAndForwardBatch](proximityreader/storeandforwardbatch.md) — A structure that stores the data to send to the payment service provider to process.
- [StoreAndForwardBatchDeletionToken](proximityreader/storeandforwardbatchdeletiontoken.md) — A secure token that you use to delete a Store and Forward batch.
- [StoreAndForwardPaymentCardReaderSession](proximityreader/storeandforwardpaymentcardreadersession.md) — The object you use to start reading a contactless payment or loyalty card in Store and Forward mode.
- [StoreAndForwardStatus](proximityreader/storeandforwardstatus.md) — A structure that describes the Store and Forward session status.
- [PaymentCardReaderStore](proximityreader/paymentcardreaderstore.md) — A structure that manages the store that contains all the Store and Forward reads.

### Loyalty card requests

- [Accepting loyalty passes from Wallet](proximityreader/accepting-loyalty-passes-from-wallet.md) — Set up the necessary components so your app can begin using Tap to Pay on iPhone to read and issue loyalty passes.
- [VASRequest](proximityreader/vasrequest.md) — A request to read a contactless loyalty card and retrieve loyalty program identifiers for the person.
- [VASReadResult](proximityreader/vasreadresult.md) — The result of a request to read loyalty card information.

### Merchant discovery

- [ProximityReaderDiscovery](proximityreader/proximityreaderdiscovery.md) — An object that presents a UI with information about how to use Tap to Pay on iPhone.

### Mobile document reader

- [Adopting the Verifier API in your iPhone app](proximityreader/adopting-the-verifier-api-in-your-iphone-app.md) — Configure and test ID Verifier support in your app for reading mobile documents.
- [Generating reader tokens for the Verifier API](proximityreader/generating-reader-tokens-for-the-verifier-api.md) — Configure your server to generate reader tokens to prepare a device for mobile document reading.
- [Checking IDs with the Verifier API](proximityreader/checking-ids-with-the-verifier-api.md) — Read and verify mobile driver’s license, photo ID, and National ID information without any additional hardware.
- [MobileDocumentReader](proximityreader/mobiledocumentreader.md) — An object for configuring mobile document reading on the current device.
- [MobileDocumentReaderSession](proximityreader/mobiledocumentreadersession.md) — The object you use to start reading a mobile document.

### Mobile document requests

- [MobileDriversLicenseDisplayRequest](proximityreader/mobiledriverslicensedisplayrequest.md) — A mobile driver’s license request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [MobileDriversLicenseDataRequest](proximityreader/mobiledriverslicensedatarequest.md) — A mobile driver’s license request that retrieves elements from the holder and returns the validated document elements.
- [MobileDriversLicenseRawDataRequest](proximityreader/mobiledriverslicenserawdatarequest.md) — A mobile driver’s license request which retrieves elements from the holder and returns the raw response data for processing.
- [MobileNationalIDCardDisplayRequest](proximityreader/mobilenationalidcarddisplayrequest.md) — A mobile national ID card request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [MobileNationalIDCardDataRequest](proximityreader/mobilenationalidcarddatarequest.md) — A mobile national ID card request that retrieves elements from the holder and returns the validated document elements.
- [MobileNationalIDCardRawDataRequest](proximityreader/mobilenationalidcardrawdatarequest.md) — A mobile national ID card request which retrieves elements from the holder and returns the raw response data for processing.
- [MobileDocumentDisplayRequest](proximityreader/mobiledocumentdisplayrequest.md) — A mobile document request that retrieves elements from the holder and displays the results onscreen for visual inspection.
- [MobileDocumentRequest](proximityreader/mobiledocumentrequest.md) — A type that represents a mobile document request.
- [MobileDocumentDataRequest](proximityreader/mobiledocumentdatarequest.md) — A type that represents a mobile document data request.
- [MobileDocumentRawDataRequest](proximityreader/mobiledocumentrawdatarequest.md) — A type that represents a mobile document raw data request.
- [MobilePhotoIDDataRequest](proximityreader/mobilephotoiddatarequest.md) — A photo ID request that retrieves elements from the holder and returns the validated document elements.
- [MobilePhotoIDRawDataRequest](proximityreader/mobilephotoidrawdatarequest.md) — A photo ID request which retrieves elements from the holder and returns the raw response data for processing.
- [MobileDocumentAnyOfDataRequest](proximityreader/mobiledocumentanyofdatarequest.md) — A type that describes a data request for any mobile document from a group of requests.
- [MobileDocumentAnyOfRawDataRequest](proximityreader/mobiledocumentanyofrawdatarequest.md) — A type that describes a raw data request for any mobile document from a group of requests.

### Tap to Share

- [Adding support for Tap to Share to your app](proximityreader/adding-support-for-tap-to-share-to-your-app.md) — Request and share customer information on device.
- [CustomerEngagement](proximityreader/customerengagement.md) — An enumeration of the shared data between the merchant and customer. _(beta)_
- [CustomerEngagementSession](proximityreader/customerengagementsession.md) — The object you use to share and request customer information. _(beta)_

### Errors

- [PaymentCardReaderError](proximityreader/paymentcardreadererror.md) — An error type that indicates problems with the configuration of the reader.
- [MobileDocumentReaderError](proximityreader/mobiledocumentreadererror.md) — An error type that indicates problems when preparing a mobile document reader session and performing document requests.

### Structures

- [MobileDocumentHolderName](proximityreader/mobiledocumentholdername.md) — A type that represents the mobile identity document holder’s name. _(beta)_
