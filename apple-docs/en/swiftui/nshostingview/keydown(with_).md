---
title: 'keyDown(with:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingview/keydown(with:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/keydown(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/keydown%28with%3A%29.json'
content_hash: 'sha256:45a173003ff2bf7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

# keyDown(with:)

<sub>Instance Method</sub>

Called when the user presses a key on the keyboard while this view is in the responder chain.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency override dynamic func keyDown(with event: NSEvent)
```

## See Also

### Managing keyboard interaction

- [keyUp(with:)](<keyup(with_).md>) — Called when the user releases a key on the keyboard while this view is in the responder chain.
- [performKeyEquivalent(with:)](<performkeyequivalent(with_).md>)
- [insertText(_:)](<inserttext(__).md>)
- [didChangeValue(forKey:)](<didchangevalue(forkey_).md>)
- [makeTouchBar()](<maketouchbar().md>)
