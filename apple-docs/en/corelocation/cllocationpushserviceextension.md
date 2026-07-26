---
title: CLLocationPushServiceExtension
framework: Core Location
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceextension
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceextension.json'
content_hash: 'sha256:b06dc7af9d144ad0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationPushServiceExtension

<sub>Protocol</sub>

The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
protocol CLLocationPushServiceExtension : NSObjectProtocol
```

## Overview

A type that adopts the [CLLocationPushServiceExtension](cllocationpushserviceextension.md) protocol acts as the entry point to a Location Push Service Extension. You use this type to respond to incoming location push notifications and perform app-specific tasks. For example, you use it to get someone’s current location and send it to your server.

Don’t adopt this protocol in your own custom types. Instead, add a Location Push Service Extension target to your project and modify the type that Xcode provides. To start the delivery of location push notifications, call the [- startMonitoringLocationPushesWithCompletion:](<cllocationmanager/startmonitoringlocationpushes(completion_).md>) method to request a unique token from the device. Send that token to your server and use it to generate HTTP requests for APNs to deliver to the device.

When the device receives a location push notification that your server generated, the system loads your app extension and calls its [- didReceiveLocationPushPayload:completion:](<cllocationpushserviceextension/didreceivelocationpushpayload(__completion_).md>) method. Use that method to configure a [CLLocationManager](cllocationmanager.md) object and request the person’s current location. Collect the location, encrypt it, and send it back to your server using a custom connection.

> [!important] Important
> In order for your app extension to receive push notifications, the app that contains the app extension must have Always authorization for location services. For information about how to request this access, see [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md).

Location Push Service Extensions aren’t supported in visionOS. If a compatible iPad or iPhone app contains an app extension of this type, the system doesn’t load it.

For more information about adding the extension to your app, see [Creating a location push service extension](creating-a-location-push-service-extension.md). For information about how to generate push notifications from your server, see [Setting up a remote notification server](../usernotifications/setting-up-a-remote-notification-server.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the push notification payload

- [- didReceiveLocationPushPayload:completion:](<cllocationpushserviceextension/didreceivelocationpushpayload(__completion_).md>) — Delivers a location push notification for your app extension to process.

### Handling the extension termination

- [- serviceExtensionWillTerminate](<cllocationpushserviceextension/serviceextensionwillterminate().md>) — Notifies your app extension that the system is about to terminate the extension because it’s taking too long to complete its task.

## See Also

### Location push service extension

- [Location Push Service Extension](../bundleresources/entitlements/com.apple.developer.location.push.md) — An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [CLLocationPushServiceError](cllocationpushserviceerror-swift.struct.md) — Error codes the location manager returns if starting to monitor for location push notifications fails.
- [CLLocationPushServiceErrorDomain](cllocationpushserviceerrordomain.md) — The domain for Location Push Service Extension errors.
- [Code](cllocationpushserviceerror-swift.struct/code.md) — Error codes the location manager returns if starting to monitor for location push notifications fails.
