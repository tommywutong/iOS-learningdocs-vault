---
title: Apr 13, 2023 How Device Verification protects your WhatsApp account
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2023/04/13/security/whatsapp-device-verification-protects-your-account/'
original_language: en
published: 2023-04-13
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b9262cae3a2b5dbb'
translated: false
---

> 原文：[Apr 13, 2023 How Device Verification protects your WhatsApp account](https://engineering.fb.com/2023/04/13/security/whatsapp-device-verification-protects-your-account/)　·　Meta Engineering — iOS

- WhatsApp has launched a new security feature that further helps prevent attackers from using vectors like on-device [malware](https://engineering.fb.com/2022/07/20/security/how-meta-and-the-security-industry-collaborate-to-secure-the-internet/).
- This security feature, called Device Verification, requires no action or additional steps from users and helps protect your account.
- This feature is part of our broader work to increase security for our users from the growing threat of malware.

WhatsApp’s top priority is ensuring that users can communicate privately, simply, and securely. One of the strongest tools at our disposal is[end-to-end encryption](https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/) – meaning that nobody, not even WhatsApp, can read personal messages sent between users. This protects messages from interception, however, we’ve increasingly seen attackers are targeting the end points of communication – mobile devices themselves – and we are increasing our security mechanisms to keep user accounts safe.

In particular, we are concerned about malware that infects a mobile phone in much the same way a virus infects a computer. Malware is used to advance account takeover (ATO) attacks that send messages without the user’s knowledge or permission.

In our ongoing effort to safeguard peoples’ accounts and information on WhatsApp, we’re introducing a new security measure – called Device Verification – to help prevent ATO attacks. Device Verification blocks the attacker’s connection, while allowing the victim to use their WhatsApp account uninterrupted.

## Why do we need Device Verification?

WhatsApp uses several cryptographic keys to ensure that communications across the app are end-to-end encrypted. One of these is the authentication key, which allows a WhatsApp client to connect to the WhatsApp server to re-establish a trusted connection. This authentication key allows people to use WhatsApp without having to enter a password, PIN, SMS code, or other credential every time they turn on the app.

This mechanism is secure because the authentication key cannot be intercepted by any third party including WhatsApp. If a device is infected with malware, however, the authentication key can be stolen.

We are primarily concerned about the popularity of unofficial [WhatsApp clients](https://faq.whatsapp.com/1217634902127718/?helpref=hc_fnav) that contain malware designed for this purpose. These unofficial apps put users’ security at risk – and it is why we encourage everyone using WhatsApp to use the [official WhatsApp app](https://twitter.com/wcathcart/status/1546567955671961600?lang=en).

Once malware is present on user devices, attackers can use the malware to capture the authentication key and use it to impersonate the victim to send spam, scams, phishing attempts, etc. to other potential victims.

Device Verification will help WhatsApp identify these scenarios and protect the user’s account without interruption.

## How Device Verification works

WhatsApp has built Device Verification to benefit from how people typically read and react to messages sent to their device. When someone receives a message their WhatsApp client wakes up and retrieves the offline message from WhatsApp server. This process cannot be impersonated by malware that steals the authentication key and attempts to send messages from outside the users` device.

Device Verification introduces three new parameters:

1. A security-token that’s stored on the users` device.
2. A nonce that is used to identify if a client is connecting to retrieve a message from WhatsApp server.
3. An authentication-challenge that is used to asynchronously ping the users` device.

These three parameters help prevent malware from stealing the authentication key and connecting to WhatsApp server from outside the users` device

### How a security-token gets bootstrapped

Every time someone retrieves an offline message, the security-token is updated to allow seamless reconnection attempts in future. This process is called bootstrapping the security-token.

### How a new client connection is validated

Every time a WhatsApp client connects to the WhatsApp server, we require the client to send us the security-token that’s on their device. This allows us to detect suspicious connections from malware that is trying to connect to the WhatsApp server from outside the users` device.

### What is an authentication-challenge?

An authentication-challenge is an invisible ping from the WhatsApp server to a user’s device. We only send these challenges on suspicious connections. There are three possible responses to the challenge:

1. Success: The client responds to the challenge from the connecting device.
2. Failure: The client responds to the challenge from a different device. This means the connection being challenged is very likely from an attacker and the connection will be blocked.
3. No Response: The client doesn’t respond to the challenge. This situation is rare and indicates that the connection being challenged is suspicious. We retry sending the challenge a few more times. If the client still doesn’t respond, the connection will be blocked.

## What’s next

Malware is an issue that increasingly threatens everyone’s security and privacy. Device Verification has been rolled out to 100% of WhatsApp users on Android and is in the process of being rolled out to iOS users. It enables us to increase our users’ security without interrupting their service or adding an additional step they need to take. Device Verification will serve as an important and additional tool at WhatsApp’s disposal to address rare key-theft security challenges. We will continue to evaluate new security features to protect the privacy of our users.
