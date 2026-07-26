---
title: SensorKit
framework: SensorKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/sensorkit
source_url: 'https://developer.apple.com/documentation/sensorkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sensorkit.json'
content_hash: 'sha256:7d8926f18f4fda26'
translated: false
---

> Navigation: [Technologies](technologies.md)

# SensorKit

<sub>Framework</sub>

Retrieve data and derived metrics from sensors on an iPhone, or paired Apple Watch.

## Overview

As the system gathers information using various sensors on a device, SensorKit enables an app to access select raw data, or metrics that the system processes from a sensor, such as:

- Steps information
- Accelerometer or rotation-rate data
- The configuration of a watch on the user’s wrist
- Ambient light in the physical environment
- Details about a user’s routine commute or travel

See [SRSensor](sensorkit/srsensor.md) for the complete list.

> [!note] Note
> This framework ignores calls from Mac apps that you build with Mac Catalyst, and from compatible iPad and iPhone apps running in visionOS.

## Topics

### Essentials

- [SensorKit updates](updates/sensorkit.md) — Learn about important changes to SensorKit.

### Setup

- [Configuring your project for sensor reading](sensorkit/configuring-your-project-for-sensor-reading.md) — Add metadata to your app to attain system and user permission to access sensor data.
- [SRSensorReader](sensorkit/srsensorreader.md) — An object that establishes user authorization and records data for a particular sensor. _(deprecated)_

### Authorization

- [com.apple.developer.sensorkit.reader.allow](bundleresources/entitlements/com.apple.developer.sensorkit.reader.allow.md) — The necessary entitlement to access sensor data that’s required by your app’s preapproved research study.

### Querying data

- [SRFetchRequest](sensorkit/srfetchrequest.md) — An object that defines the criteria for a sample query.
- [SRFetchResult](sensorkit/srfetchresult.md) — Recorded data that a sensor reader fetches.

### Interpreting data

- [SRAmbientLightSample](sensorkit/srambientlightsample.md) — The amount of ambient light in the user’s environment.
- [SRDeviceUsageReport](sensorkit/srdeviceusagereport.md) — The frequency and relative duration that the user uses their device, particular Apple apps, or websites.
- [SRKeyboardMetrics](sensorkit/srkeyboardmetrics.md) — The configuration of a device’s keyboard and its usage patterns.
- [SRMediaEvent](sensorkit/srmediaevent.md) — A user interaction with a media object, such as an image or a video.
- [SRMessagesUsageReport](sensorkit/srmessagesusagereport.md) — An object that describes the user’s Messages app activity over a period of time.
- [SRPhoneUsageReport](sensorkit/srphoneusagereport.md) — An object that describes the user’s phone activity over a period of time.
- [SRVisit](sensorkit/srvisit.md) — The user’s progress in their daily travel routine.
- [SRWristDetection](sensorkit/srwristdetection.md) — The configuration of a watch on the wearer’s wrist.

### Deleting samples

- [SRDeletionRecord](sensorkit/srdeletionrecord.md) — An object that describes the reason the framework deletes samples.

### Analyzing speech

- [SRSpeechMetrics](sensorkit/srspeechmetrics.md) — An object that represents metrics about a range of speech.
- [SRSpeechExpression](sensorkit/srspeechexpression.md) — An object that represents the metrics and voice analytics for a range of speech.

### Analyzing faces

- [SRFaceMetrics](sensorkit/srfacemetrics.md) — An object that represents metrics about the user’s face.
- [SR_ARKIT_SUPPORTED](sensorkit/sr_arkit_supported.md) — A flag that indicates whether the ARKit framework is available in the SDK for the SensorKit framework.

### Recording wrist temperatures

- [SRWristTemperatureSession](sensorkit/srwristtemperaturesession.md) — An object that represents wrist temperatures that a device records during a period of time.
- [SRWristTemperature](sensorkit/srwristtemperature.md) — The temperature of the user’s wrist while the user sleeps.

