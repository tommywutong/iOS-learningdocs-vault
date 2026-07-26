---
title: EnergyKit updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/energykit
source_url: 'https://developer.apple.com/documentation/updates/energykit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/energykit.json'
content_hash: 'sha256:f38ea14517a87818'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# EnergyKit updates

<sub>Article</sub>

Learn about important changes to EnergyKit.

## Overview

Browse notable changes in [EnergyKit](../energykit.md).

## June 2026

### Electric vehicle charging behavior

- Track and explain electric vehicle charging behavior with [ElectricVehicleStatusEvent](../energykit/electricvehiclestatusevent.md), which provides discrete snapshots that capture why a vehicle isn’t charging when connected, when charging will begin, and why charging started or stopped.
- Use `ElectricVehicleChargingReason` to explain charging state transitions. The framework provides `ActiveReason` for reasons why charging starts or resumes, and `IdleReason` for reasons why the vehicle remains idle when connected to a charger.
- Define charging targets with [ElectricVehicleStatusEvent.ChargingTarget](../energykit/electricvehiclestatusevent/chargingtarget-swift.struct.md) to show when charging begins and when it will complete, including the target charge, scheduled start time, and estimated completion time.

### Device identification

- Identify electrical load devices with type safety using [ElectricalLoadDevice](../energykit/electricalloaddevice.md).
- Access device names through the [deviceName](../energykit/electricvehicleloadevent/devicename.md) property for electric vehicles, and the [deviceName](../energykit/electrichvacloadevent/devicename.md) property for HVAC devices.

### Performance metrics

- Estimate driving range and battery temperature to give more context about a charging session using [ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics](../energykit/electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct.md).

### Home app integration

- Display your app’s energy data in the Home app by adopting the [EnergyKit LoadEvents Entitlement](../bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience.md). The Home app automatically shows activity logs, historical charts, trend notifications, and whole-home energy usage based on your submitted events.

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
