---
title: Capture
framework: RegexBuilder
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/capture
source_url: 'https://developer.apple.com/documentation/regexbuilder/capture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/capture.json'
content_hash: 'sha256:6c741ad1c45e5077'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# Capture

<sub>Structure</sub>

A regex component that saves the matched substring, or a transformed result, for access in a regex match.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Capture<Output>
```

## Overview

Use a `Capture` component to capture one part of a regex to access separately after matching. In the example below, `regex` matches a dollar sign (`"$"`) followed by one or more digits, a period (`"."`), and then two additional digits, as long as that pattern appears at the end of the line. Because the `Capture` block wraps the digits and period, that part of the match is captured separately.

```swift
let transactions = """
    CREDIT     109912311421    Payroll   $69.73
    CREDIT     105912031123    Travel   $121.54
    DEBIT      107733291022    Refund    $8.42
    """

let regex = Regex {
    "$"
    Capture {
      OneOrMore(.digit)
      "."
      Repeat(.digit, count: 2)
    }
    Anchor.endOfLine
}

// The type of each match's output is `(Substring, Substring)`.
for match in transactions.matches(of: regex) {
    print("Transaction amount: \(match.1)")
}
// Prints "Transaction amount: 69.73"
// Prints "Transaction amount: 121.54"
// Prints "Transaction amount: 8.42"
```

Each `Capture` block increases the number of components in the regex’s output type. In the example above, the capture type of each match is `(Substring, Substring)`.

By providing a transform function to the `Capture` block, you can change the type of the captured value from `Substring` to the result of the transform. This example declares `doubleValueRegex`, which converts the captured amount to a `Double`:

```swift
let doubleValueRegex = Regex {
    "$"
    Capture {
        OneOrMore(.digit)
        "."
        Repeat(.digit, count: 2)
    } transform: { Double($0)! }
    Anchor.endOfLine
}

// The type of each match's output is `(Substring, Double)`.
for match in transactions.matches(of: doubleValueRegex) {
    if match.1 >= 100.0 {
        print("Large amount: \(match.1)")
    }
}
// Prints "Large amount: 121.54"
```

Throwing an error from a `transform` closure aborts matching and propagates the error out to the caller. If you instead want to use a failable transformation, where a `nil` result participates in matching, use [TryCapture](trycapture.md) instead of `Capture`.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [RegexComponent](../swift/regexcomponent.md)

## Topics

### Initializers

- [init(_:)](<capture/init(__)-1tmsz.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-2f52u.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-3fgv4.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-3iklm.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-3o4p2.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-46rdv.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-4guoe.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-53k6l.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-5wvbp.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-6972d.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-6gd4p.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-6w2zh.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-751s0.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-7adb5.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-7gbb2.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-7o3nk.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-8e156.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-8hde2.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-9a7se.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-9u8yf.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-dm5i.md>) — Creates a capture for the given component.
- [init(_:)](<capture/init(__)-zp0c.md>) — Creates a capture for the given component.
- [init(_:as:)](<capture/init(__as_)-1ugzr.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-25etj.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-3466q.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-5mhxe.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-5xnic.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-6w075.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-7rcvh.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-82c2j.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-8zsdh.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-9f35e.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:)](<capture/init(__as_)-sg1w.md>) — Creates a capture for the given component using the specified reference.
- [init(_:as:transform:)](<capture/init(__as_transform_)-14ci9.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-1k7ca.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-2h2hm.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-50rsk.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-57wgq.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-7pm1.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-8qyac.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-8yapk.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-9j2it.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-i2lv.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:as:transform:)](<capture/init(__as_transform_)-kflo.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-186es.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-18ik6.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-1kfgs.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-1ns5b.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-1t85c.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-1vbtc.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-2fsxr.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-36nfu.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-36y0i.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-4bhm9.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-54rby.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-58e84.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-5loer.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-5nqht.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-5qnr.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-69jbe.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-6u44c.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-7ndmv.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-8l6vq.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-98vy5.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-9yayx.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(_:transform:)](<capture/init(__transform_)-qygd.md>) — Creates a capture for the given component, transforming with the given closure.
- [init(as:_:)](<capture/init(as___)-3d6el.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-3vlcx.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-4l8eh.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-51as9.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-56h1c.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-6esnr.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-7fs07.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-7rh88.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-8s7ds.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-9isum.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:)](<capture/init(as___)-9y6av.md>) — Creates a capture for the given component using the specified reference.
- [init(as:_:transform:)](<capture/init(as___transform_)-15sg2.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-1cz24.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-1e5w2.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-4elzn.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-617oo.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-68hzv.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-6h4i.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-6tdp8.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-82pi.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-c8qs.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.
- [init(as:_:transform:)](<capture/init(as___transform_)-jvkx.md>) — Creates a capture for the given component using the specified reference, transforming with the given closure.

## See Also

### Captures

- [TryCapture](trycapture.md) — A regex component that attempts to transform a matched substring, saving the result if successful and backtracking if the transformation fails.
- [Reference](reference.md) — A reference to a captured portion of a regular expression.
