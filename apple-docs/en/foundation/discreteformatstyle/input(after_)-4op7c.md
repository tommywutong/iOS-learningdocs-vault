---
title: 'input(after:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/discreteformatstyle/input(after:)-4op7c'
source_url: 'https://developer.apple.com/documentation/foundation/discreteformatstyle/input(after:)-4op7c'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/discreteformatstyle/input%28after%3A%29-4op7c.json'
content_hash: 'sha256:94d801dc82c3981f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DiscreteFormatStyle](../discreteformatstyle.md)

# input(after:)

<sub>Instance Method</sub>

The next input value after the given input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func input(after input: Self.FormatInput) -> Self.FormatInput?
```

## Return Value

The next “greater” input value that can be represented by [FormatInput](../formatstyle/formatinput.md) or an underlying representation the format style uses internally.

## Discussion

Use this function to determine if the return value provided by [discreteInput(before:)](<discreteinput(before_).md>) is precise enough for your use case for any input `y`:

```swift
guard let x = style.discreteInput(before: y) else {
    return
}

let z = style.input(after: x) ?? y
```

If the distance between `x` and `z` is too large for the precision you require, you may want to manually probe [format(_:)](<../formatstyle/format(__).md>) at a higher rate in that interval, as there is no guarantee for what the output will be in that interval.
