---
title: GameplayKit Programming Guide
apple_id: TP40015172
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: GameplayKit
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/RuleSystems.html
archived_at: '2026-07-15T07:34:14.825912Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [GameplayKit Programming Guide](index.md)



## Rule Systems

Some kinds of games include complex sets of rules. For example, a role-playing game with turn-based combat might include rules governing what happens when opposing characters move into the same space: Who has the upper hand in the resulting struggle? When, if at all, does either character gain an opportunity to attack the other? What happens when other characters attempt to attack or interact with one of the combatants? These sets of rules can become so complex that conditional logic statements in a programming language become unwieldy.

Some of the most interesting kinds of games include systems with _emergent behavior_—cases where the interactions between simple entities following simple rules lead to interesting patterns in the system as a whole. For example, the goals of individual enemy characters in an action game might depend on the character’s health level, how recently that enemy saw the player character, how many other enemy characters are nearby, how often the player has been defeating enemies, and other variables. Together, these factors can lead to realistic variations in gameplay, with some enemies attacking the player in swarms and others fleeing.

In GameplayKit, _rule systems_ address both of these issues. By providing an abstraction that treats certain elements of game logic as data, rule systems can help you decompose your game into functional, reusable, extensible pieces. By incorporating fuzzy logic, rule systems can treat decisions as continuous variables instead of discrete states, leading to complex behavior from even simple combinations of rules.

### Designing Rule Systems

