---
title: lineLimit
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/linelimit
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/linelimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/linelimit.json'
content_hash: 'sha256:265c6c8a0803c9d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# lineLimit

<sub>Instance Property</sub>

The maximum number of lines that text can occupy in a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var lineLimit: Int? { get set }
```

## Discussion

The maximum number of lines is `1` if the value is less than `1`. If the value is `nil`, the text uses as many lines as required. The default is `nil`.

## See Also

### Limiting line count for multiline text

- [lineLimit(_:)](<../view/linelimit(__).md>) — Sets to a closed range the number of lines that text can occupy in this view.
- [lineLimit(_:reservesSpace:)](<../view/linelimit(__reservesspace_).md>) — Sets a limit for the number of lines text can occupy in this view.
