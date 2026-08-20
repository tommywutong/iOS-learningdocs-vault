---
title: GameplayKit Programming Guide
apple_id: TP40015172
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: GameplayKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html
archived_at: '2026-07-15T07:34:17.324012Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## About GameplayKit

GameplayKit is a collection of foundational tools and technologies for building games in iOS, OS X, and tvOS. Building, evolving, and maintaining a sophisticated game requires a well-planned design—GameplayKit provides architectural tools to help you design modular, scalable game architecture with minimal effort. Creating great games also requires deploying complex algorithms to solve the problems underlying common game mechanics—GameplayKit also provides standard implementations of such algorithms, allowing you to spend more time on the features that make your gameplay unique.

Because GameplayKit is independent of high-level game engine technologies, you can combine it with any of those technologies to build a complete game: SpriteKit for 2D games, SceneKit for 3D games, or a custom or third-party game engine using Metal or OpenGL ES. For games with less demanding graphics needs, you can even use GameplayKit with UIKit (in iOS or tvOS) or AppKit (in OS X).

GameplayKit provides seven core areas of functionality, which you can combine or use independently to create your game:

![image: ../Art/icon_random_2x.png](attachments/Art/icon_random_2x.png)

[Randomization](RandomSources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqojnknltc). Use these robust, flexible implementations of standard algorithms as the building blocks for many kinds of game mechanics.

![image: ../Art/icon_entities_2x.png](attachments/Art/icon_entities_2x.png)

[Entities and Components](EntityComponent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnrnknltc). Design more reusable gameplay code by building on this architecture.

![image: ../Art/icon_state_machines.pdf](attachments/Art/icon_state_machines_2x.png)

[State Machines](StateMachine.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnznknltc). Use this architecture to untangle complex procedural code in your gameplay designs.

![image: ../Art/icon_min_max.pdf](attachments/Art/icon_min_max_2x.png)

[The Minmax Strategist](Minmax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmrnknltc). Create a model for your turn-based game and AI player objects that use the model to plan optimal moves.

![image: ../Art/icon_path_finding.pdf](attachments/Art/icon_path_finding_2x.png)

[Pathfinding](Pathfinding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmznknltc). Describe a game world as a graph, allowing GameplayKit to plan optimal routes for game characters to follow.

![image: ../Art/icon_agents.pdf](attachments/Art/icon_agents_2x.png)

[Agents, Goals, and Behaviors](Agent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqobnknltc). Use this simulation to let game characters move themselves based on high-level goals and react to their surroundings.

![image: ../Art/icon_rule.pdf](attachments/Art/icon_rule_2x.png)

[Rule Systems](RuleSystems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmjqfvjvomi). Separate game design from executable code to speed up your gameplay development cycle, or implement fuzzy logic reasoning to add realistic behavior to your game.

### Examples

The example games discussed in this book are available as sample code, so you can download each as a complete project to see GameplayKit (and other technologies) in action:

- _[Boxes: GameplayKit Entity-Component Basics](../../../samplecode/Boxes-%20GameplayKit%20Entity-Component%20Basics/Boxes-%20GameplayKit%20Entity-Component%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinjz)_ — A basic demonstration of GameplayKit’s Entity-Component system, discussed in the [Entities and Components](EntityComponent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnrnknltc) chapter.
- _[Dispenser: GameplayKit State Machine Basics](../../../samplecode/Dispenser-%20GameplayKit%20State%20Machine%20Basics/Dispenser-%20GameplayKit%20State%20Machine%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrq)_ — A basic demonstration of GameplayKit’s state machine system, discussed in the [State Machines](StateMachine.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnznknltc) chapter.
- _[Pathfinder: GameplayKit Pathfinding Basics](../../../samplecode/Pathfinder-%20GameplayKit%20Pathfinding%20Basics/Pathfinder-%20GameplayKit%20Pathfinding%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinrr)_ — A basic demonstration of GameplayKit’s pathfinding system, discussed in the [Pathfinding](Pathfinding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmznknltc) chapter.
- [Maze: Getting Started with GameplayKit](https://developer.apple.com/sample-code/wwdc/2015/downloads/Maze.zip) (未归档：ZIP 按安全策略跳过) — A simplified classic arcade game, using many of the design and gameplay features in GameplayKit. This project is discussed in the [Entities and Components](EntityComponent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnrnknltc), [State Machines](StateMachine.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnznknltc), [Pathfinding](Pathfinding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmznknltc), and [Rule Systems](RuleSystems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmjqfvjvomi) chapters.
- _[FourInARow: Using the GameplayKit Minmax Strategist for Opponent AI](../../../samplecode/FourInARow-%20Using%20the%20GameplayKit%20Minmax%20Strategist%20for%20Opponent%20AI/FourInARow-%20Using%20the%20GameplayKit%20Minmax%20Strategist%20for%20Opponent%20AI.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbs)_ — A simple board game built using UIKit (iOS only), illustrating use of the [GKMinmaxStrategist](https://developer.apple.com/documentation/gameplaykit/gkminmaxstrategist) class and related protocols, discussed in [The Minmax Strategist](Minmax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmrnknltc).
- _[AgentsCatalog: Using the Agents System in GameplayKit](../../../samplecode/AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit/AgentsCatalog-%20Using%20the%20Agents%20System%20in%20GameplayKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbr)_ — A demonstration of the [GKAgent](https://developer.apple.com/documentation/gameplaykit/gkagent) class and several of the individual goals an agent can follow, as well as how to combine goals into complex behaviors. The [Agents, Goals, and Behaviors](Agent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqobnknltc) chapter discusses this project.
- _[DemoBots: Building a Cross Platform Game with SpriteKit and GameplayKit](../../../samplecode/DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit/DemoBots-%20Building%20a%20Cross%20Platform%20Game%20with%20SpriteKit%20and%20GameplayKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzz)_ — A full-featured game, using nearly all of the systems in GameplayKit, and also demonstrating techniques for designing and building a multi-level game project using SpriteKit, on-demand resources, and new features in Xcode 7. Parts of this project are discussed in the [Agents, Goals, and Behaviors](Agent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqobnknltc) and [Rule Systems](RuleSystems.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmjqfvjvomi) chapters.

### See Also

The example games in this guide are built with the UIKit, SpriteKit, and SceneKit frameworks. Before using GameplayKit in concert with one of these technologies, you should be familiar with the relevant concepts and tools, and generally familiar with building apps for Apple platforms. See the following documents for more information about whichever game engine technology you plan to work with:

- _[SpriteKit Programming Guide](../../Graphics%20Animation/SpriteKit%20Programming%20Guide/About%20SpriteKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbt)_ and _[SpriteKit Framework Reference](https://developer.apple.com/documentation/spritekit)_
- _[Scene Kit Framework Reference](https://developer.apple.com/documentation/scenekit)_
- _[Start Developing iOS Apps (Swift)](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/DevelopiOSAppsSwift/index.html#//apple_ref/doc/uid/TP40015214)_ or _[App Programming Guide for tvOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/index.html#//apple_ref/doc/uid/TP40015241)_, and _[Xcode Overview](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_

[Randomization](RandomSources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqojnknltc)
