---
title: Secure Coding Guide
apple_id: TP40002415
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/SecurityGuidelines.html
archived_at: '2026-07-18T02:06:23.982187Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Secure Coding Guide](Introduction%20to%20Secure%20Coding%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Security%20Development%20Checklists.md)

# Third-Party Software Security Guidelines

This appendix provides secure coding guidelines for software to be bundled with Apple products.

Insecure software can pose a risk to the overall security of users’ systems. Security issues can lead to negative publicity and end-user support problems for Apple and third parties.

Your bundled software may use the Internet to communicate with your servers or third party servers. If so, you should provide clear and concise information to the user about what information is sent or retrieved and the reason for sending or receiving it.

Encryption should be used to protect the information while in transit. Servers should be authenticated before transferring information.

Provide information on how to upgrade to the latest version. Consider implementing a “Check for updates…” feature. Customers expect (and should receive) security fixes that affect the software version they are running.

You should have a way to communicate available security fixes to customers.

If possible, you should use the Mac App Store for providing upgrades. The Mac App Store provides a single, standard interface for updating all of a user’s software. The Mac App Store also provides an expedited app review process for handling critical security fixes.

Store user-specific information in the home directory, with appropriate file system permissions.

Take special care when dealing with shared data or preferences.

Follow the guidelines about file system permissions set forth in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

Take care to avoid race conditions and information disclosure when using temporary files. If possible, use a user-specific temporary file directory.

Do not require or encourage users to be logged in as an admin user to install or use your application. You should regularly test your application as a normal user to make sure that it works as expected.

Educate your developers on how to write secure code to avoid the most common classes of vulnerabilities:

- Buffer overflows
- Integer overflows
- Race conditions
- Format string vulnerabilities

Pay special attention to code that:

- deals with potentially untrusted data, such as documents or URLs
- communicates over the network
- handles passwords or other sensitive information
- runs with elevated privileges such as root or in the kernel

Use APIs appropriate for the task:

- Use APIs that take security into account in their design.
- Avoid low-level C code when possible (e.g. use NSString instead of C-strings).
- Use the security features of macOS to protect user data.

As appropriate for your product, use the following QA techniques to find potential security issues:

- Test for invalid and unexpected data in addition to testing what is expected. (Use fuzzing tools, include unit tests that test for failure, and so on.)
- Static code analysis
- Code reviews and audits

The other chapters in this document describe best practices for writing secure code, including more information on the topics referenced above.

_[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_ and _[Cryptographic Services Guide](../Cryptographic%20Services%20Guide/About%20Cryptographic%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzs)_ contain detailed information on security functionality in macOS that developers can use.

[Next](Document%20Revision%20History.md)[Previous](Security%20Development%20Checklists.md)

