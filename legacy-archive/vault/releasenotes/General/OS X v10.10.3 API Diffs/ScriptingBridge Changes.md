---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/ScriptingBridge.html
archived_at: '2026-07-18T02:52:38.979210Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# ScriptingBridge Changes

## ScriptingBridge

Modified SBApplication

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SBApplication.init(URL: NSURL!)

|  | Declaration |
| --- | --- |
| From | ``` init(URL url: NSURL!) ``` |
| To | ``` init!(URL url: NSURL!) ``` |

Modified SBApplication.init(bundleIdentifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(bundleIdentifier ident: String!) ``` |
| To | ``` init!(bundleIdentifier ident: String!) ``` |

Modified SBApplication.init(processIdentifier: pid_t)

|  | Declaration |
| --- | --- |
| From | ``` init(processIdentifier pid: pid_t) ``` |
| To | ``` init!(processIdentifier pid: pid_t) ``` |

Modified SBApplicationDelegate.eventDidFail(UnsafePointer<AppleEvent>, withError: NSError!) -> AnyObject!

|  | Declaration |
| --- | --- |
| From | ``` func eventDidFail(_ event: ConstUnsafePointer<AppleEvent>, withError error: NSError!) -> AnyObject! ``` |
| To | ``` func eventDidFail(_ event: UnsafePointer<AppleEvent>, withError error: NSError!) -> AnyObject! ``` |

Modified SBElementArray

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SBObject

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified SBObject.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified SBObject.init(data: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(data data: AnyObject!) ``` |
| To | ``` init!(data data: AnyObject!) ``` |

Modified SBObject.init(elementCode: DescType, properties:[NSObject: AnyObject]!, data: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(elementCode code: DescType, properties properties: [NSObject : AnyObject]!, data data: AnyObject!) ``` |
| To | ``` init!(elementCode code: DescType, properties properties: [NSObject : AnyObject]!, data data: AnyObject!) ``` |

Modified SBObject.lastError() -> NSError!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified SBObject.init(properties: [NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(properties properties: [NSObject : AnyObject]!) ``` |
| To | ``` init!(properties properties: [NSObject : AnyObject]!) ``` |

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
