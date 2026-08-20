---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreamsTests_DreamDiffTests_swift.html
archived_at: '2026-07-15T04:56:06.796891Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreamsTests-ValueSemanticsTestCase.swift.md)[Previous](LucidDreamsTests-DreamListViewControllerModelDiffTests.swift.md)

# LucidDreamsTests/DreamDiffTests.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Tests to make sure that the `Dream` type correctly constructs a diff.
*/

import XCTest

class DreamDiffTests: XCTestCase {
    func testDiffingEqualDreams() {
        let dream1 = Dream(description: "foo", creature: .unicorn(.pink), effects: [.fireBreathing])
        let dream2 = Dream(description: "foo", creature: .unicorn(.pink), effects: [.fireBreathing])

        let diff = dream1.diffed(with: dream2)

        XCTAssertNil(diff.creatureChange)
        XCTAssertTrue(diff.insertedEffects.isEmpty)
        XCTAssertTrue(diff.removedEffects.isEmpty)
        XCTAssertNil(diff.descriptionChange)
        XCTAssertFalse(diff.hasChanges)
    }

    func testDiffsAreEqual() {
        let dream1 = Dream(description: "foo", creature: .unicorn(.pink), effects: [.fireBreathing])
        let dream2 = Dream(description: "bar", creature: .unicorn(.white), effects: [.laserFocus, .fireflies])

        let diff = dream1.diffed(with: dream2)

        XCTAssertEqual(diff,  diff)
    }

    func testDiffingDifferentDreams() {
        let dream1 = Dream(description: "foo", creature: .unicorn(.pink), effects: [.fireBreathing])
        let dream2 = Dream(description: "bar", creature: .unicorn(.white), effects: [.laserFocus, .fireflies])

        let diff = dream1.diffed(with: dream2)

        XCTAssertEqual(diff.descriptionChange?.from, "foo")
        XCTAssertEqual(diff.descriptionChange?.to, "bar")

        XCTAssertEqual(diff.creatureChange?.from, .unicorn(.pink))
        XCTAssertEqual(diff.creatureChange?.to, .unicorn(.white))

        XCTAssertEqual(diff.removedEffects, [.fireBreathing])
        XCTAssertEqual(diff.insertedEffects, [.laserFocus, .fireflies])

        XCTAssertTrue(diff.hasChanges)
    }
}
```

[Next](LucidDreamsTests-ValueSemanticsTestCase.swift.md)[Previous](LucidDreamsTests-DreamListViewControllerModelDiffTests.swift.md)

