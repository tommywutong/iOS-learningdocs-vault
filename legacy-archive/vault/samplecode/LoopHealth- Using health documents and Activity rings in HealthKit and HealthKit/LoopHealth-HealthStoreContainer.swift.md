---
title: 'LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI'
apple_id: TP40017553
resource_type: Sample Code
platform: watchOS|iOS
topic: null
technology: null
published: '2016-12-02'
source_url: https://developer.apple.com/library/archive/samplecode/LoopHealth/Listings/LoopHealth_HealthStoreContainer_swift.html
archived_at: '2026-07-18T03:13:50.041303Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LoopHealth: Using health documents and Activity rings in HealthKit and HealthKitUI](LoopHealth-%20Using%20health%20documents%20and%20Activity%20rings%20in%20HealthKit%20and%20HealthKit.md)


[Next](LoopHealth-UIViewController%2BEnumerate.swift.md)[Previous](LoopHealth-RecordsDetailViewController.swift.md)

# LoopHealth/HealthStoreContainer.swift

```swift
/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A protocol that formally defines an object that has a `HKHealthStore` property.
 */

import HealthKit

protocol HealthStoreContainer {
    var healthStore: HKHealthStore! { get set }
}
```

[Next](LoopHealth-UIViewController%2BEnumerate.swift.md)[Previous](LoopHealth-RecordsDetailViewController.swift.md)

