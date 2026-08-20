---
title: Safari's "Mail [Contents/Link] of This page" to Mail Client events...
apple_id: DTS40010600
resource_type: QA
platform: macOS
topic: Apple Applications
technology: null
published: '2010-12-23'
source_url: https://developer.apple.com/library/archive/qa/qa1722/_index.html
archived_at: '2026-07-18T02:34:28.175796Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1722

# Safari's "Mail [Contents/Link] of This page" to Mail Client events...

## Q:  What do I have to do to make my mail client handle Safari's "Mail Contents of This page" and "Mail Link to This page" events?

A: What do I have to do to make my mail client handle Safari's "Mail Contents of This page" and "Mail Link to This page" events?

1. Add two boolean keys to your <Info.plist>: MailLinkSupported and MailPageSupported

__Figure 1__  MailLinkSupported and MailPageSupported keys in <Info.plist>.

<IMAGE>

2. Install two AppleEvent handlers:

- 'mail'/'mlpg' (for mail contents of this page)
- 'mail'/'mllk' (for mail link to this page)

__Listing 1__  Installing AppleEvent handlers:

```objc
- (void) applicationDidFinishLaunching: (NSNotification *) inNotification {      NSAppleEventManager *eventManager = [NSAppleEventManager sharedAppleEventManager];      [eventManager setEventHandler:self                       andSelector:@selector(handleMailPageEvent:withReplyEvent:)                     forEventClass:'mail'                        andEventID:'mlpg'];      [eventManager setEventHandler:self                       andSelector:@selector(handleMailLinkEvent:withReplyEvent:)                     forEventClass:'mail'                        andEventID:'mllk'];  } // applicationDidFinishLaunching
```

3. Implement the AppleEvent handlers:

__Listing 2__  Implementing the AppleEvent handlers:

```objc
- (void) handleMailPageEvent:(NSAppleEventDescriptor *) inEvent               withReplyEvent:(NSAppleEventDescriptor *) inReplyEvent {      // Get the subject and address     NSString *subject = [[inEvent paramDescriptorForKeyword:'urln'] stringValue];     NSString *address = [[inEvent paramDescriptorForKeyword:'url '] stringValue];      NSLog(@"subject: \"%@\", address: \"%@\"", subject, address);      NSData *data = [[inEvent paramDescriptorForKeyword:keyDirectObject] data];     if (data) {         // handle data here… (Safari WebArchive)     } else {         // Report error.         NSLog(@"paramDescriptorForKeyword:keyDirectObject.data is NULL.");     } } // handleMailPageEvent  - (void) handleMailLinkEvent:(NSAppleEventDescriptor *) inEvent               withReplyEvent:(NSAppleEventDescriptor *) inReplyEvent {      // Get the subject and address     NSString *subject = [[inEvent paramDescriptorForKeyword:'urln'] stringValue];     NSString *urlString = [[inEvent paramDescriptorForKeyword:keyDirectObject] stringValue];     NSLog(@"subject: \"%@\", url: <%@>", subject, urlString); } // handleMailLinkEvent
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-12-23 | New document that documents what a mail client needs to handle Safari's "Mail Contents of This page" and "Mail Link to This page" events. |

