---
title: Security Overview
apple_id: TP30000976
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Security
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/ThreatModeling/ThreatModeling.html
archived_at: '2026-07-18T02:06:31.553556Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Overview](About%20Software%20Security.md)


[Next](Code%20Security.md)[Previous](About%20Software%20Security.md)

# Risk Assessment and Threat Modeling

Before you write a single line of code, take the time to design your software with security in mind. Doing this correctly is genuinely hard; if your security analysis process seems easy, you’re probably missing something fairly fundamental and losing most of the benefits of proper secure code design.

Risk assessment and threat modeling happens in three steps:

1. __Assess risk.__ Determine how much you have to lose.
2. __Determine potential threats.__ Figure out the various things your code does that could be attacked (including things that frameworks and libraries do on your behalf).
3. __Mitigate threats.__ Ensure that the parts of your code that could be attacked are well protected.

To assess the risk that your code would pose if compromised, you should first assume that your program will be attacked.

The amount of time and effort that an attacker will spend attacking your program depends on several factors, including:

- The value of the data your program handles. Does it store thousands of credit card numbers or a user’s recipe collection?
- The trustworthiness and security of companies who provide services that your code depends on.
- The specific clients who purchased your program. Is your word processing app being used by Joe’s Auto Repair or by Big Megacorp, Inc.?
- How widely your program will be distributed. Is it an app that is used by a single, small workgroup, or is it built into an operating system that is about to be released worldwide?

Based on those same factors, you need to decide what level of risk is acceptable. A loss of data that will cost your company $1000 to rectify doesn’t justify a $10,000 development effort to close all potential security bugs. On the other hand, damage to your company’s reputation might be worth far more in the long run than it would cost to design and develop secure code.

Here are some factors to consider when evaluating risk:

- What is the worst thing that can happen if your software is successfully attacked?

  Will it allow theft of a user’s identity, allow an attacker to gain control of a user’s computer, or just enable a hacker to get an unusually high score in pinball?
- How hard is it to mount a successful attack?

  If exploiting a vulnerability would require installing a Trojan horse on the user’s computer that can take advantage of a race condition that occurs only once in 50 times the program starts up, you might decide the level of risk is acceptable. If the exploit can be used by unskilled attackers running prewritten attack scripts or be automated to spread by botnets (networks of compromised computers), the level of risk is much higher.
- How big a target is it?

  Did you sell a hundred copies of your app, or is it installed by default on hundreds of thousands of computers?

  Is it vulnerable by default, or only after a user chooses an unusual set of options?
- How many users would be affected?

  An attack on an end user’s machine usually affects one or two people, but a denial of service attack on a server might affect thousands of users if even one server is attacked. Similarly, a worm spread by a common email program might infect thousands of computers.
- How accessible is the target?

  Does running the program require local access, or does the program accept requests across a network? Is authentication required in order to establish a connection, or can anyone send requests to the program?

A risk assessment gives you some indication of how likely you are to be attacked and how much damage an attack could cause. The next step is to figure out _how_ you might be attacked, including attacks on all of your interests—not only attacks on your software but also on your servers, your company, and so on. To do this, you create a _threat model_ that describes places in which anything of value (information, money, and so on) changes hands.

The threat model for an app, daemon, or other software system should be a high-level data-flow model that diagrams every spot in which information moves into or out of your code or between major parts of your code. At a high level, it should include these pieces:

- The types of data your app will work with
- The situations in which your app must deal with untrusted data
- The types of data transport your app uses
- Ways that an attacker could exploit a piece of software that does what your app does
- Strategies for mitigating each of those types of exploits

For the purposes of this analysis, you should consider only theoretical categories of attack, not actual specific attacks. For example, a word processor could be compromised if it mishandles a corrupted file in such a way that allows an attacker to inject code. It is not important whether your specific code has specific bugs that make this possible.

Some potential attack targets might include program input or output, stored data, and the program’s operating environment.

- __Program input__. If an attacker can cause a buffer overflow, they might be able to run their own code or otherwise compromise the user’s data or system.
- __Program output__ (either to the user or to another software module). The attacker might be able to gain access to private information stored on the system, or to read and modify the information being passed between modules (a _man-in-the-middle attack_).
- __Data stored on the system__ (either permanently, as in a database, or temporarily, as in a global variable). This data could potentially be stolen and sent to an attacker, modified by an attacker, or otherwise compromised.
- __Program environment__. A program’s execution environment includes its open file descriptors, environment variables, Mach ports, preference files, and so on.

There are several types of threats to consider, including threats to data, service availability, and system integrity.

An attacker can modify data. This includes:

- Data used internally by the program (such as interprocess messages).
- Data acted on by the program (such as numbers on which the program does a statistical analysis or an audio track that the program filters).
- Data stored on disk to which the program gives access.

Similarly, an attacker can compromise data and obtain access to secrets.

An attacker can modify or compromise data directly by telling the program to modify or return data that it shouldn’t have modified or returned. However, an attacker can also modify or compromise data indirectly by using your program to take control of the computer.

