---
title: 'publisher:didReceiveEvent:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetriceventstreamsubscriber/publisher:didreceiveevent:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetriceventstreamsubscriber/publisher:didreceiveevent:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetriceventstreamsubscriber/publisher%3Adidreceiveevent%3A.json'
content_hash: 'sha256:410807c5ae247e99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetricEventStreamSubscriber](../avmetriceventstreamsubscriber.md)

# publisher:didReceiveEvent:

<sub>Instance Method</sub>

Tells the subscriber that the publisher produced a metric event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) publisher:(id<AVMetricEventStreamPublisher>) publisher didReceiveEvent:(AVMetricEvent *) event;
```

## Parameters

- `publisher` — The publisher.

- `event` — The metric.
