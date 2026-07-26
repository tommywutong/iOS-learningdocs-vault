---
title: utf8Span
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/utf8span
source_url: 'https://developer.apple.com/documentation/swift/substring/utf8span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/utf8span.json'
content_hash: 'sha256:be798789d12b9904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# utf8Span

<sub>Instance Property</sub>

A UTF-8 span over the code units that make up this substring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var utf8Span: UTF8Span { get }
```

## Return Value

A `UTF8Span` over the code units of this `Substring`.

## Discussion

> [!note] Note
> On Apple platforms, this property must transcode the code units of bridged UTF-16 `String` instances on every access.
>
> For example, if `string` has the bridged UTF-16 representation,

```swift
  for word in string.split(separator: " ") {
      useSpan(word.span)
  }
```

is accidentally quadratic because of this issue. A workaround is to explicitly convert the string into its native UTF-8 representation:

```swift
  var nativeString = consume string
  nativeString.makeContiguousUTF8()
  for word in nativeString.split(separator: " ") {
      useSpan(word.span)
  }
```

This second option has linear time complexity, as expected.

> [!abstract] Complexity
> O(1) for native UTF-8 strings, O(_n_) for bridged UTF-16 strings.
