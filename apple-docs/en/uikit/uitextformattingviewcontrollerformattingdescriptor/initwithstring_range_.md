---
title: 'initWithString:range:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextformattingviewcontrollerformattingdescriptor/initwithstring:range:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingviewcontrollerformattingdescriptor/initwithstring:range:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingviewcontrollerformattingdescriptor/initwithstring%3Arange%3A.json'
content_hash: 'sha256:6f7443a960151dcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFormattingViewControllerFormattingDescriptor](../uitextformattingviewcontrollerformattingdescriptor.md)

# initWithString:range:

<sub>Instance Method</sub>

Initializes formatting descriptor with a string and selected range of string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithString:(NSAttributedString *) string range:(NSRange) range;
```

## Parameters

- `string` — Attributed string for which we are creating formatting descriptor.

- `range` — Range of string that is being represented by descriptor
