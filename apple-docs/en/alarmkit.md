---
title: AlarmKit
framework: AlarmKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/alarmkit
source_url: 'https://developer.apple.com/documentation/alarmkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/alarmkit.json'
content_hash: 'sha256:16d3627f0d3bf6bc'
translated: false
---

> Navigation: [Technologies](technologies.md)

# AlarmKit

<sub>Framework</sub>

Schedule prominent alarms and countdowns to help people manage their time.

## Overview

Use `AlarmKit` to create custom alarms and timers in your app. `AlarmKit` provides a framework for managing alarms with customizable schedules and UI. It supports one-time and repeating alarms, with the option for countdown durations and snooze functionality. `AlarmKit` handles alarm authorization and provides UI for both templated and widget presentations. It supports traditional alarms, timers, or both, and provides methods to schedule, pause, resume, and cancel alarms.

## Topics

### Alarm management

- [Scheduling an alarm with AlarmKit](alarmkit/scheduling-an-alarm-with-alarmkit.md) — Create prominent alerts at specified dates for your iOS app.
- [AlarmManager](alarmkit/alarmmanager.md) — An object that exposes functions to work with alarms: scheduling, snoozing, cancelling.
- [Alarm](alarmkit/alarm.md) — An object that describes an alarm that can alert once or on a repeating schedule.

### Buttons

- [AlarmButton](alarmkit/alarmbutton.md) — A struct that defines the appearance of buttons.

### Views

- [AlarmPresentation](alarmkit/alarmpresentation.md) — An object that describes the content required for the alarm UI.
- [AlarmPresentationState](alarmkit/alarmpresentationstate.md) — The system managed content state of an alarm Live Activity.
- [AlarmAttributes](alarmkit/alarmattributes.md) — An object that contains all information necessary for the alarm UI.
- [AlarmMetadata](alarmkit/alarmmetadata.md) — A metadata object that contains information about an alarm.
