---
title: CTFontDescriptorGetTypeID()
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontdescriptorgettypeid()
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptorgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptorgettypeid%28%29.json'
content_hash: 'sha256:f8bcc0bb5b4d6adf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFontDescriptorGetTypeID()

<sub>Function</sub>

Returns the type identifier for Core Text font descriptor references.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTFontDescriptorGetTypeID() -> CFTypeID
```

## Return Value

The identifier for the [CTFontDescriptor](ctfontdescriptor.md) opaque type.
