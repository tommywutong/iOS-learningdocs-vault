---
title: Bundle Resources updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/bundleresources
source_url: 'https://developer.apple.com/documentation/updates/bundleresources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/bundleresources.json'
content_hash: 'sha256:e2135783d4221fe4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# Bundle Resources updates

<sub>Article</sub>

Learn about important changes to Bundle Resources.

## Overview

Browse notable changes in [Bundle Resources](../bundleresources.md).

## June 2026

### New entitlements

- Access Private Cloud Compute in your [Foundation Models](../foundationmodels.md) app using the [com.apple.developer.private-cloud-compute](../bundleresources/entitlements/com.apple.developer.private-cloud-compute.md) entitlement.
- Request insights relating to transactional activities using the [Trust Insights](../trustinsights.md) framework with the [Trust Insights](../bundleresources/entitlements/com.apple.developer.trustinsights.base.md) entitlement.
- Display energy device names and usage statistics in the Home app using the [EnergyKit](../energykit.md) framework with the [EnergyKit LoadEvents Entitlement](../bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience.md) entitlement.
- Add suggested actions to your messaging app based on message content with the [Suggested Actions](../bundleresources/entitlements/com.apple.developer.suggested-actions.md) entitlement and the [Suggested Actions](../suggestedactions.md) framework.
- Integrate a third-party media sharing protocol into the system route picker with the [com.apple.developer.media-device-extension](../bundleresources/entitlements/com.apple.developer.media-device-extension.md) entitlement.
- Manage access to connected USB devices for macOS and Linux virtual machines with the [Accessory Access](../bundleresources/entitlements/com.apple.developer.accessory-access.usb.md) entitlement.
- Protect your app against use-after-free vulnerabilities with guard objects, which the system enables automatically when you set [com.apple.security.hardened-process.enhanced-security-version](../bundleresources/entitlements/com.apple.security.hardened-process.enhanced-security-version.md) to version `2` or greater. To turn off guard objects if they impact performance, use the [com.apple.security.hardened-process.no-guard-objects](../bundleresources/entitlements/com.apple.security.hardened-process.no-guard-objects.md) entitlement.

### New information property list keys

- Declare the media device extension protocols your app supports with [MDESupportedProtocols](../bundleresources/information-property-list/mdesupportedprotocols.md).
- Indicate that your app supports URL-based playback through a media device extension with [MDESupportsUniversalURLPlayback](../bundleresources/information-property-list/mdesupportsuniversalurlplayback.md).
- Control whether only one view’s gesture recognizers can be active at a time with [NSViewGestureRecognizerIsExclusive](../bundleresources/information-property-list/nsviewgesturerecognizerisexclusive.md).
- Declare that your app handles touch input natively, without relying on AppKit’s extra mouse emulation, with [NSIsTouchNative](../bundleresources/information-property-list/nsistouchnative.md).
- Suppress keyboard shortcuts for menu items while any non-exclusive gesture recognizer is active with [NSGestureRecognizerSuppressesMainMenuActions](../bundleresources/information-property-list/nsgesturerecognizersuppressesmainmenuactions.md).

### Updated entitlements

- Define the app category to enable Cellular Network Slicing with [5G Network Slicing App Category](../bundleresources/entitlements/com.apple.developer.networking.slicing.appcategory.md). To set the application category for web browser apps, use `browser-9003`. You can also set the category to `mc-9500` for mission-critical apps that need access to ultra-constrained cellular networks.
- Define the app category for carrier-constrained satellite network access with [com.apple.developer.networking.carrier-constrained.appcategory](../bundleresources/entitlements/com.apple.developer.networking.carrier-constrained.appcategory.md). To set the application category for payment apps, use `payment-8015`. You can also set the category to `health-fitness-8014` for health and fitness apps.

## June 2025

### New entitlements

