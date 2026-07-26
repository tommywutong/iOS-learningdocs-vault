---
title: MailKit
framework: MailKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mailkit
source_url: 'https://developer.apple.com/documentation/mailkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mailkit.json'
content_hash: 'sha256:b679dae55d50a269'
translated: false
---

> Navigation: [Technologies](technologies.md)

# MailKit

<sub>Framework</sub>

Secure, customize, and act on email messages that users send and receive.

## Overview

MailKit lets your app include an app extension that customizes several features of Mail. A Mail app extension provides one or more of the following enhancements:

- A _content blocker_ defines rules to prevent loading content when users view messages.
- An _action handler_ performs actions such as flagging, setting colors, or archiving when Mail downloads messages.
- A _compose session handler_ validates recipient email addresses, displays a view controller on Mail’s compose windows, confirms if messages are suitable for delivery, and adds custom headers.
- A _message security handler_ secures messages using encryption and digital signatures.

The entry point for your extension is an object that conforms to [MEExtension](mailkit/meextension.md). When MailKit invokes your extension, this objects determines the handlers that provide each capability in the list above.

## Topics

### Essentials

- [MEExtension](mailkit/meextension.md) — A type that provides objects for manipulating email messages, such as performing actions on messages or blocking content when users view messages.
- [Build Mail App Extensions](mailkit/build-mail-app-extensions.md) — Create app extensions that block content, perform message and composing actions, and help message security.

### Content Blockers

- [MEContentBlocker](mailkit/mecontentblocker.md) — An object that provides a set of rules to block content when displaying a message.

### Message Actions

- [MEMessageActionHandler](mailkit/memessageactionhandler.md) — An object that performs actions on messages as the system downloads them.

### Compose Window Enhancements

- [MEComposeSessionHandler](mailkit/mecomposesessionhandler.md) — An object that participates in the composition of mail messages, and annotates recipient tokens.

### Message Encryption, Decryption, and Digital Signatures

- [MEMessageSecurityHandler](mailkit/memessagesecurityhandler.md) — An object that digitally signs or encrypts messages the user sends and receives.

### Message Properties

- [MEMessage](mailkit/memessage.md) — An object that contains information about a mail message, such as the subject, addressees, date sent, and the message contents.
- [MEMessageState](mailkit/memessagestate.md) — The state of a message: sent, unsent, or received.

### Custom View Controllers

- [MEExtensionViewController](mailkit/meextensionviewcontroller.md) — An object that manages a view for compose session and message security handlers.

### Structures

- [MEMessageSecurityError](mailkit/memessagesecurityerror.md)

### Classes

- [MEComposeContext](mailkit/mecomposecontext.md)
- [MEDecodedMessageBanner](mailkit/medecodedmessagebanner.md)
- [MEEmailAddress](mailkit/meemailaddress.md)
- [MEExtensionManager](mailkit/meextensionmanager.md)
