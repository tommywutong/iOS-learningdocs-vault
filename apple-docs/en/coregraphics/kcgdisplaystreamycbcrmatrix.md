---
title: kCGDisplayStreamYCbCrMatrix
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgdisplaystreamycbcrmatrix
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgdisplaystreamycbcrmatrix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgdisplaystreamycbcrmatrix.json'
content_hash: 'sha256:36dc3b91a72fa513'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGDisplayStreamYCbCrMatrix

<sub>Global Variable</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
extern CFStringRef const kCGDisplayStreamYCbCrMatrix;
```

## Discussion

When outputting frames in 420v or 420f format, this key may be used to control which YCbCr matrix is used The value should be one of the three kCGDisplayStreamYCbCrMatrix values specified below.
