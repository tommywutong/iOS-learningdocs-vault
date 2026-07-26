---
title: CTFontDescriptorMatchingState.stalled
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctfontdescriptormatchingstate/stalled
source_url: 'https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate/stalled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctfontdescriptormatchingstate/stalled.json'
content_hash: 'sha256:a91ca6cd9b23b82f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFontDescriptorMatchingState](../ctfontdescriptormatchingstate.md)

# CTFontDescriptorMatchingState.stalled

<sub>Case</sub>

A state that indicates that matching is stalled, such as while waiting for a server response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case stalled
```

## See Also

### Constants

- [kCTFontDescriptorMatchingDidBegin](didbegin.md) — A state that indicates matching is about to begin.
- [kCTFontDescriptorMatchingDidFinish](didfinish.md) — A state that indicates matching is done.
- [kCTFontDescriptorMatchingWillBeginQuerying](willbeginquerying.md) — A state that indicates communication with the server is about to begin.
- [kCTFontDescriptorMatchingWillBeginDownloading](willbegindownloading.md) — A state that indicates downloading is about to begin.
- [kCTFontDescriptorMatchingDownloading](downloading.md) — A state that indicates downloading is in progress.
- [kCTFontDescriptorMatchingDidFinishDownloading](didfinishdownloading.md) — A state that indicates downloading is done.
- [kCTFontDescriptorMatchingDidMatch](didmatch.md) — A state that indicates the font descriptor match is successful.
- [kCTFontDescriptorMatchingDidFailWithError](didfailwitherror.md) — A state that indicates an error.