- Include passthrough in screen capture on visionOS with the  [Passthrough in screen capture](../bundleresources/entitlements/com.apple.developer.screen-capture.include-passthrough.md) entitlement.
- Enable low-latency wireless networking for streaming game content on visionOS with the  [Low-Latency Streaming](../bundleresources/entitlements/com.apple.developer.low-latency-streaming.md) entitlement.
- Manage home device electricity usage with the [EnergyKit Entitlement](../bundleresources/entitlements/com.apple.developer.energykit.md) entitlement.
- Access the GPU from a background task with the [Background GPU Access](../bundleresources/entitlements/com.apple.developer.background-tasks.continued-processing.gpu.md) entitlement.
- Opt in to additional security checks with the [com.apple.security.hardened-process](../bundleresources/entitlements/com.apple.security.hardened-process.md) entitlement.
- Enable security hardening protections with the [com.apple.security.hardened-process.enhanced-security-version](../bundleresources/entitlements/com.apple.security.hardened-process.enhanced-security-version.md) entitlement.
- Mark memory the system uses for internal platform state as read only with the [com.apple.security.hardened-process.dyld-ro](../bundleresources/entitlements/com.apple.security.hardened-process.dyld-ro.md) entitlement.
- Protect memory you use for pointers by opting in to type-aware memory allocation with the [com.apple.security.hardened-process.hardened-heap](../bundleresources/entitlements/com.apple.security.hardened-process.hardened-heap.md) entitlement.
- Opt in to additional platform restrictions with the [com.apple.security.hardened-process.platform-restrictions](../bundleresources/entitlements/com.apple.security.hardened-process.platform-restrictions.md) entitlement.
- Access subscribable or publishable Wi-Fi Aware services with the [com.apple.developer.wifi-aware](../bundleresources/entitlements/com.apple.developer.wifi-aware.md) entitlement.
- Indicate that your app is optimized for a carrier-constrained network with the [com.apple.developer.networking.carrier-constrained.app-optimized](../bundleresources/entitlements/com.apple.developer.networking.carrier-constrained.app-optimized.md) entitlement.
- Define the category in which your app accesses a carrier-constrained network with the [com.apple.developer.networking.carrier-constrained.appcategory](../bundleresources/entitlements/com.apple.developer.networking.carrier-constrained.appcategory.md) entitlement.
- Report the types of identity documents your app provides with the [Digital Credentials API - Mobile Document Provider](../bundleresources/entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types.md) entitlement.
- Indicate that your app can be the default dialer app on someone’s device with the [Default Dialer App](../bundleresources/entitlements/com.apple.developer.dialing-app.md) entitlement.
- Obtain wireless service predictions with the [Wireless Insights Service Predictions](../bundleresources/entitlements/com.apple.developer.wireless-insights.service-predictions.md) entitlement.
- Indicate that your app can be the default carrier messaging app on someone’s device with the [Default Carrier Messaging App](../bundleresources/entitlements/com.apple.developer.carrier-messaging-app.md) entitlement.
- Access the camera region in your visionOS app with the [Camera Region access](../bundleresources/entitlements/com.apple.developer.arkit.camera-region.allow.md) entitlement.
- Share a coordinate space with other devices with the [Shared Coordinate Space access](../bundleresources/entitlements/com.apple.developer.arkit.shared-coordinate-space.allow.md) entitlement.
- Stop the system from capturing your app’s content with the [App-Protected Content](../bundleresources/entitlements/com.apple.developer.protected-content.md) entitlement.
- Lock your app’s windows in place relative to a person with the [Window Follow Mode](../bundleresources/entitlements/com.apple.developer.window-body-follow.md) entitlement.
- Indicate that your app can be the default dialer app on someone’s device with the [Default Dialer App](../bundleresources/entitlements/com.apple.developer.dialing-app.md) entitlement.

### New information property list keys

