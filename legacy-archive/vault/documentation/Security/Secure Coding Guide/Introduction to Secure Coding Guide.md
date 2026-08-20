---
title: Secure Coding Guide
apple_id: TP40002415
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html
archived_at: '2026-07-18T02:06:26.481958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Types%20of%20Security%20Vulnerabilities.md)

# Introduction to Secure Coding Guide

Secure coding is the practice of writing software that’s resistant to attack by malicious or mischievous people or programs. An insecure program can provide access for an attacker to take control of a server or a user’s computer, resulting in anything from denial of service to a single user, to the compromise of secrets, loss of service, or damage to the systems of thousands of users. Secure coding helps protect a user’s data from theft or corruption.

Secure coding is important for all software, from small scripts your write for yourself to large scale, commercial apps. If you write software of any kind, familiarize yourself with the information in this document.

Security is not something that can be added to software as an afterthought. Just as a shed made out of cardboard cannot be made secure by adding a padlock to the door, an insecure tool or application may require extensive redesign to secure it. You must identify the nature of the threats to your software and incorporate secure coding practices throughout the planning and development of your product. This book describes specific types of vulnerabilities and gives guidance on code hardening techniques to fix them.

### Hackers and Attackers

Contrary to the usage often found in the media, within the computer industry the term _hacker_ refers to an expert programmer—one who enjoys learning about the intricacies of code or an operating system. In general, hackers are not malicious. When most hackers find security vulnerabilities, they inform the company or organization that’s responsible for the code so that they can fix the problem. Unfortunately, however, a small but important minority of hackers devise _exploits_, code that takes advantage of the vulnerability, and use them to attack, or publish the exploits for others to use.

Attackers may be motivated by a desire to steal money, identities, and other secrets for personal gain; corporate secrets for their employer’s or their own use; or state secrets for use by hostile governments or terrorist organizations. Some break into apps or operating systems just to show that they can do it. Others seek to do real damage. Because attacks can be automated and replicated, any weakness, no matter how slight, poses a real danger.

### No Platform Is Immune

Both macOS and iOS have strong records when it comes to resisting attack. Originally built on open source software such as BSD, and reinforced over the years with technologies like code signing and App Sandbox, macOS offers many layers of defense. iOS provides even greater security by strictly enforcing sandboxing for all apps. Additionally, Apple actively reviews all of its platforms for vulnerabilities, and issues downloadable security updates regularly.

That’s the good news. The bad news is that apps and operating systems are constantly under attack. Every day, attackers look for new vulnerabilities, and for ways to exploit them. Further, a large-scale, widespread attack isn’t needed to cause monetary and other damages; a single compromised app is sufficient if it puts valuable information at risk. Although major attacks of viruses or worms get a lot of attention from the media, the destruction or compromise of data on a single computer is what matters to the average user. So it’s important to take every security risk seriously, and work to correct known problems quickly.

First, familiarize yourself with the concepts in _[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_.

This document then starts with a brief introduction to the nature of each of the types of security vulnerability commonly found in software. If you’re not sure what a race condition is, for example, or why it poses a security risk, the [Types of Security Vulnerabilities](Types%20of%20Security%20Vulnerabilities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkmrzfvjvomq) chapter is the place to start.

The remaining chapters detail specific types of security vulnerabilities. These chapters can be read in any order, or as suggested by the software development checklist in [Security Development Checklists](Security%20Development%20Checklists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknltc).

- [Avoiding Buffer Overflows and Underflows](Avoiding%20Buffer%20Overflows%20and%20Underflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdknzxfvjvomi) describes the various types of buffer overflows and explains how to avoid them.
- [Validating Input and Interprocess Communication](Validating%20Input%20and%20Interprocess%20Communication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenbwfvjvomy) discusses why and how you must validate every type of input your program receives from untrusted sources.
- [Race Conditions and Secure File Operations](Race%20Conditions%20and%20Secure%20File%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobvfvjvomi) explains how race conditions occur, discusses ways to avoid them, and describes insecure and secure file operations.
- [Elevating Privileges Safely](Elevating%20Privileges%20Safely.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomi) describes how to avoid running code with elevated privileges and what to do if you can’t avoid it entirely.
- [Designing Secure User Interfaces](Designing%20Secure%20User%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqnrsfvjvomi) discusses how the user interface of a program can enhance or compromise security and gives some guidance on how to write a security-enhancing UI.
- [Designing Secure Helpers and Daemons](Designing%20Secure%20Helpers%20and%20Daemons.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmrnknltc) describes how to design helper applications in ways that are conducive to privilege separation.

The appendix [Security Development Checklists](Security%20Development%20Checklists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknltc) provides a convenient list of tasks that you should perform before shipping an application, while the appendix [Third-Party Software Security Guidelines](Third-Party%20Software%20Security%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmjrfvjvomi) provides a list of guidelines for third-party applications bundled with macOS.

This document concentrates on security vulnerabilities and programming practices of special interest to developers using macOS or iOS. For more general treatments, see the following books and documents:

- See Viega and McGraw, _Building Secure Software_, Addison Wesley, 2002; for a general discussion of secure programming, especially as it relates to C programming and writing scripts.
- See Wheeler, _Secure Programming HOWTO_, available at [http://www.dwheeler.com/secure-programs/](http://www.dwheeler.com/secure-programs/); for discussions of several types of security vulnerabilities and programming tips for UNIX-based operating systems, most of which apply to macOS.
- See Cranor and Garfinkel, _Security and Usability: Designing Secure Systems that People Can Use_, O’Reilly, 2005; for information on writing user interfaces that enhance security.

For documentation of security-related application programming interfaces (APIs), see the following documents:

- For information on secure networking, see _[Secure Transport Reference](https://developer.apple.com/documentation/security/secure_transport)_.
- For information on macOS authorization and authentication APIs, see _[Authorization Services C Reference](https://developer.apple.com/documentation/security/authorization_services)_ and _[Security Foundation Framework Reference](https://developer.apple.com/documentation/securityfoundation)_.
- If you are using digital certificates for authentication, see _[Certificate, Key, and Trust Services Reference](https://developer.apple.com/documentation/security/certificate_key_and_trust_services)_.
- For secure storage of passwords and other secrets, see _[Keychain Services Reference](https://developer.apple.com/documentation/security/keychain_services)_.

For information about security in web application design, visit [http://www.owasp.org/](http://www.owasp.org/).

[Next](Types%20of%20Security%20Vulnerabilities.md)

