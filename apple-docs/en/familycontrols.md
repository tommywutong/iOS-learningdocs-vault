---
title: Family Controls
framework: Family Controls
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/familycontrols
source_url: 'https://developer.apple.com/documentation/familycontrols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/familycontrols.json'
content_hash: 'sha256:5e41f6f5064e45ec'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Family Controls

<sub>Framework</sub>

Authorize your app to provide parental controls on a device.

## Overview

To authorize your parental controls app, use a shared [AuthorizationCenter](familycontrols/authorizationcenter.md) instance. You can authorize parental controls on any device.

![A figure labeled allow activity. It shows an arrow from a Family Sharing logo](../../attachments/e21e1d0eba4c9be965970c6eb2fabd82/family-controls-overview@2x.png)

> [!important] Important
> You must add the Family Controls capability to your app before you call the [requestAuthorization(for:)](<familycontrols/authorizationcenter/requestauthorization(for_).md>) or [revokeAuthorization(completionHandler:)](<familycontrols/authorizationcenter/revokeauthorization(completionhandler_).md>) methods. This capability adds the [Family Controls](bundleresources/entitlements/com.apple.developer.family-controls.md) entitlement to your app. Before submitting your app to the App Store, you must [request permission](https://developer.apple.com/contact/request/family-controls-distribution) to use the entitlement. For more information, see [Adding capabilities to your app](xcode/adding-capabilities-to-your-app.md).

Authorizing parental controls for a child requires approval from a parent or guardian in the same Family Sharing group. The system displays an authentication sheet on the child’s device, and the parent or guardian approves or denies the authorization request. The system sends the result to your app’s `AuthorizationCenter`.

Authorizing parental controls for an individual requires approval from the owner of the device. The system displays a biometric authentication alert on the individual’s device after the individual approves or denies the authorization request. The system sends the result to your app’s `AuthorizationCenter`.

The Family Controls framework prevents child users, authorized by a parent or guardian, from performing actions that might circumvent the parental controls settings. For example, authorizing an app prevents the child user from deleting the app that provides parental controls. In addition, while a device has at least one app authorized for parental controls by a parent or guardian, the user can’t sign out of iCloud.

In a compatible iPad or iPhone app running in visionOS, authorization attempts always fail.

## Topics

### Authorizations

- [AuthorizationCenter](familycontrols/authorizationcenter.md) — The center for requesting authorization to provide parental controls.
- [AuthorizationStatus](familycontrols/authorizationstatus.md) — The status of your app’s authorization to provide parental controls.
- [Family Controls](bundleresources/entitlements/com.apple.developer.family-controls.md) — A Boolean value that indicates whether the app can request or revoke authorization to provide parental controls.
- [Requesting the Family Controls entitlement](familycontrols/requesting-the-family-controls-entitlement.md) — Register your app and its Screen Time API app extensions to use Family Controls.

### Account types

- [FamilyControlsMember](familycontrols/familycontrolsmember.md) — The type of account that Family Controls is currently managing.

### Activity selections

- [FamilyActivityPicker](familycontrols/familyactivitypicker.md) — A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [FamilyActivitySelection](familycontrols/familyactivityselection.md) — A collection of applications, categories, and web domains selected by the user.

### Activity labels

- [Displaying Activity Labels](familycontrols/displayingactivitylabels.md) — Provide users with a read-only, visual representation of an application, category, or web domain.

### Activity data

- [FamilyActivityData](familycontrols/familyactivitydata.md) — An interface to a person’s family activity data.

### Errors

- [FamilyControlsError](familycontrols/familycontrolserror.md) — Errors the Family Controls framework reports.
