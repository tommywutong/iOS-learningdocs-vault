---
title: dictationRecordingDidEnd()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/dictationrecordingdidend()
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/dictationrecordingdidend()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/dictationrecordingdidend%28%29.json'
content_hash: 'sha256:6557ff68adccae6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# dictationRecordingDidEnd()

<sub>Instance Method</sub>

Tells the object when there is a pending dictation result.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func dictationRecordingDidEnd()
```

## Discussion

Implement this optional method if you want to respond to the completion of the recognition of a dictated phrase.

## See Also

### Using dictation

- [- dictationRecognitionFailed](<dictationrecognitionfailed().md>) — Tells the object when dictation ends, but recognition fails.
- [- insertDictationResult:](<insertdictationresult(__).md>) — Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [insertDictationResultPlaceholder](insertdictationresultplaceholder.md) — Asks for the placeholder object to use while generating dictation results.
- [- frameForDictationResultPlaceholder:](<frame(fordictationresultplaceholder_).md>) — Asks for the rectangle for displaying the dictation placeholder animation.
- [- removeDictationResultPlaceholder:willInsertResult:](<removedictationresultplaceholder(__willinsertresult_).md>) — Tells the view that the specified placeholder object is unnecessary.
