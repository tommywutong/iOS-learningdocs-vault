---
title: 'browserAccessibilityDeleteTextAtCursor(numberOfCharacters:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, macOS, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/browseraccessibilitydeletetextatcursor(numberofcharacters:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/browseraccessibilitydeletetextatcursor(numberofcharacters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/browseraccessibilitydeletetextatcursor%28numberofcharacters%3A%29.json'
content_hash: 'sha256:6c258c64de66cb30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# browserAccessibilityDeleteTextAtCursor(numberOfCharacters:)

<sub>Instance Method</sub>

Deletes text from the element at the current cursor position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func browserAccessibilityDeleteTextAtCursor(numberOfCharacters: Int)
```

## Parameters

- `numberOfCharacters` — The number of characters to delete.

## See Also

### Improving browser accessibility

- [- browserAccessibilityAttributedValueInRange:](<browseraccessibilityattributedvalue(in_).md>) — Returns the value for this element within the given range, as an attributed string.
- [- browserAccessibilityInsertTextAtCursor:](<browseraccessibilityinserttextatcursor(text_).md>) — Inserts text into the element at the current cursor position.
- [- browserAccessibilitySelectedTextRange](<browseraccessibilityselectedtextrange().md>) — Returns the range of selected text in the element.
- [- browserAccessibilitySetSelectedTextRange:](<browseraccessibilitysetselectedtextrange(__).md>) — Updates the element’s selected text.
- [- browserAccessibilityValueInRange:](<browseraccessibilityvalue(in_).md>) — Returns this element’s value in the given range.
- [browserAccessibilityContainerType](browseraccessibilitycontainertype.md) — The kind of container that contains this element.
- [browserAccessibilityCurrentStatus](browseraccessibilitycurrentstatus.md) — A string that’s the element’s value for aria-current.
- [browserAccessibilityHasDOMFocus](browseraccessibilityhasdomfocus.md) — A Boolean value that indicates whether the element has native focus in the browser Document Object Model.
- [browserAccessibilityIsRequired](browseraccessibilityisrequired.md) — A Boolean value that’s the element’s value for aria-required.
- [browserAccessibilityPressedState](browseraccessibilitypressedstate.md) — The element’s value for aria-pressed.
- [browserAccessibilityRoleDescription](browseraccessibilityroledescription.md) — A string that describes the element’s role for assistive technologies.
- [browserAccessibilitySortDirection](browseraccessibilitysortdirection.md) — A string that’s the element’s value for aria-sort.
