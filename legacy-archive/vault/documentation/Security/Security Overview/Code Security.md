---
title: Security Overview
apple_id: TP30000976
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Security
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/SecuritySvcs/SecuritySvcs.html
archived_at: '2026-07-18T02:06:31.454439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Overview](About%20Software%20Security.md)


[Next](Authentication%20and%20Authorization.md)[Previous](Risk%20Assessment%20and%20Threat%20Modeling.md)

# Code Security

No software is perfect. Although many flaws are caused by design mistakes, some of the most devastating flaws are caused by implementation mistakes. Design flaws and implementation flaws can compromise data and can cause your software to misbehave. Attacks on implementation flaws can also sometimes cause your software to execute arbitrary binary code provided by the attacker.

In preventing these attacks, threat models can only get you so far. They identify the parts of your infrastructure that might reasonably be attacked, but they do not identify specific ways in which those pieces might be attacked.

Therefore, when you implement your software, you must take steps to make it harder to compromise your code. You must also minimize the potential for damage if an attacker does manage to compromise your code. This chapter briefly summarizes how to write secure, robust code and describes operating system and compiler features that make your job easier.

_Code hardening_ refers to fixing security holes in the code itself (as opposed to design mistakes). In essence, code hardening is like repairing the bad mortar in a castle wall to prevent an attacker from breaching it or shoring up the stern of a ship to repair a leak.

Here are some code-hardening techniques:

