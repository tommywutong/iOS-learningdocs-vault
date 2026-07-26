---
title: WirelessInsights
framework: WirelessInsights
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/wirelessinsights
source_url: 'https://developer.apple.com/documentation/wirelessinsights'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/wirelessinsights.json'
content_hash: 'sha256:c5c0e2937db224ab'
translated: false
---

> Navigation: [Technologies](technologies.md)

# WirelessInsights

<sub>Framework</sub>

Receive notifications for anticipated changes in cellular data service conditions.

## Overview

The WirelessInsights framework notifies your app about network conditions that might affect its ability to use data. The framework collects metrics on the device about cellular conditions, such as whether the device is in service, current cellular congestion, and more. With this information, you can improve someone’s experience using your app.

When your app receives a notification about a potential degradation of cellular service, you can adapt to the problem in a number of ways:

- Prefetch and buffer data prior to the event.
- Reduce your bit rate.
- Defer activity to a time when cellular conditions are better.
- Build in additional retries.

The app receives an asynchronous sequence of [ServicePrediction](wirelessinsights/serviceprediction.md) instances, which describe anticipated events in terms of their impact and expected timing. The prediction includes metrics indicating the level of confidence in each factor of the prediction.

Your app can take action appropriate to its use of cellular data; for example:

- A streaming media app might react to a prediction of a lengthy, high-impact event by buffering media in advance of the event. Or, the app might proactively reduce its bit rate.
- An app that performs one-time downloads of large files might defer a download until after an event passes.

> [!important] Important
> While the WirelessInsights framework exists in apps built with Mac Catalyst, it doesn’t have any functionality. Instead, iterating over the [servicePredictions](wirelessinsights/servicepredictionprovider/servicepredictions.md) sequence throws a [ServicePredictionError.unsupportedDevice](wirelessinsights/servicepredictionerror/unsupporteddevice.md) error. This behavior also occurs in iOS apps running in visionOS or in macOS on Apple silicon. On iPad, the framework may provide predictions on a cellular iPad device, but not on Wi-Fi-only devices. Anticipate this error in your app and handle it gracefully on unsupported devices.

## Topics

### Essentials

- [ServicePredictionProvider](wirelessinsights/servicepredictionprovider.md) — A class that provices cellular service predictions about upcoming events and anomalies.
- [Wireless Insights Service Predictions](bundleresources/entitlements/com.apple.developer.wireless-insights.service-predictions.md) — A Boolean value that indicates whether the app can use the WirelessInsights framework to obtain wireless service predictions.
