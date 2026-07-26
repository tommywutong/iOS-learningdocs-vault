---
title: UINibProxiedObjectsKey
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（3.0 起废弃）, iPadOS 2.0+（3.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uinibproxiedobjectskey
source_url: 'https://developer.apple.com/documentation/uikit/uinibproxiedobjectskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinibproxiedobjectskey.json'
content_hash: 'sha256:aae533f05ce6be67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UINibProxiedObjectsKey

<sub>Global Variable</sub>

The runtime replacement objects for any proxy objects in the nib file.

> [!warning] Deprecated
> Use the [UINibExternalObjects](uinib/optionskey/externalobjects.md) key instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const UINibProxiedObjectsKey;
```

## Discussion

In iOS 2, the value for this key is a dictionary that contains the runtime replacement objects for any proxy objects used in the nib file. In this dictionary, the keys are the names associated with the proxy objects and the values are the actual objects from your code that should be used in their place.
