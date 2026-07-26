---
title: UTTypeEXE
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeexe
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeexe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeexe.json'
content_hash: 'sha256:1af2cd830307a75a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeEXE

<sub>Global Variable</sub>

A type that represents a Windows executable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeEXE;
```

## Discussion

The identifier for this type is `public.windows-executable`.

This type conforms to [UTTypeData](uttypedata.md) and [UTTypeExecutable](uttypeexecutable.md).

## See Also

### Executables

- [UTTypeExecutable](uttypeexecutable.md) — A type that represents an executable.
- [UTTypeUnixExecutable](uttypeunixexecutable.md) — A type that represents a UNIX executable.
