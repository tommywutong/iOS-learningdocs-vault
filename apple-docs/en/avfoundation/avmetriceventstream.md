---
title: AVMetricEventStream
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetriceventstream
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetriceventstream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetriceventstream.json'
content_hash: 'sha256:158721db28b744de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricEventStream

<sub>Class</sub>

An object that allows clients to add publishers and then subscribe to specific metric event classes from those publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface AVMetricEventStream : NSObject
```

## Overview

Publishers are [AVFoundation](../avfoundation.md) types that adopt [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md). The protocol allows clients to receive metric events with a subscriber delegate which adopts the [AVMetricEventStreamSubscriber](avmetriceventstreamsubscriber.md) protocol.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Getting the event stream

- [eventStream](avmetriceventstream/eventstream.md)

### Adding a publisher

- [addPublisher:](avmetriceventstream/addpublisher_.md)

### Subscribing to events

- [subscribeToAllMetricEvents](avmetriceventstream/subscribetoallmetricevents.md)
- [subscribeToMetricEvent:](avmetriceventstream/subscribetometricevent_.md)
- [subscribeToMetricEvents:](avmetriceventstream/subscribetometricevents_.md)

### Setting a subscriber

- [setSubscriber:queue:](avmetriceventstream/setsubscriber_queue_.md)

## See Also

### Metrics

- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — An object that provides metrics related to video playback quality.
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — A type for objects that publish metric events to the event stream.
- [AVMetricEventStreamSubscriber](avmetriceventstreamsubscriber.md) — A type for objects that receive metric events.
- [AVMetricEvent](avmetricevent.md) — A base class that represents a metric event.
- [AVMetricErrorEvent](avmetricerrorevent.md) — An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)
