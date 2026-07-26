---
title: 'input(before:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/discreteformatstyle/input(before:)'
source_url: 'https://developer.apple.com/documentation/foundation/discreteformatstyle/input(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/discreteformatstyle/input%28before%3A%29.json'
content_hash: 'sha256:7835b98ff930a62d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DiscreteFormatStyle](../discreteformatstyle.md)

# input(before:)

<sub>Instance Method</sub>

The next input value before the given input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func input(before input: Self.FormatInput) -> Self.FormatInput?
```

## Return Value

The next “smalller” input value that can be represented by [FormatInput](../formatstyle/formatinput.md) or an underlying representation the format style uses internally.

## Discussion

Use this function to determine if the return value provided by [discreteInput(after:)](<discreteinput(after_).md>) is precise enough for your use case for any input `y`:

```swift
guard let x = style.discreteInput(after: y) else {
    return
}

let z = style.input(before: x) ?? y
```

If the distance between `z` and `x` is too large for the precision you require, you may want to manually probe [format(_:)](<../formatstyle/format(__).md>) at a higher rate in that interval, as there is no guarantee for what the output will be in that interval.

## Default Implementations

### DiscreteFormatStyle Implementations

- [input(before:)](<input(before_)-4vowu.md>) — The next input value before the given input.
- [input(before:)](<input(before_)-78v7r.md>) — The next input value before the given input.
- [input(before:)](<input(before_)-7kuw0.md>) — The next input value before the given input.
- [input(before:)](<input(before_)-guib.md>) — The next input value before the given input.