- Add code that validates inputs to prevent integer overflows.
- Replace any unsafe string function calls with calls that are buffer-size-aware to prevent buffer overflows.
- Avoid passing data to interpreters whenever possible. When the use of interpreters is unavoidable, pass data to the interpreters in a safe fashion.

  To prevent command injection attacks in SQL queries, use parameterized APIs (or manually quote the strings if parameterized APIs are unavailable).

  Avoid the POSIX [system](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/system.3.html#//apple_ref/doc/man/3/system) function.
- Set reasonable values for environment variables (`PATH`, `USER`, and so on) and do not make security decisions based on their values.
- Fix bugs that cause race conditions; these can lead to incorrect behavior (or worse).

At the end of this chapter, you’ll find a link to a document that describes these techniques in more detail, along with other code-hardening techniques.

Code signing is a technology for ensuring the authenticity of executable code. By signing your code, the operating system can verify that an app has not been modified by other software and can verify that updates to that app were actually released by its author. Other technologies, such as the keychain and app sandboxing, take advantage of this signature to better protect your users’ data.

To understand the details, however, you’ll have to learn a few more concepts. For this reason, code signing is revisited in [Cryptographic Services](Cryptographic%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzwfvbuqmznknltc).

The principle of least privilege states that a piece of code should, to the extent practical, run with exactly the permissions it needs, and no more.

The closest analog in the physical world is designating certain areas for certain activities, and only allowing people to enter those areas if they have a legitimate need to perform those activities. At a conference, for example, the technical crew does not need access to the speaker support center, nor do the speakers (usually) need access to the backstage areas.

In much the same way, your software should never take on or grant others any more permissions than are necessary to do a particular job. For example, an app should _not_:

- Request elevated privileges unless absolutely necessary
- Relax permissions on portions of its app bundle
- Make unnecessary network connections
- Listen for connections on unnecessary network ports
- Listen for connections on public network interfaces inadvertently
- Read or write files in publicly writable folders unless directed to do so by the user

These are just a few examples. Because many of these activities are ancillary to your app’s main behavior, it is critically important to regularly perform threat modeling as you add new code.

To parents, a sandbox is a safe haven in which their children can play without needing to worry about them getting hurt. It is a somewhat enclosed, safe environment, free from things that might injure them. And as long as the children are inside the sandbox, they cannot (easily) be causing mischief outside the sandbox.

Similarly, in computing, the benefits of a sandbox are not limited to bad apps. Any app that contains security holes can “go bad” if exploited properly, potentially causing the app to run arbitrary code. Thus, in computing, sandboxes should be applied broadly—to all apps, ideally—ensuring that they cannot cause much harm if they get compromised.

To achieve this goal, a sandbox limits an app’s capabilities to match its expected behavior (as defined by the APIs that it uses and, in some cases, by a list of additional entitlements requested by the author of the app).

Thus, in computing, a sandbox more closely resembles the watchful eye of a Neighborhood Watch crime prevention program. If someone appears who is acting suspicious, the neighbors can take action. In a similar fashion, a sandboxed environment allows an app to do the things it normally would do. However, if it steps out of line, the operation fails, and in some cases, the process is killed outright.

In an ideal world, writing software according to the principle of least privilege would be straightforward; the user would grant each process just enough privilege required to do a job, and no more. However, this approach can be challenging in practice, particularly when the nature of the job is poorly defined.

For a real-world example, a janitor needs to be able to take out the trash. A janitorial position does not typically require a high security clearance. But suppose there is a trash can in a room filled with top-secret documents. Because that trash can is ostensibly the janitor’s responsibility, the minimum privilege for the job is rather broad—the janitor needs a high security clearance. A better solution is to move the trash can outside the door. Alternatively, an employee who already has the necessary clearance could take the trash can out at the end of the day.

In computers, the solution to this problem is privilege separation—breaking up a piece of software into multiple pieces so that each piece individually requires fewer capabilities and so that those capabilities are protected from inappropriate use by other parts of the app, tool, or daemon. This separation between pieces is called a _trust boundary_.

For example, a word processor that accesses help files over a network might separate out the networking portions into a separate help file downloader app. The main app should scrutinize the data sent back from this helper, both to ensure that it was not tampered with during transit and to ensure that the helper, if compromised, cannot easily attack the main app.

Privilege separation is performed by writing a helper, daemon, or agent whose purpose is to do work on the behalf of another piece of software. That helper, daemon, or agent may be sandboxed, unsandboxed, or privileged.

- A sandboxed helper, daemon, or agent has fewer privileges than an ordinary app running as the user. It may still have more permissions than the calling app, however, because the caller may be in an even stricter sandbox.
- An unsandboxed helper, daemon, or agent has the same privileges as the user. However, because the calling app may be running in a sandbox, this unsandboxed helper may have more privileges than the caller.
- A privileged helper, daemon, or agent runs as another user who has broader permissions (often as the root user, or superuser, which is essentially unlimited in terms of what operations it can perform).

  Privileged helpers cannot be created within a sandboxed environment; however, they play a pivotal role in making that environment more usable. For example, a privileged agent (privileged only because it is running outside the sandbox) is used by the OS to provide a number of services to sandboxed apps, such as the powerbox, which displays an “open file” dialog on behalf of the app and then temporarily adds the chosen file to the app’s sandbox entitlements.

Because a differently privileged helper, daemon, or agent has the potential to allow its caller to significantly violate established privilege boundaries, it must be written in such a way that limits what its caller can do. For example, the powerbox allows an app to gain access to files outside the app’s container directory, but it does so in a way that requires that the user take an explicit action to show consent.

OS X 10.7 introduced the XPC Services API for creating sandboxed helper apps that are specific to a single app. These helper apps can have different privileges than the main app. macOS 10.8 and later also provides the NSXPC API, which makes the process of privilege separation even more transparent by allowing the main app to remotely call a specified set of methods on specific objects in the helper app and vice versa.

For a more detailed conceptual overview of code hardening, read _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_.

To learn more about App Sandbox, read _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

For more information about XPC Services and NSXPC, read _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

You can also learn about other Apple and third-party security books in [Other Security Resources](Other%20Security%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzwfvbuqnznknltc).

[Next](Authentication%20and%20Authorization.md)[Previous](Risk%20Assessment%20and%20Threat%20Modeling.md)