Further, direct modifications often lead to further access that can allow additional indirect modifications. For example, an attacker might modify internal program data directly, then use that modified data to inject arbitrary code that adds a new admin user to the system’s password database.

An attack designed to reduce service availability is called a _denial of service attack_. These attacks can cause an app or daemon to stop functioning, or make a server so busy that legitimate users can’t get access to it.

An attacker can perform a denial of service attack in many ways:

- Attack bugs in the networking stack.
- Open connections to the daemon, start sending a request, then continue sending it very, very slowly.
- Convince thousands of people to voluntarily attack your server.
- Open millions of connections to the daemon from a botnet.

When a denial of service attack is carried out by a large number of machines, it is called a _distributed denial of service attack_, or _DDoS_.

Attacks on system integrity build upon other attacks to modify the system in such a way that it can no longer be trusted. If an attacker can find a security flaw in your code, the attacker might be able to:

- __Execute malicious code, especially with administrator or root access.__ The attacker might cause your code to execute the attacker’s code by exploiting a buffer overflow or by code insertion in a URL command, for example.

  If your code is a daemon running with administrative privileges, the attacker’s code will be privileged as well. Once an attacker has administrative control of a computer, any efforts to mitigate threats become futile.
- __Impersonate a user or server.__ The attacker might be able to guess or obtain a valid username and password and therefore authenticate as an authorized user.

  Similarly, a spoofed server might be able to convince a client app that it is a legitimate server, then get the client to give it data or get the user to provide secrets, such as passwords.

  Finally, a spoofed server might be able to convince a naïve user that the server is legitimate. For example, a user might not examine the window containing a web page sufficiently to notice that the lock icon (or other indicator of a secure site) is missing. Using such a malicious website to obtain user data is called _phishing_.
- __Repudiate an action.__ A malicious user might modify your software in such a way that allows him or her to deny performing an operation (such as using a specific credit card number). There are a number of techniques you can use to ensure nonrepudiation, such as code signature verification, data integrity checks, and so on.

After you have determined which parts of your software ecosystem (apps, servers, local daemons and agents, and so on) might be attacked, you must take steps to mitigate those threats—that is, to make them less damaging.

The means of mitigating threats in computer software are many and varied, but a few core techniques are common:

- Take extra care when working with data from a potentially untrusted source. In particular, secure software must always validate its inputs.
- Take advantage of sandboxing—setting developer-defined limits on what your app can do—to minimize the damage that an app can cause if it gets compromised.
- Minimize the risk of information disclosure by compartmentalizing your apps and ensuring that each part of an app can access only the information that it needs.
- Perform fuzzing—sending bad data to your app or daemon to see if it breaks—and fix any bugs that you find in the process.
- Take advantage of the security functionality built into the operating system instead of reinventing the wheel.

When deciding how to mitigate a threat, keep in mind that there are often tradeoffs between security and convenience. Software security must strike a balance between security and usability. Consider two extreme examples of software design:

- One program requires authentication using multiple authentication methods before performing any operation, runs only long enough to perform that operation, does not share use of the CPU with any other program, and then quits, requiring reauthorization for the next operation.

  This mode of operation is very secure and might be appropriate for a program that launches nuclear missiles, but few would want to use a word processor that acted like that.
- Another program always runs with root privileges and performs any operation you like without ever requiring authorization.

  Such a program is easy to use, and on a physically secure computer that is not connected to a network, it might even be moderately safe. However, under most normal conditions, it would be a huge security risk.

Clearly neither of these extremes strikes an optimal balance between security and user convenience. As a developer, it is your responsibility to decide where your software should fit in this continuum based on the damage that might occur if your program is compromised (the risk) and the types of attacks the software is likely to face (the threat).

Even when you finish this assessment, your job is not done; you should repeat this assessment at regular intervals along the way. In particular:

- Whenever you make any design decisions, consider how the design decisions change your threat models and update your models accordingly.
- When you add new features or functionality, create threat models for those new components.
- As you code, be aware of the threat model and make sure your code follows its guidance.

In addition to avoiding bugs in the design, you must also take steps to ensure that your code is robust against attacks on bugs in the implementation. You’ll learn more about how to do this in the next chapter.

The governments of the United States, Canada, the United Kingdom, France, Germany, and the Netherlands have worked together to develop a standardized process and set of standards that can be used to evaluate the security of software products. This process and set of standards is called the _Common Criteria_.

As an attempt to systematize security evaluations, the Common Criteria can be helpful in suggesting a large number of potential problems that you can look for. On the other hand, as with any standardization scheme, the Common Criteria cannot anticipate vulnerabilities that haven’t been seen before. Therefore, the Common Criteria standard is less flexible than one might wish.

Although opinions of security experts vary as to the value of a Common Criteria evaluation, some government agencies cannot use software that hasn’t been through a full Common Criteria evaluation by an accredited laboratory.

A number of third-party security books describe threat modeling in more detail. See [Other Security Resources](Other%20Security%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzwfvbuqnznknltc) for a complete list.

[Next](Code%20Security.md)[Previous](About%20Software%20Security.md)

