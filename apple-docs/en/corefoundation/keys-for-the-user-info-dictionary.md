---
title: Keys for the user info dictionary
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/keys-for-the-user-info-dictionary
source_url: 'https://developer.apple.com/documentation/corefoundation/keys-for-the-user-info-dictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/keys-for-the-user-info-dictionary.json'
content_hash: 'sha256:4cce2f77deaef09f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFError](cferror.md)

# Keys for the user info dictionary

<sub>API Collection</sub>

Keys in the `userInfo` dictionary.

## Overview

When you create a user info dictionary, at a minimum you should provide values for one of `kCFErrorLocalizedDescriptionKey` and `kCFErrorLocalizedFailureReasonKey`; ideally you should provide values for `kCFErrorLocalizedDescriptionKey`, `kCFErrorLocalizedFailureReasonKey`, and  `kCFErrorLocalizedRecoverySuggestionKey`. Typically, you should provide a value for one of either `kCFErrorURLKey` or `kCFErrorFilePathKey`.

## Topics

### Constants

- [kCFErrorLocalizedDescriptionKey](kcferrorlocalizeddescriptionkey.md) — Key to identify the user-presentable description in the `userInfo` dictionary.
- [kCFErrorLocalizedFailureReasonKey](kcferrorlocalizedfailurereasonkey.md) — Key to identify the user-presentable failure reason in the `userInfo` dictionary.
- [kCFErrorLocalizedRecoverySuggestionKey](kcferrorlocalizedrecoverysuggestionkey.md) — Key to identify the user-presentable recovery suggestion in the `userInfo` dictionary.
- [kCFErrorDescriptionKey](kcferrordescriptionkey.md) — Key to identify the description in the `userInfo` dictionary.
- [kCFErrorUnderlyingErrorKey](kcferrorunderlyingerrorkey.md) — Key to identify the underlying error in the `userInfo` dictionary.
- [kCFErrorURLKey](kcferrorurlkey.md) — Key to identify associated URL in the `userInfo` dictionary.
- [kCFErrorFilePathKey](kcferrorfilepathkey.md) — Key to identify associated file path in the `userInfo` dictionary.

## See Also

### Constants

- [Error domains](error-domains.md) — These constants define domains for CFError objects.
