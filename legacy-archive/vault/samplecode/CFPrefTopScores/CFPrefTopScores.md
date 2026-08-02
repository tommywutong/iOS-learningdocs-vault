---
title: CFPrefTopScores
apple_id: DTS10003414
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2006-10-09'
source_url: https://developer.apple.com/library/archive/samplecode/CFPrefTopScores/Introduction/Intro.html
archived_at: '2026-07-18T03:02:28.708488Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# CFPrefTopScores

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-10-09 How to access globally shared (writable) user preferences without requiring authentication. |
| __Build Requirements:__ | XCode |
| __Runtime Requirements:__ | Carbon mach-o |

CFPreferences by design only allows write access to the kCFPreferencesAnyUser domain by a user with admin privileges. But occasionally developers have had the need to store user preferences that are both readable and writable by all users (without authorization). Currently the only location that meets this requirement is the </Users/Shared> directory. This sample demonstrates how to use Core Foundation API's to access (globally readable and writable) preferences in this location.

[Next](main.c.md)

