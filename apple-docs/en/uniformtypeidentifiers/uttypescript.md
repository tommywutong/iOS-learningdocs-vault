---
title: UTTypeScript
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypescript
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypescript'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypescript.json'
content_hash: 'sha256:0e32d0bb15ab3a5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeScript

<sub>Global Variable</sub>

A base type that represents any scripting language source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeScript;
```

## Discussion

The identifier for this type is `public.script`.

This type conforms to [UTTypeSourceCode](uttypesourcecode.md).

## See Also

### Scripted programming language sources

- [UTTypeAppleScript](uttypeapplescript.md) — A type that represents an AppleScript text-based script.
- [UTTypeJavaScript](uttypejavascript.md) — A type that represents JavaScript source code.
- [UTTypeOSAScript](uttypeosascript.md) — A type that represents an Open Scripting Architecture binary script.
- [UTTypeOSAScriptBundle](uttypeosascriptbundle.md) — A type that represents an Open Scripting Architecture script bundle.
- [UTTypeMakefile](uttypemakefile.md) — A type that represents a Makefile.
- [UTTypeShellScript](uttypeshellscript.md) — A base type that represents a shell script.
- [UTTypePythonScript](uttypepythonscript.md) — A type that represents a Python script.
- [UTTypeRubyScript](uttyperubyscript.md) — A type that represents a Ruby script.
- [UTTypePerlScript](uttypeperlscript.md) — A type that represents a Perl script.
- [UTTypePHPScript](uttypephpscript.md) — A type that represents a PHP script.
