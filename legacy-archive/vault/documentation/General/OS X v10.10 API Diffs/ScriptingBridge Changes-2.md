---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/ScriptingBridge.html
archived_at: '2026-07-15T07:34:56.985452Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# ScriptingBridge Changes

## ScriptingBridge (Added)

Added SBApplicationAdded SBApplication.init(URL: NSURL!)Added SBApplication.activate()Added SBApplication.applicationWithBundleIdentifier(String!) -> AnyObject! [class]Added SBApplication.applicationWithProcessIdentifier(pid_t) -> AnyObject! [class]Added SBApplication.applicationWithURL(NSURL!) -> AnyObject! [class]Added SBApplication.init(bundleIdentifier: String!)Added SBApplication.classForScriptingClass(String!) -> AnyClass!Added SBApplication.delegateAdded SBApplication.launchFlagsAdded SBApplication.init(processIdentifier: pid_t)Added SBApplication.runningAdded SBApplication.sendModeAdded SBApplication.timeoutAdded SBApplicationDelegateAdded SBApplicationDelegate.eventDidFail(UnsafePointer<AppleEvent>, withError: NSError!) -> AnyObject!Added SBElementArrayAdded SBElementArray.arrayByApplyingSelector(Selector) -> [AnyObject]!Added SBElementArray.arrayByApplyingSelector(Selector, withObject: AnyObject!) -> [AnyObject]!Added SBElementArray.get() -> [AnyObject]!Added SBElementArray.objectAtLocation(AnyObject!) -> AnyObject!Added SBElementArray.objectWithID(AnyObject!) -> AnyObject!Added SBElementArray.objectWithName(String!) -> AnyObject!Added SBObjectAdded SBObject.init()Added SBObject.init(data: AnyObject!)Added SBObject.elementArrayWithCode(DescType) -> SBElementArray!Added SBObject.init(elementCode: DescType, properties:[NSObject: AnyObject]!, data: AnyObject!)Added SBObject.get() -> AnyObject!Added SBObject.lastError() -> NSError!Added SBObject.init(properties: [NSObject: AnyObject]!)Added SBObject.propertyWithClass(AnyClass!, code: AEKeyword) -> SBObject!Added SBObject.propertyWithCode(AEKeyword) -> SBObject!Added SBObject.setTo(AnyObject!)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
