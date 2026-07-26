---
title: 'discreteInput(after:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/componentsformatstyle/discreteinput(after:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/componentsformatstyle/discreteinput(after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/componentsformatstyle/discreteinput%28after%3A%29.json'
content_hash: 'sha256:217d754d2946b6d3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ComponentsFormatStyle](../componentsformatstyle.md)

# discreteInput(after:)

<sub>Instance Method</sub>

The next discretization boundary after the given input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func discreteInput(after input: Range<Date>) -> Range<Date>?
```

## Return Value

If [isPositive](ispositive.md) is true, the range `input.lowerBound..<x`, where `x` is the greatest date that is smaller than `input.upperBound` for which this style might produce a different [FormatOutput](../../formatstyle/formatoutput.md). If [isPositive](ispositive.md) is false, the range `x..<input.upperBound`, where `x` is the smallest date that is greater than `input.lowerBound` for which this style might produce a different [FormatOutput](../../formatstyle/formatoutput.md). The function may return `nil` if there is no such value smaller or equal to `input.upperBound`.

## Discussion

Use this function to determine the next greater input that warrants updating the formatted output. If [isPositive](ispositive.md) is true, the returned range has the same `lowerBound` as the `input`, but increases the `upperBound` so that the returned range produces the next greater output. If [isPositive](ispositive.md) is false, the returned range has the same `upperBound` as the `input` and a greater `lowerBound`.

```
let style = Date.ComponentsFormatStyle(style: .wide)
print(style.format(start..<end)) // "1 hour"
guard let next = style.discreteInput(after: start..<end) else {
    return
}
print(style.format(next)) // "1 hour, 1 second"
```
