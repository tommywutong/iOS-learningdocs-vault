---
title: Secure Coding Guide
apple_id: TP40002415
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/SecurityDevelopmentChecklists/SecurityDevelopmentChecklists.html
archived_at: '2026-07-18T02:06:28.354798Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Secure Coding Guide](Introduction%20to%20Secure%20Coding%20Guide.md)


[Next](Third-Party%20Software%20Security%20Guidelines.md)[Previous](Avoiding%20Injection%20Attacks%20and%20XSS.md)

# Security Development Checklists

This appendix presents a set of security audit checklists that you can use to help reduce the security vulnerabilities of your software. These checklists are designed to be used during software development. If you read this section all the way through before you start coding, you may avoid many security pitfalls that are difficult to correct in a completed program.

Note that these checklists are not exhaustive; you might not have any of the potential vulnerabilities discussed here and still have insecure code. Also, as the author of the code, you are probably too close to the code to be fully objective, and thus may overlook certain flaws. For this reason, it’s very important that you have your code reviewed for security problems by an independent reviewer. A security expert would be best, but any competent programmer, if aware of what to look for, might find problems that you may have missed. In addition, whenever the code is updated or changed in any way, including to fix bugs, it should be checked again for security problems.

This checklist is intended to determine whether your code ever runs with elevated privileges, and if it does, how best to do so safely. Note that it’s best to avoid running with elevated privileges if possible; see [Avoiding Elevated Privileges](Elevating%20Privileges%20Safely.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvooi).

1. __Reduce privileges whenever possible.__

   If you are using privilege separation with sandboxing or other privilege-limiting techniques, you should be careful to ensure that your helper tools are designed to limit the damage that they can cause if the main application gets compromised, and vice-versa. Read [Designing Secure Helpers and Daemons](Designing%20Secure%20Helpers%20and%20Daemons.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmrnknltc) to learn how.

   Also, for daemons that start with elevated privileges and then drop privileges, you should always use a locally unique user ID for your program. See [Run Daemons as Unique Users](Designing%20Secure%20Helpers%20and%20Daemons.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmrnknlto) to learn more.
2. __Use elevated privileges sparingly, and only in privileged helpers.__

   In most cases, a program can get by without elevated privileges, but sometimes a program needs elevated privileges to perform a limited number of operations, such as writing files to a privileged directory or opening a privileged port.

   If an attacker finds a vulnerability that allows execution of arbitrary code, the attacker’s code runs with the same privilege as the running code, and can take complete control of the computer if that code has root privileges. Because of this risk, you should avoid elevating privileges if at all possible.

   If you must run code with elevated privileges, here are some rules:

   - Never run your main process as a different user. Instead, create a separate helper tool that runs with elevated privileges.
   - Your helper tool should do as little as possible.
   - Your helper tool should restrict what you can ask it to do as much as possible.
   - Your helper tool should either drop the elevated privileges or stop executing as soon as possible.

   See [Elevating Privileges Safely](Elevating%20Privileges%20Safely.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomi) and [Designing Secure Helpers and Daemons](Designing%20Secure%20Helpers%20and%20Daemons.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmrnknltc) for more information.
3. __Use__ `launchd` __when possible.__

   If you are writing a daemon or other process that runs with elevated privileges, you should always use `launchd` to start it. (To learn why other mechanisms are not recommended, read [Limitations and Risks of Other Mechanisms](Elevating%20Privileges%20Safely.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomrv).)

   For more information on `launchd`, see the manual pages for `launchd`, `launchctl`, and `launchd.plist`, and _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_. For more information about startup items, see _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.
4. __Avoid using sudo programmatically.__

   If authorized to do so in the `sudoers` file, a user can use `sudo` to execute a command as root. The `sudo` command is intended for occasional administrative use by a user sitting at the computer and typing into the Terminal application. Its use in scripts or called from code is not secure.

   After executing the `sudo` command—which requires authenticating by entering a password—there is a five-minute period (by default) during which the sudo command can be executed without further authentication. It’s possible for another process to take advantage of this situation to execute a command as root.

   Further, there is no encryption or protection of the command being executed. Because sudo is used to execute privileged commands, the command arguments often include user names, passwords, and other information that should be kept secret. A command executed in this way by a script or other code can expose confidential data to possible interception and compromise.
