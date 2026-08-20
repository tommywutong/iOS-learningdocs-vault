---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOMailDelivery.html
archived_at: '2026-07-18T01:28:51.928697Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOElement.md)
[!](WORequest.md)

---

# WOMailDelivery

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

WOMailDelivery uses a tool compiled on all platforms: `/System/Library/WebObjects/Executables/WOSendMail[.exe]`. This tool constructs an email message from a file and uses SMTP to send it. It requires an SMTP server to be set. There is a default value for this SMTP hostname: "smtp". To change this value, use the following command:

> ```
> defaults write NSGlobalDomain WOSMTPHost "aHostName"
> ```

Note that this default can be handled by WOApplication as a command-line argument.

There is only one instance of WOMailDelivery, which you access with the [`sharedInstance`](#apple-gizdkoi) static. You cannot create one of your own.

---

## Method Types

**Obtaining an instance**

**[sharedInstance](#apple-gizdkoi)**

**Composing mail**

**[composeComponentEmail](#apple-gizdsnq)

**[composePlainTextEmail](#apple-gq4q)****

**Sending mail**

**[sendEmail](#apple-giztcnq)**

#

---

### sharedInstance

public static WOMailDelivery `sharedInstance`()

---

## Instance Methods Returns the current application's WOMailDelivery instance. Use this method instead of creating an instance of your own.

---

### composeComponentEmail

public java.lang.String `composeComponentEmail`(java.lang.String _sender_,
com.apple.yellow.foundation.NSArray _destination_,
com.apple.yellow.foundation.NSArray _ccAddresses_,
java.lang.String _subject_,
WOComponent _aComponent_,
boolean _flag_)

Composes an email message to _destination_ with "from," "cc," and "subject" lines. The body of the message is the HTML generated when this method invokes `generateResponse` on _aComponent_. WOMailDelivery uses the WOCGIAdaptorURL default to complete all URLs in the message to be mailed, so the email's reader can click on the URLs to visit them.

If _flag_ is true, the message is sent immediately.

---

### composePlainTextEmail

public java.lang.String `composePlainTextEmail`(java.lang.String _sender_,
com.apple.yellow.foundation.NSArray _destination_,
com.apple.yellow.foundation.NSArray _ccAddresses_,
java.lang.String _subject_,
java.lang.String _message_,
boolean _flag_)

Composes an email message to _destination_ with "from," "cc," and "subject" lines, setting the content type of the email as (Content-type: TEXT/PLAIN; CHARSET=US-ASCII). If _flag_ is YES, the message is sent immediately.

---

### sendEmail

public void `sendEmail`(java.lang.String _mailString_)

Sends _anEmail_, with _anEmail_ being a String following the SMTP format.The `compose...Email` methods return such Strings and this method lets you modify those strings before sending them.

---

[!](WOElement.md)
[!](WORequest.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
