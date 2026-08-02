---
title: Preferences Programming Topics for Core Foundation
apple_id: 10000129i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPreferences/Concepts/ApplicationIDs.html
archived_at: '2026-07-15T07:22:42.577171Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Preferences Programming Topics for Core Foundation](Introduction%20to%20Preferences%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Preference%20Domains.md)[Previous](Preferences%20Best%20Practices.md)

# Application IDs

Preferences store preference data on disk in files named using an application ID that you provide. To ensure that there are no naming conflicts, it’s a good idea to define and set a bundle identifier for your application and use it as the application ID for preferences. Bundle identifiers take the same form as Java package names—your company’s unique domain name followed by the application or library name—for example `com.apple.Finder` or `com.foo.ImageImport`. Using this scheme minimizes the possibility of collision, and leaves you responsible for managing the identifier namespace under your corporate domain. See _[Bundle Programming Guide](../Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_ for more information on bundles and bundle IDs.

[Next](Preference%20Domains.md)[Previous](Preferences%20Best%20Practices.md)

