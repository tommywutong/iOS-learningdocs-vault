---
title: 'dispatchPrecondition(condition:)'
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchprecondition(condition:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchprecondition(condition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchprecondition%28condition%3A%29.json'
content_hash: 'sha256:3c65b9f186b68cfd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatchPrecondition(condition:)

<sub>Function</sub>

Checks a dispatch condition necessary for further execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dispatchPrecondition(condition: @autoclosure () -> DispatchPredicate)
```

## Parameters

- `condition` — A dispatch predicate for the current context to check.

## Discussion

Use this function to detect conditions about the current execution context that must prevent the program from proceeding even in shipping code.

- In playgrounds and `-Onone` builds (the default for Xcode’s Debug configuration): if `condition` evaluates to `false`, stop program execution in a debuggable state.
- In `-O` builds (the default for Xcode’s Release configuration): if `condition` evaluates to `false`, stop program execution.
- In `-Ounchecked` builds, `condition` is not evaluated, but the optimizer may assume that it would evaluate to `true`. Failure to satisfy that assumption in `-Ounchecked` builds is a serious programming error.

## See Also

### Dispatch Objects

- [DispatchObject](dispatchobject.md) — The base class for most dispatch types.
- [DispatchPredicate](dispatchpredicate.md) — Logical conditions to evaluate within a given execution context.
- [Dispatch Objects](dispatch-objects.md) — The basic behaviors supported by all dispatch types.
