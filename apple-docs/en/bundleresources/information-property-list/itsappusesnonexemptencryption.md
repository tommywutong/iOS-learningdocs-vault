---
title: ITSAppUsesNonExemptEncryption
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/itsappusesnonexemptencryption
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption.json'
content_hash: 'sha256:1b14d133693fd875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# ITSAppUsesNonExemptEncryption

<sub>Property List Key</sub>

A Boolean value indicating whether the app uses encryption.

## Discussion

Set the value for this key to `NO` in your app’s [Information Property List](../information-property-list.md) file to indicate that your app—including any third-party libraries you link against—either uses no encryption, or only uses encryption that’s exempt from export compliance requirements, as described in [Overview of export compliance](https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance/). Set the value to `YES` to indicate that your app uses non-exempt encryption.

If you set the value to `YES`, you typically also provide a value for the [ITSEncryptionExportComplianceCode](itsencryptionexportcompliancecode.md) key. You set that key’s value using a code Apple provides after successfully reviewing your export compliance documentation.

If you don’t have the [ITSAppUsesNonExemptEncryption](itsappusesnonexemptencryption.md) key in your app’s `Info.plist` file, App Store Connect walks you through an export compliance questionnaire every time you upload a new version of your app. Including the key streamlines the app submission process.

For additional information, see [Complying with Encryption Export Regulations](../../security/complying-with-encryption-export-regulations.md).

## See Also

### Security

- [NSUpdateSecurityPolicy](nsupdatesecuritypolicy.md) — A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppBundlesUsageDescription](nsappbundlesusagedescription.md) — A message that tells people why the app needs to access the contents of other apps’ bundles.
- [NSAppDataUsageDescription](nsappdatausagedescription.md) — A message that tells people why the app needs to access files in other apps’ sandbox containers.
- [NSUserTrackingUsageDescription](nsusertrackingusagedescription.md) — A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
- [NSAppleEventsUsageDescription](nsappleeventsusagedescription.md) — A message that tells people why the app is requesting the ability to send Apple events.
- [NSSystemAdministrationUsageDescription](nssystemadministrationusagedescription.md) — A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSEncryptionExportComplianceCode](itsencryptionexportcompliancecode.md) — The export compliance code provided by App Store Connect for apps that require it.
