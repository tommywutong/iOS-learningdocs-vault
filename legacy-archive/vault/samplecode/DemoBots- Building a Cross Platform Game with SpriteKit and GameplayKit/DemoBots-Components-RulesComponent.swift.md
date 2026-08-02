---
title: 'DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit'
apple_id: TP40015179
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SpriteKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/DemoBots/Listings/DemoBots_Components_RulesComponent_swift.html
archived_at: '2026-07-18T03:06:17.586690Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md)


[Next](DemoBots-Components-PlayerBotHitState.swift.md)[Previous](DemoBots-Components-ChargeComponent.swift.md)

# DemoBots/Components/RulesComponent.swift

```swift
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    A `GKComponent` and associated delegate that manage and respond to a `GKRuleSystem` for an entity.
*/

import GameplayKit

protocol RulesComponentDelegate: class {
    // Called whenever the rules component finishes evaluating its rules.
    func rulesComponent(rulesComponent: RulesComponent, didFinishEvaluatingRuleSystem ruleSystem: GKRuleSystem)
}

class RulesComponent: GKComponent {
    // MARK: Properties

    weak var delegate: RulesComponentDelegate?

    var ruleSystem: GKRuleSystem

    /// The amount of time that has passed since the `TaskBot` last evaluated its rules.
    private var timeSinceRulesUpdate: TimeInterval = 0.0

    // MARK: Initializers

    override init() {
        ruleSystem = GKRuleSystem()
        super.init()
    }

    init(rules: [GKRule]) {
        ruleSystem = GKRuleSystem()
        ruleSystem.add(rules)
        super.init()
    }

    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: GKComponent Life Cycle

    override func update(deltaTime seconds: TimeInterval) {
        timeSinceRulesUpdate += seconds

        if timeSinceRulesUpdate < GameplayConfiguration.TaskBot.rulesUpdateWaitDuration { return }

        timeSinceRulesUpdate = 0.0

        if let taskBot = entity as? TaskBot,
            let level = taskBot.component(ofType: RenderComponent.self)?.node.scene as? LevelScene,
            let entitySnapshot = level.entitySnapshotForEntity(entity: taskBot),
            !taskBot.isGood {

            ruleSystem.reset()

            ruleSystem.state["snapshot"] = entitySnapshot

            ruleSystem.evaluate()

            delegate?.rulesComponent(rulesComponent: self, didFinishEvaluatingRuleSystem: ruleSystem)
        }
    }
}
```

[Next](DemoBots-Components-PlayerBotHitState.swift.md)[Previous](DemoBots-Components-ChargeComponent.swift.md)

