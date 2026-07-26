---
title: kSecTransformActionCanExecute
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformactioncanexecute
source_url: 'https://developer.apple.com/documentation/security/ksectransformactioncanexecute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformactioncanexecute.json'
content_hash: 'sha256:087f20c3879804b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformActionCanExecute

<sub>Global Variable</sub>

An action that triggers to verify that all required attributes are either set or connected to another transform.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformActionCanExecute: CFString
```

## Discussion

Overrides the standard behavior that checks to see if all of the required attributes either have been set or are connected to another transform. When overriding the default behavior the developer can decided what the necessary data is to have for a transform to be considered ‘ready to run’. Returning NULL means that the transform is ready to be run. If the transform is NOT ready to run then the override should return a CFErrorRef stipulating the error.
