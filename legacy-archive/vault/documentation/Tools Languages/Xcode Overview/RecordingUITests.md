---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/RecordingUITests.html
archived_at: '2026-07-27T06:57:08.184045Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](UsingFileSaving.md)[Previous](CheckingCodeCoverage.md)

## Recording UI Tests

Xcode can record steps in a unit test as you use your app in Simulator. After recording the test, add assertions that check if interface elements are in the expected state.

（原归档配图获取待重试：`UI_Test_record_2x.png`）

For information on accessibility, see _[Accessibility Programming Guide for iOS](../../User%20Experience/Accessibility%20Programming%20Guide%20for%20iOS/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4doobv)_ and _[Accessibility Programming Guide for OS X](../../Accessibility%20Programming%20Guide%20for%20OS%20X/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzy)_. For more information on UI tests, see _[Testing with Xcode](../../Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_.

### Recording a Test

Recording UI tests requires:

- A UI test target for your project
- Accessibility information for your UI elements
- OS X v10.11 or greater
- iOS 9 or greater

（原归档配图获取待重试：`UI_Test_ready_to_record_2x.png`）

Once your app is ready to record a test, open a source file in the UI test target and insert the cursor in a test method. You can add to an existing test method or create a new one. Click the Record button, and Xcode launches your app in Simulator. Perform the actions that make up the test. Each time you touch an element on the screen, Xcode adds a line of code to your test method. Click the Record button again to stop adding actions to the method.

Add assertions to check if the user interface is in the correct state after the test completes. You can use assertions to test parts of the interface including strings in text fields or buttons, the number of table view cells, the existence of a particular button, and much more.

（原归档配图获取待重试：`UI_Tests_assertions_2x.png`）

[Using Code Coverage](CheckingCodeCoverage.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnzufvjvomi)

[Using File Saving](UsingFileSaving.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnrvfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](UsingFileSaving.md)[Previous](CheckingCodeCoverage.md)
