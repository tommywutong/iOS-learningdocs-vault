---
title: When to upgrade your iPhone OS SDK
apple_id: DTS40009406
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2009-12-04'
source_url: https://developer.apple.com/library/archive/qa/qa1677/_index.html
archived_at: '2026-07-18T02:33:45.462764Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1677

# When to upgrade your iPhone OS SDK

## Q:  When I try to use my iPhone with Xcode, the organizer says "The version of iPhone OS on “My iPhone” does not match any of the versions of iPhone OS supported for development with this copy of Xcode." How do I resolve this issue?

A: This message in the Xcode Organizer means that either the version of the iPhone SDK that you have installed is out of date compared to your iPhone, or that your iPhone is still running an older (likely pre-release) version of iPhone OS after you have installed a new iPhone SDK. Which is correct depends on what the organizer tells you. See Figure 1 for an example of the first case.

__Figure 1__  Xcode Organizer for a device running a newer version of iPhone OS than Xcode supports.

!!

As shown in this screen shot of the organizer, "My iPhone" has iPhone OS 3.1.2 (7D11) installed on it (section 2), but the version of Xcode installed only has support for iPhone OS 3.1.1 or below (section 3). Because the version of the OS installed on "My iPhone" is newer than all of the OS versions supported by Xcode, you need a newer version of the iPhone SDK installed, which you can obtain from the [iPhone Developer Website](https://developer.apple.com/iphone/) (you can also get to the developer website by clicking on the "here" highlighted in section 1).

Apple may choose to seed developers with pre-release versions of iPhone OS and the iPhone OS SDK to support future development. When we do so, you may end up inadvertently updating the iPhone OS SDK and your Xcode tools before you update a device. If this occurs, then the Xcode Organizer will inform you that the OS installed on your device (section 2) is older than the newest version of iPhone OS that Xcode supports, while also not in the list of supported versions (section 3). In this case, you need to update the version of iPhone OS that is installed on the device using iTunes or the Xcode Organizer.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-12-04 | New document that describes what "The version of iPhone OS on 'My iPhone' is not supported by this copy of Xcode" means. |

