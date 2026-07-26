---
title: prepare()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifeedbackgenerator/prepare()
source_url: 'https://developer.apple.com/documentation/uikit/uifeedbackgenerator/prepare()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifeedbackgenerator/prepare%28%29.json'
content_hash: 'sha256:7f049ad5ab7820f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFeedbackGenerator](../uifeedbackgenerator.md)

# prepare()

<sub>Instance Method</sub>

Prepares the generator to trigger feedback.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func prepare()
```

## Discussion

When you call this method, the generator is placed into a prepared state for a short period of time. While the generator is prepared, you can trigger feedback with lower latency.

Think about when you can best prepare your generators. Call [- prepare](<prepare().md>) before the event that triggers feedback. The system needs time to prepare the Taptic Engine for minimal latency. Calling [- prepare](<prepare().md>) and then immediately triggering feedback (without any time in between) does not improve latency.

To conserve power, the Taptic Engine returns to an idle state after any of the following events:

- You trigger feedback on the generator.
- A short period of time passes (typically seconds).
- The generator is deallocated.

After feedback is triggered, the Taptic Engine returns to its idle state. If you might trigger additional feedback within the next few seconds, immediately call [- prepare](<prepare().md>) to keep the Taptic Engine in the prepared state.

You can also extend the prepared state by repeatedly calling the [- prepare](<prepare().md>) method. However, if you continue calling [- prepare](<prepare().md>) without ever triggering feedback, the system may eventually place the Taptic Engine back in an idle state and ignore any further [- prepare](<prepare().md>) calls until after you trigger feedback at least once.

If you no longer need a prepared generator, remove all references to the generator object and let the system deallocate it. This lets the Taptic Engine return to its idle state.

> [!note] Note
> The [- prepare](<prepare().md>) method is optional; however, it is highly recommended. Calling this method helps ensure that your feedback has the lowest possible latency.

## See Also

### Related Documentation

- [- selectionChanged](<../uiselectionfeedbackgenerator/selectionchanged().md>) — Triggers selection feedback.
- [- impactOccurred](<../uiimpactfeedbackgenerator/impactoccurred().md>) — Triggers impact feedback.
- [- notificationOccurred:](<../uinotificationfeedbackgenerator/notificationoccurred(__).md>) — Triggers notification feedback.
