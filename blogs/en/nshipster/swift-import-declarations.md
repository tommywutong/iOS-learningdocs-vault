---
title: Swift Import Declarations
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/import/'
original_language: en
published: 2019-01-07
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:ac107f0d610ce0a2'
translated: false
---

> 原文：[Swift Import Declarations](https://nshipster.com/import/)　·　NSHipster (Mattt)

# [Swift Import Declarations](https://nshipster.com/import/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  January 7^th, 2019

One of the first lessons we learn as software developers is how to organize concepts and functionality into discrete units. At the smallest level, this means thinking about types and methods and properties. These pieces then form the basis of one or more modules, which may then be packaged into libraries or frameworks.

In this way, import declarations are the glue that holds everything together.

Yet despite their importance, most Swift developers are familiar only with their most basic form:

```
import module
```

This week on NSHipster, we’ll explore the other shapes of this most prominent part of Swift.

---

An import declaration allows your code to access symbols that are declared in other files. However, if more than one module declares a function or type with the same name, the compiler may not be able to tell which one you want to call in code.

To demonstrate this, consider two modules representing the multisport competitions of [Triathlon](https://en.wikipedia.org/wiki/Triathlon) and [Pentathlon](https://en.wikipedia.org/wiki/Modern_pentathlon):

A triathlon consists of three events: swimming, cycling, and running.

```
// Triathlon Module
func swim() {
    print("🏊‍ Swim 1.5 km")
}

func bike() {
    print("🚴 Cycle 40 km")
}

func run() {
    print("🏃‍ Run 10 km")
}
```

The modern pentathlon comprises five events: fencing, swimming, equestrian, shooting, and running.

```
// Pentathlon Module
func fence() {
    print("🤺 Bout with épées")
}

func swim() {
    print("🏊‍ Swim 200 m")
}

func ride() {
    print("🏇 Complete a show jumping course")
}

func shoot() {
    print("🎯 Shoot 5 targets")
}

func run() {
    print("🏃‍ Run 3 km cross-country")
}
```

If we import either of the modules individually, we can reference each of their functions using their unqualified names without a problem.

```
import Triathlon

swim() // OK, calls Triathlon.swim
bike() // OK, calls Triathlon.bike
run() // OK, calls Triathlon.run
```

But if we import both modules together, we can’t always use unqualified function names. Triathlon and Pentathlon both include swimming and running, so a reference to `swim()` is ambiguous.

```
import Triathlon
import Pentathlon

bike() // OK, calls Triathlon.bike
fence() // OK, calls Pentathlon.fence
swim() // Error, ambiguous
```

How do we reconcile this? One strategy is to use fully-qualified names to work around any ambiguous references. By including the module name, there’s no confusion about whether the program will swim a few laps in a pool or a mile in open water.

```
import Triathlon
import Pentathlon

Triathlon.swim() // OK, fully-qualified reference to Triathlon.swim
Pentathlon.swim() // OK, fully-qualified reference to Pentathlon.swim
```

Another way to resolve API name collision is to change the import declaration to be more selective about what’s included from each module.

## Importing Individual Declarations

Import declarations have a form that can specify individual structures, classes, enumerations, protocols, and type aliases as well as functions, constants, and variables declared at the top-level:

```
import kind module.symbol
```

Here, `kind` can be any of the following keywords:

| Kind | Description |
|---|---|
| `struct` | Structure |
| `class` | Class |
| `enum` | Enumeration |
| `protocol` | Protocol |
| `typealias` | Type Alias |
| `func` | Function |
| `let` | Constant |
| `var` | Variable |

For example, the following import declaration adds only the `swim()` function from the `Pentathlon` module:

```
import func Pentathlon.swim

swim() // OK, calls Pentathlon.swim
fence() // Error, unresolved identifier
```

### Resolving Symbol Name Collisions

When multiple symbols are referenced by the same name in code, the Swift compiler resolves this reference by consulting the following, in order:

1. Local Declarations
2. Imported Declarations
3. Imported Modules

If any of these have more than one candidate, Swift is unable to resolve the ambiguity and raises a compilation error.

For example, importing the `Triathlon` module provides the `swim()`, `bike()`, and `run()` methods. The imported `swim()` function declaration from the `Pentathlon` overrides that of the `Triathlon` module. Likewise, the locally-declared `run()` function overrides the symbol by the same name from `Triathlon`, and would also override any imported function declarations.

```
import Triathlon
import func Pentathlon.swim

// Local function shadows whole-module import of Triathlon
func run() {
    print("🏃‍ Run 42.195 km")
}

swim() // OK, calls Pentathlon.swim
bike() // OK, calls Triathlon.bike
run() //  OK, calls local run
```

The result of calling this code? A bizarre multi-sport event involving a few laps in the pool, a modest bike ride, and a marathon run. _(@ us, IRONMAN)_

### Clarifying and Minimizing Scope

Beyond resolving name collisions, importing declarations can also be a way to clarify your intent as a programmer.

If you’re, for example, using only a single function from a mega-framework like AppKit, you might single that out in your import declaration.

```
import func AppKit.NSUserName

NSUserName() // "jappleseed"
```

This technique can be especially helpful when importing top-level constants and variables, whose provenance is often more difficult to discern than other imported symbols.

For example, the Darwin framework exports — among other things — a top-level `stderr` variable. An explicit import declaration here can preempt any questions during code review about where that variable is coming from.

```
import func Darwin.fputs
import var Darwin.stderr

struct StderrOutputStream: TextOutputStream {
    mutating func write(_ string: String) {
        fputs(string, stderr)
    }
}

var standardError = StderrOutputStream()
print("Error!", to: &standardError)
```

## Importing a Submodule

The final form of import declarations offers another way to limit API exposure:

```
import module.submodule
```

You’re most likely to encounter submodules in large system frameworks like AppKit and Accelerate. These [umbrella frameworks](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/FrameworkAnatomy.html#//apple_ref/doc/uid/20002253-97623-BAJJHAJC) are no longer considered a best-practice, but they served an important role during Apple’s transition to Cocoa in the early 00’s.

For example, you might import only the [DictionaryServices](https://nshipster.com/dictionary-services/) submodule from the [Core Services framework](https://developer.apple.com/documentation/coreservices) to insulate your code from the myriad deprecated APIs like Carbon Core.

```
import Foundation
import CoreServices.DictionaryServices

func define(_ word: String) -> String? {
    let nsstring = word as NSString
    let cfrange = CFRange(location: 0, length: nsstring.length)

    guard let definition = DCSCopyTextDefinition(nil, nsstring, cfrange) else {
        return nil
    }

    return String(definition.takeUnretainedValue())
}

define("apple") // "apple | ˈapəl | noun 1 the round fruit of a tree..."
```

In practice, isolating imported declarations and submodules doesn’t confer any real benefit beyond signaling programmer intent. Your code won’t compile any faster doing it this way. And since most submodules seem to re-import their umbrella header, this approach won’t do anything to reduce noise in autocomplete lists.

---

Like many obscure and advanced topics, the most likely reason you haven’t heard about these import declaration forms before is that you don’t need to know about them. If you’ve gotten this far making apps without them, you can be reasonably assured that you don’t need to start using them now.

Rather, the valuable takeaway here is understanding how the Swift compiler resolves name collisions. And to that end, import declarations are a concept of great import.
