---
title: Secure Coding Guide
apple_id: TP40002415
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/Glossary.html
archived_at: '2026-07-18T02:06:22.315543Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Secure Coding Guide](Introduction%20to%20Secure%20Coding%20Guide.md)


[Next](Index.md)[Previous](Document%20Revision%20History.md)

# Glossary

- __AES encryption__

  Abbreviation for Advanced Encryption Standard encryption. A Federal Information Processing Standard (FIPS), described in FIPS publication 197. AES has been adopted by the U.S. government for the protection of sensitive, non-classified information.

- __attacker__

  Someone deliberately trying to make a program or operating system do something that it’s not supposed to do, such as allowing the attacker to execute code or read private data.

- __authentication__

  The process by which a person or other entity (such as a server) proves that it is who (or what) it says it is. Compare with [authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojufvjvonq).

- __authorization__

  The process by which an entity such as a user or a server gets the right to perform a privileged operation. (Authorization can also refer to the right itself, as in “Bob has the authorization to run that program.”) Authorization usually involves first authenticating the entity and then determining whether it has the appropriate privileges. See also [authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojufvjvoni).

- __buffer overflow__

  The insertion of more data into a memory buffer than was reserved for the buffer, resulting in memory locations outside the buffer being overwritten. See also [heap overflow](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojufvjvomi) and [stack overflow](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojufvjvomq).

- __CDSA__

  Abbreviation for Common Data Security Architecture. An open software standard for a security infrastructure that provides a wide array of security services, including fine-grained access permissions, authentication of users, encryption, and secure data storage. CDSA has a standard application programming interface, called CSSM.

- __CERT Coordination Center__

  A center of Internet security expertise, located at the Software Engineering Institute, a federally funded research and development center operated by Carnegie Mellon University. CERT is an acronym for Computer Emergency Readiness Team.)

- __certificate__

  See [digital certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojufvjvony).

- __Common Criteria__

  A standardized process and set of standards that can be used to evaluate the security of software products developed by the governments of the United States, Canada, the United Kingdom, France, Germany, and the Netherlands.

- __CSSM__

  Abbreviation for Common Security Services Manager. A public application programming interface for CDSA. CSSM also defines an interface for plug-ins that implement security services for a particular operating system and hardware environment.

- __CVE__

  Abbreviation for Common Vulnerabilities and Exposures. A dictionary of standard names for security vulnerabilities located at [http://www.cve.mitre.org/](http://www.cve.mitre.org/). You can run an Internet search on the CVE number to read details about the vulnerability.

- __digital certificate__

  A collection of data used to verify the identity of the holder. macOS supports the X.509 standard for digital certificates.

- __exploit__

  A program or sample code that demonstrates how to take advantage of a vulnerability.)

- __FileVault__

  An macOS feature, configured through the Security system preference, that encrypts everything in on the root volume (or everything in the user’s home directory prior to 10.7).

- __hacker__

  An expert programmer—generally one with the skill to create an exploit. Most hackers do not attack other programs, and some publish exploits with the intent of forcing software developers to fix vulnerabilities.

- __heap__

  A region of memory reserved for use by a program during execution. Data can be written to or read from any location on the heap, which grows upward (toward higher memory addresses). Compare with stack.

- __heap overflow__

  A buffer overflow in the heap.

- __homographs__

  Characters that look the same but have different Unicode values, such as the Roman character p and the Russian glyph that is pronounced like “r”.

- __integer overflow__

  A buffer overflow caused by entering a number that is too large for an integer data type.

- __Kerberos__

  An industry-standard protocol created by the Massachusetts Institute of Technology (MIT) to provide authentication over a network.

- __keychain__

  A database used in macOS to store encrypted passwords, private keys, and other secrets. It is also used to store certificates and other non-secret information that is used in cryptography and authentication.

- __Keychain Access utility__

  An application that can be used to manipulate data in the keychain.

- __Keychain Services__

  A public API that can be used to manipulate data in the keychain.

- __level of trust__

  The confidence a user can have in the validity of a certificate. The level of trust for a certificate is used together with the trust policy to answer the question “Should I trust this certificate for this action?”

- __nonrepudiation__

  A process or technique making it impossible for a user to deny performing an operation (such as using a specific credit card number).

- __Open Directory__

  The directory server provided by macOS for secure storage of passwords and user authentication.

- __permissions__

  See [privileges](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojufvjvona).

- __phishing__

  A social engineering technique in which an email or web page that spoofs one from a legitimate business is used to trick a user into giving personal data and secrets (such as passwords) to someone who has malicious intent.

- __policy database__

  A database containing the set of rules the Security Server uses to determine authorization.

- __privileged operation__

  An operation that requires special rights or privileges.

- __privileges__

  The type of access to a file or directory (read, write, execute, traverse, and so forth) granted to a user or to a group.

- __race condition__

  The occurrence of two events out of sequence.

- __root kit__

  Malicious code that, by running in the kernel, can not only take over control of the system but can also cover up all evidence of its own existence.

- __root privileges__

  Having the unrestricted permission to perform any operation on the system.

- __signal__

  A message sent from one process to another in a UNIX-based operating system (such as macOS)

- __social engineering__

  As applied to security, tricking a user into giving up secrets or into giving access to a computer to an attacker.

- __smart card__

  A plastic card similar in size to a credit card that has memory and a microprocessor embedded in it. A smart card can store and process information, including passwords, certificates, and keys.

- __stack__

  A region of memory reserved for use by a specific program and used to control program flow. Data is put on the stack and removed in a last-in–first-out fashion. The stack grows downward (toward lower memory addresses). Compare with heap.

- __stack overflow__

  A buffer overflow on the stack.

- __time of check–time of use (TOCTOU)__

  A race condition in which an attacker creates, writes to, or alters a file between the time when a program checks the status of the file and when the program writes to it.

- __trust policy__

  A set of rules that specify the appropriate uses for a certificate that has a specific level of trust. For example, the trust policy for a browser might state that if a certificate has expired, the user should be prompted for permission before a secure session is opened with a web server.

- __vulnerability__

  A feature of the way a program was written—either a design flaw or a bug—that makes it possible for a hacker to attack the program.

[Next](Index.md)[Previous](Document%20Revision%20History.md)

