---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/ContinuousIntegrationTesting.html
archived_at: '2026-07-27T06:57:08.168728Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](CheckingCodeCoverage.md)[Previous](UnitTesting.md)

## Using Continuous Integration Testing

Xcode supports a continuous integration workflow through the Xcode service. The _Xcode service_, available in OS X Server, automates the integration process of building, running unit tests, performing static analysis, and archiving your product. The service reports build errors and warnings, static analyzer problems, and unit test failures. All tests, analysis, and archiving are performed on the server.

From Xcode on your development Mac, you create _bots_ that run on a separate server. In addition to running unit tests, bots automatically perform static analysis on your code, build your app, and archive it for distribution to testers or the App Store. Bots help you ensure that your product is always in a releasable state—and when there’s a failure, the service notifies you or the person whose code change caused the failure.

（原归档配图获取待重试：`bot_viewer-summary_2x.png`）

For information on setting up and using the service, see _[Xcode Server and Continuous Integration Guide](../../IDEs/Xcode%20Server%20and%20Continuous%20Integration%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezteojs)_.

[Using Unit Tests](UnitTesting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrtfvjvomi)

[Using Code Coverage](CheckingCodeCoverage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnzufvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](CheckingCodeCoverage.md)[Previous](UnitTesting.md)
