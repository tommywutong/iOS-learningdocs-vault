---
title: SpellingChecker CarbonCocoa Bundled
apple_id: DTS10003361
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2004-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/SpellingChecker-CarbonCocoa-Bundled/Introduction/Intro.html
archived_at: '2026-07-18T03:25:18.766419Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](SpellCheck-SpellCheck.m.md)

# SpellingChecker CarbonCocoa Bundled

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2004-08-17 How to load and call a Cocoa bundle from a Carbon CFM or Mach-O application |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X 10.1 |

SpellCheck.pbproj implements a procedural C wrapper around the Cocoa NSSpellChecker and exports it as a Mach-O bundle called "SpellCheck.bundle".

The client Carbon application SpellingChecker contains SpellCheck.bundle within its bundles "Frameworks" directory and use the CFBundle APIs to access SpellCheck.bundle.

The SpellingChecker carbon application must be therefore be bundled, but can be either CFM or Mach-O.

[Next](SpellCheck-SpellCheck.m.md)

