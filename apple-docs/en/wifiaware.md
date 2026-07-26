---
title: Wi-Fi Aware
framework: Wi-Fi Aware
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/wifiaware
source_url: 'https://developer.apple.com/documentation/wifiaware'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/wifiaware.json'
content_hash: 'sha256:3f59cfb19cdb671f'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Wi-Fi Aware

<sub>Framework</sub>

Securely pair and connect to external devices over peer-to-peer Wi-Fi.

## Overview

Wi-Fi Aware™ (also known as Neighbor Awareness Networking or NAN) is a Wi-Fi Alliance™ standard specification that enables devices to securely discover, pair, and communicate with nearby devices without an internet connection or access point. Your app can use the Wi-Fi Aware framework to connect with Wi-Fi Aware certified accessories. The framework offers a secure and standardized way to establish peer-to-peer (P2P) connections between Wi-Fi devices, providing networking capabilities such as:

- High-bandwidth and low-latency data transfers
- Connections to paired devices that are authenticated and encrypted at the Wi-Fi layer
- Simultaneous connections to multiple Wi-Fi Aware devices
- Simultaneous use of Wi-Fi Aware devices and a Wi-Fi infrastructure network
- Fully peer-to-peer topology, allowing peers to come and go without breaking connections to other peers

The Wi-Fi Aware technology works without the need for Wi-Fi infrastructure networks, cellular links, internet connections, or cloud servers. Your app can pair Wi-Fi Aware devices using [AccessorySetupKit](https://developer.apple.com/documentation/accessorysetupkit/) or [DeviceDiscoveryUI](https://developer.apple.com/documentation/devicediscoveryui). When paired, your app can create secure, authenticated, and encrypted peer-to-peer connections between paired devices on-demand, using the Wi-Fi Aware and [Network](https://developer.apple.com/documentation/Network) frameworks.

Your app may connect to paired Wi-Fi Aware devices whenever it’s running, in both foreground and background states. Your app may get runtime using any of the existing mechanisms on the platform, such as with the [BackgroundTasks](https://developer.apple.com/documentation/backgroundtasks) API.

If you are building a hardware device or accessory that uses Wi-Fi Aware, refer to the Wi-Fi Aware chapter of the [Accessory Guide](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf) for the requirements to work well with Apple devices.

> [!important] Important
> The following Apple devices support the Wi-Fi Aware framework:
>
> - iPhone 12 and later
> - iPad (10th generation) and later
> - iPad Air (4th generation) and later
> - iPad Pro 11-inch (3rd generation) and later
> - iPad Pro 12.9-inch (5th generation) and later
> - iPad mini (6th generation) and later

## Topics

### Essentials

- [Building peer-to-peer apps](wifiaware/building-peer-to-peer-apps.md) — Communicate with nearby devices over a secure, high-throughput, low-latency connection by using Wi-Fi Aware.
- [Connecting devices for peer-to-peer Wi-Fi](wifiaware/connecting-paired-devices.md) — Make outgoing and accept incoming secure connections with paired devices.
- [Adopting Wi-Fi Aware](wifiaware/adopting-wi-fi-aware.md) — Add entitlements and declare your app’s services.
- [com.apple.developer.wifi-aware](bundleresources/entitlements/com.apple.developer.wifi-aware.md) — The entitlement the system requires for an app to use the Wi-Fi Aware framework.
- [WiFiAwareServices](bundleresources/information-property-list/wifiawareservices.md) — Dictionaries of Wi-Fi Aware services that the app can publish or subscribe to.

### Host capabilities

- [WACapabilities](wifiaware/wacapabilities.md) — A structure that checks the host device’s supported features and capabilities.
- [Feature](wifiaware/wacapabilities/feature.md) — Features that your app’s current host device can support.

### Services to discover

- [WAService](wifiaware/waservice.md) — A protocol that defines a service that a device can publish or subscribe to.
- [WASubscribableService](wifiaware/wasubscribableservice.md) — A service your app discovers on remote devices and can connect to.
- [WAPublishableService](wifiaware/wapublishableservice.md) — A service, hosted by your app, that remote devices can connect to.

### Paired devices

- [WAPairedDevice](wifiaware/wapaireddevice.md) — A known Wi-Fi Aware device that your app can connect to.
- [Devices](wifiaware/wapaireddevice/devices.md) — A dictionary holding a snapshot of currently paired devices accessible and known to your app.
- [DevicesSequence](wifiaware/wapaireddevice/devicessequence.md) — A sequence that vends updates to a paired device list, as the list changes.
- [PairingInfo](wifiaware/wapaireddevice/pairinginfo-swift.struct.md) — A collection of unauthenticated information the system receives from a device before it’s paired for the first time.

### Subscriber

- [WASubscriberBrowser](wifiaware/wasubscriberbrowser.md) — The structure that configures a network browser to subscribe to a Wi-Fi Aware service and make outgoing connections to paired devices.
- [Action](wifiaware/wasubscriberbrowser/action.md) — The structure that configures the Wi-Fi Aware subscriber operation the network browser performs.
- [Devices](wifiaware/wasubscriberbrowser/devices.md) — The structure that determines the devices to connect to.

### Publisher

- [WAPublisherListener](wifiaware/wapublisherlistener.md) — Configures a network listener to publish a service over Wi-Fi Aware and accept incoming connections from paired devices.
- [Action](wifiaware/wapublisherlistener/action.md) — The structure that configures the Wi-Fi Aware publisher operation that the network listener performs.
- [Devices](wifiaware/wapublisherlistener/devices.md) — The structure that determines the devices to connect to.
- [DatapathParameters](wifiaware/wapublisherlistener/datapathparameters.md) — The parameter that sets the initial Wi-Fi Aware data path configuration for any devices that are connected.

### Parameters

- [NWParameters](network/nwparameters.md) — An object that stores the protocols to use for connections, options for sending data, and network path constraints.
- [NWParametersBuilder](network/nwparametersbuilder.md) — An opaque class that is responsible for creating and configuring NWParameters based on the parameterized protocol stack.
- [WAParameters](wifiaware/waparameters.md) — Parameters configuring a Wi-Fi Aware data path connection.

### Connections

- [WAEndpoint](wifiaware/waendpoint.md) — The endpoint of a Wi-Fi Aware connection.
- [WAConnection](wifiaware/waconnection.md) — Provides access to the Wi-Fi Aware-specific configuration and information that underlies a given `Network/NetworkConnection`.

### Security

- [WASharedSecret](wifiaware/washaredsecret.md) — A high-entropy shared secret unique to this network connection.

### Connection performance

- [NWPath](network/nwpath.md) — An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [WAPath](wifiaware/wapath.md) — A representation of the current Wi-Fi Aware path.
- [WAPerformanceMode](wifiaware/waperformancemode.md) — The performance mode that indicates what performance criterion to prioritize.
- [WAAccessCategory](wifiaware/waaccesscategory.md) — The underling quality-of-service (QoS) the Wi-Fi layer uses to transmit data packets from a connection over the air.
- [WAPerformanceReport](wifiaware/waperformancereport.md) — The current performance state of the data path.

### Errors

- [NWError](network/nwerror.md) — The errors returned by objects in the Network framework.
- [WAError](wifiaware/waerror.md) — An error in Wi-Fi Aware.

### Structures

- [WAPerformanceForecast](wifiaware/waperformanceforecast.md) — The performance forecast for a connection setup to the remote device. _(beta)_
