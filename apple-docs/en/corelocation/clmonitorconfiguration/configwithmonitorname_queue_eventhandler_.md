---
title: 'configWithMonitorName:queue:eventHandler:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clmonitorconfiguration/configwithmonitorname:queue:eventhandler:'
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitorconfiguration/configwithmonitorname:queue:eventhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitorconfiguration/configwithmonitorname%3Aqueue%3Aeventhandler%3A.json'
content_hash: 'sha256:2806fec3c12802a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitorConfiguration](../clmonitorconfiguration.md)

# configWithMonitorName:queue:eventHandler:

<sub>Type Method</sub>

Creates a location monitor instance with the name, dispatch queue, and event handler you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (CLMonitorConfiguration *) configWithMonitorName:(NSString *) name queue:(dispatch_queue_t) queue eventHandler:(void (^)(CLMonitor *monitor, CLMonitoringEvent *event)) eventHandler;
```
