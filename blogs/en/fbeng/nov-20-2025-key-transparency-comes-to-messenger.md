---
title: Nov 20, 2025 Key Transparency Comes to Messenger
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2025/11/20/security/key-transparency-comes-to-messenger/'
original_language: en
published: 2025-11-20
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fe176688d5a49284'
translated: false
---

> 原文：[Nov 20, 2025 Key Transparency Comes to Messenger](https://engineering.fb.com/2025/11/20/security/key-transparency-comes-to-messenger/)　·　Meta Engineering — iOS

- We’re excited to share another advancement in the security of your conversations on Messenger: the launch of key transparency verification for end-to-end encrypted chats.
- This new feature enables an additional level of assurance that only you — and the people you’re communicating with — can see or listen to what is sent, and that no one else, not even Meta, can do so.

[End-to-end encryption on Messenger](https://www.facebook.com/help/messenger-app/1084673321594605) already ensures that the content of your direct messages and calls are protected from the moment they leave your device to the moment they reach the receiver’s device. As part of our end-to-end encrypted chat platform, we believe it’s also important that anyone can verify that the public keys (used by the sender’s device for encrypting each message) belong to the intended recipients and haven’t been tampered with.

This launch builds upon the valuable work and experiences shared by others in the industry. [WhatsApp’s implementation of key transparency](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/) in 2023 demonstrated the feasibility of this technology for large-scale encrypted messaging. We’ve extended these pioneering efforts in our Messenger implementation to deliver a robust and reliable solution with similar security properties.

## What Is Key Transparency?

Key transparency provides messaging users with a verifiable and auditable record of public keys. It allows them to confirm that their conversations are indeed encrypted with the correct keys for their contacts, and that these keys haven’t been maliciously swapped by a compromised server. This means you can be more confident that your messages are only accessible to the people you intend to communicate with.

![](https://engineering.fb.com/wp-content/uploads/2025/11/Meta-Key-Transparency-Messenger.png)

You can already [check your keys for end-to-end encrypted chats on Messenger](https://www.facebook.com/help/messenger-app/147596532316790/Check+your+keys+for+end-to-end+encrypted+chats+on+Messenger), but this can be cumbersome for people who have logged in to Messenger on multiple devices, each of which has its own key. Moreover, these keys change when new devices are added or are re-registered, which necessitates another check of the key every time this happens.

To address this, we’ve added a new security feature, based on key transparency, that allows users to verify these keys without having to compare them manually with their contacts. Of course, anyone who wishes to continue manually verifying their keys is free to do so.

## How We’re Handling Messenger Keys at Scale

Our key transparency implementation leverages the [Auditable Key Directory (AKD) library](https://github.com/facebook/akd), mirroring the system already in place for WhatsApp. This system allows Meta to securely distribute and verify users’ public keys. To further enhance the security of this process, we use [Cloudflare’s key transparency auditor](https://developers.cloudflare.com/key-transparency/) to provide an additional layer of verification, ensuring that the distribution of keys is transparent and verifiable by anyone. Cloudflare’s auditor maintains a live log of the latest entries on the [Key Transparency Dashboard](https://dash.key-transparency.cloudflare.com/), for both the WhatsApp and Messenger directories.

Implementing key transparency on the scale of Messenger presented unique engineering challenges. One significant factor was the sheer volume and frequency of key updates. Messenger indexes keys for each and every device someone has logged in on, which means that a single user often has multiple, frequently-changing keys associated with their account.

This increased complexity leads to a much higher frequency of key updates being sequenced into our key transparency directory. Currently, we’re observing an epoch frequency of approximately 2 minutes per publish, with hundreds of thousands of new keys added in each epoch. Since we began indexing, our database has already grown to billions of key entries. We’ve implemented a number of advancements in our infrastructure and libraries to help manage this massive and constantly growing dataset, while ensuring high availability and real-time verification:

We improved the algorithmic efficiency of the existing key lookup and verification operations in the AKD library by optimizing for smaller proof sizes, even as the number of updates (versions) for a single key grows. Previously, these proofs grew linearly with the height of the transparency tree, which was still difficult to manage given the number of nodes in the tree.

We also updated our existing infrastructure to be more resilient to temporary outages and improved the process for recovering from long delays in key sequencing. These improvements were adapted from lessons learned from running WhatsApp’s key transparency log for the past two years.

With key transparency now live on Messenger, users will have the ability to automatically verify the authenticity of their contacts’ encryption keys for one-on-one chats. This represents another step forward in our ongoing investment in providing a secure and private service**.**

Stay tuned for more updates as we continue to enhance the security and privacy of end-to-end encryption in Messenger.