GameplayKit includes two main classes for building rule systems: [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule), which represents a specific decision to be made based on external state, and [GKRuleSystem](https://developer.apple.com/documentation/gameplaykit/gkrulesystem), which evaluates a set of rules against state data to determine a set of facts.

### Rules Make Basic Decisions

A [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule) object has two parts: a _predicate_ and an _action_. A rule’s predicate is the decision-making part—it evaluates a set of state information and returns a Boolean result. A rule’s action is code whose execution is triggered only when the predicate produces a true result. GameplayKit always evaluates rules in the context of a rule system. Typically, a rule’s predicate tests state data maintained by the rule system, and its action either changes the system’s state or asserts a fact—part of the rule system’s output.

Because a rule evaluates the state of a system and modifies properties of that system, a rule needs no local state data. This design allows you to design individual rules as functional units with well-defined behavior and reuse them in any rule system.

### A Rule System Uses Rules and State to Assert Facts

A [GKRuleSystem](https://developer.apple.com/documentation/gameplaykit/gkrulesystem) object has three key parts: an agenda of rules, state data, and facts.

- __The agenda.__ You combine a set of rules by adding them to the [agenda](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501078-agenda) of a rule system object (with the [addRule:](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501274-add) or [addRulesFromArray:](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501130-addrulesfromarray) method). By default, a system evaluates rules in the order they were added to its agenda—to make sure some rules are always evaluated before others, change the [salience](https://developer.apple.com/documentation/gameplaykit/gkrule/1501148-salience) property of those rules.
- __State information.__The rule system’s [state](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501238-state) dictionary contains information rules can be tested against. This dictionary can reference anything useful to your set of rules, be that simple data like strings and numbers or custom classes from your game model. How you write rules determines the structure of the data those rules will use.
- __Facts.__ A _fact_ represents a conclusions drawn from the evaluation of rules in a system, and can be any type of object—typically, simple data objects like strings suffice, but custom objects from your game model can be used as well. A fact’s _membership grade_ is a number that determines its presence in the system’s set of facts. A fact with grade 1.0 is included, and a fact with grade zero is not. When a rule system evaluates its rules, the rule actions can _assert_ a fact, adding it to the system, or _retract_ a fact, removing it from the system.

However, membership grade need not simply be a binary state—a fact can have any grade between 0.0 and 1.0. By allowing facts to vary in grade, you can use rule systems to define _fuzzy logic_, where rules can lead to conclusions with a variable strength, truth value, or confidence level. When a rule asserts or retracts a fact, it adds to or subtracts from that fact’s grade.

Your game can then use the relative strengths of various facts to create gameplay effects. For example, whether an enemy moves to attack the player might be based on a “vulnerable” fact, whose grade is based on several rules. One rule might increase the grade if the player is nearby, another might reduce the grade if the player is in full health, and so on. You can also build rule systems in which some rules assert facts, and other rules examine the grades of those facts in order to assert or retract further conclusions. You might even use the grades of facts in the system to vary the influence of corresponding factors in the game—for example, you might tie the goal weights collected in a [GKBehavior](https://developer.apple.com/documentation/gameplaykit/gkbehavior) object to the grades of corresponding facts.

### Building a Game with Rule Systems

GameplayKit offers three ways to create [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule) objects. The one you choose depends on how you want to fit the construction of rules into your development process.

- The [ruleWithPredicate:assertingFact:grade:](https://developer.apple.com/documentation/gameplaykit/gkrule/1501122-init) and [ruleWithPredicate:retractingFact:grade:](https://developer.apple.com/documentation/gameplaykit/gkrule/1501212-rulewithpredicate) methods create rules whose predicate is decided by an [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) object, and whose action is hard-coded to assert or retract a specific fact. Because the `NSPredicate` class can describe conditional logic that accesses data through key paths, and because the rule’s action is fixed at its creation, this option produces rules that can be easily archived. This design lends itself well to data-driven workflows where game designers can tweak a game’s rule systems without writing code. (You can even use the [NSRuleEditor](https://developer.apple.com/documentation/appkit/nsruleeditor) class in OS X to support editing rules at run time.) However, these rules assert or retract facts with a constant grade, so they don’t work well for fuzzy logic systems involving facts whose grade is continuously variable.
- The [ruleWithBlockPredicate:action:](https://developer.apple.com/documentation/gameplaykit/gkrule/1501102-rulewithblockpredicate) factory method creates a rule from two blocks: a predicate block to evaluate the rule and return a Boolean result, and an action block to invoke when the predicate is true. This option allows you to quickly and easily create rules in code, including fuzzy logic rules. However, the resulting rules are not archivable—they can exist only in the in-memory object graph of your game.
- You can subclass [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule) to create your own rule classes, implementing the [evaluatePredicateWithSystem:](https://developer.apple.com/documentation/gameplaykit/gkrule/1501234-evaluatepredicate) method with code to decide a rule’s predicate and the [performActionWithSystem:](https://developer.apple.com/documentation/gameplaykit/gkrule/1501111-performaction) method with code to perform an action. Or you can subclass [GKNSPredicateRule](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule), which uses an [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) object to decide the rule’s predicate so that you need to write your own code only for executing the rule’s action. Because the key attributes of the rule are implemented in your subclasses, the flexibility and reusability of this option depends on how you design those classes.

After you design your rules, building and using a rule system takes four basic steps:

1. During initialization, create a [GKRuleSystem](https://developer.apple.com/documentation/gameplaykit/gkrulesystem) object and populate its list of rules.
2. Set the rule system’s [state](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501238-state) dictionary to contain whatever game information the rules should act upon.

   Depending on how you structure this information, you might set state once, during initialization, to contain objects whose own internal state changes over the course of the game. Or you might set state to contain static objects, and update the state to summarize current conditions in the game whenever you need to evaluate the rule system.
3. To evaluate rules, call the rule system’s [evaluate](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501077-evaluate) method.

   If you periodically evaluate the same rule system, call its [reset](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501301-reset) method before evaluating to clear the results of prior evaluations.
4. After evaluating the system, examine its set of asserted facts to draw conclusions and choose a course of action.

The following sections discuss example uses of rule systems in two different games.

### A Basic Rule System for Gameplay Effects

For a simple example of rule systems in action, see the Maze sample code project. In this game (a variation on several classic arcade games, with other features discussed in the [Entities and Components](EntityComponent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnrnknltc), [State Machines](StateMachine.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqnznknltc), and [Pathfinding](Pathfinding.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqmznknltc) chapters), a simple rule system determines the behavior of enemy characters in their normal state. Listing 8-1 shows the relevant parts for setting up and using this rule system.

> [!NOTE]
> 

__Listing 8-1__A Minimal Rule System

1. `- (instancetype)initWithGame:(AAPLGame *)game entity:(AAPLEntity *)entity {`
2. `self = [super initWithGame:game entity:entity];`
3. `if (self) {`
4. `// 1`
5. `_ruleSystem = [[GKRuleSystem alloc] init];`
6. `NSPredicate *playerFar = [NSPredicate predicateWithFormat:@"$distanceToPlayer.floatValue >= 10.0"];`
7. `[_ruleSystem addRule:[GKRule ruleWithPredicate:playerFar assertingFact:@"hunt" grade:1.0]];`
8. `NSPredicate *playerNear = [NSPredicate predicateWithFormat:@"$distanceToPlayer.floatValue < 10.0"];`
9. `[_ruleSystem addRule:[GKRule ruleWithPredicate:playerNear retractingFact:@"hunt" grade:1.0]];`
10. `}`
11. `return self;`
12. `}`

15. `- (void)updateWithDeltaTime:(NSTimeInterval)seconds {`
16. `// 2`
17. `NSUInteger distanceToPlayer = [self pathToPlayer].count;`
18. `self.ruleSystem.state[@"distanceToPlayer"] = @(distanceToPlayer);`
20. `// 3`
21. `[self.ruleSystem reset];`
22. `[self.ruleSystem evaluate];`
24. `// 4`
25. `self.hunting = ([self.ruleSystem gradeForFact:@"hunt"] > 0.0);`
26. `if (self.hunting) {`
27. `[self startFollowingPath:[self pathToPlayer]];`
28. `} else {`
29. `[self startFollowingPath:[self pathToNode:self.scatterTarget]];`
30. `}`

In this example, there are four steps to using a rule system:

1. The `initWithGame:entity:` method creates a [GKRuleSystem](https://developer.apple.com/documentation/gameplaykit/gkrulesystem) instance and populates it with [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule) objects. The rule system will be reused, so this example keeps it in a property.
2. The per-frame [updateWithDeltaTime:](https://developer.apple.com/documentation/gameplaykit/gkstate/1501136-update) method uses the rule system to determine what an enemy character will do next. First, it calculates the distance from the enemy character to the player character, and stores that information in the rule system’s [state](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501238-state) dictionary.
3. Next, this method resets the rule system (returning previously evaluated rules to the system’s agenda and clearing any facts asserted in past calls to the update method) and evaluates the rule system using the newly updated state information.
4. Finally, the update method uses the [gradeForFact:](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501177-grade) method to test whether the rule system asserted a fact, and based on that information, chooses a behavior for the enemy character.

This code shows a minimal use of rule systems—in fact, it does nothing that couldn’t be achieved with a simple `if` statement. However, by expanding on this sample, you can easily add sophisticated behavior to a game. For example:

- Add more state information, such as the distances from this enemy character to each other enemy character, the amount of time since the game started, or the player’s progress toward completing a level.
- Add more rules that test the additional state information. Add more facts representing the conclusions of of the added rules, and choose a behavior for the enemy character based on which combination of facts the system asserts.
- Move the [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) definitions that set the conditions to be tested by each rule out of your source code and into a data file, so that you or other members of your team can modify your game’s behavior without using Xcode to recompile the game from source.
- Alternatively, use the [ruleWithBlockPredicate:action:](https://developer.apple.com/documentation/gameplaykit/gkrule/1501102-rulewithblockpredicate) method or create custom [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule) subclasses to make rules that assert facts with variable grade, and use the fuzzy logic operators [minimumGradeForFacts:](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501211-minimumgradeforfacts) and [maximumGradeForFacts:](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501081-maximumgrade) to choose a behavior based on which combination of facts the system has asserted with the highest confidence.

### A Fuzzy Logic Rule System for Emergent Behavior

The DemoBots sample code project uses several of the options suggested above to create characters with interesting behaviors. In each level of this game there are several “task bot” characters, each of which can be in either a “good” or a “bad” state. The object of the game is for the player (a “debug bot” character) to find each bad bot and “debug” it, changing the bot to the good state. Good bots simply follow a predefined path around the level, but a bad bot can act in any of several ways—it might try to hunt and attack the player character, seek out good bots and turn them bad, or patrol around the level looking for trouble to cause.

> [!NOTE]
> 

This game uses a rule system to decide which of these actions a bad bot takes at any moment. Unlike the previous example, this rule system uses fuzzy logic—the rules in this system assert facts with variable grades, and after evaluating its rule system, a bot compares the grades of several facts to decide which course of action to take.

Each rule in this system uses a snapshot of summary information about the state of the game (see the `TaskBotSnapshot` class in the sample code project) so that multiple rule classes can use such information without recalculating it. The game generates a snapshot only when evaluating the rule system, and minimizes unnecessary computation by evaluating the rule system only periodically, not on every frame.

To build this system, DemoBots defines a set of [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule) subclasses, each of which performs a simple calculation to determine the grade for an associated fact. For example, Listing 8-2 shows the rule class for determining whether the number of bad bots currently in the level is low.

__Listing 8-2__An Example Fuzzy Logic Rule

1. `class BadTaskBotPercentageLowRule: FuzzyTaskBotRule {`
2. `override func grade() -> Float {`
3. `return max(0.0, 1.0 - 3.0 * snapshot.badBotPercentage)`
4. `}`
5. `init() { super.init(fact: .BadTaskBotPercentageLow) }`
6. `}`

This rule provides its highest grade when the level contains zero bad bots, and diminishes its grade as the ratio of bad bots to total bots in the level increases. The rule’s grade is zero when a third or more of the bots in a level are bad.

In DemoBots, a superclass, shown in abbreviated form in Listing 8-3, provides a common infrastructure for evaluating these rules and asserting facts with the grade each rule calculates.

__Listing 8-3__A Common Superclass for Fuzzy Logic Rules

1. `class FuzzyTaskBotRule: GKRule {`
2. `var snapshot: EntitySnapshot!`
3. `func grade() -> Float { return 0.0 }`
4. `let fact: Fact`
6. `init(fact: Fact) {`
7. `self.fact = fact`
8. `super.init()`
9. `// Set the salience so that 'fuzzy' rules will evaluate first.`
10. `salience = Int.max`
11. `}`
13. `override func evaluatePredicateWithSystem(system: GKRuleSystem) -> Bool {`
14. `snapshot = system.state["snapshot"] as! EntitySnapshot`
15. `if grade() >= 0.0 {`
16. `return true`
17. `}`
18. `return false`
19. `}`
21. `override func performActionWithSystem(system: GKRuleSystem) {`
22. `system.assertFact(fact.rawValue, grade: grade())`
23. `}`
24. `}`

With this infrastructure, constructing a rule system is a simple matter of creating instances of each rule class. Then, after providing a snapshot and evaluating the rule system, an instance of the `TaskBot` class compares the grades of any facts asserted by the system with the minimum and maximum functions, as shown in Listing 8-4.

__Listing 8-4__Drawing Conclusions from A Rule System

1. `// 1`
2. `let huntPlayerBotRaw = [`
3. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageHigh.rawValue, Fact.PlayerBotNear.rawValue]),`
4. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageMedium.rawValue, Fact.PlayerBotNear.rawValue]),`
5. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageHigh.rawValue, Fact.PlayerBotFar.rawValue]),`
6. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageHigh.rawValue, Fact.PlayerBotMedium.rawValue, Fact.GoodTaskBotMedium.rawValue]),`
7. `]`
8. `let huntPlayerBot = huntPlayerBotRaw.reduce(0.0, combine: max)`
9. `let huntTaskBotRaw = [`
10. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageLow.rawValue, Fact.GoodTaskBotNear.rawValue]),`
11. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageMedium.rawValue, Fact.GoodTaskBotNear.rawValue]),`
12. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageLow.rawValue, Fact.PlayerBotMedium.rawValue, Fact.GoodTaskBotMedium.rawValue]),`
13. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageMedium.rawValue, Fact.PlayerBotFar.rawValue, Fact.GoodTaskBotMedium.rawValue]),`
14. `ruleSystem.minimumGradeForFacts([Fact.BadTaskBotPercentageLow.rawValue, Fact.PlayerBotFar.rawValue, Fact.GoodTaskBotFar.rawValue])`
15. `]`
16. `let huntTaskBot = huntTaskBotRaw.reduce(0.0, combine: max)`
18. `// 2`
19. `if huntPlayerBot >= huntTaskBot && huntPlayerBot > 0.0 {`
20. `guard let playerBotAgent = state.playerBotTarget?.target.agent else { return }`
21. `mandate = .HuntAgent(playerBotAgent)`
22. `} else if huntTaskBot > huntPlayerBot {`
23. `mandate = .HuntAgent(state.nearestGoodTaskBotTarget!.target.agent)`
24. `} else {`
25. `switch mandate {`
26. `case .FollowBadPatrolPath:`
27. `break`
28. `default:`
29. `let closestPointOnBadPath = closestPointOnPath(badPathPoints)`
30. `mandate = .ReturnToPositionOnPath(float2(closestPointOnBadPath))`
31. `}`
32. `}`

The code in this listing performs two main tasks (indicated by the numbered comments above):

1. Compare the grades of facts in the system to draw conclusions.

   In fuzzy logic, the minimum function (in the example above, the [minimumGradeForFacts:](https://developer.apple.com/documentation/gameplaykit/gkrulesystem/1501211-minimumgradeforfacts) call) and the maximum function (the `reduce(_:combine:)` call) behave similarly to the AND and OR operators of Boolean logic. Thus, the `huntPlayerBotRaw` and `huntPlayerBot` calculations are similar to the following pseudocode:

   `huntPlayerBot = (PlayerBotNear AND BadTaskBotPercentageHigh) OR (PlayerBotNear AND BadTaskBotPercentageMedium) OR ...`

   However, unlike in Boolean logic, each element in this calculation is a grade—a level of confidence in an assertion—so the resulting `huntPlayerBot` value is also a grade. You can think of this as a probability: “The likelihood that I should hunt for the player is…”
2. Use the conclusions to choose a course of action.

   This set of `if` statements sets the `TaskBot` object’s `mandate` property to a value that determines its objective for the next few moments of gameplay. If the `huntPlayerBot` score is nonzero and greater than the `huntTaskBot` score, the bot moves to attack the player character; if the `huntTaskBot` score is greater, the bot moves to the nearest good bot to turn it bad; and if both scores are zero, the bot simply patrols its route.

   This objective holds until the next time the `TaskBot` object evaluates its rule system. In the meantime, per-frame update methods in other game components use the `mandate` value to drive the bot’s actions. Depending on the bot’s mandate, the [GKAgent](https://developer.apple.com/documentation/gameplaykit/gkagent) object responsible for the bot’s movement gets a set of goals that cause the bot to find and follow a path toward a target, or a different set of goals that cause the bot to patrol around the game level.

[Agents, Goals, and Behaviors](Agent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tcnzsfvbuqobnknltc)
