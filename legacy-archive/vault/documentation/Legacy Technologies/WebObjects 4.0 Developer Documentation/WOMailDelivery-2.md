---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOMailDelivery.html
archived_at: '2026-07-18T01:28:54.107825Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOElement-2.md)
[!](WORequest-2.md)

---

# WOMailDelivery

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOMailDelivery.h

---

## Class Description

WOMailDelivery uses a tool compiled on all platforms: `/System/Library/WebObjects/Executables/WOSendMail[.exe]`. This tool constructs an email message from a file and uses SMTP to send it. It requires an SMTP server to be set. There is a default value for this SMTP hostname: "smtp". To change this value, use the following command:

> ```
> defaults write NSGlobalDomain WOSMTPHost "aHostName"
> ```

Note that this default can be handled by WOApplication as a command-line argument.

There is only one instance of WOMailDelivery, which you access with the [__sharedInstance__](#apple-gizdkoi) class method. You cannot create one of your own.

---

## Method Types

**Obtaining an instance**

**[- sharedInstance](#apple-gizdkoi)**

**Composing mail**

**[- composeEmailFrom:to:cc:subject:component:send:](#apple-gizdsnq)

**[- composeEmailFrom:to:cc:subject:plainText:send:](#apple-gq4q)****

**Sending mail**

**[- sendEmail:](#apple-giztcnq)**

---

## Class Methods

---

### sharedInstance

+ (WOMailDelivery \*)__sharedInstance__

Returns the current application's WOMailDelivery instance. Use this method instead of creating an instance of your own.

---

## Instance Methods

---

### composeEmailFrom:to:cc:subject:component:send:

- (NSString \*)__composeEmailFrom:__ (NSString \*)_sender___to:__ (NSArray \*)_destination___cc:__ (NSArray \*)_ccAddresses___subject:__ (NSString \*)_subject___component:__ (WOComponent \*)_aComponent___send:__ (BOOL)_flag_

Composes an email message to _destination_ with "from," "cc," and "subject" lines. The body of the message is the HTML generated when this method invokes __generateResponse__  on _aComponent_. WOMailDelivery uses the WOCGIAdaptorURL default to complete all URLs in the message to be mailed, so the email's reader can click on the URLs to visit them.

If _flag_ is YES, the message is sent immediately.

---

### composeEmailFrom:to:cc:subject:plainText:send:

- (NSString \*)__composeEmailFrom:__ (NSString \*)_sender___to:__ (NSArray \*)_destination___cc:__ (NSArray \*)_ccAddresses___subject:__ (NSString \*)_subject___plainText:__ (NSString \*)_message___send:__ (BOOL)_flag_

Composes an email message to _destination_ with "from," "cc," and "subject" lines, setting the content type of the email as (Content-type: TEXT/PLAIN; CHARSET=US-ASCII). If _flag_ is YES, the message is sent immediately.

---

### sendEmail:

- (void)__sendEmail:__ (NSString \*)_mailString_

Sends _anEmail_, with _anEmail_ being an NSString following the SMTP format.The __composeEmailFrom...__  methods return such NSStrings and this method lets you modify those strings before sending them.

---

[!](WOElement-2.md)
[!](WORequest-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
