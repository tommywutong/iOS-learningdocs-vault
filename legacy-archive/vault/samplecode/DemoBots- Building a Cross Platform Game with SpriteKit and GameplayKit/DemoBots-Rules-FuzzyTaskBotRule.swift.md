---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Rules_FuzzyTaskBotRule_swift.html
archived_at: '2026-07-18T03:06:20.624367Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-LevelScenePauseState.swift.md)[Previous](DemoBots-Rules-Rules.swift.md)

# DemoBots/Rules/FuzzyTaskBotRule.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    `FuzzyTaskBotRule` is a `GKRule` subclass that asserts a `fact` if and only if its `grade()` function returns a non-zero value. Subclasses for the specific rules used in the game can be found in Rules.swift.
*/

import GameplayKit

class FuzzyTaskBotRule: GKRule {
    // MARK: Properties

    var snapshot: EntitySnapshot!

    func grade() -> Float { return 0.0 }

    let fact: Fact

    // MARK: Initializers

    init(fact: Fact) {
        self.fact = fact

        super.init()

        // Set the salience so that 'fuzzy' rules will evaluate first.
        salience = Int.max
    }

    // MARK: GPRule Overrides

    override func evaluatePredicate(in system: GKRuleSystem) -> Bool {
        snapshot = system.state["snapshot"] as! EntitySnapshot

        if grade() >= 0.0 {
            return true
        }

        return false
    }

    override func performAction(in system: GKRuleSystem) {
        system.assertFact(fact.rawValue as NSObject, grade: grade())
    }
}
```

[Next](DemoBots-LevelScenePauseState.swift.md)[Previous](DemoBots-Rules-Rules.swift.md)

