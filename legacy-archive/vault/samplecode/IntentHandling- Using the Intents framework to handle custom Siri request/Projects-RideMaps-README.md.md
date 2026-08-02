---
title: 'IntentHandling: Using the Intents framework to handle custom Siri request'
apple_id: TP40017335
resource_type: Sample Code
platform: iOS
topic: null
technology: Intents
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/IntentHandling/Listings/Projects_RideMaps_README_md.html
archived_at: '2026-07-18T03:13:01.813299Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [IntentHandling: Using the Intents framework to handle custom Siri request](IntentHandling-%20Using%20the%20Intents%20framework%20to%20handle%20custom%20Siri%20request.md)


[Next](Projects-RideMaps-RideMaps-AppDelegate.swift.md)[Previous](Projects-RideMaps-GetRideStatusIntentExtension-IntentHandler.swift.md)

# Projects/RideMaps/README.md

```
#RideMaps
##Overview

The ridesharing domain consists of 3 individual intent handling protocols that you must conform to:
1. `INListRideOptionsIntentHandling`
2. `INRequestRideIntentHandling`
3. `INGetRideStatusIntentHandling`

Each of the handling protocols can have resolve..., confirm..., and handle... methods. For the Maps context, we never need to implement the resolve... methods, and only need to implement the confirm method for `INRequestRideIntentHandling`.

In this project, each protocol in the domain has been separated into its own extension. This way you can isolate your code for each protocol in different processes.

This project includes copious comments to help you implement the ridesharing domain for intents. It does not include implementation, but will have hints about where to perform certain implementation tasks.

*The intents you wish to handle in an extension must be declared in the extension's Info.plist.*
```

[Next](Projects-RideMaps-RideMaps-AppDelegate.swift.md)[Previous](Projects-RideMaps-GetRideStatusIntentExtension-IntentHandler.swift.md)

