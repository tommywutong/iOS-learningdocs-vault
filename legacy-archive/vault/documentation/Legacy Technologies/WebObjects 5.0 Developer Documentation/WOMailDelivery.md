---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOMailDelivery.html
archived_at: '2026-07-15T08:15:15.657211Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOMailDelivery

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOMailDelivery uses a tool compiled on all platforms: /System/Library/WebObjects/Executables/WOSendMail[.exe]. This tool constructs an Email message from a file and uses SMTP to send it. It requires an SMTP server to be set. There is a default value for this SMTP hostname: "smtp". To change this value, use the following command:

defaults write NSGlobalDomain WOSMTPHost "_aHostName_"

Note that this default can be handled by WOApplication as a command-line argument.

There is only one instance of WOMailDelivery, which you access with the [sharedInstance](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6tlbnfweizlmnf3gk4tzf5zwqylsmvses3ttorqw4y3f) static. You cannot create one of your own.

## Method Types

---

> **Obtaining an instance**
> : [sharedInstance](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6tlbnfweizlmnf3gk4tzf5zwqylsmvses3ttorqw4y3f)
>
> **Composing mail**
> : [composeComponentEmail](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvqws3cemvwgs5tfoj4s6y3pnvyg643finxw24dpnzsw45cfnvqws3a): [composePlainTextEmail](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvqws3cemvwgs5tfoj4s6y3pnvyg643fkbwgc2lokrsxq5cfnvqws3a)
>
> **Sending mail**
> : [sendEmail](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pjvqws3cemvwgs5tfoj4s643fnzsek3lbnfwa)

## Constructors

---

### __WOMailDelivery__

`protected WOMailDelivery()`

This protected constructor initializes a newly-instantiated WOMailDelivery object. WebObjects applications shouldn't allocate WOMailDelivery objects, but instead should make use of the shared instance provided by WOMailDelivery's __sharedInstance()__ class method.

---

## Static Methods

---

### sharedInstance

`public static WOMailDelivery sharedInstance()`

Returns the current application's WOMailDelivery instance. Use this method instead of creating an instance of your own.

---

## Instance Methods

---

### composeComponentEmail

`public String composeComponentEmail( String sender, NSArray destination, NSArray ccAddresses, String subject, WOComponent aComponent, boolean flag)`

Composes an email message to _destination_ with "from," "cc," and "subject" lines. The body of the message is the HTML generated when this method invokes __generateResponse__ on _aComponent_. WOMailDelivery uses the WOCGIAdaptorURL default to complete all URLs in the message to be mailed, so the email's reader can click on the URLs to visit them.

If _flag_ is true, the message is sent immediately.

---

### composePlainTextEmail

`public String composePlainTextEmail( String sender, NSArray destination, NSArray ccAddresses, String subject, String message, boolean flag)`

Composes an email message to _destination_ with "from," "cc," and "subject" lines, setting the content type of the email as (Content-type: TEXT/PLAIN; CHARSET=US-ASCII). If _flag_ is YES, the message is sent immediately.

---

### sendEmail

`public void sendEmail(String mailString)`

Sends _anEmail_, with _anEmail_ being a String following the SMTP format.The __compose...Email__ methods return such Strings and this method lets you modify those strings before sending them.

---

### __toString__

`public String toString()`

Returns a String representation of the WOMailDelivery object containing the receiver's class name and the SMTP host name.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
