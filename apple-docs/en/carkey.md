---
title: CarKey
framework: CarKey
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/carkey
source_url: 'https://developer.apple.com/documentation/carkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/carkey.json'
content_hash: 'sha256:03fc8d3d3acfcda6'
translated: false
---

> Navigation: [Technologies](technologies.md)

# CarKey

<sub>Framework</sub>

Access the remote keyless features of configured vehicles in the Wallet app.

## Overview

The CarKey framework offers a way to communicate with vehicles already provisioned to someone’s Apple Wallet. Car manufacturers adopt this framework in the apps they use to support and control their vehicles. For example, your app might use it to lock or unlock the vehicle, or open a power sunroof. To control a vehicle remotely, you need the following information for that vehicle:

- The function identifiers for each of your vehicle’s features.
- The action identifiers for each action you can perform on a feature.
- The execution status the vehicle can return in response to an action.

The Wallet app maintains a list of vehicles that match your company’s make, and that the user previously configured for remote access. Create a session object to get information about those vehicles and to establish a connection to ones that are in range. Use the session to retrieve the list of commands available to the current person, and to initiate actions from your app.

> [!note] Note
> Your app must have the `com.apple.developer.carkey.session` entitlement to use this framework. To request the entitlement, you must be an automaker enrolled in the MFi Program. For details, see [https://developer.apple.com/mfi/](https://developer.apple.com/mfi/).

## Topics

### Setup

- [CarKeyRemoteControl](carkey/carkeyremotecontrol.md) — The object you use to start a new vehicle-related session.
- [CarKeyRemoteControlSession](carkey/carkeyremotecontrolsession.md) — The object that manages communication with the vehicles you manufacture.
- [CarKeyRemoteControlSessionDelegate](carkey/carkeyremotecontrolsessiondelegate.md) — An interface you use to receive session- and vehicle-related information from the system.
- [VehicleReport](carkey/vehiclereport.md) — A type that contains information about a vehicle configured for remote keyless entry in the user’s Apple Wallet.

### Vehicle Actions

- [RemoteKeylessEntryAction](carkey/remotekeylessentryaction.md) — An automatically ending action that you want to perform on a vehicle.
- [RemoteKeylessEntryEnduringAction](carkey/remotekeylessentryenduringaction.md) — An action with an optional stopping point that you want to perform on a vehicle. _(deprecated)_
- [FunctionIdentifier](carkey/functionidentifier.md) — A type that stores the designation code for one of your vehicle’s features.
- [ActionIdentifier](carkey/actionidentifier.md) — A type that stores the designation code for one of the actions that a vehicle feature supports.

### Error Codes

- [CarKeyErrorCode](carkey/carkeyerrorcode.md) — The errors that can occur when you perform remote-keyless entry operations on a vehicle.

### Structures

- [ExecutionStatus](carkey/executionstatus.md) — A type that contains the status code a vehicle returns after executing an action.
- [RemoteKeylessEntryConfigurableEnduringAction](carkey/remotekeylessentryconfigurableenduringaction.md) — An action with an optional stopping point that you want to perform on a vehicle.
