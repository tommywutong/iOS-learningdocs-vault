---
title: Exposure Notification
framework: Exposure Notification
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 13.5+, iPadOS 13.5+, Mac Catalyst 13.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/exposurenotification
source_url: 'https://developer.apple.com/documentation/exposurenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/exposurenotification.json'
content_hash: 'sha256:89fec5b1526e460f'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Exposure Notification

<sub>Framework</sub>

Implement a COVID-19 exposure notification system that protects user privacy.

## Overview

Use the Exposure Notification framework to inform people of potential exposure to COVID-19, the disease caused by the SARS-CoV-2 virus. You can build a notification system that employs random, rotating keys and identifiers to convey positive diagnoses in addition to data such as associated symptoms, proximity, and duration.

### Establish User Roles

The ExposureNotification framework defines two user roles:

- **Affected user** — When a user has a confirmed or probable diagnosis of COVID-19 (as defined by the Health Authority), the framework identifies them as _affected_ and shares their diagnosis keys to alert other users to potential exposure.
- **Potentially exposed user** — To assign a user the _potentially exposed_ role, use the framework to determine whether a set of temporary exposure keys indicate proximity to an affected user. If so, the app can retrieve additional information such as date and duration from the framework.

> [!important] Important
> Before you can develop an app that uses ExposureNotification, you need the [com.apple.developer.exposure-notification](bundleresources/entitlements/com.apple.developer.exposure-notification.md) entitlement. For more information on this entitlement, see [Exposure Notification APIs Addendum](https://developer.apple.com/contact/request/download/Exposure_Notification_Addendum.pdf). To get permission to use this entitlement, see [Exposure Notification Entitlement Request](https://developer.apple.com/contact/request/exposure-notification-entitlement).

### Identify Your App’s Region

All EN apps must specify the region for which they work by adding a key called [ENDeveloperRegion](bundleresources/information-property-list/endeveloperregion.md) to the app’s `Info.plist` file. The value for `ENDeveloperRegion` is set to a string that represents the app’s region. This value can be an ISO 3166-1 country code (for example, “CA” for Canada), or the ISO 3166-1/3166-2 country code plus subdivision code (“US-CA” for California).

Explicitly set the associated domain link to your region code. Avoid using wildcards because they can impact system operations. See [Associated Domains Entitlement](bundleresources/entitlements/com.apple.developer.associated-domains.md) for more information.

### Specify Exposure Notification API Version

iOS 13.7 introduces a new method of calculating the user’s Exposure Risk Value, described in [ENExposureConfiguration](exposurenotification/enexposureconfiguration.md). Apps can implement this new method, or continue to use the calculation method introduced in earlier versions of iOS. To choose your app’s approach, add an entry to your app’s `Info.plist` file with a key of [ENAPIVersion](bundleresources/information-property-list/enapiversion.md). To use the new approach, specify a value of `2`. To use the original approach, specify a value of `1`.

### Support Exposure Notification Express

Starting with iOS 13.7, Health Authorities can inform users of potential exposure to COVID-19 without a dedicated Exposure Notification app. This feature is called Exposure Notification Express and must be enabled by a Health Authority. For more information, see [Supporting Exposure Notifications Express](exposurenotification/supporting-exposure-notifications-express.md).

## Topics

### Essentials

- [Supporting Exposure Notifications Express](exposurenotification/supporting-exposure-notifications-express.md) — Configure servers to notify users of potential exposures to COVID-19 without an app.
- [Building an App to Notify Users of COVID-19 Exposure](exposurenotification/building-an-app-to-notify-users-of-covid-19-exposure.md) — Inform people when they may have been exposed to COVID-19.
- [Setting Up a Key Server](exposurenotification/setting-up-a-key-server.md) — Ensure that your server meets the requirements for supporting Exposure Notifications.
- [ENManager](exposurenotification/enmanager.md) — A class that manages exposure notifications. _(deprecated)_
- [ENDeveloperRegion](bundleresources/information-property-list/endeveloperregion.md) — A string that specifies the region that the app supports.
- [ENAPIVersion](bundleresources/information-property-list/enapiversion.md) — A number that specifies the version of the API to use.
- [Changing Configuration Values Using the Server‑to‑Server API](exposurenotification/changing-configuration-values-using-the-server-to-server-api.md) — Update Exposure Notifications configuration values from a Public Health Authority’s server.
- [Testing Exposure Notifications Apps in iOS 13.7 and Later](exposurenotification/testing-exposure-notifications-apps-in-ios-13-7-and-later.md) — Perform end-to-end validation of Exposure Notifications apps on a device by manually loading configuration files.
- [Supporting Exposure Notifications in iOS 12.5](exposurenotification/supporting-exposure-notifications-in-ios-12-5.md) — Prepare your Exposure Notifications app to run on a previous version of iOS.

### Exposures

- [Configuring Exposure Notifications](exposurenotification/configuring-exposure-notifications.md) — Define how Exposure Notifications work for a region by assigning server-based key-value pairs.
- [ENExposureConfiguration](exposurenotification/enexposureconfiguration.md) — The object that contains parameters for configuring exposure notification risk scoring behavior. _(deprecated)_
- [ENExposureWindow](exposurenotification/enexposurewindow.md) — A set of scan events from observed beacons within a time span. _(deprecated)_
- [ENScanInstance](exposurenotification/enscaninstance.md) — The aggregation of attenuations of beacons received during a scan. _(deprecated)_
- [Exposure Parameter Limits](exposurenotification/exposure-parameter-limits.md) — The limits for the parameters you use in exposure risk calculations.

### Summaries

- [ENExposureDetectionSummary](exposurenotification/enexposuredetectionsummary.md) — A summary of exposures. _(deprecated)_
- [ENExposureDaySummary](exposurenotification/enexposuredaysummary.md) — The summary of exposure information for a single day. _(deprecated)_
- [ENExposureSummaryItem](exposurenotification/enexposuresummaryitem.md) — The summary of exposures for a specific time period or report type. _(deprecated)_

### Status

- [ENAuthorizationStatus](exposurenotification/enauthorizationstatus.md) — A set of cases that indicates the authorization status for the app. _(deprecated)_
- [ENStatus](exposurenotification/enstatus.md) — A set of cases that represents the overall status of exposure notification on the system. _(deprecated)_

### Errors

- [ENError](exposurenotification/enerror.md) — Errors that the exposure notification framework issues. _(deprecated)_
- [Code](exposurenotification/enerror/code.md) — Error codes that the exposure notification framework issues. _(deprecated)_
- [ENErrorDomain](exposurenotification/enerrordomain.md) — The domain for an error. _(deprecated)_
- [ENErrorHandler](exposurenotification/enerrorhandler.md) — The handler for error conditions. _(deprecated)_

### Variables

- [ENRiskWeightDefaultV2](exposurenotification/enriskweightdefaultv2.md) — This weight is not used. _(deprecated)_
- [ENRiskWeightMaxV2](exposurenotification/enriskweightmaxv2.md) — This weight is not used. _(deprecated)_
- [EN_FEATURE_GENERAL](exposurenotification/en_feature_general.md)

### Type Aliases

- [ENDetectExposuresHandler](exposurenotification/endetectexposureshandler.md) — The definition of a handler that returns exposure summaries. _(deprecated)_
- [ENErrorOutType](exposurenotification/enerrorouttype.md) — Type for returning NSError’s from functions. Avoids long and repetitious method signatures. _(deprecated)_
- [ENGetDiagnosisKeysHandler](exposurenotification/engetdiagnosiskeyshandler.md) — The definition of a handler that returns diagnosis keys. _(deprecated)_
- [ENGetExposureInfoHandler](exposurenotification/engetexposureinfohandler.md) — The definition of a handler that receives exposure info. _(deprecated)_
