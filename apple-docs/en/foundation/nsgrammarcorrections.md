---
title: NSGrammarCorrections
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsgrammarcorrections
source_url: 'https://developer.apple.com/documentation/foundation/nsgrammarcorrections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgrammarcorrections.json'
content_hash: 'sha256:e37eaab2c80d4cb5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSGrammarCorrections

<sub>Global Variable</sub>

The value for the `NSGrammarCorrections` key should be an `NSArray` of `NSStrings` representing potential substitutions to correct the problem, but it is expected that this may not be available in all cases. `NSGrammarUserDescription` or `NSGrammarCorrections` must be supplied in order for correction guidance to be presented to the user.

<sub>macOS</sub>

```swift
let NSGrammarCorrections: String
```

## See Also

### Constants

- [NSGrammarRange](nsgrammarrange.md) — The value for the `NSGrammarRange` dictionary key should be an `NSValue` containing an `NSRange`, a subrange of the sentence range used as the return value, whose location should be an offset from the beginning of the sentence–so, for example, an `NSGrammarRange` for the first four characters of the overall sentence range should be `{0, 4}`. If the `NSGrammarRange` key is not present in the dictionary it is assumed to be equal to the overall sentence range.
- [NSGrammarUserDescription](nsgrammaruserdescription.md) — The value for the `NSGrammarUserDescription` dictionary key should be an `NSString` containing descriptive text about that range, to be presented directly to the user; it is intended that the user description should provide enough information to allow the user to correct the problem. It is recommended that `NSGrammarUserDescription` be supplied in all cases, however, `NSGrammarUserDescription` or `NSGrammarCorrections` must be supplied in order for correction guidance to be presented to the user.