- Describe why your app tracks an accessory’s position and location with [NSAccessoryTrackingUsageDescription](../bundleresources/information-property-list/nsaccessorytrackingusagedescription.md).
- Indicate that the system should automatically download your asset packs and keep them up to date with [BAHasManagedAssetPacks](../bundleresources/information-property-list/bahasmanagedassetpacks.md).
- Use Apple’s service to host your asset packs with [BAUsesAppleHosting](../bundleresources/information-property-list/bausesapplehosting.md).
- Identify the app group that your app and extension use to share asset packs with [BAAppGroupID](../bundleresources/information-property-list/baappgroupid.md).
- Describe Wi-Fi Aware services your app publishes and subscribes to with [WiFiAwareServices](../bundleresources/information-property-list/wifiawareservices.md).
- Indicate that your app supports game mode with [LSSupportsGameMode](../bundleresources/information-property-list/lssupportsgamemode.md).

### Updated entitlements

- Add the [com.apple.developer.kernel.increased-memory-limit](../bundleresources/entitlements/com.apple.developer.kernel.increased-memory-limit.md) entitlement to your visionOS app.

### Updated information property list keys

- Indicate that your visionOS app supports spatial gamepads with [GCSupportedGameControllers](../bundleresources/information-property-list/gcsupportedgamecontrollers.md).

## June 2024

### New entitlements

- Enable access to a Personalized Sound Profile to allow the app to use the information in the profile to render audio with [com.apple.developer.spatial-audio.profile-access](../bundleresources/entitlements/com.apple.developer.spatial-audio.profile-access.md).
- Enable access to head tracking info to allow an app to render audio with head tracking with [com.apple.developer.coremotion.head-pose](../bundleresources/entitlements/com.apple.developer.coremotion.head-pose.md).
- Allow CoreMIDI to match MIDIDriverKit drivers with devices that support MIDI with [com.apple.developer.driverkit.family.midi](../bundleresources/entitlements/com.apple.developer.driverkit.family.midi.md).

### Updated entitlement

- Define the app category to enable Cellular Network Slicing with [5G Network Slicing App Category](../bundleresources/entitlements/com.apple.developer.networking.slicing.appcategory.md). To set the application category for streaming apps, use `streaming-9001`. You can also set the category to `gaming-6014` for gaming apps, and `communication-9000` for communication apps.

### New Info.plist keys

- Indicate if the game app bypasses system spatial audio with [AVGameBypassSystemSpatialAudio](../bundleresources/information-property-list/avgamebypasssystemspatialaudio.md).
- Indicate to the system that your app receives copies of re-engagement postbacks, a type of postback introduced in iOS 17.5, with [EligibleForAdAttributionKitReengagementPostbackCopies](../bundleresources/information-property-list/eligibleforadattributionkitreengagementpostbackcopies.md).
- Indicate to the system that your app supports the Music Haptics feature with [MusicHapticsSupported](../bundleresources/information-property-list/musichapticssupported.md).
- Indicate to the system the interfaces AccessorySetupKit uses to discover and configure accessories using Bluetooth or Wi-Fi with [NSAccessorySetupSupports](../bundleresources/information-property-list/nsaccessorysetupsupports.md).
- Provide the company identifier for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with [NSAccessorySetupBluetoothCompanyIdentifiers](../bundleresources/information-property-list/nsaccessorysetupbluetoothcompanyidentifiers.md).
- Provide the name for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with [NSAccessorySetupBluetoothNames](../bundleresources/information-property-list/nsaccessorysetupbluetoothnames.md).
- Provide the services for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with [NSAccessorySetupBluetoothServices](../bundleresources/information-property-list/nsaccessorysetupbluetoothservices.md).
- Provide a message that tells the user why the app requests access to financial data stored in Wallet with [NSFinancialDataUsageDescription](../bundleresources/information-property-list/nsfinancialdatausagedescription.md).
- Track “finished” consumable in-app purchases in StoreKit and return the transactions when iterating the `Transaction` APIs with [SKIncludeConsumableInAppPurchaseHistory](../bundleresources/information-property-list/skincludeconsumableinapppurchasehistory.md).

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md) — Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
