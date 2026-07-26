---
title: 'init(forReadingFrom:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedunarchiver/init(forreadingfrom:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedunarchiver/init(forreadingfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedunarchiver/init%28forreadingfrom%3A%29.json'
content_hash: 'sha256:d979242376fc1e21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedUnarchiver](../nskeyedunarchiver.md)

# init(forReadingFrom:)

<sub>Initializer</sub>

Initializes an archiver to decode data from the specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forReadingFrom data: Data) throws
```

## Parameters

- `data` — An archive previously encoded by [NSKeyedArchiver](../nskeyedarchiver.md).

## Discussion

This initializer enables [requiresSecureCoding](requiressecurecoding.md) by default, and sets the [decodingFailurePolicy](decodingfailurepolicy.md) to [NSDecodingFailurePolicySetErrorAndReturn](../nscoder/decodingfailurepolicy-swift.enum/seterrorandreturn.md).

Call [- finishDecoding](<finishdecoding().md>) when you finish decoding data

This method throws an error if `data` isn’t a valid keyed archive.

> [!important] Important
> If you are adapting existing code to use this initializer, make sure you have adopted [NSSecureCoding](../nssecurecoding.md) in the types you decode. If any call to a `decode`-prefixed method fails, the default [decodingFailurePolicy](decodingfailurepolicy.md) sets the [error](../nscoder/error.md) rather than throwing an exception. In this case, the current and all subsequent decode calls return `0` or `nil`.

## See Also

### Creating a Keyed Unarchiver

- [- init](<init().md>) — Initializes an archiver to decode data. _(deprecated)_
- [- initForReadingWithData:](<init(forreadingwith_).md>) — Initializes an archiver to decode data from the specified location. _(deprecated)_
