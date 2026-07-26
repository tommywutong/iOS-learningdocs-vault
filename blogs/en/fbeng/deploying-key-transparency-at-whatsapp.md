---
title: Deploying key transparency at WhatsApp
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/'
original_language: en
published: 2023-04-13
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ca5c8341a87813ed'
translated: false
---

> 原文：[Deploying key transparency at WhatsApp](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/)　·　Meta Engineering — iOS

- WhatsApp has launched a [new cryptographic security feature](https://www.whatsapp.com/security/WhatsApp-Key-Transparency-Whitepaper.pdf) to automatically verify a secured connection based on key transparency.
- The feature requires no additional actions or steps from users and helps ensure that a conversation is secure.
- Key transparency solutions help strengthen the guarantee that end-to-end encryption provides to private, personal messaging applications in a transparent manner available to all.
- We have published an open-source library called [Auditable Key Directory (AKD)](https://github.com/facebook/akd/). This enables anyone to verify audit proofs of the directory’s correctness. This underpins our key transparency deployment.

End-to-end encryption is the foundation of private messaging on WhatsApp, helping to ensure that only you and the person you’re communicating with can read what’s sent, and nobody in between, not even WhatsApp. It is among the most widely used deployments of end-to-end encryption and relies on public key cryptography first developed in the 1970s. From a technical point of view, for end-to-end encryption to be trusted, the “ends” of a conversation need to know that one another’s encryption keys are authentic and valid.

To do so, our most security conscious users have always been able to take advantage of our [security code verification feature](https://faq.whatsapp.com/820124435853543) available under a user’s contact info. When in person, keys can be validated with a quick QR code scan or, if remote, sharing the unique 60-digit code.

This is the one of the strongest ways of verifying if a connection is secure. But in reality we know that double checking a long code is cumbersome, and our team has been looking at ways to make this easier for some time.

We’re excited to introduce a new cryptographic security feature to automatically verify a secure connection without the need for this long code. To do so, we’re building on key transparency by developing a new Auditable Key Directory (AKD), which is based on an [open-sourced library](https://github.com/facebook/akd). The AKD will enable WhatsApp clients to automatically validate that a user’s encryption key is genuine and enables anyone to verify audit proofs of the directory’s correctness.

Our approach to key transparency is two-pronged and introduces two new components:

1. The server (WhatsApp) maintains an append-only AKD of public keys mapped to user accounts.
2. A third-party audit record, wherein any change in the server directory is recorded in a publicly available, privacy-preserving audit record for anyone to verify.

With these two additions, users can automatically verify their conversation security thanks to the WhatsApp directory. As this is rolled out, security-conscious users who utilize the verify security code page will notice this verification process occurs quickly and automatically.

This system is a new service provided by WhatsApp that relies on public auditing to verify the end-to-end encryption status of personal conversations. While this system provides easy and convenient verification tools to our users, those who wish to verify their end-to-end encrypted sessions without utilizing WhatsApp servers at all are encouraged to utilize the traditional security code verification process in addition to this new automated process.

The public keys are only a tool that users have to encrypt their messages. The private key – which is used to decrypt messages – is on user devices. Nobody – not even WhatsApp – has access to those private keys. A list of public keys alone cannot provide access to anyone’s content.

## How the “Verify Security Code” page works

The crux of end-to-end encrypted messaging is public/private key pairs. The private key is what you utilize to decrypt your messages sent from another party and never leaves your device. The public key, however, is what you give to others so they can encrypt messages. This is done by first giving the key to WhatsApp, where we store it on your behalf and give it to users who wish to message you.

The classic concern that end-to-end encryption was designed to guard against is a person-in-the-middle attack where you _think_ you’re talking to just one user; however, you’re actually talking to a middle-man attacker, who provides an incorrect public key so that they hold the private key and can read your messages. The attacker may then use the correct public key for your contact, re-encrypt the message with it, and send it to the user.   
   
 What stops this today? WhatsApp has a _Security Page_ for each contact that has a QR code and a 60-digit number that can be verified outside of WhatsApp to make sure it matches what your contact sees on their device. In short, it’s a unique hash of both your public keys and their public keys, so if either of you have the wrong value, the hashes won’t match. When they do match this confirms a secure, end-to-end encrypted conversation.

## What’s the problem key transparency is fixing?

While providing a strong guarantee of security, the QR code scanning/number matching feature requires communicating with your contacts outside of WhatsApp – whether it’s over a video-call, in real-life, on the phone, etc. This is:

1. Difficult to do in 1:1 communications, especially as users change devices (and therefore encryption keys) over time;
2. Even harder in small groups, since each _pair_ of participants has a unique code (there are no “group” codes);
3. Is near-impossible to perform in large groups. Every time someone joins or leaves, enrolls a new companion device, changes their phone, etc. this needs to be redone for all participants. For example, in a group of 100 people, that’s 4950 pairs of security verifications.

Ideally, this wouldn’t be a manual process and could be verified through some kind of automated flow.

Enter **key** **transparency**: A protocol in which we establish an AKD on WhatsApp that maintains a record of public key changes. Additionally, we’ve established a third-party public repository of auditable change logs to the directory that updates whenever there’s additions to the directory. This is vital for transparency and to further strengthen our end-to-end encrypted guarantee. In effect, this confirms that the same public keys a user uses to contact a recipient are the same ones that everybody else also uses to communicate with the recipient.

Although key transparency does not substitute QR code scanning, it enhances and complements it in the following ways:

1. QR code scanning requires two people to coordinate out-of-band verification. In contrast, key transparency requires only a single client to initiate and perform a check against the directory, thus improving accessibility of the check process;
2. Key transparency serves as a public key consistency mechanism when manual QR code verification is impractical (for example in large group communication scenario);
3. It also serves as a lightweight first-check of end-to-end encryption, which improves adoption of end-to-end encryption checks to more users, benefiting messaging security at-large.

In the event that the automatic check returns a result showing that the connection may not be secure, we recommend users proceed with the manual security verification check.

## The history of key transparency

Key transparency describes a protocol in which the server maintains an append-only record of the mapping between a user’s account and their public identity key. This allows the generation of _inclusion_ proofs to assert that a given mapping exists in the directory at the time of the most recent update.

WhatsApp’s realization of key transparency is based on the original academic works on key transparency, starting with [CONIKS](https://eprint.iacr.org/2014/1004.pdf) and [SEEMless](https://eprint.iacr.org/2018/607.pdf), with extensions from a recent paper called [Parakeet](https://eprint.iacr.org/2023/081.pdf). Together, this resulted in the Rust [AKD](https://github.com/facebook/akd/) crate, which serves as the foundation for maintaining a key transparency solution along with generating inclusion and key history proofs from the directory. WhatsApp is hosting this AKD directory as an infrastructure available to all of our users.

Public keys cannot be used to decrypt a user’s messages or determine who you’ve been talking to. They are, however, necessary to make sure that someone is sending a message to the intended recipient by encrypting messages that only the holder of the public key’s associated private key can read.

A user may have many entries as they update their key over time. At WhatsApp’s scale this equates to billions of entries continually growing over time. When a user deletes their account, we remove all of the public keys for that account, but the fact a key existed at a point in time is immutable (we just can’t say what the key was).

## How does key transparency work?

### Security on principle

From a core design choice, multiple factors helped us decide to enhance the openness and security of this project. [First off, the AKD, with all of its proof generation and verification logic, is open-source code.](https://github.com/facebook/akd) This is a [Rust](https://engineering.fb.com/2021/04/29/developer-tools/rust/)-based crate (library) for any entity that wants to manage an append-only directory with a publicly verifiable log or verify append-only audit proofs and participate as a public auditor of WhatsApp’s key transparency solution. A list of public keys alone cannot provide access to anyone’s content.

This library allows for the system to provide a significant guarantee on the correctness of the directory entries while not compromising security by being vulnerable to memory-based attacks. Additionally, we stuck with the decision to utilize Rust in most of the internal components outlined below.

## Applying AKD to WhatsApp

### High-volume key changes

WhatsApp deals with tens of thousands of key changes (registration, re-registration, etc.) per minute. This kind of volume is difficult to deal with when trying to insert into an append-only log.

Therefore, we decided to implement a distributed, high-throughput queue where “pending changes” live prior to being gathered together into a batch and inserted to form the next epoch. This allows us to do far larger batch inserts and greatly limits the number of database operations we need to make.

Since the changes to the AKD are additive based on the previous _epoch_ we need to make sure that only a single update occurs at a time. A single processor, sequentially handling each update one-by-one, wouldn’t be able to keep up with the rate of changes within WhatsApp (no matter the database implementation). This adds some latency from the time a key is added or updated to when it’s “published” in the directory.

By batching keys together and making an _epoch_ a collection of changes committed atomically, we can benefit from a lot of query optimizations due to many shared paths in the Merkle Tree stored in the database. The frequency to publish and emit new _epochs_ is a tunable parameter that may be adjusted over time.

### Public auditing at scale

The general requirement for all transparency solutions is to be _publicly auditable_, meaning that anyone, should they want to, can verify the transactions on the directory to assert that:

1. The history hasn’t been changed (existing records aren’t deleted or updated).
2. Changes are append-only.

When publishing a new change to the AKD, we emit an audit proof of those changes that is put into public storage for anyone interested. These audit records guarantee the properties of immutable history for anyone to verify should they want to while preserving the privacy of all users in the directory.

This does not risk anyone’s actual info from being public, nor does it reveal any patterns of behavior for any users. You can read more about how this privacy guarantee works as outlined in [SEEMless and](https://eprint.iacr.org/2018/607.pdf) [Parakeet](https://eprint.iacr.org/2023/081.pdf), the academic works from which key transparency is based off.

## WhatsApp’s key transparency rollout

Key transparency solutions help strengthen the guarantee that end-to-end encryption provides to private personal messaging applications in a transparent manner available to all. This technology underpins WhatsApp commitment and leadership in the security domain.

WhatsApp is already hosting and operating an AKD for all of our users, regardless of the version or platform of the application you’re utilizing. Users who utilize the verify security code function will start to notice that the verification is automatic as this rolls out on Android in the coming months.* This is an important mechanism that empowers security-conscious users to verify an end-to-end encrypted personal conversation quickly.

## Read the whitepaper

Read the [WhatsApp Key Transparency Overview whitepaper](https://www.whatsapp.com/security/WhatsApp-Key-Transparency-Whitepaper.pdf) for a more technical deep-dive that goes through potential attacks, additional details on data-flows, and formats.

_*UPDATE: Key Transparency is now fully available on WhatsApp for Android and iOS._
