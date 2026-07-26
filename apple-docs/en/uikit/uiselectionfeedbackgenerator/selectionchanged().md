---
title: selectionChanged()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiselectionfeedbackgenerator/selectionchanged()
source_url: 'https://developer.apple.com/documentation/uikit/uiselectionfeedbackgenerator/selectionchanged()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiselectionfeedbackgenerator/selectionchanged%28%29.json'
content_hash: 'sha256:5fbf2c67a4af3f7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISelectionFeedbackGenerator](../uiselectionfeedbackgenerator.md)

# selectionChanged()

<sub>Instance Method</sub>

Triggers selection feedback.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func selectionChanged()
```

## Discussion

This method tells the generator that the user has changed a selection. In response, the generator may play the appropriate haptics. Don’t use this feedback when the user makes or confirms a selection; use it only when the selection changes.

For information on setting up a feedback generator, see the [UIFeedbackGenerator](../uifeedbackgenerator.md) class.

## See Also

### Related Documentation

- [- prepare](<../uifeedbackgenerator/prepare().md>) — Prepares the generator to trigger feedback.

### Reporting selection changes

- [- selectionChangedAtLocation:](<selectionchanged(at_).md>) — Triggers selection feedback at the specified location.
