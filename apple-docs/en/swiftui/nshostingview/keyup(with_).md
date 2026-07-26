---
title: 'keyUp(with:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/nshostingview/keyup(with:)'
source_url: 'https://developer.apple.com/documentation/swiftui/nshostingview/keyup(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/nshostingview/keyup%28with%3A%29.json'
content_hash: 'sha256:d5b415578a301375'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NSHostingView](../nshostingview.md)

# keyUp(with:)

<sub>Instance Method</sub>

Called when the user releases a key on the keyboard while this view is in the responder chain.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency override dynamic func keyUp(with event: NSEvent)
```

## See Also

### Managing keyboard interaction

- [keyDown(with:)](<keydown(with_).md>) — Called when the user presses a key on the keyboard while this view is in the responder chain.
- [performKeyEquivalent(with:)](<performkeyequivalent(with_).md>)
- [insertText(_:)](<inserttext(__).md>)
- [didChangeValue(forKey:)](<didchangevalue(forkey_).md>)
- [makeTouchBar()](<maketouchbar().md>)
