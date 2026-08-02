---
title: 'LucidDreams: Protocol and Value Oriented Programming Sample Code'
apple_id: TP40017334
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/LucidDreams/Listings/LucidDreamsTests_DreamListViewControllerModelDiffTests_swift.html
archived_at: '2026-07-15T04:56:06.804565Z'
---
> 导航：[总目录](../../README.md) · [LucidDreams](../../_indexes/LucidDreams.md) · [LucidDreams: Protocol and Value Oriented Programming Sample Code](LucidDreams-%20Protocol%20and%20Value%20Oriented%20Programming%20Sample%20Code.md)


[Next](LucidDreamsTests-DreamDiffTests.swift.md)[Previous](LucidDreamsTests-LayoutTests.swift.md)

# LucidDreamsTests/DreamListViewControllerModelDiffTests.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Tests to make sure that the `DreamListViewControllerModel` type correctly
                constructs a diff.
*/

import XCTest

class DreamListViewControllerModelDiffTests: XCTestCase {
    func testDiffingEqualModels() {
        let dream1 = Dream(description: "foo", creature: .unicorn(.pink), effects: [.fireBreathing])
        let dream2 = Dream(description: "bar", creature: .unicorn(.yellow), effects: [.rain])

        let model1 = DreamListViewControllerModel(favoriteCreature: .unicorn(.pink), dreams: [
            dream1,
            dream2
        ])

        let model2 = DreamListViewControllerModel(favoriteCreature: .unicorn(.pink), dreams: [
            dream1,
            dream2
        ])

        let diff = model1.diffed(with: model2)

        XCTAssertFalse(diff.hasAnyDreamChanges)
        XCTAssertFalse(diff.hasAnyDreamChanges)
        XCTAssertFalse(diff.favoriteCreatureChanged)
        XCTAssertEqual(diff.from, model1)
        XCTAssertEqual(diff.to, model2)
        XCTAssertNil(diff.dreamChange)
    }

    func testDiffRemovingDreamFromModel() {
        let dream1 = Dream(description: "foo", creature: .unicorn(.pink), effects: [.fireBreathing])
        let dream2 = Dream(description: "bar", creature: .unicorn(.white), effects: [.laserFocus, .fireflies])
        let dream3 = Dream(description: "baz", creature: .unicorn(.white), effects: [.laserFocus, .fireflies])

        let model1 = DreamListViewControllerModel(favoriteCreature: .unicorn(.pink), dreams: [
            dream1,
            dream2,
            dream3
        ])

        let model2 = DreamListViewControllerModel(favoriteCreature: .unicorn(.pink), dreams: [
            dream1,
            dream2
        ])

        let diff = model1.diffed(with: model2)
        XCTAssertEqual(diff.dreamChange, .removed(dream3))
    }

    func testDiffAppendingDreamFromModel() {
        let dream1 = Dream(description: "foo", creature: .unicorn(.pink), effects: [.fireBreathing])
        let dream2 = Dream(description: "bar", creature: .unicorn(.white), effects: [.laserFocus, .fireflies])
        let dream3 = Dream(description: "baz", creature: .unicorn(.white), effects: [.laserFocus, .fireflies])

        let model1 = DreamListViewControllerModel(favoriteCreature: .unicorn(.pink), dreams: [
            dream1,
            dream2
        ])

        let model2 = DreamListViewControllerModel(favoriteCreature: .unicorn(.pink), dreams: [
            dream1,
            dream2,
            dream3
        ])

        let diff = model1.diffed(with: model2)
        XCTAssertEqual(diff.dreamChange, .inserted(dream3))
    }

    func testDiffFavoriteCreatureChanged() {
        let model1 = DreamListViewControllerModel(favoriteCreature: .unicorn(.pink), dreams: [])
        let model2 = DreamListViewControllerModel(favoriteCreature: .unicorn(.yellow), dreams: [])

        let diff = model1.diffed(with: model2)
        XCTAssertTrue(diff.favoriteCreatureChanged)
    }
}
```

[Next](LucidDreamsTests-DreamDiffTests.swift.md)[Previous](LucidDreamsTests-LayoutTests.swift.md)

