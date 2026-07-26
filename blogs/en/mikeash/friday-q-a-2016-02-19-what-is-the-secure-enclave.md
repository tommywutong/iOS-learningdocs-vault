---
title: 'Friday Q&A 2016-02-19: What Is the Secure Enclave?'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2016-02-19-what-is-the-secure-enclave.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ebbd547607f436d6'
translated: false
---

> 原文：[Friday Q&A 2016-02-19: What Is the Secure Enclave?](https://www.mikeash.com/pyblog/friday-qa-2016-02-19-what-is-the-secure-enclave.html)　·　mikeash.com Friday Q&A

Posted at 2016-02-19 14:40 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2016-03-04: Swift Asserts](https://www.mikeash.com/pyblog/friday-qa-2016-03-04-swift-asserts.html)  
Previous article: [Friday Q&A 2016-01-29: Swift Struct Storage](https://www.mikeash.com/pyblog/friday-qa-2016-01-29-swift-struct-storage.html)  
Tags: [apple](https://www.mikeash.com/pyblog/?tag=apple) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [security](https://www.mikeash.com/pyblog/?tag=security)

Friday Q&A 2016-02-19: What Is the Secure Enclave?

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Lithuanian (translation by Giedrius Sadauskas)](http://crowfer.com/kas-yra-saugus-anklava/).

A quick note before I get started: my usual approach to writing articles is to dig all the way down to the bits and bytes and then discuss what's there. This is necessarily somewhat different. By its very nature, the Secure Enclave is inaccessible to mere mortals like myself. Instead, most of the knowledge here comes from the information in [Apple's iOS Security Guide](https://www.apple.com/business/docs/iOS_Security_Guide.pdf), plus some general theory. The intent is to extract the relevant bits from that guide, explain them, and think through the implications. This article must assume Apple's information is accurate, since there's no practical way to check from the outside. The result will only be as good as the product of the guide's accuracy and my own understanding, so reader beware.

Also, this is intended to examine the technical aspects of this case and the Secure Enclave technology. No opinions on the merits of the FBI's request or Apple's response or any other political matters are stated or implied. If you want to discuss the political aspects of this case, there are many other places where you can do so.

With that out of the way, let's get started.

**Review**  
The iPhone in question is protected by a passcode, which isn't stored anywhere on the device. The only way to get in is to brute-force the passcode. The computation needed to verify a passcode is deliberately slow, requiring about 80 milliseconds per attempt. Still, brute force cracking is feasible. For a four-digit passcode, trying 10,000 combinations at 80 milliseconds each would take less than 15 minutes. A six-digit passcode would take about a day.

This means that passcodes are not terribly secure. Apple mitigates this with additional delays after too many failed attempts. After a few failed attempts, the iPhone will make you wait before you can try again, starting with a one-minute delay, then a five-minute delay, and beyond. This makes a brute force attack impractical.

One might think that you could work around this if you pulled the flash memory out of the iPhone, copied its contents, then tried to crack it on a fast computer. You wouldn't have any software imposing additional delays. As a bonus, the 80 milliseconds needed for each attempt could go a lot faster with a faster computer, and you could run many attempts in parallel. However, this doesn't work. The data encryption is tied to the hardware, so the brute force attack must be run on the original device.

On the older iPhones without the Secure Enclave, there is a weakness in this system. The escalating delays prevent brute force cracking of the passcode, but these delays are just a feature of the phone's OS. The 80 millisecond key derivation is an inherent property of that computation, but the additional minutes or hours delay after too many failed attempts is just the OS code refusing to accept additional input until some time has passed. The FBI wants Apple to build and install a special OS version that doesn't enforce these delays and which allows passcodes to be submitted electronically. This would allow the FBI to crack the passcode within a few minutes or hours. iPhones won't accept OS updates from anyone besides Apple, so this system is secure from outside attackers, but it's not secure against Apple itself.

Note that this is based on the user using a numeric passcode. A good complex password is still secure even on these older iPhones. An eight-character alphanumeric password would take about 550,000 years to try all possible combinations, for example.

**Unreadable UIDs**  
Each iOS CPU is built with a 256-bit unique identifier or UID. This UID is burned into the hardware and not stored anywhere else. The UID is not only inaccessible to the outside world, but it's inaccessible even to the software running at the highest privilege levels on the CPU. Instead, the CPU contains a hardware AES encryption engine, and the only way the UID can be accessed by the hardware is by loading it into the AES engine as a key and using it to encrypt or decrypt data.

Apple uses this hardware to entangle the user's passcode with the device. By setting the device's UID as the AES key and then encrypting the passcode, the result is a random-looking bunch of data which can't be recreated anywhere else, since it depends on both the user's passcode _and_ the secret, unreadable, device-specific UID. This process is repeated over many rounds using the [PBKDF2 function](https://en.wikipedia.org/wiki/PBKDF2), feeding each round's output back into the next round's input, performing the heavy computation needed to force 80 milliseconds of work for each passcode verification attempt.

**Secure Enclave**  
The Secure Enclave was introduced with Apple's A7 system on a chip. All iPhones starting with the 5s have it. The 5/5c and below do not. On the iPad side, everything starting from the iPad Mini 2 and the iPad Air have it.

The Secure Enclave is a separate CPU within the A7 (or later) that's responsible for low-level cryptographic operations. It doesn't run iOS or anything resembling iOS, but instead runs a modified [L4 microkernel](https://en.wikipedia.org/wiki/L4_microkernel_family). L4 is intended to run as little code as possible in the kernel, which should theoretically make the system more secure by reducing the amount of potentially buggy code running with elevated privileges. The Secure Enclave uses a secure boot system to ensure that it the code it runs can't be modified, and it uses encrypted memory to ensure that the rest of the system can't read or tamper with its data. This effectively forms a little computer within the computer that's difficult to attack.

The Secure Enclave contains its own UID and hardware AES engine. The passcode verification process takes place here, separated from the rest of the system. The Secure Enclave also handles Touch ID fingerprint processing and matching, and authorizing payments for Apple Pay.

The Secure Enclave performs all key management for encrypted files. File encryption applies to nearly all user data. Most system apps use it, and third party apps all use it by default if running on iOS 7 or later. Each encrypted file has a unique key, which is in turn encrypted with another key derived from the device UID and the user's passcode. The main CPU can't read encrypted files on its own. It must request the file's keys from the Secure Enclave, which in turn is unable to provide them without the user's passcode.

The escalating delays for failed passcode attempts are enforced by the Secure Enclave. The main CPU merely submits passcodes and receives the results. The Secure Enclave performs the checks, and if there have been too many failures it will delay peforming those checks. The main CPU can't speed things along.

**Implications**  
What does the Secure Enclave mean for the security of the system as a whole?

On most systems, if you can get into the OS kernel then you own the entire system. The kernel can do anything. It can read and write every byte of system memory, it can control all of the hardware, and it's in charge of all of the application code the system runs, which it can subvert at will.

Since the Secure Enclave is a separate CPU mostly cut off from the rest of the system, it isn't under the kernel's control. On an older iPhone, owning the kernel means owning everything done by the system, including the passcode verification process. With the Secure Enclave, no matter who is in control of the main CPU, no matter what code is in the OS running on it, the basic security functions remain intact.

This system essentially allows arbitrary code to be placed in front of cryptographic functions such that this arbitrary code can't be bypassed. It's a bit like a super-sized version of the 80 millisecond computation time for password attempts. That delay is enforced by using a calculation that inherently takes that much time. This means it can't be bypassed, but there are limits on what you can create from the inherent limitations of calculations. For example, you can't add a one-minute delay to the fifth attempt, because raw cryptographic constructs don't have a concept of "fifth attempt." With the Secure Enclave, that one-minute delay can be enforced, since even with the rest of the system subverted, the delay code in the Secure Enclave remains intact.

**Software Updates**  
The iPhone 5c (and other pre-A7 iPhones) can be subjected to a brute force attack by creating a new OS without the artificial delays, loading that onto the device, and then testing passcodes as fast as the hardware can compute. The Secure Enclave prevents this. But what about carrying out the same kind of attack one level further down, by loading new software into the Secure Enclave which eliminates its artificial delays?

Apple's guide contains this discussion of software updates for the Secure Enclave:

> "It utilizes its own secure boot and personalized software update separate from the application processor."

That's it! There are no details whatsoever. What is the actual situation? Here, we must enter the realm of speculation, because as far as I can dig up there is no information out there about how Secure Enclave software updates actually work. I see two possibilities.

The first possibility is that the Secure Enclave uses the same sort of software update mechanism as the rest of the device. That is, updates must be signed by Apple, but can be freely applied. This would make the Secure Enclave useless against an attack by Apple itself, since Apple could just create new Secure Enclave software that removes the limitations. The Secure Enclave would still be a useful feature, helping to protect the user if the main OS is exploited by a third party, but it would be irrelevant to the question whether Apple can break into its own devices.

The second possibility is that the Secure Enclave's software update mechanism does something more sophisticated to protect against an attack even from Apple. The whole idea of the Secure Enclave is that it enforces additional rules that can't be bypassed from the outside. This could include additional rules about its own software updates. Given the goal of protecting the user's data, it would make a lot of sense for the Secure Enclave to refuse to apply any software update unless the device has already been unlocked with the user's passcode. For a case where the user has forgotten the passcode and wants to wipe the device and start over, the Secure Enclave could allow updates but delete the master keys protecting the user's data.

Which one is true? For now, we don't know. Apple put in a lot of effort to protect user data, and it would make a lot of sense for them to take the second approach, where updates wipe the device if applied without the user's passcode. This would be fairly easy to implement, and shouldn't affect the usability of the device. Given Apple's public stance on user privacy, I would find it extremely weird if it the Secure Enclave's software update mechanism _wasn't_ implemented in this way. On the other hand, Tim Cook's public letter implies that all iPhone models are potentially vulnerable, so perhaps they haven't taken this extra step.

When it comes to the matter of law enforcement forcing Apple to attack an iOS device, this is the key question. If Secure Enclave updates are secured even against Apple, then the FBI's ability to make these requests stops at the iPhone 5s. If they're not, then even the latest 6s could potentially be attacked. I am deeply interested in learning the answer to this question.

**Conclusion**  
The Secure Enclave adds an additional line of defense against attacks by implementing core security and cryptography features in a separate CPU within Apple's hardware. This separate CPU runs special software and is walled off from the rest of the system, placing it outside the control of the main OS, including the kernel. The Secure Enclave implements device passcode verification, file encryption, Touch ID recognition, and Apple Pay, and enforces security restrictions such as the escalating delays applied after excessive incorrect passcode attempts.

The iPhone 5c that the FBI is asking Apple to break into predates the Secure Enclave, and so can be subverted by installing a new OS signed by Apple that removes the artificial passcode delays. Whether newer phones can be similarly subverted depends on how the Secure Enclave's software update mechanism is implemented. If software updates erase the master encryption keys when installed without the passcode, then newer iPhones can't be attacked in this way, even by Apple. If updates are allowed without the passcode and without erasing keys, then the Secure Enclave can potentially be subverted just as older iPhones can be. As far as I'm able to determine, whether this is the case remains an open question.

That's it for today! Come back again for more exciting adventures, probably with fewer inaccessible and opaque CPUs. Friday Q&A is driven by reader ideas, so if you have something you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2016-02-19-what-is-the-secure-enclave.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
