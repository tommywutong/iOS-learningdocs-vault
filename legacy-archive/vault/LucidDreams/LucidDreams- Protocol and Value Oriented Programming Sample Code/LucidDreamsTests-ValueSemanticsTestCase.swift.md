---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreamsTests_ValueSemanticsTestCase_swift.html
archived_at: '2026-07-15T04:56:06.825456Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreamsTests-DreamTests.swift.md)[Previous](LucidDreamsTests-DreamDiffTests.swift.md)

# LucidDreamsTests/ValueSemanticsTestCase.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Provides a generic implementation of testing a value for value semantics.
*/

import XCTest

/**
    A generic implementation that allows you to test whether or not your value
    has value semantics.
*/
func testValueSemantics<Value: Equatable>(initial: Value, mutations: (inout Value) -> Void) {
    var copy = initial
    XCTAssertEqual(initial, copy)

    mutations(&copy)
    XCTAssertNotEqual(initial, copy)
}
```

[Next](LucidDreamsTests-DreamTests.swift.md)[Previous](LucidDreamsTests-DreamDiffTests.swift.md)

