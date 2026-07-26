---
title: 'matchingFontDescriptors(withMandatoryKeys:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifontdescriptor/matchingfontdescriptors(withmandatorykeys:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/matchingfontdescriptors(withmandatorykeys:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/matchingfontdescriptors%28withmandatorykeys%3A%29.json'
content_hash: 'sha256:2e82d4e6900ca39c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFontDescriptor](../uifontdescriptor.md)

# matchingFontDescriptors(withMandatoryKeys:)

<sub>Instance Method</sub>

Returns all the fonts available in the system with specified attributes that match those of the font.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func matchingFontDescriptors(withMandatoryKeys mandatoryKeys: Set<UIFontDescriptor.AttributeName>?) -> [UIFontDescriptor]
```

## Parameters

- `mandatoryKeys` — Keys that must be identical to be matched. Can be `nil`.

## Return Value

The matching font descriptors. If the attribute value specified does not exist in the input dictionary or if there is no font that matches the given mandatory key values, an empty array is returned.

## Discussion

For example, suppose there are two versions of a given font installed that differ in the number of glyphs covered (the new version has more glyphs). If you explicitly specify `UIFontDescriptorNameAttribute` as the only mandatory key, then a font descriptor that specifies a font name and character set by default matches both versions, because the character set attribute isn’t used for matching. If you specify that font name and character set keys are mandatory, the returned array contains only the font that matches both keys.
