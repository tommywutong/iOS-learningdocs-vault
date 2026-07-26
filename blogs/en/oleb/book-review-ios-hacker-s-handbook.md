---
title: 'Book Review: iOS Hacker''s Handbook'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/07/ios-hackers-handbook/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:84192bdce176edc1'
translated: false
---

> 原文：[Book Review: iOS Hacker's Handbook](https://oleb.net/blog/2012/07/ios-hackers-handbook/)　·　Ole Begemann

# Book Review: iOS Hacker's Handbook

[![iOS Hacker's Handbook Cover](https://oleb.net/media/ios-hackers-handbook.jpg)](https://www.amazon.com/iOS-Hackers-Handbook-Charlie-Miller/dp/1118204123)

Most of the things discussed in the [iOS Hacker’s Handbook](https://www.amazon.com/iOS-Hackers-Handbook-Charlie-Miller/dp/1118204123) are probably not directly relevant to most app developers. In fact, if you’re like me, you won’t even understand a lot of the explanations and examples because they are full of assembly code. And yet, despite the fact that the book is way over my head in many ways, I highly recommend it to any iOS developer.

# iOS Security Measures

The book begins with a short description of the security architecture on iOS and how it evolved since 2007. This short history lesson makes you appreciate how much effort any platform developer has to put into security today and how far iOS security has come along. iOS 5 not only enforces sandboxing and code signing for all processes, it also uses measures like [Data execution prevention](https://en.wikipedia.org/wiki/Data_execution_prevention) (DEP)^[1](#fn:1) and [Address space layout randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization) (ASLR)^[2](#fn:2) to make it harder for attackers to exploit vulnerabilities.

Incredible as it may seem today, iPhone OS 1.0 did not have any of these features:

> There was no privilege separation: All processes ran as root. There was no code-signing enforcement. There was no DEP. There was no ASLR. There was no sandboxing.

# Attack Vectors

A hacker’s handbook is not complete without discussing how an attacker might try to circumvent these security measures and find vulnerabilities in them, of course. And in fact, a good part of the book deals with these topics. The attack methods mentioned include [fuzzing](https://en.wikipedia.org/wiki/Fuzz_testing) (a way to automate the process of feeding an app tampered data that could expose vulnerabilities in parsers and renderers), [Return-oriented programming](https://en.wikipedia.org/wiki/Return-oriented_programming) (ROP)^[3](#fn:3) and ways to get around ASLR and find vulnerabilities in the kernel.

The authors go into a lot of detail here. They describe the reasoning and procedure for several successful attacks on various iOS versions, including the code you have to write to reproduce them on your on (jailbroken) device. An example is how [Charlie Miller](https://twitter.com/0xcharlie/) took advantage of a bug in the kernel’s code signing checks to get an app to execute unsigned code downloaded from a remote server. You may remember that Miller managed to get an app showing this vulnerability on the App Store whereupon Apple [expelled him from the developer program](http://news.cnet.com/8301-27076_3-57320190-248/apple-boots-security-guru-who-exposed-iphone-exploit/).^[4](#fn:4)

Another example that really blew me away involves deep knowledge of WebKit’s memory allocator and garbage collector and then using correctly designed Javascript memory allocations in order to enforce a very specific heap layout that would then allow you to place a malicious object in a predictable place in memory. The detailed descriptions lets you appreciate both the hoops attackers (and security investigators) have to jump through and the things developers have to anticipate if they want to write secure code.

# Sandboxing, Code Signing and Jailbreaking Explained

One of the most useful pieces of knowledge I got from the book was the explanation how sandboxing and the code signing enforcment work under the covers. Both sandboxing and code signing take advantage of the [TrustedBSD](http://www.trustedbsd.org) project’s [Mandatory Access Control framework](http://www.trustedbsd.org/mac.html) and its ability to inject permission checks into many potentially destructive system calls. The sandbox kernel extension checks the entitlements of the current process and rejects the system call if the process doesn’t have the proper entitlement to execute it.

I now definitely appreciate more what an important part of security the locking down of the device plays. By not allowing the execution of arbitrary code, Apple really doesn’t just want to patronize users and developers. It’s worth realizing that jailbreaking a device completely breaks the device’s security architecture.^[5](#fn:5)

The authors also devote one chapter to describing the inner workings of various jailbreaking processes. If you want to follow along with the extensive sample code in the book, a jailbroken device is required (I didn’t and still enjoyed it).

# Conclusion

For app developers, the books is a very interesting read even if a lot of the contents will not be usable in your day-to-way work. Reading it definitely helps to develop a mindset that can make you write more secure code, though. And that is a very good thing.

1. DEP prevents the execution of code from memory regions that are writable for an application. Without DEP, an application could download malicious code from the network and simply mark the region where this code is stored in memory as executable. (The requirement that all code must be signed by Apple before it can be executed also helps against such an attack.) [↩︎](#fnref:1)
2. ASLR randomly arranges the memory locations of library code. When attackers can’t rely on where in memory certain libraries are located, it is much harder for them to write an exploit. In iOS 5, ASLR is implemented for user space processes. As mentioned on a slide in the WWDC 2012 keynote, [ASLR for the kernel space comes with iOS 6](http://nakedsecurity.sophos.com/2012/06/12/wwdc-apple-security-strengths-weaknesses/). [↩︎](#fnref:2)
3. ROP is way to circumvent DEP and code signing where the attacker tries to build the malicious code he wants to execute out of code fragments in the existing (already code-signed) libraries. [↩︎](#fnref:3)
4. Apple [fixed this vulnerability in iOS 5.0.1](http://support.apple.com/kb/HT5052?viewlocale=en_US&locale=en_US). [↩︎](#fnref:4)
5. Here’s a relevant quote from the book:

  > [iOS’s] Mandatory Code Signing is much stronger than DEP [Data Execution Prevention]. As a way around these memory protections, attackers typically use Return Oriented Programming (ROP). Against systems with DEP or similar protections, attackers need to perform ROP only long enough to disable DEP and then execute their native code payloads. However, in iOS, it is impossible to turn off the Mandatory Code Signing, and because the native code payload will not be signed, it cannot be run. Therefore, the entire iOS payload must be executed in ROP, which is much more difficult to accomplish than the analogous attack against DEP.

  [↩︎](#fnref:5)