5. __Minimize the amount of code that must be run with elevated privileges.__

   Ask yourself approximately how many lines of code need to run with elevated privileges. If this answer is either “all” or is a difficult number to compute, then it will be very difficult to perform a security review of your software.

   If you can’t determine how to factor your application to separate out the code that needs privileges, you are strongly encouraged to seek assistance with your project immediately. If you are an ADC member, you are encouraged to ask for help from Apple engineers with factoring your code and performing a security audit. If you are not an ADC member, see the ADC membership page at [http://developer.apple.com/programs/](https://developer.apple.com/programs/).
6. __Never run a GUI application with elevated privileges.__

   You should never run a GUI application with elevated privileges. Any GUI application links in many libraries over which you have no control and which, due to their size and complexity, are very likely to contain security vulnerabilities. In this case, your application runs in an environment set by the GUI, not by your code. Your code and your user’s data can then be compromised by the exploitation of any vulnerabilities in the libraries or environment of the graphical interface.

Some security vulnerabilities are related to reading or writing files. This checklist is intended to help you find any such vulnerabilities in your code.

1. __Be careful when working with files in untrusted locations.__

   If you write to any directory owned by the user, then there is a possibility that the user will modify or corrupt your files.

   Similarly, if you write temporary files to a publicly writable place (for example, `/tmp`, `/var/tmp`, `/Library/Caches` or another specific place with this characteristic), an attacker may be able to modify your files before the next time you read them.

   If your code reads and writes files (and in particular if it uses files for interprocess communication), you should put those files in a safe directory to which only you have write access.

   For more information about vulnerabilities associated with writing files, and how to minimize the risks, see [Time of Check Versus Time of Use](Race%20Conditions%20and%20Secure%20File%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobvfvjvomq).
2. __Avoid untrusted configuration files, preference files, or environment variables.__

   In many cases, the user can control environment variables, configuration files, and preferences. If you are executing a program for the user with elevated privileges, you are giving the user the opportunity to perform operations that they cannot ordinarily do. Therefore, you should ensure that the behavior of your privileged code does not depend on these things.

   This means:

   - Validate all input, whether directly from the user or through environment variables, configuration files, preferences files, or other files.

     In the case of environment variables, the effect might not be immediate or obvious; however the user might be able to modify the behavior of your program or of other programs or system calls.
   - Make sure that file paths do not contain wildcard characters, such as `../` or `~`, which an attacker can use to switch the current directory to one under the attacker’s control.
   - Explicitly set the privileges, environment variables, and resources available to the running process, rather than assuming that the process has inherited the correct environment.
3. __Load kernel extensions carefully (or not at all).__

   A kernel extension is the ultimate privileged code—it has access to levels of the operating system that cannot be touched by ordinary code, even running as root. You must be extremely careful why, how, and when you load a kernel extension to guard against being fooled into loading the wrong one. It’s possible to load a root kit if you’re not sufficiently careful. (A _root kit_ is malicious code that, by running in the kernel, can not only take over control of the system but can cover up all evidence of its own existence.)

   To make sure that an attacker hasn’t somehow substituted his or her own kernel extension for yours, you should always store kernel extensions in secure locations. You may, if desired, use code signing or hashes to further verify their authenticity, but this does not remove the need to protect the extension with appropriate permissions. (Time-of-check vs. time-of-use attacks are still possible.) Note that in recent versions of macOS, this is partially mitigated by the KEXT loading system, which refuses to load any kext binary whose owner is not `root` or whose group is not `wheel`.

   In general, you should avoid writing kernel extensions (see [Keep Out](https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/keepout/keepout.html#//apple_ref/doc/uid/TP30000905-CH205) in _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_). However, if you must use a kernel extension, use the facilities built into macOS to load your extension and be sure to load the extension from a separate privileged process.

   See [Elevating Privileges Safely](Elevating%20Privileges%20Safely.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobzfvjvomi) to learn more about the safe use of root access. See _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ for more information on writing and loading kernel extensions. For help on writing device drivers, see _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

This checklist is intended to help you find vulnerabilities related to sending and receiving information over a network. If your project does not contain any tool or application that sends or receives information over a network, skip to [Audit Logs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknltk) (for servers) or [Integer and Buffer Overflows](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknlto) for all other products.

1. __Use assigned port numbers.__

   Port numbers 0 through 1023 are reserved for use by certain services specified by the Internet Assigned Numbers Authority (IANA; see [http://www.iana.org/](http://www.iana.org/)). On many systems including macOS, only processes running as root can bind to these ports. It is not safe, however, to assume that any communications coming over these privileged ports can be trusted. It’s possible that an attacker has obtained root access and used it to bind to a privileged port. Furthermore, on some systems, root access is not needed to bind to these ports.

   You should also be aware that if you use the `SO_REUSEADDR` socket option with UDP, it is possible for a local attacker to hijack your port.

   Therefore, you should always use port numbers assigned by the IANA, you should always check return codes to make sure you have connected successfully, and you should check that you are connected to the correct port. Also, as always, never trust input data, even if it’s coming over a privileged port. Whether data is being read from a file, entered by a user, or received over a network, you must validate all input.

   See [Validating Input and Interprocess Communication](Validating%20Input%20and%20Interprocess%20Communication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenbwfvjvomy) for more information about validating input.
2. __Choose an appropriate transport protocol.__

   Lower-level protocols, such as UDP, provide higher performance for some types of traffic, but are easier to spoof than higher-level protocols, such as TCP.

   Note that if you’re using TCP, you still need to worry about authenticating both ends of the connection, but there are encryption layers you can add to increase security.
3. __Use existing authentication services when authentication is needed.__

   If you’re providing a free and nonconfidential service, and do not process user input, then authentication is not necessary. On the other hand, if any secret information is being exchanged, the user is allowed to enter data that your program processes, or there is any reason to restrict user access, then you should authenticate every user.

   macOS provides a variety of secure network APIs and authorization services, all of which perform authentication. You should always use these services rather than creating your own authentication mechanism. For one thing, authentication is very difficult to do correctly, and dangerous to get wrong. If an attacker breaks your authentication scheme, you could compromise secrets or give the attacker an entry to your system.

   The only approved authorization mechanism for networked applications is Kerberos; see [Client-Server Authentication](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknltm). For more information on secure networking, see _[Secure Transport Reference](https://developer.apple.com/documentation/security/secure_transport)_ and _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_.
4. __Verify access programmatically.__

   UI limitations do not protect your service from attack. If your service provides functionality that should only be accessible to certain users, that service _must_ perform appropriate checks to determine whether the current user is authorized to access that functionality.

   If you do not do this, then someone sufficiently familiar with your service can potentially perform unauthorized operations by modifying URLs, sending malicious Apple events, and so on.
5. __Fail gracefully.__

   If a server is unavailable, either because of some problem with the network or because the server is under a denial of service attack, your client application should limit the frequency and number of retries and should give the user the opportunity to cancel the operation.

   Poorly-designed clients that retry connections too frequently and too insistently, or that hang while waiting for a connection, can inadvertently contribute to—or cause their own—denial of service.
6. __Design your service to handle high connection volume.__

   Your daemon should be capable of surviving a denial of service attack without crashing or losing data. In addition, you should limit the total amount of processor time, memory, and disk space each daemon can use, so that a denial of service attack on any given daemon does not result in denial of service to every process on the system.

   You can use the `pfctl`firewall program to control packets and traffic flow for internet daemons. For more information on `pfctl`, see the `pfctl` manual page. For more advice on dealing with denial of service attacks, see Wheeler, _Secure Programming HOWTO_, available at [http://www.dwheeler.com/secure-programs/](http://www.dwheeler.com/secure-programs/).
7. __Design hash functions carefully.__

   Hash tables are often used to improve search performance. However, when there are hash collisions (where two items in the list have the same hash result), a slower (often linear) search must be used to resolve the conflict. If it is possible for a user to deliberately generate different requests that have the same hash result, by making many such requests an attacker can mount a denial of service attack.

   It is possible to design hash tables that use complex data structures such as trees in the collision case. Doing so can significantly reduce the damage caused by these attacks.

It’s very important to audit attempts to connect to a server or to gain authorization to use a secure program. If someone is attempting to attack your program, you should know what they are doing and how they are doing it.

Furthermore, if your program is attacked successfully, your audit log is the only way you can determine what happened and how extensive the security breach was. This checklist is intended to help you make sure you have an adequate logging mechanism in place.

1. __Audit attempts to connect.__

   Your daemon or secure program should audit connection attempts (both successful attempts and failures).

   Note that an attacker can attempt to use the audit log itself to create a denial of service attack; therefore, you should limit the rate of entering audit messages and the total size of the log file. You also need to validate the input to the log itself, so that an attacker can’t enter special characters such as the newline character that you might misinterpret when reading the log.

   See Wheeler, _Secure Programming HOWTO_ for some advice on audit logs.
2. __Use the__ `libbsm` __auditing library where possible.__

   The `libbsm` auditing library is part of the TrustedBSD project, which in turn is a set of trusted extensions to the FreeBSD operating system. Apple has contributed to this project and has incorporated the audit library into the Darwin kernel of the macOS operating system. (This library is not available in iOS.)

   You can use the `libbsm` auditing library to implement auditing of your program for login and authorization attempts. This library gives you a lot of control over which events are audited and how to handle denial of service attacks.

   The libbsm project is located at [http://www.opensource.apple.com/darwinsource/Current/bsm/](http://www.opensource.apple.com/darwinsource/Current/bsm/).
3. __If you cannot use__ `libbsm`__, be careful when writing audit trails.__

   When using audit mechanisms other than `libbsm`, there are a number of pitfalls you should avoid, depending on what audit mechanism you are using:

   - `syslog`

     Prior to the implementation of the `libbsm` auditing library, the standard C library function `syslog` was most commonly used to write data to a log file. If you are using `syslog`, consider switching to `libbsm`, which gives you more options to deal with denial of service attacks. If you want to stay with `syslog`, be sure your auditing code is resistant to denial of service attacks, as discussed in step 1.
   - Custom log file

     If you have implemented your own custom logging service, consider switching to `libbsm` to avoid inadvertently creating a security vulnerability. In addition, if you use `libbsm` your code will be more easily maintainable and will benefit from future enhancements to the `libbsm` code.

     If you stick with your own custom logging service, you must make certain that it is resistant to denial of service attacks (see step 1) and that an attacker can’t tamper with the contents of the log file.

     Because your log file must be either encrypted or protected with access controls to prevent tampering, you must also provide tools for reading and processing your log file.

     Finally, be sure your custom logging code is audited for security vulnerabilities.

If any private or secret information is passed between a daemon and a client process, both ends of the connection should be authenticated. This checklist is intended to help you determine whether your daemon’s authentication mechanism is safe and adequate. If you are not writing a daemon, skip to [Integer and Buffer Overflows](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknlto).

1. __Do not store, validate, or modify passwords yourself.__

   It’s a very bad idea to store, validate, or modify passwords yourself, as it’s very hard to do so securely, and macOS and iOS provide secure facilities for just that purpose.

   - In macOS, you can use the keychain to store passwords and Authorization Services to create, modify, delete, and validate user passwords (see _[Keychain Services Reference](https://developer.apple.com/documentation/security/keychain_services)_ and _[Authorization Services Programming Guide](../Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_).
   - In macOS, if you have access to an macOS Server setup, you can use Open Directory (see _[Open Directory Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Directory/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000917)_) to store passwords and authenticate users.
   - On an iOS device, you can use the keychain to store passwords. iOS devices authenticate the application that is attempting to obtain a keychain item rather than asking the user for a password. By storing data in the keychain, you also ensure that they remain encrypted in any device backups.
2. __Never send passwords over a network connection in cleartext form.__

   You should never assume that an unencrypted network connection is secure. Information on an unencrypted network can be intercepted by any individual or organization between the client and the server.

   Even an intranet, which does not go outside of your company, is not secure. A large percentage of cyber crime is committed by company insiders, who can be assumed to have access to a network inside a firewall.

   macOS provides APIs for secure network connections; see _[Secure Transport Reference](https://developer.apple.com/documentation/security/secure_transport)_ and _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_ for details.
3. __Use server authentication as an anti-spoofing measure.__

   Although server authentication is optional in the SSL/TLS protocols, you should always do it. Otherwise, an attacker might spoof your server, injuring your users and damaging your reputation in the process.
4. __Use reasonable pasword policies.__

   - Password strength

     In general, it is better to provide the user with a means to evaluate the strength of a proposed password rather than to require specific combinations of letters, numbers, or punctuation, as arbitrary rules tend to cause people to choose bad passwords to fit the standard (Firstname.123) instead of choosing good passwords.
   - Password expiration

     Password expiration has pros and cons. If your service transmits passwords in cleartext form, it is absolutely essential.

     If your password transmission is considered secure, however, password expiration can actually weaken security by causing people to choose weaker passwords that they can remember or to write their passwords down on sticky notes on their monitors.

     See [Password Expiration Considered Harmful](http://cryptosmith.com/password-sanity/exp-harmful/) for more information.
   - Non-password authentication

     Hardware-token-based authentication provides far more security than any password scheme because the correct response changes every time you use it. These tokens should always be combined with a PIN, and you should educate your users so that they do not write their user name or PIN on the token itself.
   - Disabled accounts

     When an employee leaves or a user closes an account, the account should be disabled so that it cannot be compromised by an attacker. The more active accounts you have, the greater the probability that one will have a weak password.
   - Expired accounts

     Expiring unused accounts reduces the number of active accounts, and in so doing, reduces the risk of an old account getting compromised by someone stealing a password that the user has used for some other service.

     Note, however, that expiring a user account without warning the user first is generally a bad idea. If you do not have a means of contacting the user, expiring accounts are generally considered poor form.
   - Changing passwords

     You can require that the client application support the ability to change passwords, or you can require that the user change the password using a web interface on the server itself.

     In either case, the user (or the client, on behalf of the user) must provide the previous password along with the new password (twice unless the client is updating it programmatically over a sufficiently robust channel).
   - Lost password retrieval (such as a system that triggers the user’s memory or a series of questions designed to authenticate the user without a password)

     Make sure your authentication method is not so insecure that an attacker doesn’t even bother to try a password, and be careful not to leak information, such as the correct length of the password, the email address to which the recovered password is sent, or whether the user ID is valid.

     You should always allow (and perhaps even require) customer to choose their own security questions. Pre-written questions are inherently dangerous because any question that is general enough for you to ask it of a large number of people is:

     - likely to be a request for information that a large number of that person’s friends already know. In all likelihood, everyone who attended your high school can guess (in a handful of guesses) who your kindergarten teacher was, who your high school mascot was, and so on.
     - probably on your public profile on a social networking site. For example, if you ask where you were born, chances are that’s public information. Even if it isn’t on your profile, someone can dig it up through government records.
     - potentially guessable given other information about the person. For example, given the last four digits of a social security number, someone’s birthdate, and the city in which that person was born, you can fairly easily guess the entire social security number.

     Finally, you should always allow your users the option of _not_ filing out security questions. The mere existence of security questions makes their accounts less secure, so security-conscious individuals should be allowed to refuse those questions entirely.
   - Limitations on password length (adjustable by the system administrator)

     In general, you should require passwords to be at least eight characters in length. (As a side note, if your server limits passwords to a maximum of eight characters, you need to rethink your design. There should be no maximum password length at all, if possible.)

   The more of these policies you enforce, the more secure your server will be. Rather than creating your own password database—which is difficult to do securely—you should use the Apple Password Server. See _[Open Directory Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Directory/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000917)_ for more information about the Password Server, _Directory Service Framework Reference_ for a list of Directory Services functions, and the manual pages for `pwpolicy(8)`, `passwd(1)`, `passwd(5)`, and `getpwent(3)` at [http://developer.apple.com/documentation/Darwin/Reference/ManPages/index.html](https://developer.apple.com/documentation/Darwin/Reference/ManPages/index.html) for tools to access the password database and set password policies.
5. __Do not store unencrypted passwords and do not reissue passwords.__

   In order to reissue a password, you first have to cache the unencrypted password, which is bad security practice. Furthermore, when you reissue a password, you might also be reusing that password in an inappropriate security context.

   For example, suppose your program is running on a web server, and you use SSL to communicate with clients. If you take a client’s password and use it to log into a database server to do something on the client’s behalf, there’s no way to guarantee that the database server keeps the password secure and does not pass it on to another server in cleartext form. Therefore, even though the password was in a secure context when it was being sent to the web server over SSL, when the web server reissues it, it’s in an insecure context.

   If you want to spare your client the trouble of logging in separately to each server, you should use some kind of forwardable authentication, such as Kerberos. For more information on Apple’s implementation of Kerberos, see [http://developer.apple.com/darwin/projects/kerberos/](https://developer.apple.com/darwin/projects/kerberos/).

   Under _no circumstances_ should you design a system in which system administrators or other employees can see users’ passwords. Your users are trusting you with passwords that they may use for other sites; therefore, it is extremely reckless to allow anyone else to see those passwords. Administrators should be allowed to reset passwords to new values, but should _never_ be allowed to see the passwords that are already there.
6. __Support Kerberos.__

   Kerberos is the only authorization service available over a network for macOS servers, and it offers single-sign-on capabilities. If you are writing a server to run on macOS, you should support Kerberos. When you do:

   1. Be sure you’re using the latest version (v5).
   2. Use a service-specific principal, not a host principal. Each service that uses Kerberos should have its own principal so that compromise of one key does not compromise more than one service. If you use a host principal, anyone who has your host key can spoof login by anybody on the system.

   The only alternative to Kerberos is combining SSL/TLS authentication with some other means of authorization such as an access control list.
7. __Restrict guest access appropriately.__

   If you allow guest access, be sure that guests are restricted in what they can do, and that your user interface makes clear to the system administrator what guests can do. Guest access should be off by default. It’s best if the administrator can disable guest access.

   Also, as noted previously, be sure to limit what guests can do in the code that actually performs the operation, not just in the code that generates the user interface. Otherwise, someone with sufficient knowledge of the system can potentially perform those unauthorized operations in other ways (by modifying URLs, for example).
8. __Do not implement your own directory service.__

   Open Directory is the directory server provided by macOS for secure storage of passwords and user authentication. It is important that you use this service and not try to implement your own, as secure directory servers are difficult to implement and an entire directory’s passwords can be compromised if it’s done wrong. See _[Open Directory Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Directory/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000917)_ for more information.
9. __Scrub (zero) user passwords from memory after validation.__

   Passwords must be kept in memory for the minimum amount of time possible and should be written over, not just released, when no longer needed. It is possible to read data out of memory even if the application no longer has pointers to it.

As discussed in [Avoiding Buffer Overflows and Underflows](Avoiding%20Buffer%20Overflows%20and%20Underflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdknzxfvjvomi), buffer overflows are a major source of security vulnerabilities. This checklist is intended to help you identify and correct buffer overflows in your program.

1. __Use unsigned values when calculating memory object offsets and sizes.__

   Signed values make it easier for an attacker to cause a buffer overflow, creating a security vulnerability, especially if your application accepts signed values from user input or other outside sources.

   Be aware that data structures referenced in parameters might contain signed values.

   See [Avoiding Integer Overflows and Underflows](Avoiding%20Buffer%20Overflows%20and%20Underflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdknzxfvjvony) and [Calculating Buffer Sizes](Avoiding%20Buffer%20Overflows%20and%20Underflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdknzxfvjvooi) for details.
2. __Check for integer overflows (or signed integer underflows) when calculating memory object offsets and sizes.__

   You must always check for integer overflows or underflows when calculating memory offsets or sizes. Integer overflows and underflows can corrupt memory in ways that can lead to execution of arbitrary code.

   See [Avoiding Integer Overflows and Underflows](Avoiding%20Buffer%20Overflows%20and%20Underflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdknzxfvjvony) and [Calculating Buffer Sizes](Avoiding%20Buffer%20Overflows%20and%20Underflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdknzxfvjvooi) for details.
3. __Avoid unsafe string-handling functions.__

   The functions [strcat](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/strcat.3.html#//apple_ref/doc/man/3/strcat), [strcpy](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/strcpy.3.html#//apple_ref/doc/man/3/strcpy), [strncat](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/strncat.3.html#//apple_ref/doc/man/3/strncat), [strncpy](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/strncpy.3.html#//apple_ref/doc/man/3/strncpy), [sprintf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sprintf.3.html#//apple_ref/doc/man/3/sprintf), [vsprintf](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/vsprintf.3.html#//apple_ref/doc/man/3/vsprintf), and [gets](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/gets.3.html#//apple_ref/doc/man/3/gets) have no built-in checks for string length, and can lead to buffer overflows.

   For alternatives, read [String Handling](Avoiding%20Buffer%20Overflows%20and%20Underflows.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdknzxfvjvomjq).

This checklist is intended to help you determine whether your program has any vulnerabilities related to use of encryption, cryptographic algorithms, or random number generation.

1. __Use trusted random number generators.__

   Do not attempt to generate your own random numbers. Use the Randomization Services programming interface, as described in _[Randomization Services Reference](https://developer.apple.com/documentation/security/randomization_services)_.

   Note that [rand](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/rand.3ssl.html#//apple_ref/doc/man/3/rand) does not return good random numbers and should not be used.
2. __Use TLS/SSL instead of custom schemes.__

   You should always use accepted standard protocols for secure networking. These standards have gone through peer review and so are more likely to be secure.

   In addition, you should always use the most recent version of these protocols.

   To learn more about the secure networking protocols available in macOS and iOS, read [Transmitting Data Securely](https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/SecureNetworkCommunicationAPIs/SecureNetworkCommunicationAPIs.html#//apple_ref/doc/uid/TP40011172-CH13) in _[Cryptographic Services Guide](../Cryptographic%20Services%20Guide/About%20Cryptographic%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzs)_.
3. __Don’t roll your own crypto algorithms.__

   Always use existing optimized functions. It is very difficult to implement a secure cryptographic algorithm, and good, secure cryptographic functions are readily available.

   To learn about the cryptographic services available in macOS and iOS, read _[Cryptographic Services Guide](../Cryptographic%20Services%20Guide/About%20Cryptographic%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzs)_.

Many security vulnerabilities are caused by problems with how programs are installed or code modules are loaded. This checklist is intended to help you find any such problems in your project.

1. __Don’t install components in__ `/Library/StartupItems` __or__ `/System/Library/Extensions`__.__

   Code installed into these directories runs with root permissions. Therefore, it is very important that such programs be carefully audited for security vulnerabilities (as discussed in this checklist) and that they have their permissions set correctly.

   For information on proper permissions for startup items, see [Startup Items](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html#//apple_ref/doc/uid/10000172i-SW9). (Note that in macOS 10.4 and later, startup items are deprecated; you should use `launchd` to launch your daemons instead. See _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_ for more information.)

   For information on permissions for kernel extensions, see _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_. (Note that beginning in macOS 10.2, macOS checks for permissions problems and refuses to load extensions unless the permissions are correct.)
2. __Don’t use custom install scripts.__

   Custom install scripts add unnecessary complexity and risk, so when possible, you should avoid them entirely.

   If you must use a custom install script, you should:

   - If your installer script runs in a shell, read and follow the advice in [Shell Script Security](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/ShellScriptSecurity/ShellScriptSecurity.html#//apple_ref/doc/uid/TP40004268-CH8) in _[Shell Scripting Primer](../../Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denry)_.
   - Be sure that your script follows the guidelines in this checklist just as the rest of your application does.

     In particular:

     - Don’t write temporary files to globally writable directories.
     - Don’t execute with higher privileges than necessary.

       In general, your script should execute with the same privileges the user has normally, and should do its work in the user’s directory on behalf of the user.
     - Don’t execute with elevated privileges any longer than necessary.
     - Set reasonable permissions on your installed app.

       For example, don’t give everyone read/write permission to files in the app bundle if only the owner needs such permission.
     - Set your installer’s file code creation mask (umask) to restrict access to the files it creates (see [Securing File Operations](Race%20Conditions%20and%20Secure%20File%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdkobvfvjvooi)).
     - Check return codes, and if anything is wrong, log the problem and report the problem to the user through the user interface.

   For advice on writing installation code that needs to perform privileged operations, see _[Authorization Services Programming Guide](../Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_. For more information about writing shell scripts, read _[Shell Scripting Primer](../../Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denry)_.
3. __Load plug-ins and libraries only from secure locations.__

   An application should load plug-ins only from secure directories. If your application loads plug-ins from directories that are not restricted, then an attacker might be able to trick the user into downloading malicious code, which your application might then load and execute.

   Be aware that the dynamic link editor (`dyld`) might link in plugins, depending on the environment in which your code is running. If your code uses loadable bundles (`CFBundle` or `NSBundle`), then it is dynamically loading code and could potentially load bundles written by a malicious hacker.

   See _[Code Loading Programming Topics](../../Cocoa/Code%20Loading%20Programming%20Topics/Introduction%20to%20Dynamically%20Loading%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2te2i)_ for more information about dynamically loaded code.

If your program includes or uses any command-line tools, you have to look for security vulnerabilities specific to the use of such tools. This checklist is intended to help you find and correct such vulnerabilities.

1. __Execute tools safely.__

   If you are using routines such as `popen` or `system` to send commands to the shell, and you are using input from the user or received over a network to construct the command, you should be aware that these routines do not validate their input. Consequently, a malicious user can pass shell metacharacters—such as an escape sequence or other special characters—in command line arguments. These metacharacters might cause the following text to be interpreted as a new command and executed.

   In addition, when calling functions such as `execlp`, `execvp`, `popen`, or `system` that use the `PATH` environment variable to search for executables, you should always specify a complete absolute path to any tool that you want to run. If you do not, a malicious attacker can potentially cause you to run a different tool using an environment variable attack. When possible, use `execvP` (which takes an explicit search path argument) or avoid these functions altogether.

   See Viega and McGraw, _Building Secure Software_, Addison Wesley, 2002, and Wheeler, _Secure Programming HOWTO_, available at [http://www.dwheeler.com/secure-programs/](http://www.dwheeler.com/secure-programs/), for more information on problems with these and similar routines and for secure ways to execute shell commands.
2. __Do not pass sensitive information on the command line.__

   If your application executes command-line tools, keep in mind that your process environment is visible to other users (see `man ps(1)`). You must be careful not to pass sensitive information in an insecure manner. Instead, pass sensitive information to your tool through some other means such as:

   - __Pipe or standard input__

     A password is safe while being passed through a pipe; however, you must be careful that the process sending the password obtains and stores it in a safe manner.
   - __Environment variables__

     Environment variables can potentially be read by other processes and thus may not be secure. If you use environment variables, you must be careful to avoid passing them to any processes that your command-line tool or script might spawn.

     See [Shell Script Security](https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/ShellScriptSecurity/ShellScriptSecurity.html#//apple_ref/doc/uid/TP40004268-CH8) in _[Shell Scripting Primer](../../Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denry)_ for details.
   - __Shared memory__

     Named and globally-shared memory segments can be read by other processes. See [Interprocess Communication and Networking](Validating%20Input%20and%20Interprocess%20Communication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenbwfvjvomjq) for more information about secure use of shared memory.
   - __Temporary file__

     Temporary files are safe only if kept in a directory to which only your program has access. See [Data, Configuration, and Temporary Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknltg), earlier in this chapter, for more information on temporary files.
3. __Validate all arguments (including the name).__

   Also, remember that anyone can execute a tool—it is not executable exclusively through your program. Because all command-line arguments, including the program name (`argv(0)`), are under the control of the user, your tool should validate every parameter (including the name, if the tool’s behavior depends on it).

This checklist is intended to help you program safely in the kernel.

1. __Verify the authenticity of Mach-based services.__

   Kernel-level code can work directly with the Mach component. A Mach port is an endpoint of a communication channel between a client who requests a service and a server that provides the service. Mach ports are unidirectional; a reply to a service request must use a second port.

   If you are using Mach ports for communication between processes, you should check to make sure you are contacting the correct process. Because Mach bootstrap ports can be inherited, it is important for servers and clients to authenticate each other. You can use audit trailers for this purpose.

   You should create an audit record for each security-related check your program performs. See [Audit Logs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknltk), earlier in this chapter, for more information on audit records.
2. __Verify the authenticity of other user-space services.__

   If your kernel extension was designed to communicate with only a specific user-space daemon, you should check not only the name of the process, but also the owner and group to ensure that you are communicating with the correct process.
3. __Handle buffers correctly.__

   When copying data to and from user space, you must:

   1. Check the bounds of the data using unsigned arithmetic—just as you check all bounds (see [Integer and Buffer Overflows](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjvfvbuqmjnknlto), earlier in this chapter)—to avoid buffer overflows.
   2. Check for and handle misaligned buffers.
   3. Zero all pad data when copying to or from user-space memory.

      If you or the compiler adds padding to align a data structure in some way, you should zero the padding to make sure you are not adding spurious (or even malicious) data to the user-space buffer, and to make sure that you are not accidentally leaking sensitive information that may have been in that page of memory previously.
4. __Limit the memory resources a user may request.__

   If your code does not limit the memory resources a user may request, then a malicious user can mount a denial of service attack by requesting more memory than is available in the system.
5. __Sanitize any kernel log messages.__

   Kernel code often generates messages to the console for debugging purposes. If your code does this, be careful not to include any sensitive information in the messages.
6. __Don’t log too much.__

   The kernel logging service has a limited buffer size to thwart denial of service attacks against the kernel. This means that if your kernel code logs too frequently or too much, data can be dropped.

   If you need to log large quantities of data for debugging purposes, you should use a different mechanism, and you _must_ disable that mechanism before deploying your kernel extension. If you do not, then your extension could become a denial-of-service attack vector.
7. __Design hash functions carefully.__

   Hash tables are often used to improve search performance. However, when there are hash collisions (where two items in the list have the same hash result), a slower (often linear) search must be used to resolve the conflict. If it is possible for a user to deliberately generate different requests that have the same hash result, by making many such requests an attacker can mount a denial of service attack.

   It is possible to design hash tables that use complex data structures such as trees in the collision case. Doing so can significantly reduce the damage caused by these attacks.

[Next](Third-Party%20Software%20Security%20Guidelines.md)[Previous](Avoiding%20Injection%20Attacks%20and%20XSS.md)

