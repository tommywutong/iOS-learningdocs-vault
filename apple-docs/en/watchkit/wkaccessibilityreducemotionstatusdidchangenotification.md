---
title: WKAccessibilityReduceMotionStatusDidChangeNotification
framework: WatchKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [watchOS 4.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/watchkit/wkaccessibilityreducemotionstatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/watchkit/wkaccessibilityreducemotionstatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/watchkit/wkaccessibilityreducemotionstatusdidchangenotification.json'
content_hash: 'sha256:22a600732e64f816'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WatchKit](../watchkit.md)

# WKAccessibilityReduceMotionStatusDidChangeNotification

<sub>Global Variable</sub>

Tells the interface controller that the reduce motion status has changed.

<sub>watchOS</sub>

```objc
extern NSString * const WKAccessibilityReduceMotionStatusDidChangeNotification;
```

## Discussion

Use this notification to customize your application’s user interface for when reduced motion is enabled. You can also use the [WKAccessibilityIsReduceMotionEnabled](<wkaccessibilityisreducemotionenabled().md>) function to determine whether reduced motion is enabled.

Observe this notification using the default notification center. This notification doesn’t include a parameter.

## See Also

### Managing Notifications

- [WKAccessibilityVoiceOverStatusChanged](wkaccessibilityvoiceoverstatuschanged.md) — Tells the interface controller that the VoiceOver status has changed.
