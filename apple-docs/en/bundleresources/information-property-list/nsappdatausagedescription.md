---
title: NSAppDataUsageDescription
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [macOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/nsappdatausagedescription
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/nsappdatausagedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/nsappdatausagedescription.json'
content_hash: 'sha256:d4aa5b9db4ce4865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# NSAppDataUsageDescription

<sub>Property List Key</sub>

A message that tells people why the app needs to access files in other apps’ sandbox containers.

## Discussion

When your app tries to open a file that’s in another app’s sandbox container, the system requests permission from the person using the app and presents this message. If your app doesn’t have a value for the `NSAppDataUsageDescription` key in its information property list, the system presents a default message.

The system uses this message any time your app tries to access files in another app’s container, and your app can’t provide different messages for attempts to access containers from different apps.

## See Also

### Security

- [NSUpdateSecurityPolicy](nsupdatesecuritypolicy.md) — A dictionary that identifies which apps or installer packages the operating system allows to write to the app’s bundle.
- [NSAppBundlesUsageDescription](nsappbundlesusagedescription.md) — A message that tells people why the app needs to access the contents of other apps’ bundles.
- [NSUserTrackingUsageDescription](nsusertrackingusagedescription.md) — A message that informs the user why an app is requesting permission to use data for tracking the user or the device.
- [NSAppleEventsUsageDescription](nsappleeventsusagedescription.md) — A message that tells people why the app is requesting the ability to send Apple events.
- [NSSystemAdministrationUsageDescription](nssystemadministrationusagedescription.md) — A message in macOS that tells people why the app is requesting to manipulate the system configuration.
- [ITSAppUsesNonExemptEncryption](itsappusesnonexemptencryption.md) — A Boolean value indicating whether the app uses encryption.
- [ITSEncryptionExportComplianceCode](itsencryptionexportcompliancecode.md) — The export compliance code provided by App Store Connect for apps that require it.
