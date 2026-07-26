---
title: AVPlayerInterstitialEventMonitor.ScheduleRequestCompleted
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/schedulerequestcompleted
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/schedulerequestcompleted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/schedulerequestcompleted.json'
content_hash: 'sha256:115e9cedd3dda205'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# AVPlayerInterstitialEventMonitor.ScheduleRequestCompleted

<sub>Structure</sub>

A NotificationCenter AsyncMessage that is sent when a daterange-schedule request completes

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScheduleRequestCompleted
```

## Parameters

- `scheduleIdentifier` — The ID attribute of the daterange-schedule

- `result` — On success, the serialized JSON Data from the schedule response

## Relationships

- **Conforms To**: [NotificationCenter.AsyncMessage](../../foundation/notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting the completion

- [scheduleIdentifier](schedulerequestcompleted/scheduleidentifier.md)
- [result](schedulerequestcompleted/result.md)
