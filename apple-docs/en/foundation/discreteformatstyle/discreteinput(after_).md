---
title: 'discreteInput(after:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/discreteformatstyle/discreteinput(after:)'
source_url: 'https://developer.apple.com/documentation/foundation/discreteformatstyle/discreteinput(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/discreteformatstyle/discreteinput%28after%3A%29.json'
content_hash: 'sha256:3e73c51602144233'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DiscreteFormatStyle](../discreteformatstyle.md)

# discreteInput(after:)

<sub>Instance Method</sub>

The next discretization boundary after the given input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func discreteInput(after input: Self.FormatInput) -> Self.FormatInput?
```

## Return Value

For most `input`s, the method returns the “smallest” value “greater” than `input` for which the style produces a different [FormatOutput](../formatstyle/formatoutput.md), or `nil` if no such value exists. For some input values, the function may also return a value “greater” than `input` for which the style still produces the same [FormatOutput](../formatstyle/formatoutput.md) as for `input`.

## Discussion

Use this function to determine the next “greater” input that warrants updating the formatted output. The following example prints all possible outputs the format style can produce upwards starting from the `startInput`:

```swift
var previousInput = startInput
while let nextInput = style.discreteInput(after: previousInput) {
    print(style.format(nextInput))
    previousInput = nextInput
}
```
