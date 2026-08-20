---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/PreferencePanes.html
archived_at: '2026-07-18T02:53:40.676754Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# PreferencePanes Changes for Swift

### PreferencePanes

Removed NSPreferencePaneUnselectReply.init(_: UInt32)Removed NSPreferencePaneUnselectReply.valueModified NSPreferencePane

|  | Declaration |
| --- | --- |
| From | ``` class NSPreferencePane : NSObject {     init!(bundle bundle: NSBundle!)     var bundle: NSBundle! { get }     func loadMainView() -> NSView!     func mainViewDidLoad()     var mainNibName: String! { get }     func assignMainView()     func willSelect()     func didSelect()     var shouldUnselect: NSPreferencePaneUnselectReply { get }     func replyToShouldUnselect(_ shouldUnselect: Bool)     func willUnselect()     func didUnselect()     var mainView: NSView!     var initialKeyView: NSView!     var firstKeyView: NSView!     var lastKeyView: NSView!     var autoSaveTextFields: Bool { get }     var selected: Bool { get }     func updateHelpMenuWithArray(_ inArrayOfMenuItems: [AnyObject]!) } ``` |
| To | ``` class NSPreferencePane : NSObject {     init(bundle bundle: NSBundle)     var bundle: NSBundle { get }     func loadMainView() -> NSView     func mainViewDidLoad()     var mainNibName: String { get }     func assignMainView()     func willSelect()     func didSelect()     var shouldUnselect: NSPreferencePaneUnselectReply { get }     func replyToShouldUnselect(_ shouldUnselect: Bool)     func willUnselect()     func didUnselect()     var mainView: NSView     var initialKeyView: NSView?     var firstKeyView: NSView?     var lastKeyView: NSView?     var autoSaveTextFields: Bool { get }     var selected: Bool { get }     func updateHelpMenuWithArray(_ inArrayOfMenuItems: [[String : String]]?) } ``` |

Modified NSPreferencePane.bundle

|  | Declaration |
| --- | --- |
| From | ``` var bundle: NSBundle! { get } ``` |
| To | ``` var bundle: NSBundle { get } ``` |

Modified NSPreferencePane.firstKeyView

|  | Declaration |
| --- | --- |
| From | ``` var firstKeyView: NSView! ``` |
| To | ``` var firstKeyView: NSView? ``` |

Modified NSPreferencePane.init(bundle: NSBundle)

|  | Declaration |
| --- | --- |
| From | ``` init!(bundle bundle: NSBundle!) ``` |
| To | ``` init(bundle bundle: NSBundle) ``` |

Modified NSPreferencePane.initialKeyView

|  | Declaration |
| --- | --- |
| From | ``` var initialKeyView: NSView! ``` |
| To | ``` var initialKeyView: NSView? ``` |

Modified NSPreferencePane.lastKeyView

|  | Declaration |
| --- | --- |
| From | ``` var lastKeyView: NSView! ``` |
| To | ``` var lastKeyView: NSView? ``` |

Modified NSPreferencePane.loadMainView() -> NSView

|  | Declaration |
| --- | --- |
| From | ``` func loadMainView() -> NSView! ``` |
| To | ``` func loadMainView() -> NSView ``` |

Modified NSPreferencePane.mainNibName

|  | Declaration |
| --- | --- |
| From | ``` var mainNibName: String! { get } ``` |
| To | ``` var mainNibName: String { get } ``` |

Modified NSPreferencePane.mainView

|  | Declaration |
| --- | --- |
| From | ``` var mainView: NSView! ``` |
| To | ``` var mainView: NSView ``` |

Modified NSPreferencePane.updateHelpMenuWithArray(_: [[String : String]]?)

|  | Declaration |
| --- | --- |
| From | ``` func updateHelpMenuWithArray(_ inArrayOfMenuItems: [AnyObject]!) ``` |
| To | ``` func updateHelpMenuWithArray(_ inArrayOfMenuItems: [[String : String]]?) ``` |

Modified NSPreferencePaneUnselectReply [enum]

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` struct NSPreferencePaneUnselectReply {     init(_ value: UInt32)     var value: UInt32 } ``` | -- | OS X 10.10 | -- |
| To | ``` enum NSPreferencePaneUnselectReply : UInt {     case UnselectCancel     case UnselectNow     case UnselectLater } ``` | Equatable, Hashable, RawRepresentable | OS X 10.11 | UInt |

Modified NSPreferencePaneUnselectReply.UnselectCancel

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | NSUnselectCancel | ``` var NSUnselectCancel: NSPreferencePaneUnselectReply { get } ``` | OS X 10.10 |
| To | UnselectCancel | ``` case UnselectCancel ``` | OS X 10.11 |

Modified NSPreferencePaneUnselectReply.UnselectLater

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | NSUnselectLater | ``` var NSUnselectLater: NSPreferencePaneUnselectReply { get } ``` | OS X 10.10 |
| To | UnselectLater | ``` case UnselectLater ``` | OS X 10.11 |

Modified NSPreferencePaneUnselectReply.UnselectNow

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | NSUnselectNow | ``` var NSUnselectNow: NSPreferencePaneUnselectReply { get } ``` | OS X 10.10 |
| To | UnselectNow | ``` case UnselectNow ``` | OS X 10.11 |

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
