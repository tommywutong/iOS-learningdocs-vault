---
title: 'performKeyEquivalent(with:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingview/performkeyequivalent(with:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/performkeyequivalent(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/performkeyequivalent%28with%3A%29.json'
content_hash: 'sha256:4f15bea0dd430dd1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

# performKeyEquivalent(with:)

<sub>Instance Method</sub>

<sub>macOS</sub>

```swift
@MainActor @preconcurrency override dynamic func performKeyEquivalent(with nsEvent: NSEvent) -> Bool
```

## See Also

### Managing keyboard interaction

- [keyDown(with:)](<keydown(with_).md>) — Called when the user presses a key on the keyboard while this view is in the responder chain.
- [keyUp(with:)](<keyup(with_).md>) — Called when the user releases a key on the keyboard while this view is in the responder chain.
- [insertText(_:)](<inserttext(__).md>)
- [didChangeValue(forKey:)](<didchangevalue(forkey_).md>)
- [makeTouchBar()](<maketouchbar().md>)
