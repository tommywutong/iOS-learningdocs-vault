---
title: Preparing your interface for localization
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/preparing-your-interface-for-localization
source_url: 'https://developer.apple.com/documentation/xcode/preparing-your-interface-for-localization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/preparing-your-interface-for-localization.json'
content_hash: 'sha256:121b30097d340f01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Localization](localization.md)

# Preparing your interface for localization

<sub>Article</sub>

Find text in your app that needs translation and verify that your interface adapts to translated text.

## Overview

Before you localize your app, use Xcode to identify nonlocalized strings in your interface and to verify whether your interface adjusts to the characteristics of localized strings.

### Find nonlocalized strings

Nonlocalized strings are text that appears in your interface that Xcode won’t include in exported files. To find nonlocalized strings in your app, choose Product \> Scheme \> Edit Scheme in Xcode. In the sheet that appears, select the Run scheme action in the left column, and click Options on the right. Then select “Show non-localized strings” under Localization Debugging and click Close.

When you run your app, the nonlocalized strings appear in all caps.

![](../../../attachments/2f16e334b21b1b262df18b3d6a8e0f0b/preparing-your-interface-for-localization-1@2x.png)

<sub>Screenshot of the Xcode Scheme editor with the Run scheme selected and showing the App Language and App Region menus in the detail area.</sub>

### Run your app using pseudolanguages

You can test your interface with samples of text that exhibit the characteristics of different types of languages. In Xcode, choose Product \> Scheme \> Edit Scheme. In the sheet that appears, select the Run scheme action in the left column, and click Options on the right. Choose one of the pseudolanguages at the bottom of the App Language pop-up menu and click Close in the sheet.

| Pseudolanguage | Description |
|---|---|
| Double-Length Pseudolanguage | Doubles the length of localizable strings to test whether views adjust their size and position. |
| Right-to-Left Pseudolanguage | Simulates a right-to-left writing direction to test whether views flip accordingly. |
| Emotional Pseudolanguage | Simulates emojis in a string. |
| Accented Pseudolanguage | Adds accents to localizable strings to test whether views adjust to languages that have high and low ascenders. |
| Bounded String Pseudolanguage | Wraps strings to identify places where localized strings may appear truncated. |
| Right-to-Left Pseudolanguage With Right-to-Left Strings | Simulates a right-to-left writing direction, using right-to-left strings. |
| Tall Pseudolanguage | Simulates languages that require significantly more vertical space. |

## See Also

### Strings and text

- [Preparing your app’s text for translation](preparing-your-apps-text-for-translation.md) — Use localizable APIs to populate string catalogs automatically with your app’s user-facing text.
- [Preparing dates, currencies, and numbers for translation](preparing-dates-numbers-with-formatters.md) — Ensure that dates, currencies, and numbers display correctly across multiple languages and locales by using formatters.
