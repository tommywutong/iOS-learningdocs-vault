---
title: Checking IDs with the Verifier API
framework: ProximityReader
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/proximityreader/checking-ids-with-the-verifier-api
source_url: 'https://developer.apple.com/documentation/proximityreader/checking-ids-with-the-verifier-api'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/proximityreader/checking-ids-with-the-verifier-api.json'
content_hash: 'sha256:edc61071df43f9b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ProximityReader](../proximityreader.md)

# Checking IDs with the Verifier API

<sub>Article</sub>

Read and verify mobile driver’s license, photo ID, and National ID information without any additional hardware.

## Overview

> [!note] Note
> This sample code project is associated with WWDC23 session 10114: [What’s new in Wallet and Apple Pay](https://developer.apple.com/wwdc23/10114/).

### Configure the sample code project

The project contains two targets:

- `VerifierAPISample-DisplayRequest`: This target is configured to perform a [MobileDriversLicenseDisplayRequest](mobiledriverslicensedisplayrequest.md).
- `VerifierAPISample-DataRequest`: This target is configured to perform a [MobileDriversLicenseDataRequest](mobiledriverslicensedatarequest.md).

## See Also

### Mobile document reader

- [Adopting the Verifier API in your iPhone app](adopting-the-verifier-api-in-your-iphone-app.md) — Configure and test ID Verifier support in your app for reading mobile documents.
- [Generating reader tokens for the Verifier API](generating-reader-tokens-for-the-verifier-api.md) — Configure your server to generate reader tokens to prepare a device for mobile document reading.
- [MobileDocumentReader](mobiledocumentreader.md) — An object for configuring mobile document reading on the current device.
- [MobileDocumentReaderSession](mobiledocumentreadersession.md) — The object you use to start reading a mobile document.
