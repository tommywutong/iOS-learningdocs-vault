---
title: completionBlock()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction/completionblock()
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/completionblock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/completionblock%28%29.json'
content_hash: 'sha256:0036b6ce99721fc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# completionBlock()

<sub>Type Method</sub>

Returns the completion block object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func completionBlock() -> (() -> Void)?
```

## Discussion

See [+ setCompletionBlock:](<setcompletionblock(__).md>) for a description of the role of the completion block object.

## See Also

### Getting and Setting Completion Block Objects

- [+ setCompletionBlock:](<setcompletionblock(__).md>) — Sets the completion block object.
