---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreamsTests_DreamTests_swift.html
archived_at: '2026-07-15T04:56:06.813033Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](README.md.md)[Previous](LucidDreamsTests-ValueSemanticsTestCase.swift.md)

# LucidDreamsTests/DreamTests.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Defines test to make sure that the `Dream` type has value semantics.
*/

import XCTest

class DreamValueSemanticsTestCase: XCTestCase {
    func testDreamHasValueSemantics() {
        let dream = Dream(description: "Saw the light", creature: .unicorn(.yellow), effects: [.fireBreathing])

        testValueSemantics(initial: dream, mutations: { (copy: inout Dream) in
            /*
                Change the copy's description to something different than the 
                original dream.
            */
            copy.description = "Saw the light (copy)"
        })
    }
}
```

[Next](README.md.md)[Previous](LucidDreamsTests-ValueSemanticsTestCase.swift.md)

