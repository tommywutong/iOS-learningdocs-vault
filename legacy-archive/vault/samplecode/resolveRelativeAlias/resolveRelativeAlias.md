---
title: resolveRelativeAlias
apple_id: DTS10000476
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/resolveRelativeAlias/Introduction/Intro.html
archived_at: '2026-07-26T19:52:28.325163Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Document%20Revision%20History.md)

# Retired Document

__Important:__
This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/LowLevelFileMgmt/Introduction.html](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/LowLevelFileMgmt/Introduction.html)

# resolveRelativeAlias

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 Demonstrates the steps involved in creating and resolving a relative alias. |
| __Build Requirements:__ | n/a |
| __Runtime Requirements:__ | Carbon System 7.0 |

__Important__ This sample code may not represent best practices for current development. The project may use deprecated symbols and illustrate technologies and techniques that are no longer recommended.

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/LowLevelFileMgmt/Introduction.html](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/LowLevelFileMgmt/Introduction.html)

This sample tool demonstrates the steps involved in creating and resolving the alias. Instead of creating a document to store the alias, the tool wimps out and stores the alias in a preference file. The tool puts up a StandardGetFile dialog. Selecting a file creates the preference file containing the relative alias; clicking Cancel instead gets the preference file, resolves it, and prints the vRefNum and name of the target. Requirements: System 7.0 Keywords: Alias Manager, relative alias

[Next](Document%20Revision%20History.md)