### Recording ectrocardiogram data

- [SRElectrocardiogramSample](sensorkit/srelectrocardiogramsample.md) — The sample electrocardiogram sensor data.

### Recording photoplethysmogram data

- [SRPhotoplethysmogramSample](sensorkit/srphotoplethysmogramsample.md) — The sample photoplethysmogram (PPG) sensor data.

### Classes

- [SRAcousticSettings](sensorkit/sracousticsettings.md)
- [SRHeadphoneSettings](sensorkit/srheadphonesettings.md) _(beta)_
- [SRReader](sensorkit/srreader.md) — `SRReader` serves as the primary interface for accessing sensor data from various device sensors. _(beta)_
- [SRSleepSession](sensorkit/srsleepsession.md)
- [SRSourceDevice](sensorkit/srsourcedevice.md) _(beta)_

### Protocols

- [SRDataSensor](sensorkit/srdatasensor.md) — `SRDataSensor` serves as the foundational protocol for all sensor types, providing type safety and consistency across the SensorKit ecosystem. Each conforming sensor type specifies the kind of data it produces, enabling compile-time verification and type-safe data access patterns. _(beta)_

### Structures

- [SRAccelerometerSensor](sensorkit/sraccelerometersensor.md) _(beta)_
- [SRAcousticSettingsSensor](sensorkit/sracousticsettingssensor.md) _(beta)_
- [SRAmbientLightSensor](sensorkit/srambientlightsensor.md) _(beta)_
- [SRAmbientPressureSensor](sensorkit/srambientpressuresensor.md) _(beta)_
- [SRDeviceUsageSensor](sensorkit/srdeviceusagesensor.md) _(beta)_
- [SRElectrocardiogramSensor](sensorkit/srelectrocardiogramsensor.md) _(beta)_
- [SRFaceMetricsSensor](sensorkit/srfacemetricssensor.md) _(beta)_
- [SRFetchResponse](sensorkit/srfetchresponse.md) — A generic container that holds sensor data samples retrieved from SensorKit data streams. _(beta)_
- [SRHeadphoneMotionSensor](sensorkit/srheadphonemotionsensor.md) _(beta)_
- [SRHeadphoneSettingsSensor](sensorkit/srheadphonesettingssensor.md) _(beta)_
- [SRHeartRateSensor](sensorkit/srheartratesensor.md) _(beta)_
- [SRKeyboardMetricsSensor](sensorkit/srkeyboardmetricssensor.md) _(beta)_
- [SRMediaEventsSensor](sensorkit/srmediaeventssensor.md) _(beta)_
- [SRMessagesUsageSensor](sensorkit/srmessagesusagesensor.md) _(beta)_
- [SROdometerSensor](sensorkit/srodometersensor.md) _(beta)_
- [SROnWristStateSensor](sensorkit/sronwriststatesensor.md) _(beta)_
- [SRPedometerDataSensor](sensorkit/srpedometerdatasensor.md) _(beta)_
- [SRPhoneUsageSensor](sensorkit/srphoneusagesensor.md) _(beta)_
- [SRPhotoplethysmogramSensor](sensorkit/srphotoplethysmogramsensor.md) _(beta)_
- [SRRotationRateSensor](sensorkit/srrotationratesensor.md) _(beta)_
- [SRSiriSpeechMetricsSensor](sensorkit/srsirispeechmetricssensor.md) _(beta)_
- [SRSleepSessionsSensor](sensorkit/srsleepsessionssensor.md) _(beta)_
- [SRTelephonySpeechMetricsSensor](sensorkit/srtelephonyspeechmetricssensor.md) _(beta)_
- [SRVisitsSensor](sensorkit/srvisitssensor.md) _(beta)_
- [SRWristTemperatureSensor](sensorkit/srwristtemperaturesensor.md) _(beta)_
