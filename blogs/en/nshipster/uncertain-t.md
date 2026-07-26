---
title: Uncertain⟨T⟩
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/uncertainty/'
original_language: en
published: 2025-07-25
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:564753ba208baa60'
translated: false
---

> 原文：[Uncertain⟨T⟩](https://nshipster.com/uncertainty/)　·　NSHipster (Mattt)

# [Uncertain⟨T⟩](https://nshipster.com/uncertainty/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  July 25^th, 2025

You know what’s wrong with people? They’re too sure of themselves.

Better to be wrong and own it than be right with caveats. Hard to build a personal brand out of nuance these days. People are attracted to confidence — however misplaced.

But can you blame them? (People, that is) Working in software, the most annoying part of reaching Senior level is having to say _“it depends”_ all the time. Much more fun getting to say _“let’s ship it and iterate”_ as Staff or _“that won’t scale”_ as a Principal.

Yet, for all of our intellectual humility, why do we ~~write~~ vibe code like this?

```
if currentLocation.distance(to: target) < 100 {
    print("You've arrived!") // But have you, really? 🤨
}
```

GPS coordinates aren’t exact. They’re noisy. They’re approximate. They’re probabilistic. That `horizontalAccuracy` property tucked away in your `CLLocation` object is trying to tell you something important: you’re _probably_ within that radius. _Probably._

A `Bool`, meanwhile, can be only `true` or `false`. That `if` statement needs to make a choice one way or another, but code like this doesn’t capture the uncertainty of the situation. If truth is light, then current programming models collapse the wavefunction too early.

## Picking the Right Abstraction

In 2014, researchers at the University of Washington and Microsoft Research proposed a radical idea: What if uncertainty were encoded directly into the type system? Their paper, _[Uncertain\<T\>: A First-Order Type for Uncertain Data](https://www.microsoft.com/en-us/research/publication/uncertaint-a-first-order-type-for-uncertain-data-2/)_ introduced a probabilistic programming approach that’s both mathematically rigorous and surprisingly practical.

As you’d expect for something from Microsoft in the 2010s, the paper is implemented in C#. But the concepts translate beautifully to Swift.

You can find [my port on GitHub](https://github.com/mattt/Uncertain):

```
import Uncertain
import CoreLocation

let uncertainLocation = Uncertain<CLLocation>.from(currentLocation)
let nearbyEvidence = uncertainLocation.distance(to: target) < 100
if nearbyEvidence.probability(exceeds: 0.95) {
    print("You've arrived!") // With 2σ confidence 🤓
}
```

When you compare two `Uncertain` values, you don’t get a definitive `true` or `false`. You get an `Uncertain<Bool>` that represents the _probability_ of the comparison being `true`.

The same is true for other operators, too:

```
// How fast did we run around the track?
let distance: Double = 400 // meters
let time: Uncertain<Double> = .normal(mean: 60, standardDeviation: 5.0) // seconds
let runningSpeed = distance / time // Uncertain<Double>

// How much air resistance?
let airDensity: Uncertain<Double> = .normal(mean: 1.225, standardDeviation: 0.1) // kg/m³
let dragCoefficient: Uncertain<Double> = .kumaraswamy(alpha: 9, beta: 3) // slightly right-skewed distribution
let frontalArea: Uncertain<Double> = .normal(mean: 0.45, standardDeviation: 0.05) // m²
let airResistance = 0.5 * airDensity * frontalArea * dragCoefficient * (runningSpeed * runningSpeed)
```

This code builds a computation graph, sampling only when you ask for concrete results. The library uses [Sequential Probability Ratio Testing (SPRT)](https://en.wikipedia.org/wiki/Sequential_probability_ratio_test) to efficiently determine how many samples are needed — maybe a few dozen times for simple comparisons, scaling up automatically for complex calculations.

```
// Sampling happens only when we need to evaluate
if ~(runningSpeed > 6.0) {
    print("Great pace for a 400m sprint!")
}
// SPRT might only need a dozen samples for this simple comparison

let sustainableFor5K = (runningSpeed < 6.0) && (airResistance < 50.0)
print("Can sustain for 5K: \(sustainableFor5K.probability(exceeds: 0.9))")
// Might use 100+ samples for this compound condition
```

Using an abstraction like `Uncertain<T>` forces you to deal with uncertainty as a first-class concept rather than pretending it doesn’t exist. And in doing so, you end up with much smarter code.

To quote [Alan Kay](https://en.wikipedia.org/wiki/Alan_Kay):

> Point of view is worth 80 IQ points Alan Kay

---

Before we dive deeper into probability distributions, let’s take a detour to Monaco and talk about [Monte Carlo sampling](https://en.wikipedia.org/wiki/Monte_Carlo_method).

## The Monte Carlo Method

Behold, a classic slot machine (or “fruit machine” for our UK readers 🇬🇧):

```
enum SlotMachine {
    static func spin() -> Int {
        let symbols = [
            "◻️", "◻️", "◻️",  // blanks
            "🍒", "🍋", "🍊", "🍇", "💎"
        ]

        // Spin three reels independently
        let reel1 = symbols.randomElement()!
        let reel2 = symbols.randomElement()!
        let reel3 = symbols.randomElement()!

        switch (reel1, reel2, reel3) {
        case ("💎", "💎", "💎"): return 100  // Jackpot!
        case ("🍒", "🍒", "🍒"): return 10
        case ("🍇", "🍇", "🍇"): return 5
        case ("🍊", "🍊", "🍊"): return 3
        case ("🍋", "🍋", "🍋"): return 2
        case ("🍒", _, _), // Any cherry
             (_, "🍒", _),
             (_, _, "🍒"):
            return 1
        default:
            return 0  // Better luck next time
        }
    }
}
```

Should we play it?

Now, we _could_ work out these probabilities analytically — counting combinations, calculating conditional probabilities, maybe even busting out some combinatorics.

Or we could just let the computer pull the lever a bunch and see what happens.

```
let expectedPayout = Uncertain<Int> {
    SlotMachine.spin()
}.expectedValue(sampleCount: 10_000)
print("Expected value per spin: $\(expectedPayout)")
// Expected value per spin: ≈ $0.56
```

At least we know one thing for certain: _The house always wins._

## Beyond Simple Distributions

While one-armed bandits demonstrate pure randomness, real-world applications often deal with more predictable uncertainty.

`Uncertain<T>` provides a [rich set of probability distributions](https://github.com/mattt/Uncertain?tab=readme-ov-file#distribution-constructors):

```
// Modeling sensor noise
let rawGyroData = 0.85  // rad/s
let gyroReading = Uncertain.normal(
    mean: rawGyroData,
    standardDeviation: 0.05  // Typical gyroscope noise in rad/s
)

// User behavior modeling
let userWillTapButton = Uncertain.bernoulli(probability: 0.3)

// Network latency with long tail
let apiResponseTime = Uncertain.exponential(rate: 0.1)

// Coffee shop visit times (bimodal: morning rush + afternoon break)
let morningRush = Uncertain.normal(mean: 8.5, standardDeviation: 0.5)  // 8:30 AM
let afternoonBreak = Uncertain.normal(mean: 15.0, standardDeviation: 0.8)  // 3:00 PM
let visitTime = Uncertain.mixture(
    of: [morningRush, afternoonBreak],
    weights: [0.6, 0.4]  // Slightly prefer morning coffee
)
```

`Uncertain<T>` also provides comprehensive [statistical operations](https://github.com/mattt/Uncertain?tab=readme-ov-file#statistical-operations):

```
// Basic statistics
let temperature = Uncertain.normal(mean: 23.0, standardDeviation: 1.0)
let avgTemp = temperature.expectedValue() // about 23°C
let tempSpread = temperature.standardDeviation() // about 1°C

// Confidence intervals
let (lower, upper) = temperature.confidenceInterval(0.95)
print("95% of temperatures between \(lower)°C and \(upper)°C")

// Distribution shape analysis
let networkDelay = Uncertain.exponential(rate: 0.1)
let skew = networkDelay.skewness() // right skew
let kurt = networkDelay.kurtosis() // heavy tail

// Working with discrete distributions
let diceRoll = Uncertain.categorical([1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1])!
diceRoll.entropy()  // Randomness measure (~2.57)
(diceRoll + diceRoll).mode() // Most frequent outcome (7, perhaps?)

// Cumulative probability
if temperature.cdf(at: 25.0) < 0.2 {  // P(temp ≤ 25°C) < 20%
    print("Unlikely to be 25°C or cooler")
}
```

The statistics are computed through sampling. The number of samples is configurable, letting you trade computation time for accuracy.

## Putting Theory to Practice

Users don’t notice when things work correctly, but they definitely notice impossible behavior. When your running app claims they just sprinted at 45 mph, or your IRL meetup app shows someone 500 feet away when GPS accuracy is ±1000 meters, that’s a bad look 🤡

So where do we go from here? Let’s channel our Senior+ memes from before for guidance.

That Staff engineer saying _“let’s ship it and iterate”_ is right about the incremental approach. You can migrate uncertain calculations piecemeal rather than rewriting everything at once:

```
extension CLLocation {
    var uncertain: Uncertain<CLLocation> {
        Uncertain<CLLocation>.from(self)
    }
}

// Gradually migrate critical paths
let isNearby = (
    currentLocation.uncertain.distance(to: destination) < threshold
).probability(exceeds: 0.68)
```

And we should consider the Principal engineer’s warning of _“that won’t scale”_. Sampling has a cost, and you should understand the computational overhead for probabilistic accuracy:

```
// Fast approximation for UI updates
let quickEstimate = speed.probability(
    exceeds: walkingSpeed,
    maxSamples: 100
)

// High precision for critical decisions
let preciseResult = speed.probability(
    exceeds: walkingSpeed,
    confidenceLevel: 0.99,
    maxSamples: 10_000
)
```

Start small. Pick one feature where GPS glitches cause user complaints. Replace your distance calculations with uncertain versions. Measure the impact.

Remember: the goal isn’t to eliminate uncertainty — it’s to acknowledge that it exists and handle it gracefully. Because in the real world, nothing is certain except uncertainty itself.

And perhaps, with better tools, we can finally stop pretending otherwise.
