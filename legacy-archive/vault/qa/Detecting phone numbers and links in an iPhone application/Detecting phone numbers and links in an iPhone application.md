---
title: Detecting phone numbers and links in an iPhone application
apple_id: DTS40009340
resource_type: QA
platform: iOS
topic: User Experience
technology: UIKit
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1495/_index.html
archived_at: '2026-07-18T02:31:30.760314Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1495

# Detecting phone numbers and links in an iPhone application

## Q:  How do I detect phone numbers and links in an iPhone application?

A: How do I detect phone numbers and links in an iPhone application?

As of iPhone OS 3.0, text views and web views support the detection of phone numbers, email addresses, and HTTP links. iPhone OS 3.0 scans for these types of data, highlights them when found, and renders them into clickable URLs as shown in Figure 1. You can detect phone numbers and links programmatically or by using Interface Builder 3.1.2 or later.

__Figure 1__  Detecting phone numbers, email addresses, and HTTP links in a text view

!

The iPhone OS SDK 3.0 introduces the `UIDataDetectorTypes` enumeration constant, which defines the types of data that can be found in web views and text views. Table 1 provides a description of these data types.

__Table 1__  Types of data detected in web views and text views

| Constant | Description |
| UIDataDetectorTypePhoneNumber | Detect strings formatted as phone numbers. |
| UIDataDetectorTypeLink | Detect strings formatted as URLs. |
| UIDataDetectorTypeNone | Do not detect any data. |
| UIDataDetectorTypeAll | Detect all available types of data. This constant is recommended for detecting data. |

To programmatically detect phone numbers or links, create an instance of your view and set its `dataDetectorTypes` property to one of the data types in Table 1. See Listing 1 for an example that scans for phone numbers, emails, and URLs in a text view.

__Listing 1__  Programmatically detecting phone number and links in a text view

```objc
- (void)viewDidLoad {     self.textView.dataDetectorTypes = UIDataDetectorTypeAll; }
```


Follow these steps to detect phone numbers and links using Interface Builder 3.1.2 or later:

1. Open the Nib file containing your web view or text view in Interface Builder.
2. Select your view, then choose Tools > Attributes Inspector. The Attributes Inspector contains the `Detect Phone Numbers` and `Detect Links` options, which respectively turn on phone numbers detection and links (email and URLs) detection.
3. Check one of these options or both of them according to your needs as shown in Figure 2.

__Figure 2__  Turning on both phone number and links in a text view

!

[UIDataDetectorTypes](https://developer.apple.com/iphone/library/documentation/UIKit/Reference/UIKitDataTypesReference/Reference/reference.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-27 | New document that describes how to detect phone numbers and links in an iPhone application. |

