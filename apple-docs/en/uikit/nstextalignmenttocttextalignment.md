---
title: NSTextAlignmentToCTTextAlignment
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextalignmenttocttextalignment
source_url: 'https://developer.apple.com/documentation/uikit/nstextalignmenttocttextalignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextalignmenttocttextalignment.json'
content_hash: 'sha256:a70aea1245b838c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextAlignmentToCTTextAlignment

<sub>Function</sub>

Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern CTTextAlignment NSTextAlignmentToCTTextAlignment(NSTextAlignment nsTextAlignment);
```

## Parameters

- `nsTextAlignment` — The UIKit text alignment constant you want to convert.

## Return Value

The Core Text alignment that corresponds to the value specified in `nsTextAlignment`.

## Discussion

Use this function when you need to map between the UIKit and Core Text constants for text alignment.

## See Also

### Text manipulations

- [NSTextAlignmentFromCTTextAlignment](<nstextalignment/init(__).md>) — Converts a Core Text alignment constant value to the matching constant value in UIKit.
